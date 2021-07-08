#Напишите программу, которая считывает целое число и выводит текст, аналогичный приведенному в примере
#(пробелы важны!). Первая строка содержит следующее значение, а вторая строка содержит предыдущее значение введёного
#числа
#Please enter an integer number: 1234
#The next number for the number 1234 is 1235.
#The previous number for the number 1234 is 1233.]

num1=int(input('Please enter an integer number: '))
num2=num1+1
num3=num1-1

print('''
The next number for the number {0} is {1}.
The previous number for the number {0} is {2}.'''.format(num1, num2, num3))
