#include<stdio.h>

int main(void){
	
	int a,b,c;
	
	while(scanf("%d%d%d",&a,&b,&c)==3)
	{
	    	if(a>b){
	    	    if(a>c)
	    	        printf("%d ",a);
	    	    else
	    	        printf("%d ",c);
	    	}
	    	else{
	    	    if(b>c)
	    	        printf("%d ",b);
	    	    else
	    	        printf("%d ",c);
	        }
	}
	return 0;
}
