# genSumCulator

Это генератор [sumCulator](https://github.com/The220th/sumCulator). Чтобы сгенерировать, выполните:

``` bash
> python genSumCulator.py N [fileName]

# N - максимальное число, которое может суммироваться

# fileName - это опциональный аргумент. Обозначает имя файла, куда сохранится вывод программы
```

Например, если выполнить:

``` bash
> python genSumCulator.py 4 sumCulator

# или

> python genSumCulator.py 4 sumCulator.py
```

то сгенерируется файл `sumCulator.py`, содержимое которого будет:

``` python
import sys
# -*- coding: utf-8 -*-

def sum2Number(a : int, b : int):
    if(a < 0 or b < 0):
        raise ValueError("sumCulator can add only positive (+ zero) numbers")
    if(a > 4 or b > 4):
        raise ValueError("sumCulator can add only numbers, not more than 4")

    if(a == 0 and b == 0):
        print(0)
    if(a == 0 and b == 1):
        print(1)
    if(a == 0 and b == 2):
        print(2)
    if(a == 0 and b == 3):
        print(3)
    if(a == 0 and b == 4):
        print(4)
    if(a == 1 and b == 0):
        print(1)
    if(a == 1 and b == 1):
        print(2)
    if(a == 1 and b == 2):
        print(3)
    if(a == 1 and b == 3):
        print(4)
    if(a == 1 and b == 4):
        print(5)
    if(a == 2 and b == 0):
        print(2)
    if(a == 2 and b == 1):
        print(3)
    if(a == 2 and b == 2):
        print(4)
    if(a == 2 and b == 3):
        print(5)
    if(a == 2 and b == 4):
        print(6)
    if(a == 3 and b == 0):
        print(3)
    if(a == 3 and b == 1):
        print(4)
    if(a == 3 and b == 2):
        print(5)
    if(a == 3 and b == 3):
        print(6)
    if(a == 3 and b == 4):
        print(7)
    if(a == 4 and b == 0):
        print(4)
    if(a == 4 and b == 1):
        print(5)
    if(a == 4 and b == 2):
        print(6)
    if(a == 4 and b == 3):
        print(7)
    if(a == 4 and b == 4):
        print(8)

if __name__ == "__main__":
    if(len(sys.argv) != 3):
        print("sumCulator can add only 2 numbers. For example: ")
        print("> python sumCulator.py number1 number2")
        exit()
    a, b = map(int, (sys.argv[1], sys.argv[2]))
    sum2Number(a, b)
```