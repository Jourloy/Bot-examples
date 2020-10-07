
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
            print('[LOG] > Bot get request')

    def Understand(self):
        if Settings.LOGGING:
            print('[LOG] > Bot get request, but didn\'n find answer')

    def UnderstandMessage(self):
        return 'Я не совсем понял, что Вы хотели сказать'

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
        if Settings.LOGGING:
            print('[LOG] > Check settings')

        if (Settings.GROUP_TOKEN == None):
            print('[ERROR] > Need group token')
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
            print("""[ERROR] > Error with connect to VK.com.

What you can:
1. Check group token in settings. For example:
   GROUP_TOKEN = "a1s2d3f4g5h6j7k8l9"

2. Check Ethernet connection.

3. Maybe VK.com is not work now, try later.

More info about error:
----------------------------------------------------
{}""".format(Exception))
        else:
            if Settings.LOGGING:
                print("[LOG] > Bot on and ready")
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
    VKbot.Connect()