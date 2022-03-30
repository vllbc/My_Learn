#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;
int k;
int main(){
    long long test;
    cin>>test;
    int weekdays = 52;
    long long sums;
        for(int x = 100;x>=1;x--){
            if(((test/52)-7*x)%21==0){
                k = ((test/52)-7*x)/21;
                if(k>0){
                    cout<<x<<endl;
                    cout<<k;
                    break;
                }
                else
                {
                    continue;
                }
                
               
            }
            else
            {
                continue;
            }
            
            // for(int k=1;k<=test;k++){
            //     sums=7*x+21*k;
            //     if(sums*52==test){
            //         cout<<x<<endl;
            //         cout<<k;
            //         break;
            //         }
            //     else
            //     {
            //         continue;
            //     }
            // }
            // if(sums*52==test){
            //         break;
            //        }
        }
        

    
    return 0;
}