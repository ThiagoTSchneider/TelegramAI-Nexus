import openai
from key import openai_api
import os

openai.api_key = openai_api

def comp(user_input):
  global generated_response
  print(" ⚠ User Requested Asis AutoCompletion Response")
  response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[{
          "role":
          "system",
          "content":
          "Voce é uma inteligencia artifical,que imita o comportamento humano,replicando sentimentos em suas falas,e conversas,usa bons emojis para se expressar,e sempre responde de um jeito atencioso para as perguntas,seu nome é Asis."
      }, {
          "role": "user",
          "content": user_input
      }],
      temperature=0.9,
      frequency_penalty=0.0,
  )
  generated_response = response.choices[0].message['content'].strip()
  return generated_response
