usr_input = input("Please enter a string.")

def is_palyndrom(string):
    if len(string)==0:
        return ' IS '
    else:
        if string[0].isalpha():
            if string[-1].isalpha():
                if string[0].lower() == string[-1].lower():
                    return is_palyndrom(string[1:-1])
                else:
                    return ' is not '
            else:
                return is_palyndrom(string[:-1])
        else:
            return is_palyndrom(string[1:])
        
def reverse(string):
    if len(string)==0:
        return string
    else:
        return reverse(string[1:])  + string[0]

print('The reverse of the string provided: ', reverse(usr_input))
print('Your string' + is_palyndrom(usr_input) + 'a palyndrom.')
