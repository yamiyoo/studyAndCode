#include<stdio.h>
#include<stdlib.h>
int main(int argc,char *argv[]){
	int heads = 0,leg = 0;
	if (argc < 3){
		printf("erro\n");
		return 0;
	}
	heads = atoi(argv[1]);
	leg = atoi(argv[2]);
	int num = 0;
	for(num = 0;num<=heads;num++){
		if(4*num + 2*(heads-num)==leg){
			printf("兔%d鸡%d",num,heads-num);
			return 0;
		}
		}
	return 0;
}
