def strToint(s):
    number=''
    for i in s:
        number+=str(ord(i))
    return (number)
print strToint("abc")