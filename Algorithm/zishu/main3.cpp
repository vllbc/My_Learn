#include <iostream>
template <class T>
void swap(T &a, T &b)
{
       T temp;
    temp = a;
    a = b;
    b = temp;
}
void swap(int &a, int &b)
{
   int temp;
   temp = a;
   a = b;
   b = temp;
   std::cout<<"swap two int!"<<"  ";
}
int main(void)
 {
   int i=1, j=2;
   double x=1.1, y=2.2;
   char a='x', b='z';
   swap(i,j);                                 
   swap(a,b);
   swap(x,y);
   std::cout<<i<<","<<j<<"  ";
   std::cout<<a<<","<<b<<"  ";
   std::cout<<x<<","<<y<<"  ";
 }