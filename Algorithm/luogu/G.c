#include <stdio.h>
int re_sum(int n){
    if(n==1){
        return 1;
    }
    else
    {
        return n+re_sum(n-1);
    }
    
}
int main(){
    int i;
    long sums;
    scanf("%d",&i);
    for(int n=1;n<=i;n++){
        sums+=re_sum(n);
    }
    printf("%d",sums);
    return 0;
}