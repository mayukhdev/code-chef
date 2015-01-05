#include<stdio.h>
#include<stdlib.h>

int max_of_two(int one,int two){
    if (one>two)
        return 1;
    else
        return 2;
}

int main(void){

    int n,*lead,i,*win;
    int one,two,max,one_total=0,two_total=0;
    scanf("%d",&n);
    lead = (int*)malloc(sizeof(int)*n);
    win = (int*)malloc(sizeof(int)*n);
    
    for(i=0;i<n;i++){
        scanf("%d %d",&one,&two);
        one_total+=one;
        two_total+=two; 
        lead[i] = abs(one_total-two_total);
        win[i] = max_of_two(one,two);
        if(i==0)
            max = i;
        else if(lead[i]> lead[max])
                max = i;
    }
    
    printf("%d %d",win[max],lead[max]);
    
    return 0;   

}
