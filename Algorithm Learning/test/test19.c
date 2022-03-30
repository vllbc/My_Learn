#include <stdio.h>

int main(){
    int a,b,c,m;
    scanf("%d,%d,%d",&a,&b,&c);
    if(a>=b){
        m = a;
    }
    else
    {
        m = b;
    }
    
    if(c>=m){
        m = c;
    }
    printf("max=%d",m);
    return 0;
}