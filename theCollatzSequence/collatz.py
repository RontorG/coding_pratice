def collatz(number):
    if number % 2 == 0:
        value = number // 2
        print(value)
    elif number % 2 == 1:
        value = 3 * number + 1
        print(value) 
    return value
    

def valid(intNum, txt=""):
    print(txt)
    while True: 
        try:
            n = int(input(intNum))
            break
        except ValueError:
            print("EU DISSE INTEIRO!!!")
    return n

""" Escrever um programa que  permite o usuário enviar um número
inteiro e continuará chamando a função collatz no número até 
retonranr o valor 1"""

print("O mais simples problema impossível")
num = valid("Digite um número inteiro") 
v = num

while True:
    v = collatz(v)
    if v == 1:
        break
    

