#include<stdio.h>
int main(){
	char *strs[] = {"abc","def","qpr","vbn","xyz"};
	//字符指针数
	char strs1[][10] = {"abc","def","qpr","vbn","xyz"};
	int num = 0;
	for(num = 0;num<=4;num++){
		printf("%s\n",strs[num]);
		printf("%s\n",strs1[num]);
	}
	return 0;
}
