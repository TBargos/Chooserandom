import random

arr = input("Введите варианты из одного слова, между вариантами поставьте один пробел.\n"
            "По завершении нажмите Enter\n").split()
print(arr[random.randint(0, len(arr)-1)])
