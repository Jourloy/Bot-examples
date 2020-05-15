import random

from VKbot import Logging as log

class Commands():
    def __init__(self):
        pass
    
    def Answer(self, userText):

        if userText.lower() == 'привет':
            hello = ['Привет', 'Хай', 'Здрасте', 'Приветули']
            number = random.randint(0, len(hello) - 1)

            return hello[number]
        elif userText.lower() == 'спасибо':
            welcome = ['На здоровье', 'Всегда пожалуйста', 'Не за что :)', 'Всегда рад помочь']
            number = random.randint(0, len(hello) - 1)

            return welcome[number]
        elif userText.lower() == 'придумай пароль':
            count = random.randint(12, 18)
            Password = "Ваш пароль: "
            for x in range(count):
                Password += random.choice(
                    list("1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"))
            return Password
        # Далее идет пример команды. Если вы хотите вставить пример кода, то вставляйте его выше этого комментария
        #
        # Обратите внимание, что команда пользователя в коде пишется ОБЯЗАТЕЛЬНО маленькими буквами. 
        # Это сделано для того, чтобы если даже пользователь отправит боту сообщение только из больших букв, то бот все равно мог понять запрос
        # Пример:
        # Пользователь может прислать либо "ПРИВЕТ", либо "ПрИвЕт", либо "привет" и вы хотите чтобы бот отреагировал на каждый вариант запроса
        # Поэтому вместо "пример_команды_пользователя" вы должны вписать только "привет".
        elif userText.lower() == 'пример_команды_пользователя':
            answer = 'Это сообщение, которое бот пришлет в ответ. Обратите внимание, что команда пользователя в коде пишется ОБЯЗАТЕЛЬНО маленькими буквами. Это сделано для того, чтобы если даже пользователь отправит боту сообщение только из больших букв, то бот все равно мог понять запрос.'
            return answer
        # Здесь пример команды заканчивается
        else:
            log.Understand()
            return log.UnderstandMessage()