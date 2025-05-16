### ✉️ AI Email Rewriter
Transform your emails with AI-powered tone and clarity enhancement using Cohere and Streamlit!

🚀 Overview
The AI Email Rewriter is a web application that leverages Cohere's natural language processing capabilities to rewrite emails in various tones (Professional, Friendly, Persuasive, Apologetic). Built with Streamlit, this app provides a sleek and interactive interface for users to enhance their email communication effortlessly.
✨ Features

📝 Rewrite emails in multiple tones with a single click.
🧠 Powered by Cohere's advanced language models (command, command-light).
🌟 Interactive UI with diff view to compare original and rewritten emails.
⚙️ Easy setup with environment variables for API keys.
☁️ Deploy on Streamlit Community Cloud in minutes!

🛠️ Tech Stack


📋 Prerequisites
Before you begin, ensure you have the following:

🐍 Python 3.8+ installed on your system.
🔑 A Cohere API Key (see Cohere API Setup below).
☁️ A GitHub account for deployment on Streamlit Community Cloud.
🐳 (Optional) Docker for containerized deployment.


🔑 Cohere API Setup
The app uses Cohere's /chat endpoint to rewrite emails. Follow these steps to obtain and integrate your Cohere API key:

Sign Up for Cohere  

Visit Cohere's Dashboard and sign up for an account.
After signing up, navigate to the API Keys section.


Generate an API Key  

Click on Create API Key to generate a new key.
Copy the key (it will look like a 40-character string, e.g., your-cohere-api-key-here).


Add the API Key to Your Project  

Create a .env file in the root of your project directory (D:\OM_CHOKSI\AI_EMAIL\AI-Email-Rewriter\.env).
Add the following line to the .env file:COHERE_KEY=your-cohere-api-key-here


Replace your-cohere-api-key-here with your actual Cohere API key.


How the Cohere API is Integrated  

The app uses the cohere Python library to interact with Cohere's API.
In email_rewriter.py, the EmailRewriter class initializes a Cohere client with your API key:self.client = cohere.Client(api_key=api_key)


The /chat endpoint is called to rewrite emails using the command model (default):response = self.client.chat(
    model=config.model,
    message=prompt,
    temperature=config.temperature,
    max_tokens=config.max_tokens
)


The app supports models like command and command-light, which are hardcoded in api_model_checker.py since Cohere doesn’t provide a /models endpoint as of May 2025.




⚙️ Local Setup
Follow these steps to set up and run the app locally on your machine.
1. Clone the Repository
If you have a GitHub repository, clone it. Otherwise, ensure all project files (app.py, email_rewriter.py, api_model_checker.py, .env) are in your project directory (D:\OM_CHOKSI\AI_EMAIL\AI-Email-Rewriter).
git clone <your-repository-url>
cd AI-Email-Rewriter

2. Set Up a Virtual Environment
Create and activate a virtual environment to manage dependencies.
python -m venv venv
.\venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On Unix-based systems

3. Install Dependencies
Install the required Python packages using pip.
pip install streamlit python-dotenv cohere

4. Run the App Locally
Start the Streamlit app to test it on your local machine.
streamlit run app.py


The app will open in your browser at http://localhost:8501.
Enter your Cohere API key in the sidebar (or ensure it’s in the .env file).
Paste an email, select a tone, choose a model, and click "Rewrite Email" to see the magic! 🎉


☁️ Streamlit Deployment
Deploy your app to Streamlit Community Cloud to share it with the world. This is a free and hassle-free way to deploy Streamlit apps directly from a GitHub repository.
1. Push Your Code to GitHub
Ensure your project is in a GitHub repository.

Initialize a Git repository (if not already done):git init
git add .
git commit -m "Initial commit"


Create a new repository on GitHub and push your code:git remote add origin https://github.com/your-username/your-repo-name.git
git branch -M main
git push -u origin main



2. Create a requirements.txt File
Streamlit Community Cloud needs a requirements.txt file to install dependencies. Create this file in your project root:
streamlit
python-dotenv
cohere

3. Sign Up for Streamlit Community Cloud

Visit Streamlit Community Cloud and sign up using your GitHub account.
Log in to your account.

4. Deploy the App

On the Streamlit Community Cloud dashboard, click New App.
Select your GitHub repository, branch (e.g., main), and main file path (app.py).
In the Advanced Settings, add your Cohere API key as an environment variable:
Key: COHERE_KEY
Value: your-cohere-api-key-here


Click Deploy. Wait a few minutes, and your app will be live on the web! 🌐

5. Share Your App

Once deployed, Streamlit will provide a URL (e.g., https://your-app-name.streamlit.app).
Share this URL with others to let them use your app.
Add a Streamlit badge to your GitHub repository’s README.md:[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-name.streamlit.app)



File Structure 
```
│
├── app.py                   # Main Streamlit app for the UI and user interaction
├── email_rewriter.py        # Logic for rewriting emails using Cohere API
├── api_model_checker.py     # Manages available Cohere models (hardcoded list)
├── .env                     # Environment file for storing the Cohere API key
├── requirements.txt         # Dependency file for Streamlit Community Cloud deployment
├── venv\                    # Virtual environment folder
│   ├── Scripts\             # Virtual environment scripts (e.g., activate.bat)
│   └── Lib\site-packages\   # Installed Python packages (streamlit, python-dotenv, cohere)
├── README.md                # Stylish project documentation with setup and deployment instructions
├── LICENSE                  # Optional: MIT License file for open-source projects
└── .gitignore               # Optional: Git ignore file for excluding unnecessary files

```



📸 Usage

Enter Your API KeyInput your Cohere API key in the sidebar or ensure it’s in the .env file.

Paste Your EmailPaste the email you want to rewrite in the text area.

Select a Tone and ModelChoose a tone (e.g., Professional) and a Cohere model (e.g., command).

Rewrite and CompareClick "Rewrite Email" to generate the rewritten email. Check "Show changes" to see a diff view.



🛠️ Customization

Add New Tones: Modify the tone options in app.py by updating the st.selectbox for tones:tone = st.selectbox("✍️ Select Tone", ["Professional", "Friendly", "Persuasive", "Apologetic", "Casual"])


Update Models: If Cohere introduces new models, update the model list in api_model_checker.py:models = ["command", "command-light", "new-model"]


Enhance the Prompt: Adjust the prompt in email_rewriter.py to improve rewriting quality:return f"""Rewrite the following email in a {tone.lower()} tone. ..."""




🐛 Troubleshooting

Invalid Cohere API Key: Ensure your API key is correct. Test it using:curl https://api.cohere.ai/v1/chat \
  -H "Authorization: Bearer your-cohere-api-key-here" \
  -H "Content-Type: application/json" \
  -d '{"message": "test", "model": "command", "max_tokens": 5}'


Model Not Found: Verify the model name in email_rewriter.py matches Cohere’s available models (check Cohere Docs).
Deployment Fails on Streamlit Cloud: Ensure requirements.txt is correct and the COHERE_KEY is set in the Advanced Settings.


📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙌 Acknowledgments

Cohere for their amazing NLP API.
Streamlit for making web app development a breeze.
Inspired by tutorials on Cohere’s Blog and Streamlit Docs.


Made with ❤️ by Your Om Choksi
