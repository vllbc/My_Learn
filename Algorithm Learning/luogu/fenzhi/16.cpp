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

}