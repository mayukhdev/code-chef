#include<stdio.h>
#include<stdlib.h>

void fact2(int n){
    int *a = (int*)malloc(200*sizeof(int));
    int m = 1,temp,index,val,i;
    
    a[0] = 1;
    
    while(n>1){
    /*
        for(i=m-1;i>=0;i--)
            printf("%d",a[i]);
        printf(" x %d , m=%d",n,m);
        printf("\n");
    */    
        index=0;
        temp=0;
        for(i=0;i<m;i++){
            val = a[index]*n + temp;
            a[index] = val%10;
            temp = val/10;
            index+=1;
        }
        
        while(temp>0){
            a[index++] = temp%10;
            temp = temp/10;
            m+=1;
        }
        
        n-=1;
    }
    
    for(i=m-1;i>=0;i--)
        printf("%d",a[i]);
    
        
    free (a);
}


int main(void){

    int t,*arr,i;
    scanf("%d",&t);
    
    arr = (int*)malloc(t * sizeof(int));
    
    for(i=0;i<t;i++)
        scanf("%d",&arr[i]);
    
    //printf("\n");
    for(i=0;i<t;i++){
        fact2(arr[i]);
        if(i!=t-1)
            printf("\n");
    }
        
    free (arr);    
    return 0;
}

