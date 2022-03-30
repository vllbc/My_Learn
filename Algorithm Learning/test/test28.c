#include <stdio.h>

int main(){
    int num1,num2;
    char fu;
    scanf("%d %d\n%c",&num1,&num2,&fu);
    switch(fu){
        case '+': printf("%d",num1+num2);break;
        case '-': printf("%d",num1-num2);break;
        case '*': printf("%d",num1*num2);break;
        case '/': printf("%d",num1/num2);break;
    }

    return 0;
}