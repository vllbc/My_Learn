#include <cstdio>
#include <iostream>
using namespace std;

int main(){
    long long n,k,t;
    cin>>n>>k>>t;//n=10 k=5 t=12
    //t<=k时，输出t 
    //t>k t<=n 时 输出t-(t-k)
    //t>n 输出n+k-t
    if(t<=k){
        cout<<t;
    }
    else if(t>k && t<=n){
        cout<<k;
    }
    else if(t>n){
        cout<<n+k-t;
    }


    return 0;
}