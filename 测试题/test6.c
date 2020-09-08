//#include <stdio.h>
//int main()
//{
	
	// char b;
	// scanf("%c", &b);
	// if (b >= 'A' && b <= 'Z')
	// 	{
	// 		b = b + 32;
	// 		printf("%c", b);
	// 	}
	// else if (b >= 'a' && b <= 'z')
	// 	{
	// 		b = b - 32;
	// 		printf("%c", b);
	// 	}
	
	// return 0;只能实现一个字母的转换
	
// 	int xxx = 2;
// 	while (xxx)

// 	{
// 		char b;
// 		scanf("%c",&b);
// 		if(b >= 'A' && b <= 'Z'){   
// 			b = b+32;
// 			printf("%c",b);
// 		}
// 		else if(b >='a' && b <= 'z')
// 		{
// 			b = b-32;
// 			 printf("%c",b);
// 		}
// 		// 注意是单引号 代表的是字符 不是字符串 相当于一个整数
// 		/* code */
// 	}
// 	return 0;/*注意不要吧return写在while循环里面否则就会运行一次*/
	
// }
#include  <stdio.h>
int main(){

  char charr;
  scanf("%c",&charr);
  printf("%c",charr-32);
  return 0;
}
