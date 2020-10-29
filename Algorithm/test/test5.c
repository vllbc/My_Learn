#include <stdio.h>
int main(){
    int a,b;
    scanf("%d",&a);
    scanf("%d",&b);
    int c;
    c = b;
    b = a;
    a = c;
    printf("%d %d",a,b);
    return 0;
}
