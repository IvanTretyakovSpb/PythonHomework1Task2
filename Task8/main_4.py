# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

width = int(input('Введите ширину шоколадки: '))
length = int(input('Введите длину шоколадки: '))
numberPieces = int(input('Введите количество отламываемых долек: '))
if numberPieces % width == 0 or numberPieces % length == 0:
    print(f'{width} {length} {numberPieces} -> yes')
else:
    print(f'{width} {length} {numberPieces} -> no')