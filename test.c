#include<stdio.h>
#include "mod.h"

int main(void){

    int n,m;
    scanf("%d%d",&n,&m);
    
    printf("%d",mod(n,m));

    return 0;
}
