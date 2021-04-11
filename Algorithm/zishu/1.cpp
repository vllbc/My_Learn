#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

class Date{
    public:
    Date(int,int,int);
    Date(int,int);
    Date(int);
    Date();
    void display();
    private:
    int month;
    int day;
    int year;
}

int main(){


    return 0;

}