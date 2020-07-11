# The first step is to generate lists of Letters

Ualpha = list("ABECDEFGHIJKLMNOPQRSTUVWXYZ")
Lalpha = list("abcdefghijklmnopqrstuvwxyz")
num = list("1234567890")

Password = list(input('Type password here'))
Key = list(input('Type Key here'))
key_len = len(Key)
pas_len = len(Password)

for i in range(pas_len):
    if 'Password[i]' in Ualpha:
        Ualpha.find(str(Password[i]))

    if 'Password[i]' in Lalpha:
        Lalpha.find('Password[i]')

    if 'Password[i]' in num:
        num.find('Password[i]')