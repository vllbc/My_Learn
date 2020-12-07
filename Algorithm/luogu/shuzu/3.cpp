#include <iostream>
using  namespace std;

int main(){
    long long n,a[100000],temp=1;
    cin>>n;
    a[0] = n;
    while(n != 1){
        
        if(n%2 != 0){
            n = n*3+1;
            a[temp++] = n;
            continue;
        }
        if(n%2 == 0){
            n/=2;
            a[temp++] = n;
            continue;
        }
    }
    for(int i=temp-1;i>=0;i--){
        cout<<a[i]<<" ";
    }
    return 0;
}
