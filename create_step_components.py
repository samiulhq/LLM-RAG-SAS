import json
import os


with open("/Users/sinsrn/current_projects/LLM-RAG-SAS/LLM - Azure OpenAI RAG.step") as f:
    step = json.load(f)

# for key in step:
#     print(key)

with open(os.path.join(os.getcwd(),"extras","LLM - Azure Open AI RAG.sas"),"w") as f:
          f.write(step["templates"]["SAS"]
                  )
print("\n")

print(step["ui"])



    

