#include<stdio.h>
#include<string.h>
void main()  {
    char input[100][100];
    int i=0,j=0,flag=0,n;
printf("Enter the line of productions:");
scanf("%d",&n);
    printf("Enter the productions: ");
for(int i=0;i<n;i++)
    scanf("%s",input[i]);
    
for(i=0;i<n;i++)
recursion(input[i]);

}

void recursion(char *input)
{
int i=0,j=0,flag=0;
char *l,*r,*temp,productions[25][50];
 l = strtok(input,"->");
    r = strtok(NULL,"->");
    temp = strtok(r,"|");
    while(temp)  {
        if(temp[0] == l[0])  {
            flag = 1;
            sprintf(productions[i++],"%s'->%s%s'\0",l,temp+1,l);//E'->aE'
        }
        else
            sprintf(productions[i++],"%s->%s%s'\0",l,temp,l);//E->bE'
        temp = strtok(NULL,"|");
    }
    sprintf(productions[i++],"%s->ε\0",l);
    if(flag == 0)
        printf("The given productions don't have Left Recursion");
    else
        for(j=0;j<i;j++)  {
            printf("\n%s",productions[j]);
        }
}

/*
Enter the productions: E->EAX|A
E'->AXE'
E->AE'
E'->ε
*/
