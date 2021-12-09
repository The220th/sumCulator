# sumCulator

Это калькулятор, который умеет складывать 2 числа. Но есть условия:

1. Эти 2 числа не могут быть отрицательными (всё-таки это вычитание, а не сложение).

1. В текущей версии эти 2 числа должны быть не больше, чем `1051`.

# Использование

Чтобы запустить, выполните:

``` bash
> python sumCulator.py number1 number2

# number1 - это первое число

# number2 - это второе число
```

Также `sumCulator` можно использовать как модуль. Например:

``` python
import sumCulator
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    print( sumCulator.sum2Number(1376, 3675) ) # выведет 5051
```

# Системные требования

**RECOMMENDED:**
**Requires a 64-bit processor and operating system**
*OS:*  **Windows 7/8/10 (64 bits), Ubuntu 20.04 LTS**
*Memory:*  **48 ± 16 GB RAM**
*Processor:*  **Intel Core i9-11900KF (5.3 GHz)**
*Storage:*  **100 МB available space**
*Additional Notes:*  **IT MAY TAKE A VERY LONG TIME TO "INITIALIZE" THE `sumCulator`**