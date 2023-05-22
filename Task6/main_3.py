# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*
# 385916 -> yes
# 123456 -> no

ticketNumber = int(input('Введите шестизначный номер билета: '))
digit1 = ticketNumber // 100000 
digit2 = ticketNumber // 10000 % 10
digit3 = ticketNumber // 1000 % 10
sum1 = digit1 + digit2 + digit3
digit4 = ticketNumber // 100 % 10
digit5 = ticketNumber // 10 % 10
digit6 = ticketNumber % 10
sum2 = digit4 + digit5 + digit6
if sum1 == sum2:
    print(f'{ticketNumber} -> yes ({digit1} + {digit2} + {digit3} = {digit4} + {digit5} + {digit6})')
else:
    print(f'{ticketNumber} -> no ({digit1} + {digit2} + {digit3} не равно {digit4} + {digit5} + {digit6})')