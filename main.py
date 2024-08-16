from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
from config import TELEGRAM_TOKEN
from handlers import start, quiz, button, help_command

# Главная функция, где происходит настройка и запуск бота
if __name__ == '__main__':
    # Создаем приложение и передаем ему токен нашего бота
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    # Добавляем обработчики команд и кнопок
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("quiz", quiz))
    app.add_handler(CallbackQueryHandler(button))
    app.add_handler(CommandHandler("help", help_command))

    # Запуск бота в режиме polling
    app.run_polling()