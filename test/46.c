// #include <stdio.h>
// //ц╟ещеепР 
// int main(){
//     int a[10];
//     int i,j,temp;
//     for(i=0;i<=9;i++){
//         scanf("%d",&a[i]);
//     }
//     for(j=1;j<=9;j++){
//         for(i=0;i<=9-j;i++){
//             if(a[i]>a[i+1]){
//                 temp=a[i];
//                 a[i]=a[i+1];
//                 a[i+1]=temp;
//             }
//         }
//     }
//     for(i=0;i<=9;i++){
//         printf("%d ",a[i]);
//     }


//     return 0;
// }
#include <stdio.h>

int main(){
    int num[10],num2[10];
    int i;
    for(i=0;i<=9;i++){
        scanf("%d",&num[i]);
    }
    for(i=0;i<=9;i++){
        num2[i]=num[9-i];
        printf("%d ",num2[i]);
		
    }


    return 0;
}
