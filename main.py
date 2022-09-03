import random
import re
class CardError(Exception):
    pass

class CardFormatError(CardError):
    pass

class CardAlgorithmError(CardError):
    pass

class words_in_number(CardError):
  pass

class low_len(CardError):
  pass

class err_server(CardError):
  pass

class empty_input(CardError):
  pass



def get_card_number():
    card_number = input("Введите номер карты (16 цифр): ")
    card_number = "".join(card_number.strip().split())
    if card_number.isdigit() and len(card_number) == 16:
        return card_number
    else:
      if card_number =="":
        raise empty_input("Пустой ввод")
      elif card_number.isalnum():
        raise words_in_number("Буквы в номере")
      elif len(card_number)<16:
        raise low_len("Символов меньше 16")
      raise CardFormatError('Неверный формат номера')


def double(x):
    res = x * 2
    if res > 9:
        res = res - 9
    return res


def luhn_algorithm(card):
    odd = map(lambda x: double(int(x)), card[::2])
    even = map(int, card[1::2])
    if (sum(odd) + sum(even)) % 10 == 0:
        return True
    else:
      raise CardAlgorithmError('Недействительный номер карты')


def process():
    while True:

        try:
            number = get_card_number()
            if luhn_algorithm(number):
              if random.randint(1, 6) == 5:
                raise err_server("Ошибка сервера")
              print("Ваша карта обрабатывается...")
              break
            else:
                print("Номер недействителен. Попробуйте снова.")
        except CardError as e:
            print('Ошибка!', e)


process()