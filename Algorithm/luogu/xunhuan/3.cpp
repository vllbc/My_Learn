#include <iostream>
#include <cstdio>
#include <stdlib.h>
using namespace std;

int main(){
    int a;
    cin>>a;
    int coutn=1;
    while (a>1)
    {
        a/=2;
        ++coutn;

    }
    cout<<coutn;
    system("pause");
    return 0;
}
