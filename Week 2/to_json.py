import json
import functools

"""
Функция-декоратор, возвращает преобразованные в json данные
"""


def to_json(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        data = func(*args, **kwargs)
        json_data = json.dumps(data)
        return json_data

    return wrapped
