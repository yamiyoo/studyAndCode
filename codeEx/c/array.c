#include <stdio.h>
int main(){
	int a[5][5]={0};
	int row=0,col=0;
	for(row = 0;row<=4;row++){
    	for(col = 0;col<=4;col++){
		if(!row && col <=3)
			a[row][col]=1;
		else if(row<=3 && col==4)
			a[row][col]=2;
		else if(row==4 && col>=1)
			a[row][col]=3;
		else if(row>=1 && !col)
			a[row][col]=4;
		}}
	for(row = 0;row<=4;row++){
    	for(col = 0;col<=4;col++){
			printf("%d",a[row][col]);
		}
	printf("\n");}
}
