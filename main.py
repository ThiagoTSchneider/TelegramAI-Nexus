import telebot
import os
import aiogram

from elevenlabs import generate, save
from elevenlabs import set_api_key

from key import elevenlabs_key
from gpt import comp
from key import Telegram_api

set_api_key(elevenlabs_key)
voice_model = "Adam"
Telegram_API = Telegram_api

asis = telebot.TeleBot(Telegram_API, parse_mode='HTML')
print('Asis: {✓} Successfully Connected to Telegram API')


def generate_and_send_audio(chat_id, response):
  print("Initializing Audio Generation\n")
  audio = generate(text=response,
                   voice=voice_model,
                   model='eleven_multilingual_v1')
  save(audio, "Asis.ogg")
  voice = open('Asis.ogg', 'rb')
  asis.send_voice(chat_id, voice,)
  print("Audio Generated, Asis is Free for New Requests\n")


@asis.message_handler(func=lambda message: True)
def handle_all_messages(message):
  user_input = message.text
  response = comp(user_input)
  asis.send_message(message.chat.id, response)
  generate_and_send_audio(message.chat.id, response)
  print('{✓} AsisAutoCompletion Done')


asis.polling()
