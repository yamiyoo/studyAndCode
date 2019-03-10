#include<stdio.h>
int main(){
int a=0;
int b=0;
int c=0;
int g=0;
a++;
++b;
c=++c;
g=g++;
printf("%d%d%d%d",a,b,c,g);
int d=0,e=0;
1 || ++d;
1 || e++;
printf("%d%d",d,e);
int i=3;
int k=(i++) + (i++) + (i++);
printf("/n%d%d",k,i);
}
