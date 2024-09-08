from time import time
from typing import Any


def log(filename: str) -> Any:
    """Функция-декоратор для логирования работы функции с записью результата в файл или выводом в консоль"""

    def wrapper(function: Any) -> Any:
        def inner(*args: Any, **kwargs: Any) -> Any:
            time_1 = time()
            if filename:
                try:
                    result = function(*args, **kwargs)
                    with open(filename, "a") as file:
                        file.write(f"{function.__name__} ok\n")
                    return result
                except Exception as e:
                    with open(filename, "a") as file:
                        file.write(f"{function.__name__} error: {e}. Inputs: {args}, {kwargs}\n")
            else:
                try:
                    result = function(*args, **kwargs)
                    print(f"{function.__name__} ok\n")
                    return result
                except Exception as e:
                    print(f"{function.__name__} error: {e}. Inputs: {args}, {kwargs}\n")
            time_2 = time()
            return time_2 - time_1

        return inner

    return wrapper
