#include <stdio.h>
int judge(double a, double b, double c) {
	int flag;
	if (a <= 0 || b <= 0 || c <= 0) {
		flag = 0;
	}
	else {
		if (a + b > c&&a + c >= b && b + c >= a)
		{
			flag = 1;
		}
		else
			flag = 0;
	}
	return flag;
}
 
int main()
{
	double a[3], b[3], temp;
	while(scanf("%lf %lf %lf %lf %lf %lf", &a[0],&a[1],&a[2],&b[0],&b[1],&b[2])!=EOF)
	{
		if (judge(a[0],a[1],a[2])&&judge(b[0], b[1], b[2]))
		{
			int i,j;
			for (i = 0; i < 2; i++)
			{
				for (j = 0; j < 2 - i; j++)//冒泡排序
				{
					if (a[j] > a[j + 1])
					{
						temp = a[j];
						a[j] = a[j + 1];
						a[j + 1] = temp;
					}
				}
			}
			int m,n;
			for (m = 0; m < 2; m++)
			{
				for (n = 0; n < 2 - m; n++)//冒泡排序
				{
					if (b[n] > b[n + 1])
					{
						temp = b[n];
						b[n] = b[n + 1];
						b[n + 1] = temp;
					}
				}
			}
			if (a[0] > b[0])
			{
				if (a[0] / b[0] == a[1] / b[1] && a[0] / b[0] == a[2] / b[2] && a[1] / b[1] == a[2] / b[2])
					printf("YES\n");
				else
					printf("NO\n");
 
			}
			else
			{
				if (b[0] / a[0] == b[1] / a[1] && b[0] / a[0] == b[2] / a[2] && b[1] / a[1] == b[2] / a[2])
					printf("YES\n");
				else
					printf("NO\n");
			}
		}
		else
		{
			printf("NO\n");
		}
	}
	return 0;
}
