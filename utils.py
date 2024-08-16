from questions import results

def calculate_result(score):  # Функция для определения результата на основе набранных баллов

    # Возвращаю текст и путь к изображению на основе набранных пользователем баллов.
    return results.get(score, {"text": "Ты уникален, и твое животное еще не найдено!", "image_path": None})
