import hashlib 
import random

def hash_md5(pwd):   
    pwd=hashlib.md5(str(pwd).encode('utf-8')).hexdigest()
    return pwd

def hash_sha256(pwd):    
    pwd = hashlib.sha256(str(pwd).encode('utf-8')).hexdigest()
    return pwd
