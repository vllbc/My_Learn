#include <iostream>
using namespace std;

class base
{
public:
    void fun1() { cout << "base" << endl; }
    virtual void fun2() { cout << "base" << endl; }
};

class derived : public base
{
public:
    void fun1() { cout << "derived" << endl; }
    void fun2() { cout << "derived" << endl; }
};
void f(base &b)
{
    b.fun1();
    b.fun2();
}
int main()
{
    derived obj;
    f(obj);
    return 0;
}