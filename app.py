"""
TalentScout Hiring Assistant Chatbot
AI/ML Intern Assignment - A sophisticated hiring assistant for initial candidate screening
"""

import streamlit as st
import openai
from datetime import datetime
import json
import re
from utils.prompt_manager import PromptManager
from utils.tech_stack_questions import TechStackQuestionGenerator
from utils.data_handler import DataHandler
from config.settings import OPENAI_API_KEY, APP_CONFIG

# Initialize OpenAI API
openai.api_key = OPENAI_API_KEY

# Initialize helper classes
prompt_manager = PromptManager()
question_generator = TechStackQuestionGenerator()
data_handler = DataHandler()


def initialize_session_state():
    """Initialize all session state variables for maintaining conversation context"""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    if "conversation_stage" not in st.session_state:
        st.session_state.conversation_stage = "greeting"
    
    if "candidate_data" not in st.session_state:
        st.session_state.candidate_data = {
            "full_name": None,
            "email": None,
            "phone": None,
            "years_of_experience": None,
            "desired_position": None,
            "current_location": None,
            "tech_stack": [],
            "technical_responses": []
        }
    
    if "current_question_index" not in st.session_state:
        st.session_state.current_question_index = 0
    
    if "technical_questions" not in st.session_state:
        st.session_state.technical_questions = []
    
    if "conversation_active" not in st.session_state:
        st.session_state.conversation_active = True


def check_exit_keywords(user_input):
    """Check if user wants to end the conversation"""
    exit_keywords = ["exit", "quit", "bye", "goodbye", "end chat", "stop", "terminate"]
    return any(keyword in user_input.lower() for keyword in exit_keywords)


def extract_candidate_info(user_input, field):
    """Extract specific information from user input using pattern matching"""
    if field == "email":
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        match = re.search(email_pattern, user_input)
        return match.group(0) if match else None
    
    elif field == "phone":
        phone_pattern = r'\b(?:\+?\d{1,3}[-.\s]?)?(?:\(?\d{3}\)?[-.\s]?)?\d{3}[-.\s]?\d{4}\b'
        match = re.search(phone_pattern, user_input)
        return match.group(0) if match else None
    
    elif field == "years_of_experience":
        experience_pattern = r'(\d+(?:\.\d+)?(?:-\d+)?)\s*(?:years?|yrs?)'
        match = re.search(experience_pattern, user_input.lower())
        return match.group(1) if match else None
    
    return None


def process_user_input(user_input):
    """Process user input based on current conversation stage"""
    stage = st.session_state.conversation_stage
    candidate_data = st.session_state.candidate_data
    
    if check_exit_keywords(user_input):
        st.session_state.conversation_stage = "closing"
        st.session_state.conversation_active = False
        return
    
    if stage == "greeting":
        st.session_state.conversation_stage = "collecting_name"
    
    elif stage == "collecting_name":
        if len(user_input.strip()) > 0:
            candidate_data["full_name"] = user_input.strip()
            st.session_state.conversation_stage = "collecting_email"
    
    elif stage == "collecting_email":
        email = extract_candidate_info(user_input, "email")
        if email:
            candidate_data["email"] = email
            st.session_state.conversation_stage = "collecting_phone"
    
    elif stage == "collecting_phone":
        phone = extract_candidate_info(user_input, "phone")
        if phone:
            candidate_data["phone"] = phone
            st.session_state.conversation_stage = "collecting_experience"
    
    elif stage == "collecting_experience":
        experience = extract_candidate_info(user_input, "years_of_experience")
        if experience:
            candidate_data["years_of_experience"] = experience
            st.session_state.conversation_stage = "collecting_position"
        else:
            numbers = re.findall(r'\d+', user_input)
            if numbers:
                candidate_data["years_of_experience"] = numbers[0]
                st.session_state.conversation_stage = "collecting_position"
    
    elif stage == "collecting_position":
        if len(user_input.strip()) > 0:
            candidate_data["desired_position"] = user_input.strip()
            st.session_state.conversation_stage = "collecting_location"
    
    elif stage == "collecting_location":
        if len(user_input.strip()) > 0:
            candidate_data["current_location"] = user_input.strip()
            st.session_state.conversation_stage = "collecting_tech_stack"
    
    elif stage == "collecting_tech_stack":
        if len(user_input.strip()) > 0:
            tech_items = [item.strip() for item in re.split(r',|;|\band\b', user_input)]
            candidate_data["tech_stack"] = [item for item in tech_items if len(item) > 0]
            
            questions = question_generator.generate_questions(candidate_data["tech_stack"])
            st.session_state.technical_questions = questions
            st.session_state.current_question_index = 0
            st.session_state.conversation_stage = "asking_technical_questions"
    
    elif stage == "asking_technical_questions":
        if st.session_state.current_question_index < len(st.session_state.technical_questions):
            current_q = st.session_state.technical_questions[st.session_state.current_question_index]
            candidate_data["technical_responses"].append({
                "question": current_q,
                "answer": user_input
            })
            
            st.session_state.current_question_index += 1
            
            if st.session_state.current_question_index >= len(st.session_state.technical_questions):
                st.session_state.conversation_stage = "closing"
                st.session_state.conversation_active = False


def get_next_bot_message():
    """Generate the next bot message based on current conversation stage"""
    stage = st.session_state.conversation_stage
    
    if stage == "greeting":
        return prompt_manager.get_greeting_message()
    
    elif stage == "collecting_name":
        return "Great! Let's get started. May I have your full name, please?"
    
    elif stage == "collecting_email":
        return f"Thank you, {st.session_state.candidate_data['full_name']}! What's the best email address to reach you?"
    
    elif stage == "collecting_phone":
        return "Perfect! And what's your phone number?"
    
    elif stage == "collecting_experience":
        return "Got it! How many years of professional experience do you have?"
    
    elif stage == "collecting_position":
        return "Excellent! What position(s) are you interested in applying for?"
    
    elif stage == "collecting_location":
        return "Thanks! Where are you currently located?"
    
    elif stage == "collecting_tech_stack":
        return """Now, let's talk about your technical skills! Please list your tech stack - including programming languages, frameworks, databases, and tools you're proficient in. 

(For example: Python, React, PostgreSQL, Docker, AWS)"""
    
    elif stage == "asking_technical_questions":
        if st.session_state.current_question_index < len(st.session_state.technical_questions):
            question = st.session_state.technical_questions[st.session_state.current_question_index]
            question_num = st.session_state.current_question_index + 1
            total_questions = len(st.session_state.technical_questions)
            return f"**Technical Question {question_num}/{total_questions}:**\n\n{question}"
        else:
            return "Thank you for answering all the technical questions!"
    
    elif stage == "closing":
        data_handler.save_candidate_data(st.session_state.candidate_data)
        
        return f"""Thank you so much for your time, {st.session_state.candidate_data.get('full_name', 'candidate')}! 

We've collected all the necessary information for the initial screening. Our team will review your responses and get back to you within 3-5 business days at {st.session_state.candidate_data.get('email', 'your email')}.

If you're selected for the next round, we'll reach out to schedule a detailed technical interview.

Best of luck with your application! Have a wonderful day! """
    
    return "I'm here to help. How can I assist you?"


def main():
    """Main application function"""
    st.set_page_config(
        page_title="TalentScout Hiring Assistant",
        page_icon="",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    initialize_session_state()
    
    with st.sidebar:
        st.title(" TalentScout")
        st.subheader("Hiring Assistant Bot")
        st.markdown("---")
        
        st.markdown("""
        ### About
        This AI-powered hiring assistant helps TalentScout with initial candidate screening.
        
        ### What I Do:
        -  Collect your basic information
        -  Understand your tech stack
        -  Ask relevant technical questions
        -  Provide a smooth interview experience
        
        ### Privacy Notice:
        Your data is handled securely and in compliance with GDPR regulations.
        """)
        
        st.markdown("---")
        
        if any(v for v in st.session_state.candidate_data.values()):
            st.subheader(" Information Collected:")
            data = st.session_state.candidate_data
            
            if data["full_name"]:
                st.text(f"Name: {data['full_name']}")
            if data["email"]:
                st.text(f"Email: {data['email']}")
            if data["phone"]:
                st.text(f"Phone: {data['phone']}")
            if data["years_of_experience"]:
                st.text(f"Experience: {data['years_of_experience']} years")
            if data["desired_position"]:
                st.text(f"Position: {data['desired_position']}")
            if data["current_location"]:
                st.text(f"Location: {data['current_location']}")
            if data["tech_stack"]:
                st.text(f"Tech Stack: {', '.join(data['tech_stack'])}")
        
        st.markdown("---")
        st.caption("Powered by OpenAI GPT-3.5")
    
    st.title(" TalentScout Hiring Assistant")
    st.markdown("Welcome to TalentScout's AI-powered hiring assistant. I'm here to help with your initial screening!")
    
    chat_container = st.container()
    
    with chat_container:
        if len(st.session_state.messages) == 0:
            greeting = get_next_bot_message()
            st.session_state.messages.append({
                "role": "assistant",
                "content": greeting
            })
        
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
    
    if st.session_state.conversation_active:
        user_input = st.chat_input("Type your response here...")
        
        if user_input:
            st.session_state.messages.append({
                "role": "user",
                "content": user_input
            })
            
            process_user_input(user_input)
            
            bot_response = get_next_bot_message()
            
            st.session_state.messages.append({
                "role": "assistant",
                "content": bot_response
            })
            
            st.rerun()
    else:
        st.info("Conversation has ended. Thank you for your time!")
        
        if st.button("Start New Conversation"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()


if __name__ == "__main__":
    main()
