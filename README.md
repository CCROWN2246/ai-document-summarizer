# 📄 AI Document Summarizer

A fast, flexible, and interview-ready tool that uses GPT-4o to intelligently summarize PDF, DOCX, and TXT documents. Designed for rapid deployment, clean code structure, and real-world use cases—perfect for showcasing your applied AI and Python development skills.

---

## 🚀 Features

- ✅ Upload and parse documents (`.pdf`, `.docx`, `.txt`)
- 🧠 Summarize using OpenAI’s `gpt-4o` model
- 📝 Choose from **short**, **detailed**, or **bullet point** summaries
- 💡 Clean, modular Python backend for easy customization
- ⚡ Interactive UI built with Streamlit

---

## 🔧 Tech Stack

| Tool/Library       | Purpose                            |
|--------------------|------------------------------------|
| Python             | Core logic                         |
| Streamlit          | Frontend + local app interface     |
| OpenAI GPT-4o      | Summarization model                |
| PyPDF2             | PDF text extraction                |
| python-docx        | DOCX parsing                       |
| python-dotenv      | Secure API key management          |

---

## 🛠️ Setup & Installation (PowerShell)

> ✅ Recommended: Use Visual Studio Code + PowerShell terminal (default on Windows)

1. **Clone the repository**
   ```powershell
   git clone https://github.com/yourusername/document-summarizer.git
   cd document-summarizer

---

## 🧠 Requirements

- Python 3.10+
- An Azure OpenAI resource with a deployed model (e.g., `gpt-4o`)
- Your own API key and endpoint

Install dependencies:

```powershell
pip install -r requirements.txt

## Create the virtual environment
python -m venv .venv

##get rid of powershell script execution error
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser


## activate the environment
.venv\Scripts\activate

## create the .env file

AZURE_OPENAI_API_KEY=your-api-key-here
AZURE_OPENAI_ENDPOINT=https://your-resource-name.cognitiveservices.azure.com
AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4o
AZURE_OPENAI_MODEL=gpt-4o
AZURE_OPENAI_API_VERSION=2024-12-01-preview

## file structure

ai-document-summarizer/
│
├── app.py                  # Main app logic (Streamlit or CLI interface)
├── summarizer.py           # GPT-4o summarization logic
├── file_handler.py         # Handles file uploads and parsing
├── .env                    # API key, model config
├── requirements.txt        # Dependencies
├── README.md               # Project overview
└── examples/               # Sample docs for demo/testing


## how to run the app
streamlit run app.py