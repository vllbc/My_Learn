#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

struct Student
{
        int id;
        string name;
        int score1;
        int score2;
        int score3;
        float avg;
};
int main()
{
        Student student[10];
        for (int i = 0; i < 10; i++)
        {
                scanf("%d %s %d %d %d", &student[i].id, student[i].name, &student[i].score1, &student[i].score2, &student[i].score3);
                student[i].avg = (student[i].score1 + student[i].score2 + student[i].score3) / 3;
        }
        float sum = 0;
        Student the_max_stu;
        float max = 0;
        float res;
        for (int i = 0; i < 10; i++)
        {
                if (student[i].avg > max)
                {
                        max = student[i].avg;
                        the_max_stu = student[i];
                }
                sum += student[i].avg;
        }
        res = sum / 10;
        cout << "3门总成绩" << res;
        cout << "最高分学生:" << the_max_stu.id << the_max_stu.name << the_max_stu.avg;
        return 0;
}