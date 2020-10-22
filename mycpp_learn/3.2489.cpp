#include <iostream>
#include <cstdio>
#include <cmath>
#include <stdlib.h>
using namespace std;
#define PI acos(-1)
int main(){
    double r = 1.5;
    double h = 3.0;
   
    printf("Բ�ܳ�%.2lf\n",2*PI*r);
    printf("Բ���%.2lf\n",PI*r*r);
    printf("�����%.2f\n",4*PI*r*r);
    printf("�����%.2f\n",(4/3)*PI*pow(r,3));
    printf("Բ�����%.2f",PI*r*r*h);
    //(1) 二者即可
    //(2) 强制转换成整形变量 然后cout输出
    //(1) false
    //(2) true
    //(3) true
    //(4) false
    //(5) true
    // int a,b,c,temp;
    // cin>>a>>b>>c;
    // if(a>=b){
    //     temp = a;
    // }
    // else
    // {
    //     temp = b;
    // }
    // if (temp >=c)
    // {
    //     cout<<temp;
    // }
    // else
    // {
    //     cout<<c;
    // }
    
    system("pause");
    

    return 0;
}
