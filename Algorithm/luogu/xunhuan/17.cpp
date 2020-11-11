#include <algorithm>
#include <iostream>
#include <cstdio>
#include <stdlib.h>
#include <cmath>
using namespace std;

int main(){
    long long n;
    cin>>n;
    for(int i=2;i<=sqrt(n);i++){
        if(n%i==0){
            cout<<n/i;
        }
    }
    return 0;
}