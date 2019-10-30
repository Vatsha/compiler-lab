import java.io.*;
import java.util.*;
public class LeftRecursion
{
	
	public static void main(String args[])
	{	
				
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter no of line of grammar");
		int n=sc.nextInt();
		 String[] mgrammer=new String[n];
		System.out.println("Enter your grammar");
		for(int i=0;i<n;i++)
		{
			mgrammer[i]=sc.next();
			/*String s[]=mgrammer[i].split("->|\\|");
		for(int k=0;i<s.length;k++)
		{
			System.out.println(s[k]);
		}*/
		}
		
		for(int i=0;i<mgrammer.length;i++)
		RemoveLeftRecursion(mgrammer[i]);
		
		

	}
	public static void RemoveLeftRecursion(String mgrammer)
	{
		ArrayList al=new ArrayList();
		ArrayList al1=new ArrayList();
		String []s=mgrammer.split("->|\\+|\\*|\\/");
		char []c=mgrammer.toCharArray();
		
		if(c[0]==c[3])
		{
			//System.out.println("It is a left recursive grammar");
			int i=4;
			while(c[i]!='|')
			{
				al.add(c[i]);
				i++;	
			}
			for(int k=i+1;k<c.length;k++)
			{
				al1.add(c[k]);
			}
			Iterator itr=al.iterator();  
 			
			Iterator itr1=al1.iterator();  

				//System.out.println("Removing The Left Recursion") ;
				System.out.print(c[0]+"->");
				while(itr1.hasNext())
				{
					
					System.out.print(itr1.next());
				}
				System.out.print(c[0]+"'");
				System.out.println();
				System.out.print(c[0]+"'"+"->");
				while(itr.hasNext())
				{
					System.out.print(itr.next());
				}
				System.out.print(c[0]+"'"+"|"+"eplson");
				System.out.println();
		}
		else
		{
			System.out.print(mgrammer);
			System.out.println();
		}
	
	}
}
