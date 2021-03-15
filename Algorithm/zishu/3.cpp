#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

struct Student{
        int num;
        string name;
        int score[3];
};

void print(Student stu){
    cout << "序号为" << stu.num << endl;
    cout << "姓名为" << stu.name << endl;
    cout << "成绩分别为" << stu.score[0] << stu.score[1] << stu.score[2] << endl; 
}

int main(){
    Student student[5] = {1,"Zhang",{9,8,9},2,"Li",{7,8,6},3,"Wang",{9,10,6},4,"Zhao",{7,5,8},5,"Wei",{9,7,8}};
    for (int i = 0; i < 5; i++){
        print(student[i]);
    }
    return 0;
}

