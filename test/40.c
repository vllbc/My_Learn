#include <stdio.h>

int main(){
    int num;
    scanf("%d",&num);
    while(num>=1){
        int a,b,c,reg;
        scanf("%d %d %d",&a,&b,&c);
        reg = (a+b+c)/3;
        if((reg>=a&&reg>=b)||(reg>=a&&reg>=c)||(reg>=b&&reg>=c)){
            printf("No\n");
            num--;
            continue;
        }
        printf("Yes\n");
        num--;
    }
    
    return 0;
}
