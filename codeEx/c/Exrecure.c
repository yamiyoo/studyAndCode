#include <stdio.h>
/*int add(int e){
	if(e==1)
	{  return 1;
	}
	return (e+add(e-1));
}*/
int arr[50];
int fbl(int e){
//	int arr[50]={0};局部变量每一次调用都重新组建
	if(e <= 1){
	return 1;}
	if(!arr[e-2]){
	arr[e-2] = fbl(e-2);
	}
	if(!arr[e-1]){
	arr[e-1] = fbl(e-1);
	}
	return arr[e-1]+arr[e-2];
}
int main(){
	int s;
//	s = add(10);
//	printf("%d\n",s);
    scanf("%d",&s);
	printf("%d",fbl(s));
	return 0;
}
