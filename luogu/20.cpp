#include <iostream>
#include <cstdio>
#include <stdlib.h>
using namespace std;

int countones(int num){
    int count = 0;
    while(num>0){
        
        if((num & 1)==1){
            count++;
        }
        num = (num>>1);
        
}
    return count;
}
int main(){
    int c = countones(17);
    printf("%d\n",c);
    system("pause");

    return 0;
}