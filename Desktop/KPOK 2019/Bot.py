import requests
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

vk_session = vk_api.VkApi(token='f1dc08e74f4757ddfc8a358c1c676889d18ee81fa22bb5e52ba76ebc02061dc693add7fcb342513f2a686')

Global_i = 0
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        if event.text == 'Начать':
            vk.messages.send(
                user_id=event.user_id,
                message='Привет! Я твой персональный бот :)', random_id=Global_i)
            Global_i += 1

        elif event.text == 'Привет' or event.text == 'Здрасте' or event.text == 'Здраствуй' or event.text == 'Здорово':
            vk.messages.send(
                user_id=event.user_id,
                message='Привет', random_id=Global_i)
            Global_i += 1
        else: 
            event.text = event.text.split() 
            if len(event.text) >= 3 and event.text[0].lower() == 'зашифровать': 
                word = event.text[1] 
                n = event.text[2] 
                vk.messages.send() 
            elif len(event.type) >= 3 and event.text[0].lower() == 'расшифровать': 
                word = event.text[1] 
                n = event.text[2] 
                vk.messages.send() 
            else:
                vk.messages.send(
                    user_id=event.user_id,
                    message='Не понял :(', random_id=Global_i)
                Global_i += 1
