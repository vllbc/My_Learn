#include <stdio.h>

// int main(){
//     int num;
//     scanf("%d",num);
//     num = num *10;
//     if(num %3 == 0){
//         printf("%d %d",num/3,0);

//     }
//     else
//     {
//         int intt;
//         intt = num - num %3;
//         printf("%d",intt/3,num %3);

//     }
//     return 0;
    
// }
int main(){
    int intt;
    printf("��Ҫ��С褶���Ԫ��");
    scanf("%d",&intt);
    intt = intt *10;
    if(intt %3 == 0){
        printf("��������%d��",intt/3,0);
    }
    else
    {
        int iii = intt - intt%3;
        printf("����%d�� ��ʣ%dë",iii/3,intt%3);

    }
    
    return 0;
}
//ע��