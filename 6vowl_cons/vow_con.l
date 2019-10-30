%{
		#include<stdio.h>
        	int no_count=0;
		int vo_count=0;
		int co_count=0;
		int co_line =0;
		int co_art = 0;
		int index1 = 0;
%}
alpha    [a-zA-Z]*
digit      [0-9]+
space    [ \t\n]
vow     [a|e|i|o|u|E|A|I|O|U]
con		[a-zA-Z (^a|i|e|o|u|E|A|I|O|U)]
end     [.|,]
article_vo [\b(a|an)\b]
article [\b\(the)b]

%%

{digit}{space} {no_count++;index1++;printf("%s starts with number at %d\n",yytext,index1);}
{article}{space}					{co_art++;printf("%s is article\n",yytext);}
{article_vo}{space}		{co_art++;vo_count++;index1++;printf("%s is article and vowels at %d\n",yytext,index1);}
{vow}{alpha}{space}					{vo_count++;index1++;printf("%s starts with vowelat %d\n",yytext,index1);}
{con}{alpha}{space}					{co_count++;index1++;printf("%s starts with consonants at %d\n",yytext,index1);}
{end}				{co_line++;index1++;}
;

%%

int main(int ac, char **av)
{
    FILE    *fd;

    if (ac == 2)
    {
        if (!(fd = fopen(av[1], "r")))
        {
            perror("Error: ");
            return (-1);
        }
        yyset_in(fd);
        yylex();
	printf("number count= %d\n",no_count);
	printf("vowels count= %d\n",vo_count);
	printf("consonats count= %d\n",co_count);
	printf("line count= %d\n",co_line);
	printf("article count= %d\n",co_art);
        fclose(fd);
    }
    else
        printf("Usage: a.out filename\n");
    return (0);
}
