#include<iostream>
#include <sstream> 
#include<bits/stdc++.h>
using namespace std;

int main()
{
	string table[7][5]={{"s3", "s4", "1", "2", "0"},
						{"0", "0", "0", "0", "1"},
						{"s3", "s4", "0", "5", "0"},
						{"s3", "s4", "0", "6", "0"},
						{"r3", "r3", "0", "0", "r3"},
						{"0", "0", "0", "0", "r1"},
						{"r2", "r2", "0", "0", "r2"}
						};
	stack<int> s1;
	stack<char> s2;
	s1.push(0);
	s2.push('$');
	string s;
	cout<<"Enter the string\n";
	cin>>s;
	s=s+"$";
	bool flag=1;
	int i=-1;
	int helper=0;

	while(flag==1)
	{
		i++;
		string check;
		char c=s[i];
		cout<<"char: "<<c<<" s1 "<<s1.top();
		if(c=='a')
			check=table[s1.top()][0];
		else if(c=='d')
			check=table[s1.top()][1];
		else if(c=='$')
			check=table[s1.top()][4];
		else
			check="0";
		cout<<"check: "<<check<<"\n";
		if(check=="1")
		{
			cout<<"Accepted\n";
			flag=0;
			break;
		}
		else if(check=="0")
		{
			cout<<"Not a valid string";
			flag=0;
			break;
		}
		else if(check[0]=='s')
		{
			s2.push(s[i]);
			s1.push((int)(check[1]-48));	
		}
		else 
		{
			string div;
			int j=(int)(check[1]-48);
			if(j==1||j==2)
			{
				for(int k=0;k<2;k++)
				{
					s1.pop();
					s2.pop();
				}
				if(j==1)
					div=table[s1.top()][2];
				if(j==2)
					div=table[s1.top()][3];
			}
			if(j==3)
			{
				s1.pop();
				s2.pop();
				div=table[s1.top()][3];
			}
			s1.push(atoi(div.c_str()));
			i--;
		}
	}

}
//input grammar A->cc C->ac C->d






       




