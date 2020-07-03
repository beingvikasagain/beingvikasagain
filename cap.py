
def mydeco(fun):
    def inner(fun):
        print("this is decorator")
        fun(mystr)
    mystr = input("Enter a name: ")
    inner(fun)


@mydeco
def myfun(mystr):
    print("This is function and this is {}".format(mystr))
