import re


def create_slug(title: str) -> str:
    """
    Функция для создания slug из названия товара.
    """
    # Удаляем все символы, которые не являются буквой, цифрой или дефисом
    title = re.sub(r'[^a-zA-Z0-9-]', ' ', title)

    # Заменяем пробелы на дефисы и переводим строку в нижний регистр
    slug = title.replace(" ", "-").lower()

    return slug