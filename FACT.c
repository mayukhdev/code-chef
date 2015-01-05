//Trailing 0 problem: positive integer N,Z(N) is the number of zeros at the end of the form of number N!. 
#include<stdio.h>
#include<math.h>
#define MAX 100000

int trail(int n);

int main (void)
{
	int t=0,i,a=0,b=0;
	int n;
	int num[MAX];
	scanf("%d",&t);
	
	for(i=0;i<t;i++)
	{
	    //printf("Enter n");
		scanf("%d",&n);
		num[i]=n;			
	}
	
	printf("\n");
	for(i=0;i<t;i++)
	{
	   a = num[i];
	   b = trail(a); 
	   printf("%d\n",b); 
	}		
}

int trail(int n)
{
    int i,x=0;
    //printf("Hello %d ",n);
    for (i = 1;1;i++)
    {
       if(n/pow(5,i)< 1)
            break;
      else
         x = x + n/pow(5,i); 
       //printf("this is %d",x);
    }
    return x;
}









	
