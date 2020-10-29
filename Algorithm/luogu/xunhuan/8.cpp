#include <iostream>
#include <cstdio>
#include <stdlib.h>
#include <cmath>
using namespace std;
int main(){
    int k,i;
    cin>>k;
    int sums = 0;
    for(i =1;k-i>=0;k-=i++){
        sums += i*i;
    }
    cout<<sums+k*i;
    system("pause");
    return 0;
}
