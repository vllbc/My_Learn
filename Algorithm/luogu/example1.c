#include <stdio.h>
void bools_sort(int a[],int n){
    int i,j;
    for(i=0;i<=n-1;i++){
        for(j=0;j<n-i-1;j++){
            if(a[j]>a[j+1]){
                int temp = a[j];
                a[j] = a[j+1];
                a[j+1] = temp;
            }
        }
    }
}
int main(){
    int n;
    scanf("%d",&n);
    int a[n+2];
    int i;
    for(i=0;i<=n-1;i++){
        scanf("%d",&a[i]);
    }
    bools_sort(a,n);
    long sums=0;
    for(i=2;i<=n-3;i++){
        sums+=a[i];
    }
 
    double mean  = sums/(n*1.0-4.0);
    printf("%.2lf",mean);
    return 0;
    
}
