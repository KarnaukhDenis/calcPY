x = float(input('First number: '))
y = float(input('Second number: '))
operation = input('Operation: ')

result = None

if operation == '+':
    result = x + y
elif operation == '-':
    result = x - y
elif operation == '*':
    result = x * y
elif operation == '/':
    result = x / y
elif operation == '%':
    result = x % y
else:
    print('Unsupported operation')

if result is not None:
    print('Result: ', result)


def func():
    if result == 100:
        print('Hello World!!!')


func()
