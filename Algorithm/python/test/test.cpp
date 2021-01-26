#include <iostream>
using namespace std;
int main()
{int a[30][30],b[30][30],n,m,i,j;
cin>>n>>m;
for (i=0;i<n;i++)
 {for (j=0;j<m;j++)
  b[i][j] = 1;
 }
for (i=0;i<n;i++)
 {for (j=0;j<m;j++)
  cin>>a[i][j];
 }
cout<<endl;
for (i=0;i<n;i++)
 {for (j=0;j<m-2;j++)
  {if (a[i][j]==a[i][j+1]&&a[i][j+1]==a[i][j+2]) 
   {b[i][j]=0;
    b[i][j+1]=0;
    b[i][j+2]=0;
   }
  }
 }
for (i=0;i<n-2;i++)
 {for (j=0;j<m;j++)
  {if (a[i][j]==a[i+1][j]&&a[i+1][j]==a[i+2][j]) 
   {b[i][j]=0;
    b[i+1][j]=0;
    b[i+2][j]=0;
   }
  }
 }
for (i=0;i<n;i++)
 {for (j=0;j<m-1;j++)
  {if (b[i][j]==0) 
   cout<<b[i][j]<<" ";
	else cout << a[i][j]<<" ";
  }
  if (b[i][j]==0) 
   cout<<b[i][j]<<endl;
	else cout << a[i][j]<<endl;
 }
//for (i=0;i<n;i++)
// {for (j=0;j<m-1;j++)
//  cout<<a[i][j]<<" ";
//  cout<<a[i][j]<<endl;
// }
return 0;
}

