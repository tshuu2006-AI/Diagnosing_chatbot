from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from transformers import pipeline

class ActionClassifyIntent(Action):
    def name(self):
        return "action_classify_intent"

    def __init__(self):
        self.classifier = pipeline("text-classification", model="bert-base-uncased")

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        user_message = tracker.latest_message.get("text")
        intent_prediction = self.classifier(user_message)
        predicted_intent = intent_prediction[0]["label"]
        confidence = intent_prediction[0]["score"]

        # Ghi lại câu nếu độ tin cậy thấp 
        if confidence < 0.5:  # Ngưỡng confidence
            with open("unlabeled_data.txt", "a") as f:
                f.write(f"{user_message}\n")
            dispatcher.utter_message(text="Tôi chưa hiểu ý bạn, tôi sẽ học thêm.")
        else:
            dispatcher.utter_message(text=f"Intent dự đoán: {predicted_intent}")