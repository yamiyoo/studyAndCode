#include <stdio.h>
int Gnum;
void fun(void){
    static int num;
   /* Gnum = num;
printf("%d %d",num,Gnum);
*/
	printf("%d\n",num);
	num=10;
}
void func(void){
	int num=100;
	fun();	
}
int main(){
	fun();
	func();
	return 0;
//	int num;
//printf("%d %d",num,Gnum);
}


