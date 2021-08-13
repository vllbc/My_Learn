#include <iostream>
using namespace std;
class complex{
    double re,im;
    public:
        complex(double r,double i):re(r),im(i){}
        double real() const{return re;}
        double image() const{return im;}
        complex& operator+=(complex a){
            re += a.re;
            im += a.im;
            return *this;
        }
};
ostream &operator<<(ostream&s,const complex& z){
    return s<<'('<<z.real()<<','<<z.image()<<')';
}

int main()
{
    complex x(1,-2),y(2,3);
    cout << (x+=y) << endl;
    return 0;
}