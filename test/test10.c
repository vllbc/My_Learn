#include <stdio.h>

int main(){
    float P = 3.1415926;
    float r,h;
    scanf("%f %f",&r,&h);
    float l,s,c,v;
    l = 2 *r*P;
    s = r*r*P;
    c = l * h;
    v = s*h;
    printf("%.2f %.2f %.2f %.2f",l,s,c,v);
    return 0;
}
