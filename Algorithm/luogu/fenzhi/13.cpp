#include <cmath>
#include <cstdio>
#include <iostream>
#include <stdlib.h>
using namespace std;
int re_gongyin(int a,int b){
    return (b==0)?a:re_gongyin(b,a%b);//求最大公因式
}
int main(){
    // cout<<re_gongyin(5,3);
    int a,b,c;
    cin>>a>>b>>c;
    int ma,mi;
    ma = max(max(a,b),c);
    mi = min(min(a,b),c);
    while(re_gongyin(ma,mi)!=1)
    {
        int temp = ma;
        ma/=re_gongyin(ma,mi);
        mi/=re_gongyin(temp,mi);
    }
    printf("%d/%d",mi,ma);
    
    system("pause");
    return 0;
}