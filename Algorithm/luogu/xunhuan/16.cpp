#include <iostream>
#include <stdlib.h>
#include <cstdio>
#include <algorithm>
using namespace std;
int ans=0,maxs=0;
int main(){
    int n;
    cin>>n;
    long long a[n+2];
    for(int i = 0;i<=n-1;i++){
        cin>>a[i];
    }
   
    for(int i=0;i<n-1;i++){
       if(a[i+1]-a[i]==1){
           ans++;
       }
       else
       {
           ans=0;
       }
       if(ans>maxs){
           maxs = ans;
       }
       
    }
    printf("%d",++maxs);
    system("pause");
    return 0;
}