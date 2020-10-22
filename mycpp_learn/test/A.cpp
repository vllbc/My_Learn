#include <iostream>
#include <cstdio>
using namespace std;

int main(){
    double sum = 0;
    int n;
    scanf("%d",&n);
    while (n--)
    {
        int m;
        cin>>m;
        if(sum<100.0 || sum >=400.0){
            sum+=m;
        }
        else if(sum>=100.0 && sum<150.0)
        {
            sum+=m*0.8;
        }
        else if(sum>=150.0 && sum<400.0){
            sum+=m*0.5;
        }
        
    }
    printf("%.2lf",sum);
    return 0;
}