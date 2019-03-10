#include<stdio.h>
#include<string.h>
int main(){
	char str[10] = {0};
	int i = 0;
	for(i=1;i<=3;i++){
		printf("用户名: ");
		fgets(str,10,stdin);
		if (strlen(str)==9 && str[8]!='\n'){
			scanf("%*[^\n]");
			scanf("%*c");}
		if(strcmp(str,"admin\n")){
			continue;}
		printf("密码: ");
		fgets(str,10,stdin);
		if (strlen(str)==9 && str[8]!='\n'){
			scanf("%*[^\n]");
			scanf("%*c");}
		if(strcmp(str,"123456\n")){
			continue;}
		break;
	}
	if(i<=3){
		printf("登录成功\n");}
	else{
		printf("登录失败\n");}
	return 0;
}
