#include <stdio.h>


int main(){
    int year,mouth;
    scanf("%d\\%d",&year,&mouth);
    if(mouth == 2){
        if(panduan(year) == 2){
            printf("%d",29);
        }
        else
        {
            printf("%d",28);
        }
        
    }
    else if(mouth==1 || mouth==3 || mouth ==5 ||mouth==7||mouth==8||mouth==10||mouth==12){
            printf("%d",31);
        }
    else
    {
        printf("%d",30);
    }
    
    return 0;
}
int panduan(year){

    if(year %4==0){
        if(year%100 !=0){
            return 2;
        }
        else if (year %400==0)
        {
            return 2;
        }
        else{
            return 3;
        }
    }
    else
    {
        return 3;
    }
    
}