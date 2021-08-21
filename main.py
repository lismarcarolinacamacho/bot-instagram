#instalar instabot miniconda: pip install instabot
# para seguir los seguidores de lismarcarolina_
from instabot import Bot

# ruta de instalacion C:\Users\miusuario\miniconda3\Lib\site-packages\instabot\bot
#ejecutar mi bot:  miniconda: python main.py
mi_bot = Bot()
mi_bot.login(username='lismar_carolina', password='miclave')
mi_bot.follow_followers('lismarcarolina_')

