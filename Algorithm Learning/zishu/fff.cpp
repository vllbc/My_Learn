#include <iostream>
using namespace std;
#include<string>
struct student {
	int num;
	string name;
	int score[3];
};
void print(student stu)
{
	
	for (int i = 0; i < 4; i++) {
		cout << stu.score[i] << " ";
	}
	int xb = 0;
	xb = (stu.score[0] + stu.score[1] + stu.score[2]) / 3;
	cout << "平均分" << xb;
}
int max(double a,double b) {
	if (a > b) {
		return a;
	}
	else{
		return b;
	}
}
double agx(student stu){
	double xb = (stu.score[0] + stu.score[1] + stu.score[2]) / 3;
	return xb;
}
int main() {
	struct student stu[5] = { {10101,"Li Lin",{60,70,80}},{10102,"Zhang Fun",{75,90,80}},{10103,"Wang Min",{85,75,85}},{10104,"Wen Wu",{60,72,80}},{10105,"Xiao Ming",{95,85,80}} };
	for (int i = 0; i < 5; i++) {
		print(stu[i]);
	}
	double maxs = 0;
	string name;
	for (int i = 0; i<5; i++){
		if (agx(stu[i]) > maxs){
			name = stu[i].name;
		}
	}
	cout << name;
	return 0;
}