#include <iostream>
#include <stdlib.h>
#include <cmath>
#include <cstdio>
using namespace std;

int main(){
    int m,t,s;
    cin>>m>>t>>s;
    if(t==0){
        cout<<0<<endl;
        ;
    }
    else if (s%t==0)
    {
        cout<<max(m-s/t,0)<<endl;//吃完为0
    }
    else
    {
        cout<<max(m-1-s/t,0)<<endl;
    }
    system("pause");

    ;
}