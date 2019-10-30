%{


%}
%%
[\t\n]+
[a-zA-Z]+[ ][a-zA-Z]+[ ][a-zA-Z]+ {
       printf("%s:  svo\n", yytext);
      }
.|\n        { printf("");/* normal default anyway */ }

%%

main()
{
     yylex();
}
