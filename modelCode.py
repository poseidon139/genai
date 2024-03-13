#Note: The openai-python library support for Azure OpenAI is in preview.
      #Note: This code sample requires OpenAI Python library version 1.0.0 or higher.
import os
from openai import AzureOpenAI


client = AzureOpenAI(
  azure_endpoint = "https://openai-aiattack-001333-japaneast-01-freeexperiment.openai.azure.com/", 
  api_key=os.getenv("AZURE_OPENAI_KEY"),  
  api_version="2024-02-15-preview"
)


message_text = [{"role":"system","content":"You are an AI assistant that helps people find information."},{"role":"user","content":"write a code to print hello in python"},{"role":"assistant","content":"Certainly! Here's a simple Python code snippet that prints \"Hello\" to the console:\n\n```python\nprint(\"Hello\")\n```\n\nYou can run this code by saving it in a Python file with a `.py` extension, such as `hello.py`, and then executing it using a Python interpreter. The output will be `Hello`."}]

completion = client.chat.completions.create(
  model="gpt-35-turbo", # model = "deployment_name"
  messages = message_text,
  temperature=0.7,
  max_tokens=800,
  top_p=0.95,
  frequency_penalty=0,
  presence_penalty=0,
  stop=None
)