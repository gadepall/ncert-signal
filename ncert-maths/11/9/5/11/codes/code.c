#include <stdio.h>
#include <math.h>
int main(){
for(int r=-10;r<=10;r++){
if(pow(r,5)-4*pow(r,4)+pow(r,3)-4*pow(r,2)+r-4==0){
printf("%d",r);
}
}
return 0;
}
