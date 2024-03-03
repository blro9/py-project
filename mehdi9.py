def zaribe3ya5(n):
    if n % 3 == 0 or n % 5 == 0:
        return True
    else:
        return False

sum = 0
for i in range(1,1000):
    #print("cheking", i)
    if zaribe3ya5(i):
        #print('zaribe is fine for', i)
        sum = sum + i
        #print('jame miseh', sum)


print(sum)


#ta qesmat 011 didm bayd 012 ro bbinm :D