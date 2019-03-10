#include<stdio.h>

//#include<string.h>
int main(){
	char str[] = "abc";
	printf("有效字符%lu\n",strlen(str));
	printf("sizeof%lu\n",sizeof(str));
	printf("%s\n",strcat(str,"def"));
	printf("%s\n",str);
//第一个参数只能是字符数组
	printf("%s\n",strncat(str,"def",2));
	printf("返回值:%d\n",strcmp("abc","abd"));
	printf("返回值:%d\n",strncmp("abc","abd",2));
	printf("%s\n",strcpy(str,"xyz"));
	printf("%s\n",strncpy(str,"xyz",2));
	memset(str,'h',6);
	printf("%s\n",str);
	printf("%d",strstr("asdadadefijk","def"));
	return 0;
}
