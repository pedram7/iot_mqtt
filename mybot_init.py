from telegram.ext import *


def handle_start(update, context):
    update.message.reply_text('Hi. Start to you too :) :*')


def handle_whoami(update, context):
    update.message.reply_text('Well... let me guess.\n {}, is that you?'.format(update.message.chat.id))


def main():
    updater = Updater('1815234860:AAHNqiI5pDl0YyIt30qLlJzXZPWbe7rVJNE', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', handle_start))
    dp.add_handler(CommandHandler('whoami', handle_whoami))

    updater.start_polling()
    updater.idle()
    print('Ok. We\'re done here')


if __name__ == '__main__':
    main()
