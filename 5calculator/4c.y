%{
#include<stdio.h>
int flag=0;
%}

%token NUMBER
%left '+' '-'
%left '*' '/' '%'
%left '(' ')'

%%

ArithmeticExpression: E{
printf("\nResult=%d\n",$$);
return 0;
};

E :E'+'E   {$$=$1+$3;}
  |E'-'E   {$$=$1-$3;}
  |E'*'E   {$$=$1*$3;}
  |E'/'E   {$$=$1/$3;}
  |E'%'E   {$$=$1%$3;}
  |'('E')' {$$=$2;}
  |NUMBER  {$$=$1;}
;

%%

void main()
{
printf("\nArithmetic Expression like add, sub, mul...");
yyparse();
if(flag==0)
printf("\narithmeticaly correct\n");
}

void yyerror(){
printf("\narithmeticaly wrong\n");
flag=1;
}
