# The first step is to generate lists of Letters

Ualpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Lalpha = "abcdefghijklmnopqrstuvwxyz"
num = "0123456789"
spec = "!@#$%^&()_:\"{}<>?\'~`;,.[]=/*-+'|"

Password = input('Type password here:   ')
Key = input('Type Key here:   ')
key_len = len(Key)
pas_len = len(Password)

X = []
for i in range(pas_len):
    if Password[i] in Ualpha:
        X.append(Ualpha.find(Password[i]))

    if Password[i] in Lalpha:
        X.append(Lalpha.find(Password[i])+26)

    if Password[i] in num:
        X.append(num.find(Password[i])+52)

    if Password[i] in spec:
        X.append(spec.find(Password[i])+62)

print(X)

Y = []
for i in range(key_len):
    if Key[i] in Ualpha:
        Y.append(Ualpha.find(Key[i]))

    if Key[i] in Lalpha:
        Y.append(Lalpha.find(Key[i])+26)

    if Key[i] in num:
        Y.append(num.find(Key[i])+52)

    if Key[i] in spec:
        Y.append(spec.find(Key[i])+62)
print(Y)

enc_pass = []
for i in range(pas_len):
    diff = abs(X[i] + Y[i])
    newX = diff
    print(newX)
    if newX > 91:
        newX = newX - 92
    enc_pass.append(newX)
print(enc_pass)

Encrypt_pass = []
for i in range(len(enc_pass)):
    if -1 < enc_pass[i] < 26:
        Encoded = Ualpha[enc_pass[i]]
        Encrypt_pass.append(Encoded)
        print(Encrypt_pass)
    if 25 < enc_pass[i] < 52:
        Encoded = Lalpha[enc_pass[i]-26]
        Encrypt_pass.append(Encoded)
        print(Encrypt_pass)
    if 51 < enc_pass[i] < 62:
        Encoded = num[enc_pass[i]-52]
        Encrypt_pass.append(Encoded)
        print(Encrypt_pass)
    if 61 < enc_pass[i] < 93:
        Encoded = spec[enc_pass[i]-62]
        Encrypt_pass.append(Encoded)
        print(Encrypt_pass)

print(Encrypt_pass)

EncPass = ''.join(Encrypt_pass)
print(EncPass)
print('     ')

input('press any Enter to end the program')