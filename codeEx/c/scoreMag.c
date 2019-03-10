#include<stdio.h>
#include<string.h>
int main(){
	int score = 0;
	char str[50] = {0},tmp[10] = {0};
	while(1){
		scanf("%d",&score);
		if(score<0){
			break;}
		sprintf(tmp,"%d,",score);
		strcat(str,tmp);
	}
	str[strlen(str)-1] = 0;
	printf("成绩%s\n",str);
	return 0;
}
