# The first step is to generate lists of Letters

Ualpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Lalpha = "abcdefghijklmnopqrstuvwxyz"
num = "1234567890"

Password = input('Type password here')
Key = input('Type Key here')
key_len = len(Key)
pas_len = len(Password)

X = []
for i in range(pas_len):
    if Password[i] in Ualpha:
        X.append(Ualpha.find(Password[i]))
        print(X)
    if Password[i] in Lalpha:
        X.append(Lalpha.find(Password[i])+26)
        print(X)
    if Password[i] in num:
        X.append(num.find(Password[i])+52)
        print(X)


Y = []
for i in range(key_len):
    if Key[i] in Ualpha:
        y = Ualpha.find(Key[i])
        print(y)
        Y += str(y)
    if Key[i] in Lalpha:
        y = Lalpha.find(Key[i])
        print(y)
        Y += str(y)
    if Key[i] in num:
        y = num.find(Key[i])
        print(y)
        Y += str(y)
print(Y)

