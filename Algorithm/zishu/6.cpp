#include <iostream>
using namespace std;

class Box
{
private:
    float length;
    float width;
    float height;

public:
    void get_value();
    float volume();
    void display();
};
void Box::get_value()
{
    cin >> length;
    cin >> width;
    cin >> height;
}
float Box::volume()
{
    return (length * width * height);
}
void Box::display()
{
    cout << volume << endl;
}
int main()
{
    Box box1, box2, box3;
    box1.get_value();
    box2.get_value();
    box3.get_value();
    box1.display();
    box2.display();
    box3.display();
}