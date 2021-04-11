#include <iostream>
#include <student.h>
using namespace std;

void Student::display()
{
    cout << "num:" << num << endl;
    cout << "name" << name << endl;
    cout << "sex:" << sex << endl;
}

void Student::set_value()
{
    cin >> num;
    cin >> name;
    cin >> sex;
}