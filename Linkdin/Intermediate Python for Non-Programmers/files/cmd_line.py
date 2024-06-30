import sys

# for args in sys.argv:
#     print(args)

# CHallenge : Multiply all Command line arguments
args = sys.argv[1:]
tot = 1
for arg in args:
    try:
        tot = tot*float(arg)
    except Exception as e:
        print(e,"Only Number are allowed")
        sys.exit(1)
print(tot)