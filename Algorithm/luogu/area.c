#include <stdio.h>
#include <math.h>
int main(){
    int a,b,c;
    scanf("%d%d%d",&a,&b,&c);
    double S;
    double sums = (a+b+c)/2.0;
    S = sqrt(sums*(sums-a)*(sums-b)*(sums-c));
    printf("%.3lf",S);
    return 0;
}