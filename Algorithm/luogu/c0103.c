#include <stdio.h>

int main(){
    char a,b,c;
    b = getchar();
    a = b-1;c=b+1;
    printf("%c %c %c\n",a,b,c);
    printf("%d %d %d",(int)a,(int)b,(int)c);
    return 0;
}