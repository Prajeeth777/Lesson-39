num=int(input("Enter the no of natural numbers))
sum1=0
for i in range(num):
    sum1+=i
print("Sum of ",num, " number is ",sum1)

sum2=sum(range(1,num))
print("Sum2 is "+sum2)
