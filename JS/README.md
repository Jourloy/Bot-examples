### Установка:
Чтобы установить бота необходимо:
1. Скачать и установить [npm](https://www.npmjs.com) c официального сайта.
2. Скачайте репозиторий бота в ZIP архиве.
3. Распакуйте ZIP архив **в любое место**.

Дополнительно:
* Необходимо установить все требующиеся модули для npm. Делается это при помощи команды `npm install`, которую необходимо ввести в **cmd**, **powershell** или **любой ваш терминал**, перейдя предварительно в папку с ботом.
* После распаковки необходимо открыть файл `settings.js` и заменить присутствующие там параметры на свои.
____
### Запуск бота:
* Windows: Чтобы запустить бота, вам необходимо открыть **cmd** или **powershell**, затем перейти в папку при помощи команды `cd /ПУТЬ_К_ПАПКЕ` и ввести в командную строку `node index.js`.

* MacOS / Linux: Чтобы запустить бота, вам необходимо открыть **terminal** или **любую вашу консоль**, затем перейти в папку при помощи команды `cd /ПУТЬ_К_ПАПКЕ` и ввести в командную строку `node index.js`.
____
### Добавление новых команд:
Чтобы добавить свою собственную команду или редактировать уже существующую, вам необходимо открыть файл **index.js**.

Для создания своей собственной команды вам нужно скопировать предствленный в файле пример и вставить его перед ним, а после можно отредактировать только что вставленный блок кода.
____
### Измение сообщений выводящихся в консоль:
Чтобы изменить по своему желанию сообщения, которые выводит бот в консоль во время свой работы, вам необходимо открыть файл **indes.js** и найти строчки, отвечающие за вывод информации в консоль.
____
Бот работает на [npm модуле для VK.com](https://github.com/node-vk-bot-api/node-vk-bot-api)