#include <cstdio>
#include <iostream>
#include <cmath>
using namespace std;

int main(){
    int i;
    for(i=100;i<=999;i++){
        int a,b,c;
        a=i/100;
        b=i/10%10;
        c=i%10;
        if(pow(a,3)+pow(b,3)+pow(c,3)==i){
            printf("%d\n",i);
        }
    }

    return 0;
}