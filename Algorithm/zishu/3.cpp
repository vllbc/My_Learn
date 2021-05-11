
#include<iostream>
using namespace std;
template <class numtype>

class Compare
{
public:
	Compare(numtype a, numtype b)
	{
		x = a;
		y = b;
	}

	numtype max(); 

	numtype min();

private:
	numtype x, y;
};

template <class numtype>
numtype Compare <numtype>::max()
{
	return x > y ? x : y;
}

template <class numtype>
numtype Compare <numtype>::min()
{
	return x < y ? x : y;
}

int main()
{
	Compare <int> cmp1(1, 2);//定义对象cmp1，用于两个整数的比较 
	cout << cmp1.max() << " is the Maximum of two integer numbers." << endl;
	cout << cmp1.min() << " is the Minimum of two integer numbers." << endl << endl;

	Compare <float> cmp2(2.2f, 4.3f);//定义对象cmp2，用于两个浮点数的比较 
	cout << cmp2.max() << " is the Maximum of two integer numbers." << endl;
	cout << cmp2.min() << " is the Minimum of two integer numbers." << endl << endl;

	Compare <char> cmp3('a', 'v');//定义对象cmp3，用于两个字符的比较 
	cout << cmp3.max() << " is the Maximum of two integer numbers." << endl;
	cout << cmp3.min() << " is the Minimum of two integer numbers." << endl << endl;

	return 0;
}