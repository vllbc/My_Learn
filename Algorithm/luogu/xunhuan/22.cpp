#include <iostream>
#include <cstdio>
using namespace std;
int sum = 0,count = 0,yu;
int main(){
    for(int i =1;i<=12;i++){
        cin>>yu;
        sum+=300;
        
        if(sum>=yu){
            if((sum-yu)>=100 && (sum-yu)<200){
                sum-=100;
                sum-=yu;
                count+=100;
                continue;
            }
            else if((sum-yu)>=200 && (sum-yu)<300){
                sum-=200;
                sum-=yu;
                count+=200;
                continue;
            }
            else if((sum-yu)>=300 && (sum-yu)<400){
                sum-=300;
                sum-=yu;
                count+=300;
                continue;
            }
            else if((sum-yu)<100)
            {
                sum-=yu;
                continue;
            }
            
        }
        else
        {
            cout<<"-"<<i;
            return 0;
        }
        
    }
    cout<<sum+count*1.2;
    return 0;
}