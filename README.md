# 🎓 EduFlex AI

**EduFlex AI** is a responsible, AI-powered chatbot designed to assist in building **personalized learning platforms** for underprivileged students. It aligns with **Sustainable Development Goal 4 – Quality Education**, by supporting inclusive and adaptive education powered by artificial intelligence.

This project was developed as part of my internship and explores how LLMs can help deliver **scalable, accessible, and personalized education** to those who need it most.

---

## 🎯 Purpose: SDG Goal 4 – Quality Education

EduFlex AI contributes to **Sustainable Development Goal 4** by supporting:

- Adaptive learning systems for individual student needs
- Resource personalization for different learners
- Inclusive platforms for **underprivileged and underserved children**
- AI-driven assessments and feedback systems
- Learning tools for low-resource and multilingual environments

---

## 🧠 What EduFlex Can Do

- Respond to queries related to:
  - Personalized education design
  - Learning platforms and infrastructure
  - AI/ML use in EdTech
  - Python, ML, and UI/UX (if relevant to the platform)
- Reject unrelated queries with a helpful error message
- Stream responses in real time via Chainlit

🛑 **Off-topic questions** (e.g., finance, movies, general Python use) are blocked with this response:  
> `"Error: This assistant is focused on AI-powered personalized learning systems under SDG 4. Please ask a relevant question or clarify how it's connected to the project."`

---

## 🛠 Technologies Used

- [LangChain](https://python.langchain.com/docs/) – Prompt templates and chaining
- [Groq / ChatGroq](https://groq.com/) – LLM API provider (`llama-3.1-8b-instant`)
- [Chainlit](https://github.com/Chainlit/chainlit) – Interactive UI
- [Python](https://www.python.org/) – Backend orchestration
- [dotenv](https://pypi.org/project/python-dotenv/) – Environment management

---

## 🚀 How to Run Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/eduflex-ai.git
````

### 2️⃣ Navigate to the Project Folder

```bash
cd eduflex-ai
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Create `.env` File and Add API Key

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_groq_api_key
```

🗝️ You can get your free API key from [Groq](https://groq.com/)

### 5️⃣ Run the App

```bash
chainlit run app.py -w
```

🔗 The terminal will show a local URL. Open it in your browser to start chatting with **EduFlex AI**.



## 💬 Example Prompts

* *"How can AI personalize learning for rural students?"*
* *"Suggest a Python model for adaptive quiz generation."*
* *"What UI/UX practices are best for low-literacy student interfaces?"*
* *"Can we use ML to track student progress in offline apps?"*



## 📁 Project Structure

```
eduflex-ai/
├── app.py              # Main Chainlit application
├── .env                # API key (not tracked by Git)
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```



## 🎯 Internship Objectives

* Build a topic-restricted assistant using LLMs
* Learn prompt engineering and LangChain workflows
* Deploy a working educational tool interface
* Explore responsible AI aligned with SDGs

