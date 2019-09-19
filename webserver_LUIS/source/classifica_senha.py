

def classifica_senha(pwd):    
    
    if len(pwd) < 8:         
        if any(char.islower() for char in pwd) and any(char.isupper() for char in pwd) and any(char.isdigit() for char in pwd): 
            return 1
        if any(char.islower() for char in pwd) and any(char.isupper() for char in pwd):
            return 1        
        if any(char.isupper() for char in pwd) and any(char.isdigit() for char in pwd):
            return 1    


    if len(pwd) > 8:
        if any(char.islower() for char in pwd) and any(char.isupper() for char in pwd) and any(char.isdigit() for char in pwd): 
            return 2
        if any(char.islower() for char in pwd) and any(char.isupper() for char in pwd):
            return 1
        if any(char.isupper() for char in pwd) and any(char.isdigit() for char in pwd): 
            return 1

    
    return 0
