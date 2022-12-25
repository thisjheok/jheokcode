def palindrome(a):
    a=a.lower()
    a=a.replace(' ','')
    if(a==a[::-1]):
        print('True')
    else:
        print('False')
