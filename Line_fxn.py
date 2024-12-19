# def line(length,character):
#     if character == " ":
#         character = "*"
    

def line(length, character):
    if character == '':
        character = '*'
    print (character[0] * length )


print(line(90, "LOL"))