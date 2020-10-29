#include <stdio.h>

int main(){
    int a,b;
    scanf("%d %d",&a,&b);
    if(a>=b){
        printf("max=%d",a);
    }
    else
    {
        printf("max=%d",b);
    }
    
    return 0;
}