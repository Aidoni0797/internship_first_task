# iDONi тебе очень полезно потому что не знаешь путаешься постоянно високосный не високосный и в итоге
# unixtime неправильный ответ дает
# учись
count = 0
c = 0
for i in range(1970,2010):
    count = 0
    if i%4==0:
        if i%100==0:
            if i%400 ==0:
                count += 1
        else:
            count +=0
    else:
        count +=1
    if count>0:
            c+=1
print(c)

