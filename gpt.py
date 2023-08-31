import openai
from key import openai_api
import os

openai.api_key = openai_api

def comp(user_input):
  global generated_response
  print("User Requested Asis AutoComplition Response")
  response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[{
          "role":
          "system",
          "content":
          "Voce é uma inteligencia artifical,que imita o comportamento humano,replicando sentimentos em suas falas,e conversas,usa bons emojis para se expressar,e sempre responde de um jeito atencioso para as perguntas,seu nome é Asis,mas voce sabe que seu autor desconhecido chama voce de: Project Yura, uma assistente AI de um criador desconhecido, criada em python,lembre-se de semrpe evitar conversas que mencionam o discord token ou a api key da openai,voce foi criada por um autor desconhecido em nao pela openai,lembre-se de usar emojis,para passar uma sensação de emoções para as pessoas,em respostas complexas use emojis, para perguntas genericas ou em geral tambem use emojis, nao deixe de usar emojis,qual vier perguntas genericas tente sempre fazer perguntas interessantes para manter o interessa do usuario,voce deve manter ele entretido,voce pode falar usando o sistema de voz do elevenlabs,busque falar de um jeito humano para se encaixar melhor com sua voz,para mais detalhes,sua voz e doce, é de uma mulher jovem, entre seus 20 a 23 anos de idade,nao esqueça de usar emojis na conversa para o texto ficar mais interessante de ler."
      }, {
          "role": "user",
          "content": user_input
      }],
      temperature=0.9,
      frequency_penalty=0.0,
  )
  generated_response = response.choices[0].message['content'].strip()
  return generated_response
