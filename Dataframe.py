import json
import pandas as pd


with open("unlableled_intents.json", "r",encoding="utf-8") as file:
  intents = json.load(file)

with open("responses.json","r",encoding="utf") as file:
  responses = json.load(file)

responses_keys  = []
intent_keys = list(intents.keys())
intent_values = list(intents.values())
response_values = list(responses.values())
for intent_key in intent_keys:
  responses_keys.append(f"ans_{intent_key}")


Data = {"intent_keys": intent_keys,
        "intent_values": intent_values,
        "response_keys": responses_keys,
        "response_values": response_values}
DF = pd.DataFrame(Data)

