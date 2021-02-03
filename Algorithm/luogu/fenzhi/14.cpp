#include <iostream>
#include <cstdio>
#include <stdlib.h>
#include <cmath>
#include <algorithm>
using namespace std;

int main(){
    int a[10];
    for(int i =0;i<=9;i++){
        cin>>a[i];
    }
    sort(a,a+10);
    int longer;
    cin>>longer;
    for(int i = 0;i<=9;i++){
        if(a[i]>longer+30){
            cout<<i;
            break;    
        }
    }
    system("pause");


    return 0;
}