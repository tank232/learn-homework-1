"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например: 
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user_dict() которая с помощью input() просит 
  пользователя ввести вопрос, а затем, если вопрос есть в словаре, 
  программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""
def ask_user_dict():
    dict= {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"}
    question=input()
    print(dict[question])


def ask_user():
    ask_user_dict()
    

    
if __name__ == "__main__":
    ask_user()
