#include <iostream>
#include <cstdio>
using namespace std;
//
//int main(){
//    int a[] = {2,1,5,3,6,9,3,4};
//  
//    int n = 8;
//    for(int i=0;i < n-1;i++){
//        for(int j=0;j < n-i-1;j++){
//            if(a[j] > a[j+1]){
//                int temp = a[j];
//                a[j] = a[j+1];
//                a[j+1] = temp;
//            }
//        }
//    }
//    for(int i=0;i<n;i++){
//        cout<<a[i]<<" ";
//    }
//    return 0;
//}
int main(){
	int a[] = {2,1,5,3,6,9,3,4};
	int n = 8;
	for(int i = 0;i < n-1;i++){
		int min = i;
		for(int j=i+1;j<=n-1;j++){
			if(a[j] < a[min]){
				min = j;
			}
		}
		int temp = a[i];
		a[i] = a[min];
		a[min] = temp;
}
	
	for(int i=0;i<n;i++){
		cout<<a[i]<<" ";
	}
	return 0;
}
