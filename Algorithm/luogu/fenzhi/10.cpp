#include <iostream>
#include <stdlib.h>
#include <cstdio>
using namespace std;

int main(){
    char temp;
    char num[9];
    scanf("%c-%c%c%c-%c%c%c%c%c-%c",&num[0],&num[1],&num[2],&num[3],&num[4],&num[5],&num[6],&num[7],&num[8],&temp);
    int sum = 0;
    int X = "X";
    for(int n =1;n<=9;n++){
        sum=sum+((num[n-1]-48)*n);
    }
    
    if(sum%11 == 10){
        if(temp=="X"){
            printf("Right");
        }
        else
        {
            printf("%c-%c%c%c-%c%c%c%c%c-%c",num[0],num[1],num[2],num[3],num[4],num[5],num[6],num[7],num[8],"X");
        }
        
    }
   else if(sum%11 == (int)temp-48){
        printf("Right");
   }
   else if(sum%11 != (int)temp-48)
   {
       printf("%c-%c%c%c-%c%c%c%c%c-%c",num[0],num[1],num[2],num[3],num[4],num[5],num[6],num[7],num[8],(char)((sum%11)+48));
   }
   
    system("pause");
    return 0;
}
