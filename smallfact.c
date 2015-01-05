#include<stdio.h>
#include<math.h>
#define MAX 101

typedef long double LINT; 
LINT fact(LINT  n);
 
int main (void)
{
    
	int t,i;
	int n;
	int num[MAX];
	scanf("%d",&t);
	
	
	
	for(i=0;i<t;i++)
	{
		num[i]=0;			
	}
	
	for(i=0;i<t;i++)
	{
		scanf("%d",&n);
		num[i]=n;			
	}
	
	for(i=0;i<t;i++)
	   printf("%.0Lf\n",fact((LINT)num[i])); 
		
}
 
LINT fact(LINT n)
{
    LINT temp=1.0;

        int i;
        for(i=1;i<=n;i++)
            temp = i*temp; 
     
     return temp;       
}
