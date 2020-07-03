#one.py
def func():
    print("Func() in one.py")

print("Top level in one.py")
print("This is now in sublime text editor")

if __name__ == '__main__':
    print("One.py being run directly!")
else:
    print("one.py has been imported!")
