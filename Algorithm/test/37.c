#include <stdio.h>

int main(){
    float num;
    while(scanf("%f",&num)!=EOF){
        if(num>=0){
            printf("%.2f\n",num);
        }
        else
        {
            printf("%.2f\n",num-num*2);
        }
        

    }

    return 0;
}