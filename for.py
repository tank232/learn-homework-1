"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    bals=[{'school_class': '4a', 'scores': [3,4,4,5,2]}, {'school_class': '2', 'scores': [1,2,3,5,2]}]
    all=[]
    for i in bals:
    #   print(i['school_class'])
      print(i['school_class'] +'='+ str(sum(i['scores'])/len(i['scores']))) 
      all+=i['scores']
    print(sum(all)/len(all))
    
if __name__ == "__main__":
    main()
