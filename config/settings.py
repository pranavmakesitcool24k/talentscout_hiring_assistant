"""
Configuration settings for TalentScout Hiring Assistant
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# OpenAI API Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# Application Configuration
APP_CONFIG = {
    "app_name": "TalentScout Hiring Assistant",
    "version": "1.0.0",
    "max_conversation_history": 10,
    "default_questions_count": 5,
}

# Model Configuration
MODEL_CONFIG = {
    "model_name": "gpt-3.5-turbo",
    "temperature": 0.7,
    "max_tokens": 500,
}
