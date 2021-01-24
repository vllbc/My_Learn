// #include <iostream>
// #include <cstdio>
// #include <cstring>
// using namespace std;
// int main()
// {
//     string s;
//     int i;
    
//     getline(cin,s);
//     for (i=0;i<s.length();i++)
//     {
//         if (i==0)
//         {
//             s[i]-=32;
//         }
//         else
//         {
//             if(s[i]==' '&&s[i+1]!=' ')
//                 s[i+1]-=32;
//         }
// 	  }
//       cout<<s;
//     return 0;
// }

 
#include <iostream>
#include <cstring>
using namespace std;

int main(){
    string s;
    getline(cin,s);
    char x;
    int res;
    cin >> x;
    for (int i=0;i<s.length();i++){
        if (s[i] == x){
            res ++;
        }
    }

    cout<<res;
    return 0;
}