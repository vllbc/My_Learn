// #include <stdio.h>

// int main(){
    
//     int n;
//     while (scanf("%d",&n)!=EOF)
//     {
//         int i=1;
//         int cout=0;
//         while (i<=n)
//         {
//             if(i%5==0 || i%6==0||i%8==0){
//                 cout++;
//             }
//             i++;
//         }
//         printf("%d\n",cout);
        
//     }
    
    
//     return 0;

// 上面的代码TLE了}
#include<stdio.h>
int main()
{
   int n,a,b,c,sum,ab,ac,bc,abc;
   while(scanf("%d",&n)!=EOF)
   { 
     sum=0;
     a=n/5;
     b=n/6;
     c=n/8;
     ab=n/30;
     ac=n/40;
     bc=n/24;
     abc=n/120;
     sum=a+b+c-ab-ac-bc+abc;  //两两之间公倍数被算两次，减去一次；三个数公倍数被算三次，又被减三次，最后直接加一次
     printf("%d\n",sum);
   } 
   return 0;
}
