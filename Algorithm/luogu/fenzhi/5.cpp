#include <iostream>
#include <cstdio>
#include <stdlib.h>
#include <iomanip>
using namespace std;

int main(){
    double m;
    double h;
    cin>>m>>h;
    double bmi;
    bmi = m/(h*h);
    if (bmi<18.5)
    {
        cout<<"Underweight";
    }
    else if(bmi>=18.5&&bmi<24)
    {
        cout<<"Normal";
    }
    else
    {
        cout<<setprecision(6)<<bmi<<endl;
        cout<<"Overweight";
    }
    
    system("pause");
    


    return 0;
}