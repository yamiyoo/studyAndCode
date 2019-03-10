#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main(){

    int size,num = 0;
	srand(time(0));	
	printf("input number");
	scanf("%d",&size);
	int arr[size];
	for(num = 0;num < size;num++){
	arr[num]=rand() % 36+1;
	}
	for(num = 0;num < size;num++){
	printf("%d ",arr[num]);
	}
	printf("\n");
    return 0;
}


