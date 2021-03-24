import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import requests
from getpass import getpass
import time
vk_session = vk_api.VkApi(token='75b64361c2f4475dbc0d810b7c3c9c753cd5b41686b2ae740b35c034765dbcf8c0a44a1f1e0b7812a894d')
vk = vk_session.get_api()
a = 'vk_access_token_settings=friends,status&vk_app_id=7794757&vk_are_notifications_enabled=0&vk_is_app_user=1&vk_is_favorite=0&vk_language=ru&vk_platform=desktop_web&vk_ref=other&vk_ts=1616562113&vk_user_id=450930906&sign=CFNCsilmtQLacL_hMlFI0diO-e2M6ZQGCMO3MsBGfXY'
while True:
	response = requests.get('https://pixel.w84.vkforms.ru/HappySanta/slaves/1.0.0/start',headers={'Authorization': a})
	balance = response.json()['me']['balance']
	dohod = response.json()['me']['slaves_profit_per_min']
	slaves = response.json()['me']['slaves_count']
	messages = '💵 Баланс: ' + str(balance)+ ' \n💰 Денег в мин: ' + str(dohod)+ ' \n⛓ Всего рабов: ' + str(slaves)
	vk.messages.send(user_id = 450930906, message = messages, random_id = 0)
	print('SUCC')
	time.sleep(1800)
