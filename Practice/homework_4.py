l = []
chet = 0
nechet = 0
suma = 0
for i in range(0, 7):
    n = int(int(input()))
    l.append(n)
print(l)
for i in range(0, 7):
    if i // 2 == 0:
        chet += 1
    else:
        nechet += 1
    suma = suma + i
if chet > nechet:
    print(suma)
if nechet > chet:
    print(l[0]*l[3]*l[6])
