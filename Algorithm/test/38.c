#include<stdio.h>
#define PI 3.1415927 
int main()
{
 double a,b,c;
 while(scanf("%lf",&a)!=EOF)
 {
  c=a*a*a;
  b=((double)4/(double)3)*PI*c;
  printf("%0.3lf\n",b);
  }
   return 0;
}