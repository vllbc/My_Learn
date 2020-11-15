#include <iostream>
#include <cstdio>
using namespace std;
int re_min(int m,int n){
    return (n==0)?m:re_min(n,m%n);
}
int re_max(int m,int n){
    return (m*n)/re_min(m,n);
}
int main(){
    int m,n;
    cin>>m,n;
    cout<<re_min(m,n)<<endl;
    cout<<re_max(m,n);
    return 0;
}