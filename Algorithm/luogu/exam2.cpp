#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;
int re_min(int a,int b){
    return (b==0)?a:re_min(b,a%b);
}
int main(){
    double a,b;
    cin>>a;
    b = a;
	int count = 0;
	double n = a-(int)a;
	while((int)a != a){
		a*=10;
		count++;
	}
	long long zi = n*pow(10,count);
	long long mu = pow(10,count);
	int x = re_min(mu,zi);
	mu /= x;
	zi /= x;
	printf("%d %d %d",(int)b,zi,mu);
    return 0;
}
