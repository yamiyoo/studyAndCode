#include <stdio.h>
void print(){
printf("1\n");
print();
}
int main(){
print();
return 0;}
