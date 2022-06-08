from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

from credentials import TOKEN
from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler


def echo(update, context):
    update.message.reply_text(update.message.text)


def start(update, context):
    update.message.reply_text(
        "Привет! Я эхо-бот. Я умею дублировать ваши сообщения!")


def help(update, context):
    update.message.reply_text(
        "Я пока не умею помогать... Я только ваше эхо.")


def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    text_handler = MessageHandler(Filters.text, echo)

    dp.add_handler(text_handler)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
