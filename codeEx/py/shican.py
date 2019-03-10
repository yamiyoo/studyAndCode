def test(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

test(1,2,11,22,33,kk=44)
