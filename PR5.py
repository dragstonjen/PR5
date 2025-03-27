# Завдання 1: Перевірка критичних умов
temperature = float(input("Введіть температуру (°C): "))
humidity = float(input("Введіть вологість (%): "))

if temperature > 30 and humidity > 70:
    print("Активація системи охолодження")
else:
    print("Умови нормальні")

# Завдання 2: Валідація введення користувача
number = input("Введіть число від 1 до 100: ")

if number.isdigit():  
    number = int(number)
    if 1 <= number <= 100:
        print("Введене число коректне")
    else:
        print("Помилковий ввід: число не в межах 1-100")
else:
    print("Помилковий ввід: введене значення не є числом")

# Завдання 3: Відбір кандидатів
age = int(input("Введіть вік кандидата: "))
experience = int(input("Введіть кількість років досвіду: "))
qualification = input("Чи має кандидат спеціальну кваліфікацію? (True/False): ").strip().lower()

# Перетворюємо відповідь користувача на булеве значення
qualification = qualification == "true"

if 25 <= age <= 50 and (experience >= 3 or qualification):
    print("Кандидат відповідає вимогам")
else:
    print("Кандидат не відповідає вимогам")
