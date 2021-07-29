#include<stdio.h>
void main()
{
int a,b;
printf("Enter two numbers :");
scanf("%d%d",&a,&b);
a=a+b;
b=a-b;
a=a-b;
printf("Numbers after swapping: a=%d, b= %d ",a,b);
}
