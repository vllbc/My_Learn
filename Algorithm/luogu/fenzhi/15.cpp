#include <iostream>
#include <cstdio>
#include <stdlib.h>
#include <cmath>
using namespace std;

int main(){
    int a,b,c;
    cin>>a>>b>>c;
    if(a+b>c && a+c>b && b+c>a){
        if(pow(a,2)+pow(b,2)==pow(c,2) || pow(a,2)+pow(c,2)==pow(b,2) || pow(b,2)+pow(c,2)==pow(a,2)){
            cout<<"Right triangle"<<endl;
        }
        if(pow(a,2)+pow(b,2)>pow(c,2) && pow(a,2)+pow(c,2)>pow(b,2) && pow(b,2)+pow(c,2)>pow(a,2))
        {
            cout<<"Acute triangle"<<endl;
        }
        if(pow(a,2)+pow(b,2)<pow(c,2) || pow(a,2)+pow(c,2)<pow(b,2) || pow(b,2)+pow(c,2)<pow(a,2)){
            cout<<"Obtuse triangle"<<endl;
        }
        if(a==b || a==c || b==c){
            cout<<"Isosceles triangle"<<endl;
            
        }
        if(a == b&& a==c&&b==c){
            cout<<"Equilateral triangle"<<endl;
        }
        
        
    }
    else
    {
        cout<<"Not triangle";
    }
    system("pause");
    

    return 0;
}