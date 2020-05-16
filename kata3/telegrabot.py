from telegram.ext import Updater, CommandHandler

def main():
  tokenbot = open("./bot_token").read()
  updater = Updater(token=tokenbot, use_context=True)
  updater.dispatcher.add_handler(CommandHandler("start", start))
  updater.dispatcher.add_handler(CommandHandler("repite", repite))
  updater.dispatcher.add_handler(CommandHandler("suma", suma))

  updater.start_polling()

  updater.idle()

def start(update, context):
  update.message.reply_text("Ola, zoi un vot")

def repite(update, context):
  update.message.reply_text(update.message.text)

def suma(update, context):
  resultado = int(context.args[0]) + int(context.args[1])
  update.message.reply_text("El resultado es " + str(resultado))

main()
