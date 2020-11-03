#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;
int n;
double res,sum=0;
int main(){
    cin>>n;
    int a[n+2];
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    sort(a,a+n);
    for(int i=1;i<n-1;i++){
        sum+=a[i];
    }
    res = sum/(n-2);
    printf("%.2lf",res);
    return 0;
}