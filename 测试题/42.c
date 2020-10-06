#include <stdio.h>

int main(){
    int num;
    scanf("%d",&num);
    while(num>=1)
    {
    	int iii;
    	scanf("%d",&iii);
        if(1000000%iii==0){
            printf("%d\n",1000000/iii);
        }
        else
        {
            printf("No\n");
        }
        num--;
        
        
    }
    
    return 0;
}
