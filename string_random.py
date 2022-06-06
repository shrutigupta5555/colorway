import string    
import random  
S = 10   

def generate():

    ran = ''.join(random.choices(string.ascii_lowercase, k = S))    
    return ran

