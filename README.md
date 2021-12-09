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

def sum2Number(a : int, b : int) -> int:
    if(a < 0 or b < 0):
        raise ValueError("sumCulator can add only positive (+ zero) numbers")
    if(a > 4 or b > 4):
        raise ValueError("sumCulator can add only numbers, not more than 4")

    if(a == 0 and b == 0):
        return 0
    if(a == 0 and b == 1):
        return 1
    if(a == 0 and b == 2):
        return 2
    if(a == 0 and b == 3):
        return 3
    if(a == 0 and b == 4):
        return 4
    if(a == 1 and b == 0):
        return 1
    if(a == 1 and b == 1):
        return 2
    if(a == 1 and b == 2):
        return 3
    if(a == 1 and b == 3):
        return 4
    if(a == 1 and b == 4):
        return 5
    if(a == 2 and b == 0):
        return 2
    if(a == 2 and b == 1):
        return 3
    if(a == 2 and b == 2):
        return 4
    if(a == 2 and b == 3):
        return 5
    if(a == 2 and b == 4):
        return 6
    if(a == 3 and b == 0):
        return 3
    if(a == 3 and b == 1):
        return 4
    if(a == 3 and b == 2):
        return 5
    if(a == 3 and b == 3):
        return 6
    if(a == 3 and b == 4):
        return 7
    if(a == 4 and b == 0):
        return 4
    if(a == 4 and b == 1):
        return 5
    if(a == 4 and b == 2):
        return 6
    if(a == 4 and b == 3):
        return 7
    if(a == 4 and b == 4):
        return 8

if __name__ == "__main__":
    if(len(sys.argv) != 3):
        print("sumCulator can add only 2 numbers. For example: ")
        print("> python sumCulator.py number1 number2")
        exit()
    a, b = map(int, (sys.argv[1], sys.argv[2]))
    print(sum2Number(a, b))
```

В зависимости от `N`, файл будет занимать разный размер. Примерный размер можно высчитать по формуле: fileSize = ![(N^2/1000000)*48 (см. https://www.wolframalpha.com/input/?i=%28%28N*N%29%2F1000000%29*48)](https://i.imgur.com/4SgQYwR.png) МБ

# Известные проблемы

- Если задать N слишком большим, а потом резко выключить ПК (например, потому что он завис), то файловая система может отреагировать самым непредсказуемым образом.

![error](https://i.imgur.com/bT1KRNY.png)