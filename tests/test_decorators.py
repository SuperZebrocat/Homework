from typing import Any

import pytest

from src.decorators import log


def test_log_exception(capsys: Any) -> None:
    """Тест на вывод результата в консоль при возникновении исключения"""

    @log(filename="")
    def my_function(x: int, y: int) -> float:
        return x / y

    with pytest.raises(Exception):
        my_function(1, 0)
        captured = capsys.readouterr()
        assert captured.out == "my_function error: division by zero. Inputs: (1, 0), {}\n"


def test_log_func_is_ok(capsys: Any) -> None:
    """Тест на вывод результата в консоль при корректной работе функции"""

    @log(filename="")
    def my_function(x: int, y: int) -> float:
        return x / y

    my_function(1, 1)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n\n"


def test_log_in_file_exception(filename="mylog.txt") -> None:
    """Тест на запись результата в файл при возникновении исключения"""

    @log(filename)
    def my_function(x: int, y: int) -> float:
        return x / y

    my_function(1, 0)
    with open(filename, "r") as file:
        message = file.readlines()[-1]
    assert message == "my_function error: division by zero. Inputs: (1, 0), {}\n"


def test_log_in_file_func_ok(filename="mylog.txt") -> None:
    """Тест на запись результата в файл при корректной работе функции"""

    @log(filename)
    def my_function(x: int, y: int) -> float:
        return x / y

    my_function(1, 1)
    with open(filename, "r") as file:
        message = file.readlines()[-1]
    assert message == "my_function ok\n"
