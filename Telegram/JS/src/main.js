const TelegramBot = require('node-telegram-bot-api');
const settings = require('./settings');

const logging = {
    log: {
        ready: '[LOG] > Bot On and ready',
        getRequest: '[LOG] > Bot get request',
        checkSettings: '[LOG] > Check settings',
    },
    err: {
        groupToken: '[ERROR] > Need group token',
    }
}

/**
 * Generate random password
 * @param {Number} length 
 * @return {String}
 */
function GeneratePassword(length) {
    const str = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM';
    let password = [];
    for (let i = 0; i < length; i++) password.push(GetRandomElementFromArray(str));
    password = password.join('')
    return password
}

/**
 * Return random int between min and max
 * @param {Number} min minimal number
 * @param {Number} max maximal number
 * @returns {Number} random int between min and max
 */
function RandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

/**
 * Return random element from array
 * @param {Array} array 
 */
function GetRandomElementFromArray(array) {
    const element = array[RandomInt(0, array.length-1)];
    return element;
}

function checkFunction() {
    if (settings.logging) console.log(logging.log.checkSettings);
    if (settings.token == undefined) {
        console.log(logging.err.groupToken);
        process.exit(0)
    }
}

checkFunction();

const bot = new TelegramBot(settings.token, {polling: true});
console.log(logging.log.ready);

bot.on('message', (msg) => {
    if (settings.logging) console.log(logging.log.getRequest);
    const chatId = msg.chat.id;
    const text = msg.text.toLowerCase();
    
    if (text == 'пример команды') bot.sendMessage(chatId, `Это пример ответа на команду пользователя. В { } можно вставить любую логику`);
    else if (text == 'придумай пароль') bot.sendMessage(chatId, `Вот ваш пароль: ${GeneratePassword(15)}`);
    else if (text == 'привет') {
        const array = ['привет', 'приветули', 'хелло', 'хаюшки'];
        bot.sendMessage(chatId, `${GetRandomElementFromArray(array)}`);
    }
    else if (text == 'спасибо') {
        const array = ['на здоровье', 'не за что', 'пожалуйста', 'приходи еще'];
        bot.sendMessage(chatId, `${GetRandomElementFromArray(array)}`);
    }
});