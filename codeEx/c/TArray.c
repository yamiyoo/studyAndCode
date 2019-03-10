#include <stdio.h>
int main(){
	int arr[3][2];
	int row = 0, col = 0, cnt = 1;
	for(row = 0;row <= 2;row++){
		for(col = 0;col <= 1;col++){
			arr[row][col] = cnt;
			cnt++;
		}}
	for(row = 0;row <= 2;row++){
		for(col = 0;col <= 1;col++){
			printf("%d ",arr[row][col]);}
	printf("\n");
	}
	printf("%lu\n",sizeof(arr));
	printf("%lu\n",sizeof(arr[1]));
	printf("address:arr[1]%p, &arr[1][0]%p",arr[1],&arr[1][0]);
	return 0;
}
