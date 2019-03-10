#include <stdio.h>
double add(double,double);
//显示声明
int main(){
	int num0,num1,sum;
	scanf("%d,%d",&num0,&num1);
	sum = add(num0,num1);
    printf("%d",sum);
	return 0;
}

double add(double a,double b){//隐式声明
return (a+b);
}
