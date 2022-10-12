# Учись считать
import random

lowDiapazon = 1                      # Нижняя граница чисел
highDiapazon = 200                   # Верхняя граница чисел
sign = 0                             # Знак операции
playGame = True                      # Главный цикл
count = 0                            # Количество решённых примеров
right = 0                            # Правильные ответы
score = 0                            # Очки


# Вывод-приветствие
print("""   Компьютер составляет пример. Введите ответ.
   Для завершения работы введите STOP или S""")
print("  ", "*" * 40)

# **************************
# Главный цикл игры
# **************************
while (playGame):
    # Сообщаем информацию
    print(f"   Ваши очки: {score}")
    print(f"   Обработано задач: {count}")
    print(f"   Правильных ответов: {right}")
    print("  ", "-" * 20)
        
    # Генерируем математический знак
    # Он у нас закодирован числом:
    # 0 - плюс
    # 1 - минус
    # 2 - умножить
    # 3 - делить
    sign = random.randint(0, 3)

        
    #  ********** СЛОЖЕНИЕ
    if (sign == 0):
        z = random.randint(lowDiapazon, highDiapazon)
        x = random.randint(lowDiapazon, z)
        y = z - x
        if (random.randint(0, 1) == 0):
            print("  ", f"{x} + {y} = ?")
        else:
            print("  ", f"{y} + {x} = ?")

    # *********** ВЫЧИТАНИЕ
    elif (sign == 1):
        x = random.randint(lowDiapazon, highDiapazon)
        y = random.randint(0, x - lowDiapazon)
        z = x - y
        print("  ", f"{x} - {y} = ?")

    # *********** УМНОЖЕНИЕ
    elif (sign == 2):
        x = random.randint(1, (highDiapazon - lowDiapazon) // random.randint(1, highDiapazon // 10) + 1)
        y = random.randint(lowDiapazon, highDiapazon) // x
        z = x * y 
        print("  ", f"{x} * {y} = ?")

    # *********** ДЕЛЕНИЕ
    elif (sign == 3): 
        x = random.randint(1, (highDiapazon - lowDiapazon) // random.randint(1, highDiapazon // 10) + 1)
        y = random.randint(lowDiapazon, highDiapazon) // x
        if (y == 0):
            y = 1 
        x = x * y
        z = x // y
        print("  ", f"{x} / {y} = ?")

    # Блок ввода ответа с проверкой на ошибки
    user = ""
    while (not user.isdigit()
            and user.upper() != "STOP"
            and user.upper() != "S"
            and user.upper() != "Ы"
            and user.upper() != "ЫЕЩЗ"):
        user = input ("   Ваш ответ? ")

        # Проверяем ввод: сначала возможные команды
        if (user.upper() == "HELP"
                or user == "?"
                or user == ","
                or user.upper() == "РУДЗ"):
            # Если число состоит из двух и более цифр, то
            if (z > 9):
                # Находим последнюю цифру числа (z % 10)
                print("  ", f"Последняя цифра ответа {z % 10}")
            else:
                print("   Ответ состоит из одной цифры, подсказка невозможна.")
            # Вычитаем очки за использование подсказки
            score -= 10

        # Команда STOP
        elif (user.upper() == "STOP"
                    or user.upper() == "S"
                    or user.upper() == "Ы"
                    or user.upper() == "ЫЕЩЗ"):
            # Прекращаем игру, следующей итерации mainloop не будет
            playGame = False

        elif (not user.isdigit()):
            print("   Введите пожалуйста число!")
        
        else:
            # Счетчик обработанных вопросов
            count += 1
            if (int(user) == z):
                print("\n   Правильно!\n")
                right += 1       # Увеличиваем правильные ответы
                score += 10      # Увеличиваем очки
            else:
                # Если ответ неправильный, то выполняется этот код
                print(f"\n   Ответ неправильный... Правильно: {z}")
                print(f"   Вы можете ввести команду HELP или ? чтобы увидеть последнюю цифру ответа (-10 очков)\n")
                score -= 20

# *****************************
# КОНЕЦ ГЛАВНОГО ЦИКЛА
# *****************************

# Прощальные надписи
print("  ", "*" * 45)
print("   СТАТИСТИКА ИГРЫ:")
print(f"   Всего примеров: {count}")
print(f"   Правильных ответов: {right}")
print(f"   Неправильных ответов: {count - right}")

# count проверяем обязательно, т.к. в коде есть строка,
# в которой count выступает делителем. Он не должен быть
# равен 0
if (count > 0):
    print(f"   Процент верных ответов: {int(right / count * 100)}%")
else:
    print("   Процент верных ответов: 0%")
print("\n   Возвращайтесь!")
print("\n              Выход - enter")
input()
    # КОНЕЦ
