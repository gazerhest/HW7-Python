import random
import time

'''
Взяв для проєкту в якості апарата паркомат
'''

def get_spot_number(): # запитує номер паркомісця
    while True:
        user_input = input('Введіть номер паркомісця (до 800): ').strip().lower()
        if user_input == 'exit':
            return None

        try:
            spot_number = int(user_input)
            if 0 < spot_number < 800:
                print(f'Ви обрали паркомісце №{spot_number}')
                return spot_number
            else:
                print('Паркомісце не може бути додатнім числом, або ви ввели число за межами 800')
        except ValueError:
            'Помилка - введіть коректні дані'

def get_park_duration():    # запитує триваість паркування
    while True:
        user_input = input('Введіть кількість годин для паркування (до 48 годин): ').strip().lower()
        if user_input == 'exit':
            return None

        try:
            duration = int(user_input)
            if 1 <= duration <= 48:
                print(f'Тривалість паркування: {duration} год.')
                return duration
            else:
                print('Помилка: ви можете обрати проміжок від 1 до 48 годин')
        except ValueError:
            print('Помилка: введіть коректні дані')

def process_payment(amount): # симулюємо процес оплати
    print(f'До сплати: {amount:.2f} грн.')
    while True:
        user_input = input('Оберіть спосіб оплати: [1] Картка, [2] Готівка: ').strip().lower()
        if user_input == 'exit':
            return None
        if user_input == '1':
            print("Чекаю відповіді від термінала...")
            time.sleep(2)
            print('-> Оплата пройшла успішно!')
            return True
        elif user_input == '2':
            print("...")
            time.sleep(2)
            print("-> Оплата готівкою пройшла успішно!")
            return True
        else:
            print('Невідома опція. Введіть 1, або 2, або exit якщо потрібно повернутись назад')

def print_ticket(spot, duration):
    print('Друк талона...')
    time.sleep(1)

    print("-" * 60)
    print("          ПАРКУВАЛЬНИЙ ТАЛОН")
    print(f"   Місце: {spot}")
    print(f"   Оплачено до: {time.strftime('%H:%M', time.localtime(time.time() + duration * 3600))}")
    print("   Дякуємо, що скористалися нашими послугами!")
    print("-" * 60)

    return True

def interface():
    price_per_hour = 15.0

    while True:
        print("\n" + "=" * 40)
        print("   Вітаємо в паркоматі!")
        print("=" * 40)

        spot_number = get_spot_number()
        if spot_number is None:
            print('Скасування операції. Повернення в головне меню.')
            continue

        duration = get_park_duration()
        if duration is None:
            print('Скасування операції. Повернення в головне меню.')
            continue

        total_cost = duration * price_per_hour

        payment_successful = process_payment(total_cost)
        if not payment_successful:
            print("Операцію скасовано. Повернення в головне меню.")
            continue

        print_ticket(spot_number, duration)

        print("\nНатисніть Enter, щоб почати нову сесію...")
        input()

interface()