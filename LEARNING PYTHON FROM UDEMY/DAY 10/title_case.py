def convert( f_name, l_name):
    if f_name.isalnum()==True & l_name.isalnum()== True:
        a = f_name.title()
        b= l_name.title()
    output= a+" "+b
    return output
f_name = input('enter your first name:')
l_name = input('enter your last name:')
print(convert( f_name, l_name))