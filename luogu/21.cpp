#include <iostream>
#include <cstdio>
#include <algorithm>
#include <stdlib.h>
using namespace std;

int main(){
    int i;
    cin>>i;
    double sum;
    if(i<=150){
        sum = i*0.4463;
    }
    else if(i>=151 && i<=400){
        sum = (i-150)*0.4663 + 150*0.4463;
    }
    else if(i>=401)
    {
        sum = 150*0.4463+250*0.4664+(i-400)*0.5663;
    }
    printf("%.1lf",sum);
    system("pause");
    return 0;
}