#include <stdio.h>
int main(){
    int intt;
    scanf("%d",&intt);
    int a,b,c;
    a = intt/100;/*取百位数*/
    b = intt/10%10; /*取十位数*/
    c = intt%10;/*取个位数*/
    int m;
    m = c*100+b*10+a*1;
    printf("%d",m);
    return 0;
}