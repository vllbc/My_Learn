#include <iostream>
#include <cstdio>
using namespace std;

int main(){
    int n;
    cin>>n;
    int a[n*n],b[n*n],k[n*n];
    for(int i=1;i<=n*n;i++){
        a[i] = 0;
        b[i] = 0;
        k[i] = 0;
    }
    for(int i=1;i<=n*n;i++){
        int aa,bb;
        cin>>aa>>bb;
        if(a[aa] == 0 && b[bb] == 0){
            a[aa] = 1;
            b[bb] = 1;
            k[i] = 1;
        }
    }
    for(int i=1;i<=n*n;i++){
    	if(k[i] == 1){
    		cout<<i<<" ";
		}
	}
    return 0;
}
