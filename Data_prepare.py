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
DF_size = len(intent_keys)


if __name__ == "__main__":
  with open("domain.yml","r") as domain:
    domain_data = domain.readlines()

  mark_intents = domain_data.index("intents:\n") + 1
  for intent_key in DF["intent_keys"].tolist():
    domain_data.insert(mark_intents,f"  - {intent_key}\n")

  mark_responses = domain_data.index("responses:\n") + 1
  for i in range(DF_size):
    domain_data.insert(mark_responses,f"  {responses_keys[i]}:\n  - text: \"{response_values[i]}\"\n\n")

  with open("domain.yml","w") as domain:
    domain.writelines(domain_data)

  with open("data/nlu.yml","a") as nlu:
    for i in range(DF_size):
      nlu.write(f"- intent: {intent_keys[i]}\n  examples: |\n")
      for sentence in intent_values[i]:
        nlu.write(f"    - {sentence}\n")
      nlu.write("\n")

  with open("data/stories.yml","a") as stories:
    for i in range(DF_size):
      stories.write(f"- story: {intent_keys[i]}\n  steps:\n")
      stories.write(f"  - intent: {intent_keys[i]}\n  - action: {responses_keys[i]}\n\n")






