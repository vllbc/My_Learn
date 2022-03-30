#include <iostream>
#include <cstdio>
#include <stdlib.h>
using namespace std;

int main(){
    int num[8];
    int n =1;
    while (n<=7)
    {
        int a,b;
        cin>>a>>b;
        num[n]=a+b;
        n++;

    }
    for(int i=1;i<=7;i++){
        if(num[i]>8){
            cout<<i;
            system("pause");
            return 0;
        }
        else
        {
            continue;
        }
        
    }
    cout<<0<<endl;
    system("pause");

    


    return 0;
}