#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main(){
	int a[6][6]={0};
	int delta[][2]={-1,-1,-1,0,-1,1,0,-1,0,0,0,1,1,-1,1,0,1,1};
	// 以rowcol为00点周围八个点坐标，分为八组两个数字
	int row =0, col =0, cnt=0, num=0;
	srand(time(0));
do{	
	row=rand() % 6;
    col=rand() % 6;
     if(!a[row][col]){
	 a[row][col]=-1;
	 cnt++;}
     }
     
while(cnt<5);

for(row = 0;row<6;row++){
   for(col=0;col<6;col++){
      if(a[row][col]!=-1)
   		continue;
      /*1 1 1
	   *1 0 1  0:row col
	   *1 1 1
	   */
	 for(num=0;num<8;num++){
	   int tep_row= row+delta[num][0];
	   int tep_col= col+delta[num][1];
	 if(tep_row<0 || tep_row>5){
	 continue;
	 }
	 if(tep_col<0 || tep_col>5){
	 continue;
	 } 
	 if(a[tep_row][tep_col]==-1){
	 continue;}
	 a[tep_row][tep_col]++;
   }}}

    for(row = 0;row<6;row++){
	for(col = 0;col<6;col++){
	   if(!a[row][col]){
	      printf("X");}
		else if(a[row][col]==-1){
		printf("O");}
	   else{
	   printf("%d",a[row][col]);}}
	printf("\n");
	}
	return 0;
}
