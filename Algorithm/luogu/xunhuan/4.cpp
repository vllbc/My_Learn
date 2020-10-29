#include <iostream>
#include <stdlib.h>
#include <cstdio>
using namespace std;

int main(){
    int n;
    cin>>n;
    int num =1;
    for(int i = 1;i<=n;i++){
            for(int j =n-i+1;j>=1;j--){
                if(num<=9){
                    printf("0%d",num);
                    num++;
                }
                else
                {
                    printf("%d",num);
                    num++;
                }
                
                
            }
            printf("\n");
    }
    system("pause");

    return 0;
}