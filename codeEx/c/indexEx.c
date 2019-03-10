#include <stdio.h>
void alter(int *p_num,int *p_num1)
//定义指针用于捆绑
{
	int temp=0;
	temp= *p_num;
	*p_num=*p_num1;
	*p_num1=temp;
	
}
int main(){
	int num,num1;
	scanf("%d%d",&num,&num1);
	alter(&num,&num1);//提供地址
	printf("%d%d",num,num1);
return 0;
}
