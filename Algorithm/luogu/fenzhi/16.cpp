#include <iostream>
#include <cstdio>
using namespace std;

int main(){
    long long  res = 0,x=1;
    for(int i =1;i<=20;i++){
       x*=i;
       res+=x;
    }
    cout<<res;
    return 0;
}