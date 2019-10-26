import datetime
import requests
import vk_api
from bs4 import BeautifulSoup
from random import randint
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType
vk_session = vk_api.VkApi(token='559ca10432ed6e3fa2cb9034cd0eb28ff0543169214692db7e25bafd752c1cabf64d78bfd17eabde0a3ff')
Cities = ['москва', 'санкт-петербург', 'казань', 'новосибирск', 'екатеринбург', 'нижний новгород', 'самара', 'уфа', 'красноярск', 'краснодар', 'сочи']
longpoll = VkLongPoll(vk_session)
p=1
Exit = False
City = ''
greetings = ['привет', 'ку', 'здорово', 'здравствуй']
user_old = dict()
def send(mess):
    vk.messages.send(
        user_id=event.user_id,
        keyboard=StartKeyboard.get_keyboard(),
        message=mess, random_id=randint(0, 2147483647))


def get_names(t, town, used):
    if town == 'москва':
        town = 'msk'
    elif town == 'санкт-петербург':
        town = 'spb'
    elif town == 'казань':
        town = 'kzn'
    elif town == 'новосибирск':
        town = 'nsk'
    elif town == 'екатеринбург':
         town == 'ekb'
    elif town == 'нижний новгород':
        town = 'nnb'
    elif town == 'самара':
        town = 'smr'
    elif town == 'уфа':
        town = 'ufa'
    elif town == 'красноярск':
        town = 'krasnoyarsk'
    elif town == 'краснодар':
        town = 'krd'
    elif town == 'сочи':
        town = 'sochi'
    if t != True:
        links = []
        from random import randint
        page = requests.get('https://kudago.com/' +  town + '/events/')
        soup = BeautifulSoup(page.text, 'html.parser')
        all_list = soup.find_all(class_ = "post-title" )
        mas = []
        for a in all_list:
            links.append('https://kudago.com' + a.find('a').get('href'))
            a =  a.find('span').text.replace(u'\xa0', u' ')
            a = a.replace(u'\u200b\u200b', u' ')
            mas.append(a)
        ans_name = []
        ans_link = []
        
        for i in range(3):
            try:
                for j in range(len(mas)):
                    if mas == ans_name:
                        break
                    elif mas == used:
                        break
                    elif mas[j] in ans_name:
                        continue
                    elif mas[j] in used:
                        continue
                    else:
                        break
                if mas[j] in ans_name or mas[j] in used:
                    ans_name.append('Я не нашёл мероприятие')
                    ans_link.append('прости :(')
                else:
                    used.append(mas[j])
                    ans_name.append(mas[j])
                    ans_link.append(links[j])
            except:
                ans_name.append('Я не нашёл мероприятие')
                ans_link.append('прости :(')
        return [ans_name,ans_link]
    else:
        links = []
        from random import randint
        page = requests.get('https://kudago.com/' + town + '/events/')
        soup = BeautifulSoup(page.text, 'html.parser')
        free_list = soup.find_all(class_ = "post-title-free" )
        mas = []
        for free in free_list:
            links.append('https://kudago.com' + free.find('a').get('href'))
            free =  free.find('span').text.replace(u'\xa0', u' ')
            free = free.replace(u'\u200b\u200b', u' ')
            mas.append(free)
        ans_name = []
        ans_link = []
        for i in range(3):
            try:
                for j in range(len(mas)):
                    if mas == ans_name:
                        break
                    elif mas == used:
                        break
                    elif mas[j] in ans_name:
                        continue
                    elif mas[j] in used:
                        continue
                    else:
                        break
                if mas[j] in ans_name or mas[j] in used:
                    ans_name.append('Я не нашёл мероприятие')
                    ans_link.append('прости :(')
                else:
                    used.append(mas[j])
                    ans_name.append(mas[j])
                    ans_link.append(links[j])
            except:
                ans_name.append('Я не нашёл мероприятие')
                ans_link.append('прости :(')
        return [ans_name,ans_link]


def geo(mas):
    links = mas[1]
    do = mas[0]
    ans = []
    for i in range(3):
        try:
            page = requests.get(links[i])
            soup = BeautifulSoup(page.text, 'html.parser')
            text = str(soup.find(class_ = "addressItem addressItem--single").contents[0])
            text = text.replace('\n','')
            text = text[24:]
            ans.append([do[i], links[i], text])
        except:
            print(do, i)
            ans.append([do[i], links[i]])
    return ans




for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        event.text = event.text.lower()
        for a in Cities:
            if a == event.text:
                Exit = True
        
        if Exit == True or event.text in greetings or event.text == 'start' or event.text == 'пока' or event.text == 'спасибо' or event.text == 'начать' or event.text == 'начало' or event.text == 'все мероприятия' or event.text == 'бесплатное мероприятие' or event.text == 'поменять настройки': # Первый раз
            event.text=event.text.lower()
            if event.text in greetings:
                
                vk = vk_session.get_api()
                StartKeyboard = VkKeyboard(one_time=True)
                StartKeyboard.add_button('Поменять Настройки', color=VkKeyboardColor.NEGATIVE)
                StartKeyboard.add_button('Хочу погулять', color=VkKeyboardColor.POSITIVE)
                send('Привет''&#128075;')
            elif event.text == 'пока':
                send('Пока''&#128533;')
            elif event.text == 'спасибо':
                send('Обращайся''&#128519;')
            elif event.text == 'начать' or event.text == 'начало' or event.text == 'поменять настройки':
                if event.text == 'начать'or event.text == 'начало':
                    user_old[event.user_id] = []
                vk = vk_session.get_api()
                StartKeyboard = VkKeyboard(one_time=True)
                StartKeyboard.add_button('Москва', color=VkKeyboardColor.PRIMARY)
                StartKeyboard.add_button('Санкт-Петербург', color=VkKeyboardColor.DEFAULT)
                StartKeyboard.add_line()
                StartKeyboard.add_button('Казань', color=VkKeyboardColor.DEFAULT)
                StartKeyboard.add_button('Новосибирск', color=VkKeyboardColor.DEFAULT)
                StartKeyboard.add_line()
                StartKeyboard.add_button('Екатеринбург', color=VkKeyboardColor.DEFAULT)
                StartKeyboard.add_button('Нижний Новгород', color=VkKeyboardColor.DEFAULT)
                StartKeyboard.add_line()
                StartKeyboard.add_button('Самара', color=VkKeyboardColor.DEFAULT)
                StartKeyboard.add_button('Красноярск', color=VkKeyboardColor.DEFAULT)
                StartKeyboard.add_line()
                StartKeyboard.add_button('Краснодар', color=VkKeyboardColor.DEFAULT)
                StartKeyboard.add_button('Сочи', color=VkKeyboardColor.DEFAULT)
                send('Выберете город:')


            elif Exit == True:
                Exit = False
                City = event.text
                vk = vk_session.get_api()
                StartKeyboard = VkKeyboard(one_time=True)
                StartKeyboard.add_button('Все мероприятия', color=VkKeyboardColor.DEFAULT)
                StartKeyboard.add_button('Бесплатное мероприятие', color=VkKeyboardColor.PRIMARY)
                send('Выберите формат:')

            if event.text == 'все мероприятия': # Ответил
                vk = vk_session.get_api()
                StartKeyboard = VkKeyboard(one_time=True)
                StartKeyboard.add_button('Хочу погулять', color=VkKeyboardColor.POSITIVE)
                Free = False
                send('Хорошо')

            if event.text == 'бесплатное мероприятие':
                Free = True
                vk = vk_session.get_api()
                StartKeyboard = VkKeyboard(one_time=True)
                StartKeyboard.add_button('Хочу погулять', color=VkKeyboardColor.POSITIVE)
                send('Хорошо')

        elif event.text == 'хочу погулять':
                send('Минутку...')
                StartKeyboard = VkKeyboard(one_time=True)
                StartKeyboard.add_button('1', color=VkKeyboardColor.DEFAULT)
                StartKeyboard.add_button('2', color=VkKeyboardColor.DEFAULT)
                StartKeyboard.add_button('3', color=VkKeyboardColor.DEFAULT)
                StartKeyboard.add_line()
                StartKeyboard.add_button('Поменять Настройки', color=VkKeyboardColor.PRIMARY)
                StartKeyboard.add_button('Хочу погулять', color=VkKeyboardColor.POSITIVE)
                Name = geo(get_names(Free, City, user_old[event.user_id]))
                user_old[event.user_id].append(Name[0][0])
                user_old[event.user_id].append(Name[1][0])
                user_old[event.user_id].append(Name[2][0])
                send('1 - ' + str(Name[0][0]))
                send('2 - ' + str(Name[1][0]))
                send('3 - ' + str(Name[2][0]))

        else:
            if event.text == '1':
                send('Ok')
                if len(Name[0]) == 3:
                    send(Name[0][0] + ': ' + '\n' + Name[0][2] + '\n' + Name[0][1])
                else:
                    send(Name[0][0] + ': ' + '\n' + Name[0][1])
                
            if event.text == '2':
                send('Ok')
                if len(Name[1]) == 3:
                    send(Name[1][0] + ': ' + '\n' + Name[1][2] + '\n' + Name[1][1])
                else:
                    send(Name[1][0] + ': ' + '\n' + Name[1][1])

            if event.text == '3':
                send('Ok')
                if len(Name[2]) == 3:
                    send(Name[2][0] + ': ' + '\n' + Name[2][2] + '\n' + Name[2][1])
                else:
                    send(Name[2][0] + ': ' + '\n' + Name[2][1])
