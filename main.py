from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
from config import TELEGRAM_TOKEN
from handlers import start, quiz, button, help_command

if __name__ == '__main__':  # Главная функция, где происходит настройка и запуск бота
    # Создаю приложение и передаю ему токен ZOO-бота
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    # Добавляю обработчики команд и кнопок
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("quiz", quiz))
    app.add_handler(CallbackQueryHandler(button))
    app.add_handler(CommandHandler("help", help_command))

    app.run_polling()  # Запуск бота в режиме polling
