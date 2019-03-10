#include <stdio.h>
#include <stdlib.h>
int func(){
	printf("2\n");
  // return ;//屏蔽3	
    exit(0);//立刻结束整个函数屏蔽34
	printf("3\n");
}
int main(){
	printf("1\n");
	func();
	printf("4\n");
	return 0;
}
