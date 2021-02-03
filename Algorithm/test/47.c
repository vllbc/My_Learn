#include <stdio.h>

int main()
{
    int a, n, i, sum = 0, temp = 0;
    scanf("%d", &a);
    scanf("%d", &n);
    for(i = 1; i <= n; i++)
    {
        temp += a;
        a *= 10;
        sum += temp;
    }
    printf("%d", sum);
    return 0;
}
