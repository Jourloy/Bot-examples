#Основные библиотеки для работы с ВК
import vk_api
import requests
from vk_api.utils import get_random_id
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

#Другие библиотеки
import re
import os
import sys
import hues
import time
import shutil
import difflib
import asyncio
import traceback
from os.path import isfile

class PreStart():
    def __init__(self):
        self.situation = None
        self.ADD_TOKEN = None
        self.path = str(os.path.dirname(os.path.realpath(__file__)))

    def preStart(self):
        try:
            shutil.copy(self.path+r'\settingsEx.py', self.path+r'\settings.py')
            self.situation = True

        except:
            hues.error("Создание файла настроек провалено")
            traceback.print_exc()
            os.system("pause")
            self.situation = False

        finally:
            return self.situation

class VKbot():
    def __init__(self):
        self.userID = None
        self.log = Settings.LOG_ONLINE
        self.path = str(os.path.dirname(os.path.realpath(__file__)))
        self.set = settings.Settings()

    #Прием сообщений
    async def getEvent(self):
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.text and event.to_me:
                #Получение текстового сообщения

                self.userID = event.user_id
                userID = event.user_id

                if event.text == "Привет":
                    vk.messages.send(
                        user_id=self.userID,
                        random_id=get_random_id(),
                        message="Хеллоу! :)"
                    )

                elif event.text == "Мой ID":
                    vk.messages.send(
                        user_id=self.userID,
                        random_id=get_random_id(),
                        message="Твой ID: " + self.userID
                    )

                elif event.text == "Выключись":
                    vk.messages.send(
                        user_id=self.userID,
                        random_id=get_random_id(),
                        message="Пока :)"
                    )
                    exit()

                else:
                    vk.messages.send(
                        user_id=event.user_id,
                        random_id=get_random_id(),
                        message="Не понятно, что это за просьба :)"
                    )

    #Основной модуль бота
    async def bot(self):
        while True:
            await self.getEvent()

    @property
    def parametrs(self):
        if Settings.TOKEN == "None":
            self.ADD_TOKEN = False
        else:
            self.ADD_TOKEN = True

        return self.ADD_TOKEN

if __name__ ==  '__main__':
    path = str(os.path.dirname(os.path.realpath(__file__)))
    while True:
        if isfile(path+r'\settings.py'):
            import settings

            Settings = settings.Settings()
            VKbot = VKbot()
            token = VKbot.parametrs
            if token:
                session = requests.Session()
                vk_session = vk_api.VkApi(token=Settings.TOKEN)
                vk = vk_session.get_api()
                longpoll = VkLongPoll(vk_session)

                try:
                    print("\n\n")
                    loop = asyncio.get_event_loop()
                    hues.success("Бот включен и находится в активном состоянии")
                    loop.run_until_complete(VKbot.bot())
                except (KeyboardInterrupt, SystemExit):
                    os.system('cls')
                    hues.log("Бот выключен")
                    exit()
            else:
                os.system("cls")
                hues.error("Необходимо добавить TOKEN в файл настроек")
                exit()

        else:
            try:
                start = PreStart()
                situation = start.preStart()
            except (KeyboardInterrupt, SystemExit):
                os.system('cls')
                hues.log("Бот выключен")
                exit()
            except Exception as e:
                print("\n")
                print("----------ОШИБКА----------")
                traceback.print_exc()
                print("--------------------------")
                exit()
