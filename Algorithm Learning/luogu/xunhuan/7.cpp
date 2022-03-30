#include <iostream>
#include <cstdio>
#include <stdlib.h>
using namespace std;

int main(){
    int k;
    cin>>k;
    double sum=0;
    for(int i =1;;i++){
        sum += 1/(double)i;
        if(sum>k){
            cout<<i;
            break;
        }
        
        
    }
    system("pause");
    return 0;
}