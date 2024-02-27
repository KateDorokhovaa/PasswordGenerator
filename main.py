import random
import string

def generate_password(length, use_uppercase, use_digits, use_special_chars):
    # Створюємо список з усіма можливими символами, які можуть бути в паролі
    chars = string.ascii_lowercase  # додаємо малі літери

    if use_uppercase:
        chars += string.ascii_uppercase  # додаємо великі літери
    if use_digits:
        chars += string.digits  # додаємо цифри
    if use_special_chars:
        chars += string.punctuation  # додаємо спеціальні символи

    # Генеруємо пароль, обираючи випадковим чином символи зі списку
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    # Запитуємо користувача про параметри генерації паролю
    length = int(input("Введіть довжину паролю: "))
    use_uppercase = input("Використовувати великі літери? (Так/Ні): ").lower() == 'так'
    use_digits = input("Використовувати цифри? (Так/Ні): ").lower() == 'так'
    use_special_chars = input("Використовувати спеціальні знаки? (Так/Ні): ").lower() == 'так'

    # Генеруємо пароль
    password = generate_password(length, use_uppercase, use_digits, use_special_chars)
    
    # Виводимо пароль на екран
    print("Згенерований пароль:", password)
    
    # Запитуємо користувача, чи він хоче зберегти пароль у файл
    save_to_file = input("Зберегти пароль у файл? (Так/Ні): ").lower() == 'так'
    if save_to_file:
        filename = input("Введіть ім'я файлу для збереження паролю: ")
        with open(filename, 'w') as file:
            file.write(password)
        print("Пароль успішно збережено у файлі", filename)

if __name__ == "__main__":
    main()
