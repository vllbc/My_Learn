#include <iostream>
#include <cstdio>
#include <stdlib.h>
#include <algorithm>
#include <cmath>

using namespace std;

int main(){
    int a[3];
    for(int i=0;i<=2;i++){
        cin>>a[i];
    }
    sort(a,a+3);
    printf("%d %d %d",a[0],a[1],a[2]);
    system("pause");
    


    return 0;
}