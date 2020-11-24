#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
class Teacher
{public:
	void display();
	string title = "学生";
	string name = "高云龙";
	int age = 18;
	string sex = "女";
	string address = "山东";
	long long phone = 1235672;
};
void Teacher:: display(){
	cout<<name<<" "<<age<<" "<<sex<<" "<<address<<" "<<phone<<endl;
}
class Cadre{	
public:
	string post = "男技师";
	string name;
	int age;
	string sex;
	string address;
	long long phone;
	
};
class Teacher_Cadre:public Teacher,public Cadre{
	public:
	 	void show();
		double wages = 10;
};
void Teacher_Cadre::show(){
	Teacher::display();
	cout<<Cadre::post<<" "<<wages<<endl;
}
int main(){
	Teacher_Cadre tc;
	tc.show();
	return 0;
}