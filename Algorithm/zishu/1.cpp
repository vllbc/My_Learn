#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

bool is_leap_year(int year){
    if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0){
        return true;
    }
    else{
        return false;
    }

}

int re_(int n, int month){
    int res = 0;
    for (int i = 1; i <= month - 1; i++){
        if (i == 1){
            res += 31;
        }
        else if (i == 2){
            if (n == 1){
                res += 29;
            }
            else{
                res += 28;
            }
        }
        else if (i == 3){
            res += 31;
        }
        else if (i == 4){
            res += 30;
        }
        else if (i == 5){
            res += 31;
        }
        else if (i == 6){
            res += 30;
        }
        else if (i == 7){
            res += 31;
        }
        else if (i == 8){
            res += 31;
        }
        else if (i == 9){
            res += 30;
        }
        else if (i == 10){
            res += 31;
        }
        else if (i == 11){
            res += 30;
        }
        else if (i == 12){
            res += 31;
        }
    }
    return res;
}
int main()
{
    struct Date{
        int year;
        int month;
        int day;
    };
    int years,months,days;
    cin >> years >> months >> days;
    Date date = {years,months,days};
    if (is_leap_year(date.year)){
        cout << re_(1,date.month) + date.day;
    }
    else{
        cout << re_(2,date.month) + date.day;
    }
    return 0;
}