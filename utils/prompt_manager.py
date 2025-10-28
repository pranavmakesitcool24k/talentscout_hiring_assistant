"""
Prompt Manager - Handles all prompts for different conversation stages
"""


class PromptManager:
    """Manages system prompts for different conversation stages"""
    
    def __init__(self):
        self.prompts = {
            "greeting": self._get_greeting_prompt(),
            "information_gathering": self._get_info_gathering_prompt(),
            "tech_stack": self._get_tech_stack_prompt(),
            "technical_questions": self._get_technical_prompt(),
            "closing": self._get_closing_prompt()
        }
    
    def _get_greeting_prompt(self):
        return """You are a professional and friendly AI hiring assistant for TalentScout."""
    
    def _get_info_gathering_prompt(self):
        return """You are collecting essential candidate information for TalentScout."""
    
    def _get_tech_stack_prompt(self):
        return """You are helping candidates articulate their technical skills for TalentScout."""
    
    def _get_technical_prompt(self):
        return """You are asking technical screening questions for TalentScout."""
    
    def _get_closing_prompt(self):
        return """You are concluding the screening conversation for TalentScout."""
    
    def get_system_prompt(self, stage):
        stage_mapping = {
            "greeting": "greeting",
            "collecting_name": "information_gathering",
            "collecting_email": "information_gathering",
            "collecting_phone": "information_gathering",
            "collecting_experience": "information_gathering",
            "collecting_position": "information_gathering",
            "collecting_location": "information_gathering",
            "collecting_tech_stack": "tech_stack",
            "asking_technical_questions": "technical_questions",
            "closing": "closing"
        }
        
        prompt_key = stage_mapping.get(stage, "greeting")
        return self.prompts[prompt_key]
    
    def get_greeting_message(self):
        return """Hello!  Welcome to TalentScout!

I'm your AI hiring assistant, and I'm here to help with the initial screening for technology positions. This conversation will take about 5-10 minutes.

I'll be asking you some questions about:
- Your background and experience
- Your technical skills
- Some technical questions based on your expertise

Feel free to ask questions at any point. If you need to exit, just type 'exit' or 'goodbye'.

Ready to get started? """
