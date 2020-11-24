#include <cstdio>
#include <iostream>
using namespace std;

int main(){
    int n;
    cin>>n;
    long long a[n+2];
    for(int i=0;i<n;i++){
        cin>>a[i];
        while(a[i]%2==0) a[i]/=2;
        while(a[i]%3==0) a[i]/=3;

    }
    for(int i=0;i<n-1;i++){
        if(a[i]!=a[i+1]){
            cout<<"No";
            return 0;
        }
    }
    cout<<"Yes";
    return 0;
}