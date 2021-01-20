#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int main(){
    string str;
    cin>>str;
    if (! (str[0] >= 'A' && str[0] <= 'Z' || str[0] >= 'a' && str[0] <= 'z' || str[0] == '_')){
        cout<<"no";
        return 0;
    }
    else{
        for (int i = 0;i < str.length();i++){
            if (! (str[i] >= 'A' && str[i] <= 'Z' || str[i] >= 'a' && str[i] <= 'z' || str[i] == '_' || str[i] >= '0' && str[i] <= '9')){
                cout<<"no";
                return 0;
            }
        }
        cout<<"yes";
    }
    return 0;
}