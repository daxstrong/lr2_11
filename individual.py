#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def wrap_in_tag(tag):
    def wrap_string(s):
        return f"<{tag}>{s}</{tag}>"

    return wrap_string


if __name__ == "__main__":
    # Ввод данных
    tag_input = input("Введите тег: ")
    content_input = input("Введите содержимое: ")

    # Создание и использование замыкания
    result_closure = wrap_in_tag(tag_input)
    result = result_closure(content_input)

    # Вывод результата
    print("Результат:", result)
