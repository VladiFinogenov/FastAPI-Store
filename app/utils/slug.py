import re


def transliterate(text: str) -> str:
    """
    Функция для транслитерации русских букв в английские.
    """
    translit_dict = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
        'е': 'e', 'ё': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i',
        'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
        'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
        'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch',
        'ш': 'sh', 'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '',
        'э': 'e', 'ю': 'yu', 'я': 'ya'
    }

    result = []
    for char in text:
        if char.lower() in translit_dict:
            # Транслитерируем и учитываем регистр
            if char.isupper():
                result.append(translit_dict[char.lower()].capitalize())
            else:
                result.append(translit_dict[char])
        else:
            result.append(char)  # Добавляем символ, если он не найден

    return ''.join(result)


def create_slug(title: str) -> str:
    """
    Функция для создания slug из названия товара.
    """
    # Транслитерируем название
    title = transliterate(title)

    # Удаляем все символы, которые не являются буквой, цифрой или дефисом
    title = re.sub(r'[^a-zA-Z0-9-]', ' ', title)

    # Заменяем пробелы на дефисы и переводим строку в нижний регистр
    slug = title.replace(" ", "-").lower()

    return slug
