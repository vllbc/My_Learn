#include <iostream>
#include <cstdio>
#include <stdlib.h>
#include <cstring>
using namespace std;
// int get_length(int n){
//     int count;
//     while (n>1)
//     {
//         n/=10;
//         count++;   
//     }
//     return count+1;
    
// }
// int main(){
//     int n,x;
//     cin>>n>>x;
//     int counts;
//     for(int i = 1;i<=n;i++){
//         string stri="";
//         stri=(string)i;
//         for(int o =0;o<=)
//         for(int j = 0;j<=get_length(i)-1;j++){
//         }
//     }

    
//     return 0;
// }
int get_er(int n,int m){
    if(n<=9){
        if(m==n){
            return 1;
        }
        else
        {
            return 0;
        }
    }
    else
    {
        
        return (n%10==m)?1+get_er(n/10,m):0+get_er(n/10,m);
    }
    
}
int main(){
    int n,x,sum;
    cin>>n>>x;
    for(int i =1;i<=n;i++){
        sum+=get_er(i,x);

    }
    cout<<sum;
    system("pause");
    return 0;
}