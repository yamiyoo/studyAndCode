#include<stdio.h>
int main(){
	char str[10] = {0};
	printf("输入:");
	//scanf("%s",str);
	fgets(str,10,stdin);
	if(strlen(str)==9 && str[8]!='\n'){
		//数组里没有\n字符且被充满
		scanf("%*[^\n]");
		//丢掉str中多余内容,使下次正常输入
		scanf("\n");
	}
	printf("%s\n",str);
	printf("输入:");
	//scanf("%s",str);
	fgets(str,10,stdin);
	printf("%s\n",str);
	return 0 ;}
