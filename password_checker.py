#!/usr/bin/env python3
# Alena (@fevourss)

import re
from datetime import datetime
import random


def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 12:
        score += 2
        feedback.append("✅ Длина отличная")
    elif len(password) >= 8:
        score += 1
        feedback.append("⚠️  Нормальная длина")
    else:
        feedback.append("❌ Мало символов")

    if re.search(r'[A-ZА-Я]', password):
        score += 1
        feedback.append("✅ Заглавные есть")
    else:
        feedback.append("❌ Нет заглавных")

    if re.search(r'[a-zа-я]', password):
        score += 1
        feedback.append("✅ Строчные есть")
    else:
        feedback.append("❌ Нет строчных")

    if re.search(r'\d', password):
        score += 1
        feedback.append("✅ Цифры есть")
    else:
        feedback.append("❌ Нет цифр")

    if re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>?/~`|\\]', password):
        score += 1
        feedback.append("✅ Символы есть")
    else:
        feedback.append("❌ Нет символов")

    weak = ['123456', 'password', 'qwerty', '111111', '123123']
    if password.lower() in weak:
        score = 0
        feedback.append("❌❌❌ Слишком простой!")

    if score <= 2:
        strength = "🔴 СЛАБЫЙ"
    elif score == 3:
        strength = "🟠 НОРМ"
    elif score == 4:
        strength = "🟡 ХОРОШО"
    elif score == 5:
        strength = "🟢 ОТЛИЧНО"
    else:
        strength = "💪 СУПЕР"

    return {
        'score': score,
        'max_score': 6,
        'strength': strength,
        'feedback': feedback,
        'length': len(password)
    }


def generate_password():
    import random
    words = ['Кот', 'Солнце', 'Гора', 'Музыка', 'Игра']
    return random.choice(words) + str(random.randint(10, 99)) + random.choice(['!', '@', '#'])


def main():
    print("\n" + "=" * 50)
    print("🔐 ПРОВЕРКА ПАРОЛЯ")
    print("=" * 50)

    while True:
        print("\n1. Проверить")
        print("2. Создать пароль")
        print("3. Советы")
        print("4. Выход")

        choice = input("\nВыбери: ")

        if choice == '1':
            password = input("Твой пароль: ")
            result = check_password_strength(password)

            print(f"\nДлина: {result['length']}")
            print(f"Баллы: {result['score']}/6")
            print(f"Уровень: {result['strength']}")
            print("Советы:")
            for item in result['feedback']:
                print(f"  {item}")

            if input("\nСохранить? (да/нет): ").lower() == 'да':
                filename = f"check_{datetime.now().strftime('%H%M%S')}.txt"
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(f"Дата: {datetime.now()}\n")
                    f.write(f"Баллы: {result['score']}/6\n")
                    for item in result['feedback']:
                        f.write(f"- {item}\n")
                print(f"Сохранено в {filename}")

        elif choice == '2':
            print("\nПримеры паролей:")
            for i in range(3):
                pwd = generate_password()
                print(f"{i + 1}. {pwd}")

        elif choice == '3':
            print("\nСоветы:")
            print("1. Минимум 8 символов")
            print("2. Буквы + цифры + символы")
            print("3. Не использовать имя/дату")

        elif choice == '4':
            print("Пока!")
            break

        else:
            print("Ошибка, попробуй снова")

if __name__ == "__main__":
    main()
