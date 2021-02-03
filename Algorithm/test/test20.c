#include <stdio.h>

int main(){
    int a,b,c,max;
    scanf("%d %d %d",&a,&b,&c);
    if(a >= b && a >=c){
        max = a;
        if(b > c){
            printf("%d %d %d",max,b,c);
        }
        else
        {
            printf("%d %d %d",max,c,b);
        }
        
    }
    if(b >= a && b >=c){
        max = b;
        if(a > c){
            printf("%d %d %d",max,a,c);
        }
        else
        {
            printf("%d %d %d",max,c,a);
        }
        
    }
    if(c >= a && c >=b){
        max = c;
        if(a > b){
            printf("%d %d %d",max,a,b);
        }
        else
        {
            printf("%d %d %d",max,b,a);
        }
        
    }
    return 0;
}