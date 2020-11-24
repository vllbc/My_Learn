#include <stdio.h>

int main(){
    int a,b,c;
    scanf("%d%d%d",&a,&b,&c);
    long sums = a+b+c;
    double mean = sums/3.0;
    printf("%d\n",sums);
    printf("%.2lf",mean);
    return 0;
}