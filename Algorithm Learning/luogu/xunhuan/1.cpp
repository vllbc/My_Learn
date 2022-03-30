#include <iostream>
#include <algorithm>
#include <cstdio>
#include <stdlib.h>
using namespace std;

int main(){
    int n,mi=1001;
    cin>>n;
    for(int i =1;i<=n;i++){
        int x;
        cin>>x;
        if(x<=mi){
            mi =x;
        }
    }
    cout<<mi;
    system("pause");
    return 0;
}