
from typing import List, Dict
from ollama import chat

class OllamaClient:
    def __init__(self, model: str):
        self.model = model
        self.conversation_history: List[Dict[str, str]] = []

    def send_message(self, message:str) -> str:
        """send a message to ollama and get the response."""
        self.conversation_history.append({"role": "user", "content": message})

        try:
            response = chat(model = self.model, messages=self.conversation_history)
            answer = response["message"]["content"]
            self.conversation_history.append({"role": "assistant", "content": answer})
            return answer
        except Exception as e:
            raise OllamaError(f"Failed to get response: {str(e)}")
        
    def clear_history(self) -> None:
        """Clear the conversation history."""
        self.conversation_history = []

class OllamaError(Exception):
    pass