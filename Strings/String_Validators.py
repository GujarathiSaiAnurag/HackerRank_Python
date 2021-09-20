if __name__ == '__main__':
    string = input()
    # string = raw_input()
    l=list(string)
    a,b,c,d,e=False,False,False,False,False
    for i in l:
        if i.isalnum():
            a=True
        if i.isalpha():
            b=True
        if i.isdigit():
            c=True
        if i.islower():
            d=True
        if i.isupper():
            e=True
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    
# ANother_Method :
# s = input()
# print(any(c.isalnum()  for c in s))
# print(any(c.isalpha() for c in s))
# print(any(c.isdigit() for c in s))
# print(any(c.islower() for c in s))
# print(any(c.isupper() for c in s))
