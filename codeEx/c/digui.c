#include<stdio.h>

int getword(int n){
  if(n==1)
	  return(1);
  else return(getword(n-1)+n);
}
int main(){
  int num;
  scanf("%d",&num);
  printf("%d",getword(num));
  return 0;
}
