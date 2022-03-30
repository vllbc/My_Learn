#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
#define PI 3.1415926

class SwimmingPool{
private:
    float r;
public:
    void set_r(float a);//设置半径r的值
    void put_r();//打印泳池半径
    void fence();//计算输出围栏价格
    void aisle();//计算输出过道价格
};


void SwimmingPool::set_r(float a)//设置半径r的值
{
    r=a;
}
void SwimmingPool::put_r()//打印泳池半径
{
    cout<<"泳池半径为："<<r<<endl;
}
void SwimmingPool::fence()//计算输出围栏价格
{
    float c;
    c=2*PI*r;
    cout<<"栅栏长为："<<c<<'\t';
    cout<<"费用："<<35*c<<"元"<<endl;
}
void SwimmingPool::aisle()//计算输出过道价格
{
    float s1,s2;
    s1=PI*r*r;
    s2=PI*(r+3)*(r+3);
    cout<<"泳池面积为："<<s1<<endl;
    cout<<"过道面积为："<<s2<<'\t';
    cout<<"费用："<<(s2-s1)*20<<"元"<<endl;
}

int main()
{
    SwimmingPool A;
    A.set_r(20.0);
    A.put_r();
    A.fence();
    A.aisle();
}
