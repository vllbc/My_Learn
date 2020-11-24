#include <stdio.h>
int max(int a,int b){
    if(a>=b){
        return a;
    }
    else
    {
        return b;
    }
    
}
int min(int a,int b){
    if(a<=b){
        return a;
    }
    else
    {
        return b;
    }
    
}
int main(){
    int n;
    scanf("%d",&n);
    long maxs = -1e9,mins = 1e9;
    while (n--)
    {
        long x;
        scanf("%d",&x);
        maxs = max(maxs,x);
        mins = min(mins,x);
    }
    printf("%d %d",maxs,mins);
    return 0;
}