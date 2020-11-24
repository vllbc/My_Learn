#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int main(){
    int n;
    cin>>n;
    int a[n+2];
    for(int i=0;i<=n-1;i++){
        cin>>a[i];
    }
    int temp = a[0],count=0;
    sort(a,a+n);
    if(a[n-1]==temp && temp>a[n-2]){
        cout<<0;
        return 0;
    }
    while (a[n-1]>=temp)
    {
        a[n-1]--;
        temp++;
        sort(a,a+n);
        count++;
    }
    cout<<count;
    return 0;
}