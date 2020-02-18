'''
7. Последовательность Фибоначчи. Программа запрашивает общее количество чисел, после
выводит на экран числа в последовательности Фибониччи до этого числа.
Например:

Введите кол-во чисел: 6
Ответ: 1, 1, 2, 3, 5, 8

(Hint: Последовательность Фибоначчи - это последовательность чисел, где следующее число
в последовательности является суммой двух предыдущих чисел в последовательности.
Последовательность выглядит следующим образом: 1, 1, 2, 3, 5, 8, 13,...)
'''
# def fib(n):
#     if n<3:
#         return 1
#     return fib(n-1) + fib(n-2)


sum = 0
first_number = 0
second_number = 1
end_number = int(input("Введите конечное число для последовательности: "))

while sum <= end_number:
    print (first_number, end = ' ')
    if second_number > end_number:
        break
    else:
        print (second_number, end = ' ')
        sum = first_number + second_number
        first_number = sum
        second_number = second_number + sum