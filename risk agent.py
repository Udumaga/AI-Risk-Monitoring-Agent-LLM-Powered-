#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install openai')


# In[25]:


import os
from getpass import getpass
from openai import OpenAI

os.environ["OPENAI_API_KEY"] = getpass("Enter API key: ")
client = OpenAI()


# In[26]:


# Create sample text data
import pandas as pd
data = [
    "Customer data was exposed due to API misconfiguration.",
    "Model shows bias in loan approvals for certain demographics.",
    "System latency increased but no security issues detected."
]

df = pd.DataFrame(data, columns=["text"])


# In[27]:


# Define LLM Risk Detection Function
def analyze_risk(text):
    prompt = f"""
    Analyze the following text and identify:
    1. Type of risk (security, bias, compliance, operational)
    2. Severity (Low, Medium, High)
    3. Brief explanation

    Text: {text}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


# In[28]:


# Apply agentic logic
results = []

for i, text in enumerate(df["text"]):
    print(f"Processing {i+1}/{len(df)}...")
    try:
        result = analyze_risk(text)
    except Exception as e:
        result = f"Error: {e}"
    results.append(result)

df["risk_analysis"] = results


# In[ ]:





# In[ ]:


