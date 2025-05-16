# ✉️ AI Email Rewriter

Transform your emails with AI-powered tone and clarity enhancement using Cohere and Streamlit!

**Live app**: [Streamlit Link](https://email-rewriter-ai-sans-3010.streamlit.app/)

---

## 🚀 Overview

The AI Email Rewriter is a web application that leverages Cohere's natural language processing capabilities to rewrite emails in various tones (Professional, Friendly, Persuasive, Apologetic). Built with Streamlit, this app provides an intuitive and interactive interface for users to enhance their email communication effortlessly.

---

## ✨ Features

* 📝 Rewrite emails in multiple tones with a single click
* 🧠 Powered by Cohere's advanced language models (`command`, `command-light`)
* 🌟 Interactive UI with diff view to compare original and rewritten emails
* ⚙️ Easy setup with environment variables for API keys
* ☁️ Deployable on Streamlit Community Cloud in minutes

---

## 🛠️ Tech Stack

* Python 3.8+
* Streamlit
* Cohere Python SDK
* `python-dotenv`
* GitHub for version control and deployment

---

## 📋 Prerequisites

Ensure the following are ready before setup:

```bash
🐍 Python 3.8+ installed
🔑 A Cohere API Key
📁 GitHub account (for deployment)
📦 (Optional) Docker for containerized deployment
```

---

## 🔑 Cohere API Setup

1. **Sign Up for Cohere**

   * Visit the [Cohere Dashboard](https://dashboard.cohere.com) and sign up
   * Navigate to **API Keys** and click **Create API Key**
2. **Add the API Key**

   * Create a `.env` file in your project root:

     ```env
     COHERE_KEY=your-cohere-api-key-here
     ```
3. **Integration**

   * `email_rewriter.py` uses the API key:

     ```python
     self.client = cohere.Client(api_key=api_key)
     response = self.client.chat(
         model=config.model,
         message=prompt,
         temperature=config.temperature,
         max_tokens=config.max_tokens
     )
     ```

---

## ⚙️ Local Setup

1. **Clone the Repository**

```bash
git clone <your-repository-url>
cd AI-Email-Rewriter
```

2. **Create Virtual Environment**

```bash
python -m venv venv
./venv/Scripts/activate  # Windows
# source venv/bin/activate  # Unix
```

3. **Install Dependencies**

```bash
pip install streamlit python-dotenv cohere
```

4. **Run the App**

```bash
streamlit run app.py
```

Visit `http://localhost:8501` in your browser.

---

## ☁️ Streamlit Deployment

1. **Push Code to GitHub**

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/OMCHOKSI108/EMAIL-REWRITER.git
git branch -M main
git push -u origin main
```

2. **Create requirements.txt**

```txt
streamlit
python-dotenv
cohere
```

3. **Sign Up for Streamlit Cloud**

* Sign up via GitHub
* Deploy new app using your repo

4. **Add API Key in Deployment Settings**

```env
Key: COHERE_KEY
Value: your-cohere-api-key-here
```

5. **Deploy and Share**

* Streamlit will generate a live URL.
* Add badge to README:

```md
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-name.streamlit.app)
```

---

## 🗈 File Structure

```
.
├── app.py                   # Streamlit app UI
├── email_rewriter.py        # Email rewriting logic
├── api_model_checker.py     # Cohere model list handler
├── .env                     # Stores API key
├── requirements.txt         # Dependencies
├── venv/                    # Virtual environment (excluded in Git)
├── README.md                # Project documentation
├── LICENSE                  # MIT License (optional)
└── .gitignore               # Git ignore config
```

---

## 📸 Usage

* Input your **Cohere API key** in sidebar or `.env`
* Paste your **email text**
* Select **tone** and **model**
* Click **Rewrite Email**
* Toggle **Show changes** to view diffs

![Working Example](https://github.com/OMCHOKSI108/EMAIL-REWRITER-AI/blob/main/assets/Screenshot(191).png)

---

## 🛠️ Customization

* **Add New Tones**: Edit tone list in `app.py`

```python
tone = st.selectbox("✍️ Select Tone", ["Professional", "Friendly", "Persuasive", "Apologetic", "Casual"])
```

* **Update Models**: Edit `api_model_checker.py`

```python
models = ["command", "command-light", "new-model"]
```

* **Enhance Prompt**: Improve logic in `email_rewriter.py`

```python
return f"""Rewrite the following email in a {tone.lower()} tone..."""
```

---

## 🛠️ Troubleshooting

* **Invalid API Key**:

```bash
curl https://api.cohere.ai/v1/chat \
  -H "Authorization: Bearer your-cohere-api-key-here" \
  -H "Content-Type: application/json" \
  -d '{"message": "test", "model": "command", "max_tokens": 5}'
```

* **Model Errors**: Confirm model names match hardcoded list
* **Streamlit Deploy Errors**: Verify `requirements.txt` and environment variables

---

## 📜 License

Licensed under the **MIT License**. See `LICENSE` for details.

---

## 🙌 Acknowledgments

* [Cohere](https://cohere.com) for NLP APIs
* [Streamlit](https://streamlit.io) for the UI framework
* Tutorials from Cohere's Blog and Streamlit Docs

---

**Made with ❤️ by Om Choksi**
