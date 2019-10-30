%{
#include<stdio.h>
int valid=1;
%}
%token A B
%%
str:S'\n' {return 0;}
	;
S:A S B
	|
	;
%%
void main()
{
   printf("Enter the string:\n");
   yyparse();
   if(valid==1)
   printf("\nvalid string");
   exit(0);
}

yywrap(){}
yyerror()
{
printf("ERROR \n");
valid=0;
}
