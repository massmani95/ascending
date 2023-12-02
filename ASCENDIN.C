#include<stdio.h>
#include<conio.h>
void main()
{
int i,j,b,*p,a[100],n;
clrscr();
printf("enter n");
scanf("%d",&n);
printf("enter elements");
for(i=0;i<n;i++)
{
scanf("%d",&a[i]);
}
for(i=0;i<n;i++)
{
for(j=i+1;j<n;j++)
{
if(*(a+i)>*(a+j))
{
b=*(a+i);
*(a+i)=*(a+j);
*(a+j)=b;
}
}
}
printf("order is");
for(i=0;i<n;i++)
{
printf("%d",a[i]);
}
getch();
}
