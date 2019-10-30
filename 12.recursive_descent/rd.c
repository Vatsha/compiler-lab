#include<stdio.h>
char prod[100][10];
char s[1000],look,i=0;
prod[0][0]="nT";
prod[1][0]="*nT";
prod[1][1]="{";
s="n*n$";
flag=0;
look=s[i]
void E(){
if(look=='n'){
	match('n');
	T();
}
if(look=="$"){
	printf("SUCCESS");
	flag=1;
}
}
void T(){
if(look=="*"){
	match("*");
	if(look=="n"){
		match(n);
		T();
	}
	else{
		printf("Rejected");
		exit;
	}
}
else{
	for(i=0;i<len(prod[1]);i++){
		if(prod[1][i]=="{"){
			return;
		}
	}
	printf("Rejected");
	exit;

}
}
void match(s){
	i++;
	look=s[i];


}
void main(){
printf("Enter the String\n");
E();
}
