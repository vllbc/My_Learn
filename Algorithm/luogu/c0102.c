#include <stdio.h>
int main(){
	int sums;
    int a,b,c;
    scanf("%d",&sums);
    if(sums <0 || sums/100<1 || sums /100>=10){
    	printf("%d",-1);
    	return 0;
	}
    a = sums/100;
    b = sums/10%10;
    c = sums%10;
    if(b==0 && c==0){
        printf("%d",a);
        return 0;
    }
    if(c==0){
        printf("%d%d",b,a);
        return 0;
    }
    printf("%d%d%d",c,b,a);
    return 0;
}
