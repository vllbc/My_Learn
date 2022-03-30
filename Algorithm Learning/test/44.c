#include <stdio.h>

int main(){
    int L,M;
    while(scanf("%d %d",&L,&M)!=EOF){
        if(L%M==0){
            printf("%d\n",L/M);
        }
        else
        {
            printf("%d\n",(L-L%M)/M);
        }
        
        
    }
    return 0;
}