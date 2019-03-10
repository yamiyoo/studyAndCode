#include<stdio.h>
int *reverse(int *p_num,int size){
	int *p_head = p_num,*p_tail = p_num+size-1,tmp = 0;

	while(p_tail>p_head){
		tmp = *p_head;
		*p_head = *p_tail;
		*p_tail = tmp;
		p_head++;
		p_tail--;
	}
	return p_num;
}
int main(){
	int arr[] = {1,2,3,4,5},num = 0;
	int *p_num = reverse(arr,5);
	for(num = 0;num<=4;num++){
		printf("%d",*(p_num+num));}
	printf(" ");
    return 0;	
}
