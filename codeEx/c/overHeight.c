#include<stdio.h>

int main(){
printf("input gender,height,weight:");
int g,h,w;
scanf("%d,%d,%d",&g,&h,&w);
if((g && (h-w < 105)) || (!g && (h-w < 110)))
printf("overWeight");
else printf("health");

}
