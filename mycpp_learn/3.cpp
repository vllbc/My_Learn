#include <iostream>
#include <cstdio>
using namespace std;

int main(){
    int n;
    int a,b,c;
    while (scanf("%d %d %d",&a,&b,&c)!=EOF)
    {
        for(n=11;;n++){
            if(n%3==a && n%5==b && n%7==c){
                printf("%d\n",n);
            }
            else if(n>=100){
                printf("no aw");
                break;
            }
            
        }

        /* code */
    }
    

    return 0;
}