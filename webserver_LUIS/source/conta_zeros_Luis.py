import re
from string import digits


def conta_zeros(entrada):
    
    entrada2 = ''.join(re.findall(r"[\w\.-]+0[\w\.-]",str(entrada)))
    entrada3 = [int(digits) for digits in entrada2 if digits.isdigit()]
    
    if len(entrada) == 0:
        return False

    if len(entrada) != 0:
        for digits in entrada3:            
            return entrada3.count(0)
        
    return entrada3.count(0)



    


    