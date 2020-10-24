#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <stdlib.h>
using namespace std;
double a,b,c,p,ans;
int main(){
    cin>>a>>b>>c;
	p=(a+b+c)/2;
	ans=sqrt(p*(p-a)*(p-b)*(p-c));
	printf("%.1lf",ans);
	;
}