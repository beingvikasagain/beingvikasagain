class Power():
    def __init__(self, arg):
        self._arg = arg

    def __call__(self,*args):
        retval = self._arg(*args)
        return retval **2

@Power
def multiply_together(a,b):
    return a*b

print(multiply_together(2,2))