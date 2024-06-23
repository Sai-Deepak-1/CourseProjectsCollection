
print("before")

try:
    #4 / 0
    print(age)
except NameError as e:
    print("this was a name issue")
    print("Error is :",e)
except ZeroDivisionError:
    print("Can't divide by 0")
except Exception as e:
    print("Something went wrong")

class FirstError(Exception):
    pass

def upper_fun(word):
    if len(word) <= 0:
        raise FirstError("The word has to have at least one letter!")
    return word.upper()

#print(upper_fun(""))

print("after")

try:
    int("nick")
except:
    print("OOPS")