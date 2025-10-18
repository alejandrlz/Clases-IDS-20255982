"""a, b = map(int, input().split())
print(a+b)"""

LEN = int(input())
IDN = int(input())
LCJ = int(input())
ISND = int(input())

if LEN > IDN and LEN > LCJ and LEN > ISND:
    print("LEN")
elif IDN > LEN and IDN > LCJ and IDN > ISND:
    print("IDN")
elif LCJ > LEN and LCJ > IDN and LCJ > ISND:
    print("LCJ")
else:
    print("ISND")