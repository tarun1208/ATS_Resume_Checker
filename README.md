Python
# 🛡️ AI Resume ATS Scanner

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Flask](https://img.shields.io/badge/Framework-Flask-green)
![Gemini](https://img.shields.io/badge/AI-Google%20Gemini-orange)

An intelligent web application that helps job seekers optimize their resumes. It uses **Google's Gemini AI** to act as a strict Applicant Tracking System (ATS), parsing PDF resumes and providing a match score, pros, cons, and actionable feedback.

## 🚀 Features

* **PDF Analysis:** Robust text extraction from PDF resumes using `PyPDF2`.
* **AI-Powered Feedback:** Uses `gemini-2.5-flash` to generate human-like critiques.
* **Scoring System:** Provides a Match Score out of 100.
* **Smart UI:** Clean, responsive interface with automatic color-coding for Pros (Green) and Cons (Red).
* **Secure:** API keys are protected using environment variables.

## 📦 Required Packages

The project relies on these specific Python libraries:

1.  **`flask`**: The web framework to run the server.
2.  **`google-genai`**: The client to connect to Google's Gemini API.
3.  **`PyPDF2`**: To read and extract text from PDF files.
4.  **`python-dotenv`**: To securely load API keys from the `.env` file.

## ⚡ Installation & Setup

Follow these steps to run the project locally:

1. Clone the repository and change into the project folder:

```bash
git clone https://github.com/YOUR_USERNAME/ai-resume-scanner.git
cd ai-resume-scanner
```

2. (Recommended) Create and activate a virtual environment:

Windows (PowerShell / CMD):

```powershell
python -m venv venv
# PowerShell
venv\Scripts\Activate.ps1
# CMD
venv\Scripts\activate.bat
```

macOS / Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
# or
pip install flask google-genai PyPDF2 python-dotenv
```

Bash

pip install flask google-genai PyPDF2 python-dotenv

4. Configure secrets (recommended for local development):

- Create a file named `.env` in the project root.
- Add your API key (example):

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

- Create a `.env.example` file with placeholders (commit this file to the repo):

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

5. Run the app:

```bash
python main.py
```

By default the app should be available at http://127.0.0.1:5000 unless you changed the host/port in `main.py`.

📸 Usage
Open the app in your browser.

Click the Paperclip (📎) icon or the "Choose Resume" button.

Select a PDF resume.

Click Analyze Resume.

Wait a few seconds for the AI to generate the report.

📂 Project Structure (example)

```
ai-resume-scanner/
├── main.py              # Main Flask application logic
├── .env                 # Local secrets (DO NOT commit)
├── .gitignore           # Prevents .env and venv from being uploaded
├── requirements.txt     # List of dependencies
└── templates/
    └── home.html       # Frontend UI
```
🐛 Troubleshooting
Error: 404 models/gemini-2.5-flash not found

Fix: Ensure `main.py` is using the specific model version `gemini-2.5-flash`.

Error: Module not found

Fix: Ensure you activated your virtual environment (Step 2) before running the app.

📄 License
This project is open-source and available under the MIT License.
