#include<stdio.h>
#include<stdlib.h>

#define MAX 10001

int main(void){
	int t,n,i,*arr,*temp,j;
	scanf("%d",&t);
	for(i=0;i<t;i++){
		int value=0,count=0;
		scanf("%d",&n);
		arr = (int*) malloc(sizeof(int)*n);
		for(j=0;j<n;j++)
			scanf("%d",&arr[j]);
		temp = (int*) malloc(sizeof(int)*MAX);			
		for(j=0;j<MAX;j++)
			temp[j] = 0;
			
		for(j=0;j<n;j++)
			temp[arr[j]]+=1;
			
		for(j=0;j<MAX;j++){
			if(temp[j]>count){
				count = temp[j];
				value = j;
			}
		}
		printf("%d %d\n",value,count);
		free(temp);
		free(arr);
	}

	return 0;
}