#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;

int main(){
    long long ax,ay,bx,by,cx,cy;
    cin>>ax>>ay>>bx>>by>>cx>>cy;
    if ((bx - ax)*(cy - ay)==(by-ay)*(cx -ax))
    {
        cout<<"No";
        return 0;
    }

    if(pow(bx-ax,2)+pow(by-ay,2)==pow(bx-cx,2)+pow(by-cy,2)){
        cout<<"Yes";
    }
    else
    {
        cout<<"No";
    }

    return 0;
}