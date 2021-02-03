#include <iostream>
#include <cstdio>
#include <stdlib.h>
#include <cmath>
using namespace std;

int main(){
    double temp1,temp2;
    int n,k;
    cin>>n>>k;
    double sum1,sum2;//注意将和也定义成双精度
    int o1=0,o2=0;
    for(int i=1;i<=n;i++){
        if(i%k==0){
            sum1+=i;
            o1++;
        }
        else
        {
            sum2+=i;
            o2++;
        }
        
    }
    temp1=sum1/o1;
    temp2=sum2/o2;
    printf("%.1lf %.1lf",temp1,temp2);
    system("pause");
    return 0;
}