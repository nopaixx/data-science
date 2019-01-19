import random
import numpy as np
@profile
def  write_sorted_letter(nb_letters=10**7):
    random_string=""
    letter=tuple('abcedefghijklmenopkrstuvwxyz')
    for i in range(nb_letters):
        #aux = random.choice('abcdefghijklemenopkrstuwvz')
        aux=np.random.choice(letters)
        random_string+=aux
    sorted_string = sorted(random_string)

    with  open('sorted_text.txt','w') as sorted_text:
        for character in sorted_string:
            sorted_text.write(character)


write_sorted_letter()




