#include <stdio.h>

int main(){
    int num1,num2,guess;
    scanf("%d %d\n%d",&num1,&num2,&guess);
    if(num1+num2==guess){
        printf("YES");
    }
    else
    {
        printf("NO");
    }
    
    return 0;
}