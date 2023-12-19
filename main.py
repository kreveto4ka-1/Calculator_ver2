
a = int(input('Введите число'))
b = input('Введите арифм. знак (+, -, *, **, /)')
c = int(input('Введите число'))
result = 0
if b == '+':
    result += a + c
    print(result)
elif b == '-':
    result += a - c
    print(result)
elif b == '*':
    result += a * c
    print(result)
elif b == '/':
    result += int(a / c) 
    print(result)
elif b == '**':
    result += a ** c
    print(result)
else:
    print('Введен неправильный арифм. знак')