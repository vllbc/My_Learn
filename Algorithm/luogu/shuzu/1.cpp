#include <iostream>
#include <cstdio>
using namespace std;

int main(){
    int i;
    cin>>i;
    int a[i+2];
    for(int j=0;j<=i-1;j++){
        cin>>a[j];
    }
    for(int b=0;b<=i-1;b++){
        int count = 0;
        for(int c=0;c<=b;c++){
            if(a[b]>a[c]){
                count++;
            }
            else
            {
                continue;
            }
            
        }
        cout<<count<<" ";
    }

    return 0;
}