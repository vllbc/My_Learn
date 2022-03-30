#include <stdio.h>

int main(){
    int num1,num2;
    scanf("%d %d",&num1,&num2);
    if(num1>=num2){
        printf("max=%d",num1);
    }
    else
    {
        printf("max=%d",num2);
    }
    
    return 0;
}