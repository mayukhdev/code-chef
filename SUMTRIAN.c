#include<stdio.h>
#include<stdlib.h>

int main(void){
    int n,num;
    int i,j,k,l;
    int **store;
    scanf("%d",&n);
    
    int *output = (int*) malloc (sizeof(int)*n);
        
    for(i=0;i<n;i++){
        scanf("%d",&num);
        store  = (int**) malloc (sizeof(int*) * num);
        for(k=0;k<num;k++)
            store[k] = (int*) malloc(sizeof(int) * num);
        for(j=0;j<num;j++){
            for(l=0;l<=j;l++)
                scanf("%d",&store[j][l]);
        }
        
        for(j=num-2;j>=0;j--){
            for(l=0;l<=j;l++){
                store[j][l] += (store[j+1][l] > store[j+1][l+1])?store[j+1][l]:store[j+1][l+1];
                //printf("%d ",store[j][l]);
            }
            //printf("\n");
        }
        
        output[i] = store[0][0];
                       
        for (k = 0; k < num; k++) 
            free(store[k]);        
        free(store); 
    }
    
    for(i=0;i<n;i++)
        printf("%d\n",output[i]);
    
    free(output);
    
    return 0;
    
}
