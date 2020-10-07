const VkBot = require('node-vk-bot-api');
const settings = require('./settings');

function checkFunction() {
    if (settings.logging) console.log('[LOG] > Check settings');
    if (settings.token == undefined) {
        console.log('[ERROR] > Need group token');
        process.exit(0)
    }
}

checkFunction();

const bot = new VkBot(settings.token);

bot.on((ctx) => { 
    if (settings.logging) console.log('[LOG] > Bot get request');
    const text = ctx.message.body.toLowerCase();
    
    if (text == 'пример_команды') {
        ctx.reply(`Это пример ответа на команду пользователя. В { } можно вставить любую логику`)
    }
});

bot.startPolling(() => { if (settings.logging) console.log('[LOG] > Bot on and ready') });