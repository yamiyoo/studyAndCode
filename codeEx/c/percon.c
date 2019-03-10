#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int main(){
	char *p_grade = "10,20,30,40,50",*p_tmp = p_grade;
	int sum = 0;
	while(1){
		sum += atoi(p_tmp);
		p_tmp = strstr(p_tmp,",");
		if(!p_tmp){
			break;}
		p_tmp++;	
	}
	printf("%d\n",sum);
	return 0 ;

}
