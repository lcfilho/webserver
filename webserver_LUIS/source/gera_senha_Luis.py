import string
import random

def gera_senha(num):
    n=[]
    passwd = ''

    for n in range(int(num)):
        x = random.randint(0, 70)
        passwd = passwd + string.printable[x]
    
    if len(passwd) < 8:
        print('senha abaixo de 8 digitos')
        return False

    if len(passwd) > 16:
        print('senha acima de 16 digitos')
        return False

    return passwd

def valida_senha(passwd):    

     if not any(char.islower() for char in passwd):
         print('senha deve ter pelo menos uma letra minuscula')
         return False

     if not any(char.isupper() for char in passwd):
         print('senha deve ter pelo menos uma letra maiuscula')
         return False

     if not any(char.isdigit() for char in passwd):
         print('senha deve ter pelo menos um numero')
         return False

     return passwd


