#include<stdio.h>
int main(){
	char str[] = "abcdef";
	printf("%p\n","abc");
	printf("%p\n","ab""c");
	printf("%c\n",*"abc");
	//*"abc" = 'r'
	//错误,字面值不能修改
	printf("sizeof(str)是%lu\n",sizeof(str));
	printf("%s\n",str);
	return 0;
}
