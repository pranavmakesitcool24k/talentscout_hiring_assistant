# TalentScout Hiring Assistant


An AI-powered chatbot designed to streamline the initial candidate screening process for technology recruitment. Developed as part of an AI/ML internship, this project utilizes OpenAI's GPT-3.5 and Streamlit to provide a conversational, intuitive, and GDPR-compliant hiring assistant.

---

## Table of Contents

- [Project Overview](#project-overview)  
- [Features](#features)  
- [Technical Stack](#technical-stack)  
- [Installation & Setup](#installation--setup)  
- [Usage](#usage)  
- [Deployment](#deployment)  
- [Data Privacy & Compliance](#data-privacy--compliance)  
- [Challenges & Learnings](#challenges--learnings)  
- [Future Enhancements](#future-enhancements)  
- [Author](#author)  

---

## Project Overview

TalentScout Hiring Assistant is a conversational AI that assists recruiters by automatically engaging candidates, collecting vital information, understanding their tech skills, and dynamically generating relevant technical questions based on their expertise.

This automation reduces the recruitment cycle time and improves candidate evaluation efficiency by leveraging state-of-the-art natural language processing.

---

## Features

- **Friendly & Professional Greeting**  
- **Comprehensive Data Collection** (Name, Contact info, Experience, Position, Skills)  
- **Dynamic Technical Question Generator** tailored to candidate's tech stack  
- **Context-Aware Conversation Flow** using Streamlit session state  
- **Graceful Exit Options** responding to keywords like "exit", "bye"  
- **Real-Time Sidebar Updates** displaying collected data  
- **GDPR-Compliant Data Handling** with secure storage and anonymization  
- **Fallback Mechanisms** for handling unclear inputs  

---

## Technical Stack

- **Frontend**: Streamlit  
- **Backend/AI**: OpenAI GPT-3.5 API  
- **Data Storage**: JSON with hashing and retention policies  
- **Programming Language**: Python 3.11+  
- **Version Control**: Git/GitHub  

---

## Installation & Setup

### Prerequisites

- Python 3.8 or higher  
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))  
- Git  

### Steps

1. Clone the repository  
   ```bash  
   git clone <repository-url>  
   cd talentscout_hiring_assistant  
   ```  

2. Create virtual environment  
   ```bash  
   python -m venv venv  
   # Activate the environment:  
   # Windows: venv\Scripts\activate  
   # macOS/Linux: source venv/bin/activate  
   ```  

3. Install dependencies  
   ```bash  
   pip install -r requirements.txt  
   ```  

4. Configure environment variables  
   Copy `.env.example` to `.env` and add your OpenAI API key:  
   ```env  
   OPENAI_API_KEY=your-api-key-here  
   ```  

5. Run the app  
   ```bash  
   streamlit run app.py  
   ```  

---

## Usage

- Start the chatbot and follow the prompts.  
- Provide your personal and professional information.  
- Declare your technical skills.  
- Answer 3 to 5 technical questions related to your skills.  
- Exit anytime by typing "exit" or "bye".  

---

## Deployment

This app is ready for deployment on [Streamlit Cloud](https://share.streamlit.io/) for free hosting.

Steps include pushing the code to GitHub and connecting your repository to Streamlit Cloud with your API key set as a secret.

Full deployment instructions are available in the project documentation.

---

## Data Privacy & Compliance

- All candidate data is stored securely with consent timestamps.  
- Data retention is set to 12 months and candidates can request data deletion.  
- Emails are hashed to protect identity.  
- The app complies with GDPR standards for data management.  

---

## Challenges & Learnings

This project helped me gain hands-on experience with:

- Prompt engineering and LLM-based conversational AI  
- Managing stateful conversations with Streamlit  
- Dynamic question generation tailored to user input  
- Secure and compliant data handling in web apps  
- End-to-end application development and deployment  

---

## Future Enhancements

- Sentiment analysis for candidate mood detection  
- Multilingual support for global reach  
- Resume parsing for auto data extraction  
- Interview scheduling integration  
- Advanced analytics dashboard for recruiters  

---

## Project Structure

```
talentscout_hiring_assistant/
├── app.py                      # Main application
├── requirements.txt            # Python dependencies
├── runtime.txt                 # Python version for deployment
├── .env.example                # Environment variables template
├── .gitignore                  # Git ignore rules
├── config/
│   ├── __init__.py
│   └── settings.py             # Configuration settings
├── utils/
│   ├── __init__.py
│   ├── prompt_manager.py       # Prompt engineering module
│   ├── tech_stack_questions.py # Question generation
│   └── data_handler.py         # Data management
└── data/
    └── .gitkeep                # Data directory placeholder
```

---

## Technologies & Tools

- **Streamlit** - Web framework for Python apps
- **OpenAI GPT-3.5** - Large language model for conversational AI
- **Python-dotenv** - Environment variable management
- **JSON** - Data storage format
- **Git/GitHub** - Version control and collaboration

---

## Author

**Pranav Pardeshi**  
Aurangabad, Maharashtra, India  
📧 [imailpranav24k@gmail.com](mailto:imailpranav24k@gmail.com)  

*Developed as part of AI/ML Internship Assignment - October 2025*

---

## License

This project was created for educational and demonstration purposes as part of an internship assignment.

---

## Acknowledgments

- OpenAI for providing the GPT-3.5 API
- Streamlit for the excellent web framework
- PG-AGI for the internship opportunity

---

**⭐ If you found this project helpful, please consider giving it a star on GitHub!**
