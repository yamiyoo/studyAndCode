#include <stdio.h>
/*void print(int arr[],int size){
	
	for(int i=size-1;i>=0;i--){
printf("%d",arr[i]);
}printf("\n");
}数组参数传递到函数*/

void neg (int arr[],int size){
    int i;
	for(i=0;i<=size-1;i++){
	arr[i]=0-arr[i];
	}
}
// 数组双向传参
int main(){
  	int arr[]={1,2,3,4,5};
//	print(arr,5);
	neg(arr,5);
	for(int i=0;i<=4;i++){
	printf("%d",arr[i]);
	//主函数可使用任意存储区
	}

	return 0;}
