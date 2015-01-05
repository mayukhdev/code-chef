#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>
#include<math.h>

size_t getInput(){

    char * text;
    int index=0,sign;
    unsigned int size=1;
    char c;
    
    while(isdigit(c=getc(stdin)) || c=='-') {
        sign = (c=='-')?-1:1;
        text = (size==1)?(char*)malloc(size*sizeof(char)):(char*)realloc(text,size*sizeof(char));
        if(text==NULL)
            perror("Error in space");
        size+=1;
        text[index++]= c;
    }
    
    text[index] = '\0';
    
    size_t num = atoi(text);
    free(text);
    
    return sign*num;   
}

void printInt(int n){
    if(n<0) putchar('-');        
    if(n/10!=0) printInt(n/10);
    putchar(n%10 + '0');
}


int main(void){
    size_t n,k,num;
    int i,answer=0;
    
    n = getInput();
    k = getInput();
    
    for(i=0;i<n;i++){   
        num = getInput();
        if(num%k==0)
            answer+=1;  
    }
    
    printInt(answer);
    
    return 0;
}
