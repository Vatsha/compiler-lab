%{
#include<stdio.h>
%}

%token ID NUMBER
%left '+' '-'
%right '*' '/'

%%
stmt:expr
	;
expr: expr '+' expr
	| expr '-' expr
	| expr '*' expr
	| expr '/' expr
	| '(' expr ')'	
	| NUMBER
	| ID

%%

void main()
{
printf("enter expr :\n");
yyparse();
printf("valid expr");
exit(0);
}
yywrap(){}
yyerror()
{
printf("ERROR \n");
}
