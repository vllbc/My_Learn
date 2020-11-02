#include <iostream>
#include <cstdio>
#include <stdlib.h>
#include <algorithm>
using namespace std;

int main(){
    int i,a[102];
    cin>>i;
    for(int j =0;j<=i-1;j++){
        cin>>a[j];
    }
    sort(a,a+i);
    cout<<a[i-1]-a[0];
    system("pause");
    return 0;

}