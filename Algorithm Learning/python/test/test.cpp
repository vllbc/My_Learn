#include <iostream>
#include <Algorithm>
using namespace std;
int main()
{
int n,i,j,t;
cin>>n;
int a[n];
for (i=0;i<n;i++)
 cin>>a[i];
sort(a,a+n);
for (i=0;i<n-1;i++)
cout<<a[i]<<"->";
cout<<a[n-1]<<endl;
for (i=n-1;i>0;i--)
cout<<a[i]<<"->";
cout<<a[0];
return 0;
}

