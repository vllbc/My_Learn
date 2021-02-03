#include <iostream>
#include <stdlib.h>
#include <cstdio>
using namespace std;

int main(){
    int x;
    cin>>x;
    if(x<=1){
        printf("Today, I ate %d apple.",x);
    }
    else
    {
        printf("Today, I ate %d apples.",x);
    }
    system("pause");


    return 0;
}