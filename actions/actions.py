from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Text, Dict, List
from groq import Groq
import json
class ActionLowConfidenceFallback(Action):
    def name(self) -> Text:
        return "action_low_confidence_fallback"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        # Retrieve the user's query
        user_message = tracker.latest_message.get("text")

        # Invoke your custom model here
        response = self.call_external_model(user_message)

        # Send the model's response back to the user
        dispatcher.utter_message(text=response)

        #Save the new questions for updating chatbot
        with open("New_questions.txt","a") as New_questions:
          New_questions.write(user_message + "\n")

    def call_external_model(self, query: Text) -> Text:
      #Get the api_key
      with open("api_keys.json","r") as keys_file:
          keys = json.load(keys_file)
      
      #load model
      client = Groq(api_key=keys["groq_api_key"])

      chat_completion = client.chat.completions.create(
          messages=[
              {
                  "role": "system",
                  "content": "Your name is Hoang Sang. You are a helpful and friendly gym assistant."
              },
              {
                  "role": "user",
                  "content": f"{query}",
              }
          ],
          model="llama3-8b-8192",
      )
      response = chat_completion.choices[0].message.content
      return f"I processed your question using an external model:\n '{response}'"