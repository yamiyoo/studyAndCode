#include<stdio.h>

int *read(void){
	static int num;
	scanf("%d",&num);
	return &num;
}
int main(){
	int *p_num = read();
	printf("%d\n",*p_num);
	return 0;
}
