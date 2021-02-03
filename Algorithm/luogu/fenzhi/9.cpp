#include <iostream>
#include <cmath>
#include <cstdio>
#include <stdlib.h>
#include <algorithm>
using namespace std;

int main(){
    int n;
    cin>>n;
    int a1,a2,b1,b2,c1,c2;
    int n1,n2,n3;
    cin>>a1>>a2;
    cin>>b1>>b2;
    cin>>c1>>c2;
    n1 = a2*(n/a1+(n%a1!=0));
    n2 = b2*(n/b1+(n%b1!=0));
    n3 = c2*(n/c1+(n%c1!=0));
    cout<<min(min(n1,n2),n3);
    system("pause");
    return 0;
}