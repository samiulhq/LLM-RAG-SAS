import json
import os

with open(os.path.join(os.getcwd(),"LLM - Azure OpenAI RAG.step")) as step:
  dictt = json.load(step)

with open(os.path.join(os.getcwd(),"build","README_draft.md"),"w") as readme:
  json.dump(dictt["ui"], readme)