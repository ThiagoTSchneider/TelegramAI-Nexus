import telebot
import asyncio
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

bot = telebot.TeleBot(Telegram_API, parse_mode='HTML')
print('{✓} Successfully Connected to Telegram API\n')


def generate_and_send_audio(chat_id, response):
  print(" ⚠ Initializing Audio Generation")
  audio = generate(text=response,
                   voice=voice_model,
                   model='eleven_multilingual_v1')
  save(audio, "Asis.ogg")
  voice = open('Asis.ogg', 'rb')
  bot.send_voice(chat_id, voice,)
  print("{✓} Audio Generated\n")
  print("-> Bot is Free for New Requests <-")


@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
  user_input = message.text
  response = comp(user_input)
  bot.send_message(message.chat.id, response)
  print('{✓} Successfully Generated Response\n')
  generate_and_send_audio(message.chat.id, response)


bot.polling()
