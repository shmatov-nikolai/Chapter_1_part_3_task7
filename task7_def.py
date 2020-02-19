def Fibo_num(end_number):
    sum = 0
    first_number = 0
    second_number = 1
    
    while 1:
        if sum <= int(end_number):
            print (first_number, end = ' ')
        if second_number > int(end_number):
            end_number = int(input('''
Введите конечное число для построения последовательности ещё раз: 
для выхода, напишите:  9995999 
'''))
            first_number = 0
            second_number = 1
            sum = 0
            if end_number == 9995999:
                break
            
        else:
            print (second_number, end = ' ')
            sum = first_number + second_number
            first_number = sum
            second_number = second_number + sum
       

end_number = Fibo_num(int(input("Введите конечное число для построения последовательности: ")))

