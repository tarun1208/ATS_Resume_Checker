


from flask import Flask, request, jsonify, render_template
from google import genai
import PyPDF2
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Fetch the key securely
# If the key isn't found, this will return None and avoid crashing immediately
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("No API key found. Please set GEMINI_API_KEY in your .env file")

client = genai.Client(api_key=api_key)

@app.route('/')
def index():
    return render_template('home.html')

# Chat Route (for general questions)
@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.json
        prompt = data.get("message")
        
        # Using the specific stable version to avoid 404 errors
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ATS Analysis Route
@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No file uploaded"}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No file selected"}), 400

        # 1. Extract Text from PDF
        pdf_reader = PyPDF2.PdfReader(file)
        resume_text = ""
        for page in pdf_reader.pages:
            resume_text += page.extract_text()

        # 2. PROS & CONS PROMPT
        ats_prompt = f"""
        Act as an expert ATS (Applicant Tracking System) Scanner. 
        Analyze the following resume text.
        
        Output the response in this EXACT Markdown format:

        # 🛡️ ATS Report
        
        ## 📊 Match Score: [Score]/100
        
        ## ✅ Pros
        * [List the resume's top strengths]
        * [List specific good keywords found]
        
        ## ❌ Cons
        * [List formatting errors or missing sections]
        * [List missing critical skills]
        
        ## 💡 Final Verdict
        [One sentence summary]

        RESUME TEXT:
        {resume_text}
        """

        # 3. Generate Analysis
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=ats_prompt
        )
        
        return jsonify({"response": response.text})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Failed to process file. Ensure it is a valid PDF."}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)