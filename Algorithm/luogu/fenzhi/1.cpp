#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <stdlib.h>
using namespace std;

int main(){
    int j,a[4];
    cin>>j;
    if(j%2==0 && j>4&&j<=12){
        a[0]=1;
        a[1]=1;
    }
    else
    {
        a[0]=0;

    }
    if (j%2==0 || (j>4&&j<=12))
    {
        a[1]=1;
    }
    else
    {
        a[1]=0;
        a[2]=0;
    }
    if((j%2==0 && !(j>4&&j<=12)) || (j%2!=0&&(j>4&&j<=12))){
        a[2]=1;
    }
    else
    {
        a[2]=0;
    }
    if(j%2!=0 && !(j>4 && j<=12)){
        a[3]=1;
    }
    else
    {
        a[3]=0;
    }
    printf("%d %d %d %d",a[0],a[1],a[2],a[3]);
    system("pause");
    ;
}