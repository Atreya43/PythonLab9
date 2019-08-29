#Lambda Function
print("1)Adding two numbers using Lambda Function:");

l=lambda a,b: a+b
ans=l(5,4);

print("Addition=",ans);
print("----------------------------------------------------");
print("2)Multiplication using lambda function");

a=int(input("Enter the value1="));
b=int(input("Enter the value2="));

m=lambda a,b:a*b
mul=m(a,b);
print("Multiplication of ",a,"and",b,"=",mul);
print("----------------------------------------------------");

print("3)Lambda functiion that returns even numbers from the list");

l=[1,2,3,4,5,6,7,8,9,10];
print(l);
lst=list(filter(lambda x: (x%2==0),l));
print("Even numbers are",lst);
lst2=list(filter(lambda y: (y%2!=0),l));
print("Odd Numbers are:",lst2);
print("----------------------------------------------------");
