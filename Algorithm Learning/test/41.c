#include<stdio.h>
int main()
{
	double x,f;
	while(scanf("%lf",&x)!=EOF)
	{
		if(x>0)
		{
			f=x*x+1;
		}
		else if(x<0)
		{
			f=-x;
		}
		else
		{
			f=100.0;
		}
		printf("%.1lf\n",f);
	}
	return 0;
}