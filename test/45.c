#include <stdio.h>

int main(){
    int X,Y;
    while(scanf("%d %d",&X,&Y)!=EOF){
        if(X>0){
            if (Y>0)
            {
                printf("%d\n",1);
            }
            else
            {
                printf("%d\n",4);
            }
            
            
        }
        if(X<0){
            if(Y>0){
                printf("%d\n",2);
            }
            if(Y<0){
                printf("%d\n",3);
            }
        }


    }

    return 0;
}