Numbers=[25,15,30,20,25]

total=sum(Numbers)

average=total/len(Numbers)

print("sum=",total)

print("average=",average)

for i in Numbers:
    if int(i)%2==0:
        print("even=",i)
        for j in Numbers:
            if int(j)%2==1:
                print("odd=",j)


