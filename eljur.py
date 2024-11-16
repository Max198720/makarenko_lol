import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote, quote
import telebot
from telebot import types
import datetime
import random
import os
from make_alive import keep_aliv

def convert(lst):
    res_dict = {}
    for i in range(0, len(lst), 2):
        res_dict[lst[i]] = lst[i + 1]
    return res_dict

import re

bot = telebot.TeleBot('7780683564:AAH6TPRAbAxgNawp-zfkkMEPeKayCR_aXgU')

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0 (Edition Yx GX 03)',}
link = "https://edu.rk.gov.ru/ajaxauthorize"
datas = [{
            "username": "BobikAlexandra",
            "password": "BobikAlexandra",
            "return_uri": "/"
        },
        {
            "username": "galecansona07",
            "password": "123455432131sona",
            "return_uri": "/"
        },
        {
            "username": "katya-1988",
            "password": "rfnz010488",
            "return_uri": "/"
        },
        {
            "username": "natalyNR",
            "password": "inter4329",
            "return_uri": "/"
        }]

status = {"status": None, "id": None}

lessons_names = {
"История": "История",
"Обществознание ": "Обществознание",
"Обществознание": "Обществознание",
"Основы духовно-нравственной культуры народов России": "ОДНКНР",
"Литература": "Литература",
"Русский язык": "Русский язык",
"Иностранный язык (английский)": "Английский язык",
"Физическая культура": "Физ-ра",
"Музыка": "Музыка",
"Изобразительное искусство": "ИЗО",
"Литературное чтение": "Литературное чтение",
"Математика": "Математика",
"Окружающий мир": "Окружающий мир",
"Труд (технология) ": "Технология",
"Труд (технология)  ": "Технология",
"Труд (технология)": "Технология",
"Биология": "Биология",
"Курс по психологии «Основы психологии в школе»": "Основы психологии в школе",
"Курс по русскому языку «От слова – к предложению»": "От слова – к предложению",
"Основы религиозных культур и светской этики": "ОРКСЭ",
"Основы безопасности и защиты Родины": "ОБЗР",
"Курс по химии «Трудные вопросы в органической химии»": "Трудные вопросы в органической химии",
"Химия": "Химия",
"География": "География",
"Курс «Введение в педагогику»": "Введение в педагогику",
"Алгебра": "Алгебра",
"Вероятность и статистика": "Вероятность и статистика",
"Геометрия": "Геометрия",
'Курс по математике "По ступенькам к ОГЭ"': "По ступенькам к ОГЭ",
"Курс по математике «Практикум «Решение задач по геометрии»": "Практикум «Решение задач по геометрии»",
"Математика: алгебра и начала математического анализа": "Математика: алгебра",
"Математика: вероятность и статистика": "Математика: вероятность и статистика",
"Математика: геометрия": "Математика: геометрия",
"Физика": "Физика",
"Курс по обществознанию «Вопросы экономики»": "Вопросы экономики",
"Курс по математике «Решение уравнений, неравенств и их систем»": "Решение уравнений, неравенств и их систем",
'Курс по биологии "Основы медицины"': "Основы медицины",
"Курс по географии «Крымоведение»": "Крымоведение",
"Информатика": "Информатика",
"Информатика ": "Информатика",
"Иностранный язык (английский) ": "Английский язык",
"Иностранный язык (английский)  ": "Английский язык",
"Индивидуальный проект": "Индивидуальный проект"}

ids = {"История": 30,
"Обществознание":302,
"Основы духовно-нравственной культуры народов России":270,
"Литература":34,
"Русский язык":206,
"Иностранный язык (английский)":298,
"Физическая культура":82,
"Музыка":42,
"Изобразительное искусство":278,
"Литературное чтение":166,
"Математика":38,
"Окружающий мир":58,
"Труд (технология)":498,
"Биология":6,
"Курс по психологии «Основы психологии в школе»":338,
"Курс по русскому языку «От слова – к предложению»":442,
"Основы религиозных культур и светской этики":186,
"Основы безопасности и защиты Родины":50,
"Курс по химии «Трудные вопросы в органической химии»":514,
"Химия":90,
"География":10,
"Курс «Введение в педагогику»":438,
"Алгебра":2,
"Вероятность и статистика":430,
"Геометрия":14,
'Курс по математике "По ступенькам к ОГЭ"':510,
"Курс по математике «Практикум «Решение задач по геометрии»":330,
"Математика: алгебра и начала математического анализа":370,
"Математика: вероятность и статистика":458,
"Математика: геометрия":374,
"Физика":86,
"Курс по обществознанию «Вопросы экономики»":434,
"Курс по математике «Решение уравнений, неравенств и их систем»":322,
'Курс по биологии "Основы медицины"':394,
"Курс по географии «Крымоведение»":446,
"Информатика":26,
"Индивидуальный проект":310,
'Курс по математике "По ступенькам к ОГЭ"':510,
'Курс по биологии "Основы медицины"':394}

ids2 = {30: "История",302:"Обществознание",270:"ОДНКНР",34:"Литература",206:"Русский язык",298:"Английский язык",82:"Физ-ра",42:"Музыка",278:"ИЗО",166:"Литературное чтение",38:"Математика",58:"Окружающий мир",498:"Технология",6:"Биология",338:"Основы психологии в школе",442:"От слова – к предложению",186:"ОРКСЭ",50:"ОБЗР",514:"Трудные вопросы в органической химии",90:"Химия",10:"География",438:"Введение в педагогику",2:"Алгебра",430:"Вероятность и статистика",14:"Геометрия",510:'По ступенькам к ОГЭ',330:"Практикум «Решение задач по геометрии»",370:"Алгебра и начала математического анализа",458:"Вероятность и статистика",374:"Геометрия",86:"Физика",434:"Вопросы экономики",322:"Решение уравнений, неравенств и их систем",394:'Основы медицины',446:"Крымоведение",26:"Информатика",310:"Индивидуальный проект",510:'Курс по математике ',394:'Курс по биологии '}

ids_ = []

for id in ids:
    full = list(ids.keys())[list(ids.values()).index(ids[id])]
    short = lessons_names[full]
    ids_.append({"full": full, "short": short, "id": ids[id]})
ids = ids_

main_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
main_markup.add("Инфо", "Правила", "Поставить/убрать оценочку", row_width=2)

@bot.message_handler(content_types=['text'])
def start(message):
    global status
    if message.text == '/start':
        bot.send_message(message.from_user.id, "Ну здарова, хуесос. В общем, хочешь получить оценку по каким-то предметам - пиши сюда, я помогу.", reply_markup=main_markup)
    elif message.text == 'Инфо':
        text = "Ну в общем, был создан бот который может ТЕБЕ, долбаёбу, или другим людям ставить или убирать оценочки. \n\nИСПОЛЬЗОВАТЬ НА СВОЙ СТРАХ И РИСК!!!"    
        bot.send_message(text=text, chat_id=message.from_user.id, entities=[{'offset': text.find("ИСПОЛЬЗОВАТЬ НА СВОЙ СТРАХ И РИСК!!!"), "length": len("ИСПОЛЬЗОВАТЬ НА СВОЙ СТРАХ И РИСК!!!"), 'type': 'bold'}, {'offset': text.find("ИСПОЛЬЗОВАТЬ НА СВОЙ СТРАХ И РИСК!!!"), "length": len("ИСПОЛЬЗОВАТЬ НА СВОЙ СТРАХ И РИСК!!!"), 'type': 'underline'}], reply_markup=main_markup)
    elif message.text == 'Поставить/убрать оценочку':
        if status["status"] == "getting":
            if status["id"] != message.from_user.id:
                bot.send_message(message.from_user.id, "Пидорасы очередь заняли, поэтому подожди немного", reply_markup=main_markup)
                return
            else: 
                bot.send_message(message.from_user.id, "Не спамь уёбище, ты и так очередь занимаешь")
                return
        msg = bot.send_message(text="Получаю данные по классам...\nЖди крч, уёбок =)", chat_id=message.from_user.id)
        status["status"] = "getting"
        status["id"] = message.from_user.id
        session = requests.Session()
        data = random.choice(datas)
        response = session.post(link, data=data, headers=headers)
        response = session.get("https://edu.rk.gov.ru/journal-app/jmode.class", headers=headers)
        response = session.post("https://edu.rk.gov.ru/journal-api-messages-action?method=messages.get_recipient_structure&", headers=headers).json()
        classes = response["structure"][0]["data"][5]["data"]
        classes = list(filter(lambda x: (not re.compile(r'1\w').search(x["name"]) or len(x["name"]) == 3), classes))

        classes_names = []
        for class_ in classes:
            classes_names.append(class_["name"])

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        markup.add(*classes_names, "Отмена")

        bot.delete_message(chat_id=message.from_user.id, message_id=msg.message_id)
        bot.send_message(text="Выбирай класс ёпта", chat_id=message.from_user.id, reply_markup=markup)
        status = {"status": None, "id": None}
        bot.register_next_step_handler(message, choose_class, classes, session)
    elif message.text == 'Правила':
        bot.send_message(text="Первое правило: не упоминать обо мне\nВторое правило: не упоминать нигде обо мне\nТретье правило: не задавать вопросов\nЧетвёртое правило: никогда не задавать вопросов\nПятое правило: Канеки всегда прав", chat_id=message.from_user.id, reply_markup=main_markup)
    else:
        print(message)
def choose_class(message, classes, session):
    if message.text == "Отмена":
        bot.send_message(text="Ну лан", chat_id=message.from_user.id, reply_markup=main_markup)
        return 
    if len(list(filter(lambda x: x["name"] == message.text, classes))) == 0:
        bot.send_message(text="Бля, ты даун?", chat_id=message.from_user.id, reply_markup=main_markup)
        return 
    class_ = list(filter(lambda x: x["name"] == message.text, classes))[0]
    response = session.get(f"https://edu.rk.gov.ru/journal-schedule-action/class.{quote(message.text)}", headers=headers) 
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    lessons = soup.find_all("span", {"class": "schedule-lesson"})
    lessons_ = []
    for lesson in lessons:
        lessons_.append(lesson.contents[0].replace("\xa0", ""))
    lessons_ = list(set(lessons_))
    lessons = []
    for lesson in lessons_:
        if lesson in lessons_names:
            lessons.append(lessons_names[lesson])

    weekdays = []

    days = soup.find_all("div", {"class": "schedule__day__content__column"})

    for i in range(5):
        x = []
        lessons___ = days[i].find_all("span", {"class": "schedule-lesson"})
        lessons__ = []
        for lesson in lessons___:
            lessons__.append(lessons_names[lesson.contents[0].replace("\xa0", "")])
        x = list(set(lessons__))
        weekdays.append(x)

    weekdays.append([])
    weekdays.append([])

    # print(weekdays)


    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(*lessons, "Отмена", row_width=2)
    bot.send_message(text="Выбирай предмет теперь, чё", chat_id=message.from_user.id, reply_markup=markup)
    bot.register_next_step_handler(message, choose_lesson, class_, session, weekdays)
def choose_lesson(message, class_, session, weekdays):
    if message.text == "Отмена":
        bot.send_message(text="Ну лан", chat_id=message.from_user.id, reply_markup=main_markup)
        return
    if (not message.text in lessons_names) and (not message.text in lessons_names.values()):
        bot.send_message(text="Бля, ты даун?", chat_id=message.from_user.id, reply_markup=main_markup)
        return
    lesson = list(filter(lambda x: x["short"] == message.text, ids))[0]
    response = session.post(f"https://edu.rk.gov.ru/journal-api-messages-action?method=messages.get_recipients_list&key1=school&key2=students&key3={quote(class_['key'])}&dep=null", headers=headers).json()
    users = response["user_list"]
    user_names = []
    for user in users:
        user_names.append(f"{user['lastname']} {user['firstname']}")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(*user_names, "Отмена")
    bot.send_message(text="Теперь выбираем человека, которому дадут пизды, лол =)", chat_id=message.from_user.id, reply_markup=markup)
    bot.register_next_step_handler(message, choose_student, users, session, user_names, weekdays, lesson, class_)
def choose_student(message, users, session, user_names, weekdays, lesson, class_):
    if message.text == "Отмена":
        bot.send_message(text="Ну лан", chat_id=message.from_user.id, reply_markup=main_markup)
        return
    if len(list(filter(lambda x: x == message.text, user_names))) == 0:
        bot.send_message(text="Бля, ты даун?", chat_id=message.from_user.id, reply_markup=main_markup)
        return
    user = list(filter(lambda x: (x["firstname"] == message.text.split(" ")[1] and x["lastname"] == message.text.split(" ")[0]), users))[0]
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add("5", "4", "3", "2", "Убрать оценку(если есть)", "Отмена")
    bot.send_message(text="Ну думаю и так понятно, схуяли я вообще что-то объяснять должен?", chat_id=message.from_user.id, reply_markup=markup)
    bot.register_next_step_handler(message, choose_mark, user, session, weekdays, lesson, class_)
def choose_mark(message, user, session, weekdays, lesson, class_):
    if message.text == "Отмена":
        bot.send_message(text="Ну лан", chat_id=message.from_user.id, reply_markup=main_markup)
        return
    try:
        mark = int(message.text)
        if mark > 5 or mark < 2:
            bot.send_message(text="Бля, ты даун?", chat_id=message.from_user.id, reply_markup=main_markup)
            return
    except:
        mark = message.text
        if mark != "Убрать оценку(если есть)":
            bot.send_message(text="Бля, ты даун?", chat_id=message.from_user.id, reply_markup=main_markup)
            return
        else:
            mark = ""
    response = session.get("https://edu.rk.gov.ru/journal-app", headers=headers)
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    sp = soup.find("div", {"id": "periods-context-button"}).get_text().replace("\n", "")
    dates = []
    for i in range(10):
        dates.append(datetime.datetime.now() - datetime.timedelta(days=i))
    dates_ = []
    con_dates = []
    for i in dates:
        if lesson["short"] in weekdays[i.weekday()]:
            con_date = i.strftime("%d %b %Y").replace("Jan", "Января").replace("Feb", "Февраля").replace("Mar", "Марта").replace("Apr", "Апреля").replace("May", "Мая").replace("Sep", "Сентября").replace("Oct", "Октября").replace("Nov", "Ноября").replace("Dec", "Декабря")
            dates_.append({"con_date": f"{con_date}", "date": f"{i.strftime('%Y-%m-%d')}"})
            con_dates.append(con_date)
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(*con_dates, "Отмена")
    if (list(filter(lambda x: x["id"] == lesson["id"], ids))[0]["short"] == 'По ступенькам к ОГЭ' or list(filter(lambda x: x["id"] == lesson["id"], ids))[0]["short"] == 'История') and class_["name"][0] == '9':
        text = 'Дату на которую ставить выбирай.\n\nВАЖНАЯ ИНФА!!!\nНЕ РЕКОМЕНДУЮ ставить оценки по истории и "По ступенькам к ОГЭ" на тот день недели, в который они меняются\nИНАЧЕ ПРОИЗОЙДЁТ ПИЗДЕЦ\nВ общем, проверяйте дату'
        bot.send_message(text=text, chat_id=message.from_user.id, reply_markup=markup, entities=[{'offset': text.find("ВАЖНАЯ ИНФА!!!"), "length": len("ВАЖНАЯ ИНФА!!!"), 'type': "bold"}, {'offset': text.find("НЕ РЕКОМЕНДУЮ"), "length": len("НЕ РЕКОМЕНДУЮ"), 'type': "underline"}, {'offset': text.find("ИНАЧЕ ПРОИЗОЙДЁТ ПИЗДЕЦ"), "length": len("ИНАЧЕ ПРОИЗОЙДЁТ ПИЗДЕЦ"), 'type': "bold"}])
    else: bot.send_message(text="Дату на которую ставить выбирай", chat_id=message.from_user.id, reply_markup=markup)
    bot.register_next_step_handler(message, choose_date, class_, con_dates, dates_, lesson, user, mark, sp, session)
def choose_date(message, class_, con_dates, dates_, lesson, user, mark, sp, session):
    if message.text not in con_dates:
        bot.send_message(text="Бля, ты даун?", chat_id=message.from_user.id, reply_markup=main_markup)
        return
    date = list(filter(lambda x: x["con_date"] == message.text, dates_))[0]["date"]
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add("Ебашь", "Я всё перепутал нахуй")
    text = "Делаем?\n\n"
    text += f"Класс: {class_['name']}\n"
    text += f"Предмет: {lesson['full']}\n"
    text += f"Ученик: {user['lastname']} {user['firstname']}\n"
    if mark == "":
        text += f"Оценка: убрать\n"
    else:
        text += f"Оценка: {mark}\n"
    date_text = message.text
    text += f"Дата: {date_text}"
    bot.send_message(text=text, chat_id=message.from_user.id, reply_markup=markup)
    bot.register_next_step_handler(message, confirm, user, lesson, mark, date, sp, session, class_, date_text)
def confirm(message, user, lesson, mark, date, sp, session, class_, date_text):
    if message.text == "Я всё перепутал нахуй":
        bot.send_message(text="Ну и иди нахуй тогда", chat_id=message.from_user.id, reply_markup=main_markup)
        return
    url = f"https://edu.rk.gov.ru/journal-index-rpc-teacher-action?method=teacher.set_mark&lesson_id={lesson['id']}&student={user['id']}&date={date}&num=&nm=0&mark={mark}&type=0&grp=0&sp={quote(sp)}&load_id=&miss_type=none&miss_minutes=0&need_update_avg_cw_year=0"
    data_= quote('comment=false&avg_info=[{"uid":' + user["id"] + ',"avg":,"na_miss":false,"na_mark":true,"last_two":false,"sum":,"max":0,"deuce_list":[]}]')
    set_mark = session.post(url, data_, headers=headers).json()
    if set_mark['result'] == True: bot.send_message(text="Готово, с тебя минет", chat_id=message.from_user.id, reply_markup=main_markup)
    else: bot.send_message(text="Произошёл крч какой-то пиздец и нихуя не получилось\nПопробуй заново, мб получится", chat_id=message.from_user.id, reply_markup=main_markup)
    un = f"@{message.from_user.username}" if message.from_user.username != None else f"tg://user?id={message.from_user.id}"

    # us = f"tg://user?id={message.from_user.id}"
    text = "Какой-то чел поставил оценку\n\n"
    text += f"Чел: {un}\n"
    text += f"Класс: {class_['name']}\n"
    text += f"Предмет: {lesson['full']}\n"
    text += f"Ученик: {user['lastname']} {user['firstname']}\n"
    text += f"Отметка: убрать\n" if mark == "" else f"Отметка: {mark}\n"
    text += f"Дата: {date_text}"
    bot.send_message(text=text, chat_id=6611556422)
    # bot.send_message(text=text, chat_id=6611556422)
    # bot.send_message(text="привет", chat_id=6611556422, entities=[{"offset": 0, "length": 6, "type": "text_link", "url": f"tg://user?id={message.from_user.id}"}])
    # bot.send_message(text=f"tg://user?id={message.from_user.id}", chat_id=6611556422)

bot.polling(none_stop=True, interval=0)
