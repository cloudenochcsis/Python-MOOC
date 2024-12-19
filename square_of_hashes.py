def hash_square(length):
    i = 1
    while i <= length:
        print ("#" * length)
        i += 1
hash_square(3)


#####################

def hash_square(size):
    tows = size
    while tows > 0:
        print("#" * size)
        tows -= 1
 
if __name__ == "__main__":
    hash_square(5)
