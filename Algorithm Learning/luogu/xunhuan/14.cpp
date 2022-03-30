#include <iostream>
#include <cstdio>
#include <stdlib.h>
#include <cstring>
using namespace std;
double num[50];
int main(){
    int n;
    cin>>n;
    num[0]=0;num[1]=1;num[2]=1;
    for(int i =3;i<=n;i++){
        num[i] = num[i-1]+num[i-2];
    }
    
    printf("%.2lf",num[n]);
    system("pause");

    return 0;
}