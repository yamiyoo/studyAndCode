#include <stdio.h>
int main(){
	int arr[]={1,2,3,4,5},num = 0;
	int *p_num = arr;
	for(num = 0;num<5;num++){
	printf("%d",arr[num]);
	printf("%d",p_num[num]);
	}
	printf("\n");
    printf("arr[0]%p;arr[3]%p;arr+3%p;arr-3%p",
			arr,&arr[3],arr+3,arr-3);
}
