#include <stdio.h>

int main(){
    int num,num2;
    for(num=1;num<=6;num++){
        for(num2=1;num2<=num;num2++){
            printf("#");
        }
        printf("\n");

    }
    return 0;
}