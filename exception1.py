"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""
def ask_user_dict():
    dict= {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"}
    question=input()
    print(dict[question])

def ask_user():
    while True:
       try:
        ask_user_dict()
       except KeyboardInterrupt:
           print('Пока')
           break
    
if __name__ == "__main__":
    ask_user()
