#include<stdio.h>
#include<stdlib.h>

typedef unsigned int uint;

int cmpfunc (const void * a, const void * b)
{
   return ( *(uint*)a - *(uint*)b );
}


int main(void){
    int t,i;
    scanf("%d",&t);
    uint * temp = (uint*)malloc(sizeof(uint)*t); 
    
    for(i=0;i<t;i++)
        scanf("%u",&temp[i]);
    qsort(temp, t , sizeof(uint),cmpfunc);
    
    for(i=0;i<t;i++)
        printf("%u\n",temp[i]);
    
    return 0;
}


