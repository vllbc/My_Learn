// #include <iostream>
// #include <cstdio>
// using namespace std;

// int main(){
//     int n,m;
//     scanf("%d %d",&n,&m);
//     char ch[m];
//     int intt[m];
//     int o;
//     for(o = 0;o<=m-1;o++){
//         intt[o] = 1;
//     }
//     while (n--)
//     {
//         int j = 0;
//         char strr[m+1];
//         scanf("%s",strr);
//         int i;
//         for(i=0;i<=m-1;i++){
//             if(strr[i]==ch[i]){
//                 intt[i]++;
//             }
//             else{ch[i] = strr[i];}
//         }

//     }
//     int quanzhong[m];
//     for(o=0;o<=m-1;o++){
//         scanf("%d",&quanzhong[o]);
//     }
//     int sum;
//     for(o=0;o<=m-1;o++){
//         sum+=quanzhong[o]*intt[o];
//     }
//     printf("%d",sum);
    

//     return 0;
// }
#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
using namespace std;
int main(){
    int n,m,sum;
    int o,j;
    scanf("%d %d",&n,&m);
    char ch[n][m];
    int index[m];
    int i;
    for(i=0;i<=n-1;i++){
        int j; 
        for(j=0;j<=m-1;j++){
            scanf("%c",&ch[i][j]);
        }
    }
    
    for(o = 0;o<=m-1;o++){
        scanf("%d",&index[o]);
    }
    for(o=0;o<=m-1;o++){
        int A,B,C,D,E=0;
        for(j=0;j<=n-1;j++){
            if(ch[j][o] == 'A'){
                A++;
            }
            if(ch[j][o] == 'B'){
                B++;
            }
            if(ch[j][o] == 'C'){
                C++;
            }
            if(ch[j][o] == 'D'){
                D++;
            }
            if(ch[j][o] == 'E'){
                E++;
            }

        }
        int m;
        m = max(A,B);
        m = max(C,m);
        m = max(D,m);
        m = max(E,m);
        sum+=m*index[o];
    }
    printf("%d\n",sum);
    


    
    
}


