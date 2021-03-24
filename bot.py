import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import requests
from getpass import getpass
import time
a = 'vk_access_token_settings=friends,status&vk_app_id=7794757&vk_are_notifications_enabled=0&vk_is_app_user=1&vk_is_favorite=0&vk_language=ru&vk_platform=desktop_web&vk_ref=other&vk_ts=1616562113&vk_user_id=450930906&sign=CFNCsilmtQLacL_hMlFI0diO-e2M6ZQGCMO3MsBGfXY'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 YaBrowser/21.2.4.172 Yowser/2.5 Safari/537.36'
      }
post = requests.get('https://pixel.w84.vkforms.ru/HappySanta/slaves/1.0.0/start', headers={'Authorization': a})
for i in range(646070183, 64607000100):
	try:
		r = requests.post('https://pixel.w84.vkforms.ru/HappySanta/slaves/1.0.0/buySlave',  headers={'Authorization': a}, json = { "slave_id": i })
		print(r)
		r = requests.post('https://pixel.w84.vkforms.ru/HappySanta/slaves/1.0.0/saleSlave',  headers={'Authorization': a}, json = { "slave_id": i })
		print(r)
		r = requests.post('https://pixel.w84.vkforms.ru/HappySanta/slaves/1.0.0/buySlave',  headers={'Authorization': a}, json = { "slave_id": i })
		print(r)
		r = requests.post('https://pixel.w84.vkforms.ru/HappySanta/slaves/1.0.0/saleSlave',  headers={'Authorization': a}, json = { "slave_id": i })
		print(r)
		r = requests.post('https://pixel.w84.vkforms.ru/HappySanta/slaves/1.0.0/buySlave',  headers={'Authorization': a}, json = { "slave_id": i })
		print(r)
		r = requests.post('https://pixel.w84.vkforms.ru/HappySanta/slaves/1.0.0/saleSlave',  headers={'Authorization': a}, json = { "slave_id": i })
		print(r)
		r = requests.post('https://pixel.w84.vkforms.ru/HappySanta/slaves/1.0.0/buySlave',  headers={'Authorization': a}, json = { "slave_id": i })
		print(r)
		requests.post('https://pixel.w84.vkforms.ru/HappySanta/slaves/1.0.0/jobSlave',headers={'Authorization': a}, json = {
	"slave_id": i,
	"name": "Аниме"
} )
		print('succ', i)
		time.sleep(60)
	except:
		print('Lose')
while True:
	time.sleep
	response = requests.get('https://pixel.w84.vkforms.ru/HappySanta/slaves/1.0.0/user',headers={'Authorization': a})
	print(response.content)