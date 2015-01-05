#include<stdio.h>

int main (void)
{
	int n;
	float bal;
	
	scanf("%d %f",&n,&bal);

	
	 if( (n%5==0) && ((bal-0.5) > (float)n) )
		    printf("%.2f\n",(bal-0.5)-(float)n);
		
	else 
	    printf("%.2f\n",bal);
				
	return 0;
}		
