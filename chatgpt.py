
#install this library first  'pip install openai==0.28'

import openai
API_KEY = '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'
openai.api_key = API_KEY
response =openai.ChatCompletion.create(
  model = "gpt-3.5-turbo",
  messages=[
    {"role":"user", "content": "hii i am ameya.who r u?"}
  ]
)
print(response)

