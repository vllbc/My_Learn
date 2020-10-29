#include <stdio.h>

int main(){
    int x,y,z;
    scanf("%d,%d,%d",&x,&y,&z);
    if(x >= y && z >= y){
        if(x >= z){
            printf("%d %d %d",y,z,x);
        }
        else
        {
            printf("%d %d %d",y,x,z);
        }
        
        
    }
    if(x >= z && y >= z){
        if(x >= y){
            printf("%d %d %d",z,y,x);
        }
        else
        {
            printf("%d %d %d",z,x,y);
        }
        
        
    }
    if(y >= x && z >= x){
        if(y >= z){
            printf("%d %d %d",x,z,y);
        }
        else
        {
            printf("%d %d %d",x,y,z);
        }
        
        
    }

    return 0;
}