<<<<<<< HEAD
#include <stdio.h>

#include <string.h>

int main()

{

    int i=0,len=0;

    char c[100]="";

    char d[100]="";

    gets(c);

    for (i = 0; i < sizeof(c) / sizeof(c[0]); i++)

    {

        d[sizeof(c) / sizeof(c[0])-i]=c[i];

    }

    puts(d);  

    return 0;

=======
#include <iostream>
#include <cstdio>
using namespace std;

int main(){
    long long  res = 0,x=1;
    for(int i =1;i<=20;i++){
       x*=i;
       res+=x;
    }
    cout<<res;
    return 0;
>>>>>>> a8b720e32694def715bebe2f83bf0621a06052cf
}