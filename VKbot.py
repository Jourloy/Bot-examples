
import os
import vk_api
import platform
import requests
import traceback
from vk_api.utils import get_random_id
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

import Settings
import Commands

class Logging():
    def __init__(self):
        pass

    def GetText(self):
        if Settings.LOGGING:
            print('> Бот получил сообщение')

class Utils():
    def __init__(self):
        pass

    def Clear(self):
        if platform.os == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

class PreStart():
    def __init__(self):
        pass

    def CheckSettings(self):
        print('Проверка параметров')

        if (Settings.GROUP_TOKEN == None):
            print('Отсутствует токен группы. Его необходимо вставить в файл настроек. Процесс завершен')
            exit()

class VKbot():
    def __init__(self):
        self.log = Logging()
        self.commands = Commands.Commands()

    def Connect(self):
        try:
            session = requests.Session()
            vk_session = vk_api.VkApi(token=Settings.GROUP_TOKEN)
            vk = vk_session.get_api()
            longpoll = VkLongPoll(vk_session)
        except Exception:
            print("""Произошла ошибка при подключении к ВКонтакте.

Что можно попробовать сделать:
1. Проверьте токен группы в файле настроек. Он должен выглядеть подобно этому:
   GROUP_TOKEN = "a1s2d3f4g5h6j7k8l9"

2. Проверьте подключение к Интернет. Оно должно быть стабильное и желательно не меньше 1 Мбит/сек

3. Возможно ВКонтакте не отвечает на данный момент. Попробуйте чуть позже

Подробности ошибки:
----------------------------------------------------
{}""".format(Exception))
        else:
            print("Бот включен и находится в активном состоянии")
            self.Start(longpoll, vk)
    
    def Start(self, longpoll, vk):
        while 1:
            information = self.WaitText(longpoll)
            self.Response(information, vk)

    def WaitText(self, longpoll):
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.text and event.to_me:
                self.log.GetText()
                return [event.user_id, event.text]

    def Response(self, information, vk):
        userId = information[0]
        userText = information[1]

        responseText = self.commands.Answer(userText)

        vk.messages.send(
            user_id=userId,
            random_id=get_random_id(),
            message=responseText
        )
    

if __name__ == "__main__":
    PreStart = PreStart()
    VKbot = VKbot()

    PreStart.CheckSettings()
    try:
        VKbot.Connect()
    except Exception as e:
        print("""\nПроцесс завершен\n\nПодробности ошибки:\n----------------------------------------------------\n{}""".format(e))