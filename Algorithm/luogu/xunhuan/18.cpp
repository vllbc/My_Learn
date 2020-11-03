#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;

int main(){
    int n,count=1;
    cin>>n;
    for(int i =1;i<=n;i++){
        for(int j=1;j<=n;j++){
            if(count<=9){
                cout<<"0"<<count++;
            }
            else
            {
                cout<<count++;
            }
            
        }
        printf("\n");
    }
    cout<<endl;
    int count2=1;
    for(int i=1;i<=n;i++){
        for(int o =n-i;o>0;o--){
            cout<<"  ";
        }
        for(int j=n+1-i;j<=n;j++){
            if(count2<=9){
                cout<<"0"<<count2++;
            }
            else
            {
                cout<<count2++;
            }
        }
        cout<<endl;
    }

    return 0;
}