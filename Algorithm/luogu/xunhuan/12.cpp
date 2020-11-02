#include <iostream>
#include <cstdio>
#include <stdlib.h>
using namespace std;

int main(){
    double temp,sum=2,tip=2;
    cin>>temp;
    int t=1;
    while (sum<=temp)
    {
        sum+=tip*0.98;
        t++;
        tip*=0.98;
    }
    cout<<t;
    system("pause");
    return 0;
}