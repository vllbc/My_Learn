#include <iostream>
#include <cstdio>
#include <stdlib.h>
#include <cmath>
using namespace std;
int is_zhi(int n){
    if(n==1){
        return 0;
    }
    for(int i =2;i<=sqrt(n);i++){
        if(n%i==0){
            return 0;
        }
    }
    return 1;
}
int main(){
  
    int L,sum,count=0;
    cin>>L;
    for(int i =2;sum<=L;i++){
        if(is_zhi(i)){
            sum+=i;
            if(sum>L){
                sum-=i;
                break;
            }
            else{cout<<i<<endl;count++;}
        }
        else
        {
            continue;
        }
        
    }
    cout<<count;
  system("pause");
    return 0;
}