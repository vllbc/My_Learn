#include <iostream>
#include <cstdio>
using namespace std;
int main(){
   int m,n,a=1,c=1;
   cin>>m>>n;
   for(int i=1;i<=n;i++){ //���� 
       int b=i;
       c+=2;
       int d=m;
       for(int j=1;j<=n;j++){ //���� 
           if(b>=0){
               printf("%4d",d);
               if(b>0){
                   d--;
               }
               b--;
           }else{
               d+=a;
               printf("%4d",d);
           }
           if(j>0){
               a+=2;
           }
       }
       printf("\n");
       m+=c;
       a=1;
   }
   return 0;
}
