#include <iostream>
#include <algorithm>
#include <cstdio>
#include <stdlib.h>
using namespace std;

int main(){
    int x,n;
    cin>>x>>n;
    int sum = 0;
    while (n--)
    {
        if(x==6 || x==7){
            sum+=0;
        }
        else if (x<=5 && x>=1)
        {
            sum+=250;
        }
        x++;
        
        if(x>7){
            x=1;
        }
        
    }
    cout<<sum;
    system("pause");
    return 0;
}