import os
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from google import genai 
from dotenv import load_dotenv

# ==============================
# CONFIG & AUTH
# ==============================
load_dotenv()

# Get the key from .env
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("CRITICAL ERROR: Gemini API Key is missing in your .env file.")
    # For local testing fallback (Not recommended for production)
    API_KEY = "YOUR_ACTUAL_API_KEY_HERE"

# Initialize the modern Gemini Client
try:
    client = genai.Client(api_key=API_KEY)
    print("Neural Engine: Successfully authenticated with Google GenAI SDK.")
except Exception as e:
    print(f"Neural Engine: Initialization failed. Error: {str(e)}")

app = Flask(__name__)
# Enable CORS for frontend communication
CORS(app)

# ==============================
# UTILITY ROUTES
# ==============================
@app.route("/", methods=["GET"])
def home():
    """Root route to verify server status."""
    return jsonify({
        "status": "online",
        "engine": "OptiScan Elite Neural Backend",
        "message": "Send POST requests to /api/analyze"
    })

# ==============================
# NEURAL ENGINE LOGIC
# ==============================
def get_ats_analysis(resume_text, jd_text):
    """
    Uses Gemini 2.5 Flash via the new SDK to perform analysis.
    """
    prompt = f"""
    Act as a cynical, high-stakes Fortune 500 Executive Recruiter. 
    Analyze the following RESUME against the JOB DESCRIPTION.
    
    RESUME:
    {resume_text}

    JOB DESCRIPTION:
    {jd_text}

    Return a JSON object with these exact keys:
    - "score": (Integer 0-100 based on ATS compatibility and skill match)
    - "tier": (Single letter: S, A, B, C, or F)
    - "summary": (A sharp, 1-sentence professional critique explaining the score)
    - "missing_skills": [List of 3-5 important missing keywords]
    """

    # Generate content using the new SDK syntax
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config={
            'response_mime_type': 'application/json',
        }
    )
    
    # The new SDK returns the response text directly; we parse it to JSON
    return json.loads(response.text)

# ==============================
# API ROUTE
# ==============================
@app.route("/api/analyze", methods=["POST"])
def analyze():
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "No data provided"}), 400
            
        resume_text = data.get("resumeText")
        jd_text = data.get("jobDescription")

        if not resume_text or not jd_text:
            return jsonify({"error": "Missing resume text or job description"}), 400

        # Execute Analysis
        result = get_ats_analysis(resume_text, jd_text)

        return jsonify(result)

    except Exception as e:
        print(f"Neural Engine Error: {str(e)}")
        return jsonify({"error": f"Neural link unstable: {str(e)}"}), 500

# ==============================
# RUN SERVER
# ==============================
if __name__ == "__main__":
    app.run(debug=True, port=5000)