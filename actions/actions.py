from rasa_sdk import Action
from rasa_sdk.events import EventType
from groq import Groq
import json

with open("api_keys.json","r") as api_keys:
    api_key = json.load(api_keys)["api_key"]
class ActionAnswerWithModel(Action):
    def __init__(self):
        super().__init__()
        # Load your model (e.g., a question-answering model)
        self.model = Groq(api_key=api_key)
        

    def name(self) -> str:
        return "action_answer_with_model"

    async def run(self, dispatcher, tracker, domain) -> list[EventType]:
        # Extract user question from tracker
        user_question = tracker.latest_message.get("text")
        
        # Use your model to process the input
        result = self.model({
            "question": user_question,
            "context": "Provide relevant context for your model to work."
        })
        
        # Respond with the model's answer
        answer = result.get("answer", "I couldn't find an answer.")
        dispatcher.utter_message(text=answer)

        return []