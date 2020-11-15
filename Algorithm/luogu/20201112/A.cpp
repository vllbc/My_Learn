#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;

int main(){
    long long n,k;
    cin>>n>>k;
    long long res[10000001],temp=0;
    for(long long i=1;i<=n;i++){
        if(n%i == 0){
            res[temp++] = i;
        }
        if(i==n/2){
        	res[temp] = n;
        	break;
		}
    }
     if(k>temp){
         cout<<-1;
     }
     else{
     	cout<<res[k-1];
	 }
    return 0;
 }
