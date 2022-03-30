#include <iostream>
#include <cstdio>
using namespace std;


class CPoint
{
public:
CPoint();
CPoint(float x,float y);
CPoint(CPoint &pt);
virtual ~CPoint();
void Print();
private:
float x,y;
};
CPoint::CPoint():x(0),y(0)
{
}
CPoint::CPoint(float xx,float yy):x(xx),y(yy)
{
}
CPoint::CPoint(CPoint &pt):x(pt.x),y(pt.y)
{
}
CPoint::~CPoint()
{
}
void CPoint::Print()
{
printf("%10.6f,%10.6f\n",x,y);
}
int main(int argc, char* argv[])
{
CPoint pt1;
pt1.Print();
CPoint pt2(444,220);
pt2.Print();
CPoint pt3(pt2);
pt3.Print();
return 0;
}