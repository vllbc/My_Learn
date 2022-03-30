#include <stdio.h>

int main(){
    int a,b,c;
    scanf("%d %d %d",&a,&b,&c);
    if(a+b > a+c){
        if(b+c>a+b){
            printf("%d",b+c);
        }
        else
        {
            printf("%d",a+b);
        }
    }
   else
   {
       if(b+c>a+c){
           printf("%d",b+c);
       }
       else
       {
           printf("%d",a+c);
       }
       
   }
   
    
    return 0;
}
