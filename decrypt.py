Ualpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Lalpha = "abcdefghijklmnopqrstuvwxyz"
num = "0123456789"
# 8Xfgk
Password_enc = input('Type encrypted password here')
Key = input('Type Key here')
key_len = len(Key)
pasenc_len = len(Password_enc)

X = []
for i in range(pasenc_len):
    if Password_enc[i] in Ualpha:
        X.append(Ualpha.find(Password_enc[i]))

    if Password_enc[i] in Lalpha:
        X.append(Lalpha.find(Password_enc[i])+26)

    if Password_enc[i] in num:
        X.append(num.find(Password_enc[i])+52)

print(X)

Y = []
for i in range(key_len):
    if Key[i] in Ualpha:
        Y.append(Ualpha.find(Key[i]))

    if Key[i] in Lalpha:
        Y.append(Lalpha.find(Key[i])+26)

    if Key[i] in num:
        Y.append(num.find(Key[i])+52)



dnc_pass = []
for i in range(pasenc_len):
    diff = (X[i] - Y[i])
    newX = diff
    if newX < 0:
        newX = newX + 61
    print(newX)
    dnc_pass.append(newX)
print(dnc_pass)


decrypt_pass = []
for i in range(len(dnc_pass)):
    if -1 < dnc_pass[i] < 26:
        decoded = Ualpha[dnc_pass[i]]
        decrypt_pass.append(decoded)

    if 25 < dnc_pass[i] < 52:
        decoded = Lalpha[dnc_pass[i]-26]
        decrypt_pass.append(decoded)

    if 52 < dnc_pass[i] < 62:
        decoded = num[dnc_pass[i]-52]
        decrypt_pass.append(decoded)
print(decrypt_pass)