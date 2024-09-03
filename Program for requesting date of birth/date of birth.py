# Запрашиваем данные у пользователя
day = int(input("Введите день вашего рождения (число): "))
month = int(input("Введите месяц вашего рождения (число): "))
year = int(input("Введите год вашего рождения: "))

from datetime import datetime

# Функция для определения дня недели
def get_weekday(day, month, year):
    date = datetime(year, month, day)
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    return days[date.weekday()]

# Функция для проверки високосного года
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Функция для определения возраста
def calculate_age(day, month, year):
    today = datetime.now()
    age = today.year - year - ((today.month, today.day) < (month, day))
    return age

# Функция для прорисовки чисел
def print_date_in_stars(day, month, year):
    digits = {
        '0': ["****", "*  *", "*  *", "*  *", "****"],
        '1': ["  * ", " ** ", "  * ", "  * ", " ***"],
        '2': ["*** ", "   *", " ***", "*   ", "****"],
        '3': ["****", "   *", " ***", "   *", "****"],
        '4': ["*  *", "*  *", "****", "   *", "   *"],
        '5': ["****", "*   ", "*** ", "   *", "****"],
        '6': ["****", "*   ", "****", "*  *", "****"],
        '7': ["****", "   *", "  * ", " *  ", "*   "],
        '8': ["****", "*  *", "****", "*  *", "****"],
        '9': ["****", "*  *", "****", "   *", "****"]
    }

    # Конвертируем дату в строку и выводим
    date_str = f"{day:02d} {month:02d} {year:04d}"
    for row in range(5):
        line = ""
        for char in date_str:
            if char == ' ':
                line += "    "
            else:
                line += digits[char][row] + "  "
        print(line)

# Вызов функций
print(f"Вы родились в: {get_weekday(day, month, year)}")
print(f"Это был високосный год: {'да' if is_leap_year(year) else 'нет'}")
print(f"Ваш возраст: {calculate_age(day, month, year)} лет")
print("Дата вашего рождения:")
print_date_in_stars(day, month, year)
