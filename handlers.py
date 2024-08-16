from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from questions import questions
from utils import calculate_result

# Словарь для хранения баллов пользователей
user_scores = {}

# Обработчик команды /start
async def start(update: Update, context: CallbackContext):
    # Приветственное сообщение при запуске бота
    await update.message.reply_text("Привет! Давай узнаем, какое животное тебе подходит!")
    # Инициализация счёта для нового пользователя
    user_scores[update.effective_user.id] = 0

# Обработчик команды /quiz, который запускает викторину
async def quiz(update: Update, context: CallbackContext):
    # Начинаем викторину с первого вопроса
    await ask_question(update, context, 0)

# Функция для отправки вопроса пользователю
async def ask_question(update: Update, context: CallbackContext, question_index: int):
    # Получаем данные текущего вопроса
    question_data = questions[question_index]
    # Создаем кнопки для каждого варианта ответа
    keyboard = [[InlineKeyboardButton(opt[0], callback_data=f"{question_index}-{opt[1]}")] for opt in question_data["options"]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Отправляем вопрос и кнопки пользователю
    await update.message.reply_text(question_data["question"], reply_markup=reply_markup)

# Обработчик для кнопок с ответами
async def button(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()  # Подтверждение нажатия кнопки

    # Извлекаем индекс вопроса и баллы из нажатой кнопки
    question_index, score = map(int, query.data.split("-"))
    # Обновляем счет пользователя
    user_scores[query.from_user.id] += score

    # Если есть ещё вопросы, задаем следующий
    if question_index + 1 < len(questions):
        await ask_question(query, context, question_index + 1)
    else:
        # Если вопросы закончились, рассчитываем результат
        result = calculate_result(user_scores[query.from_user.id])
        # Отправляем результат (текст и изображение) пользователю
        await query.message.reply_text(result["text"])
        if result["image_path"]:
            await query.message.reply_photo(photo=open(result["image_path"], "rb"))

# Обработчик команды /help для помощи пользователю
async def help_command(update: Update, context: CallbackContext):
    await update.message.reply_text("Этот бот поможет тебе узнать твоё тотемное животное!")