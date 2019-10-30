import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.regex.Pattern;
import java.util.regex.Matcher;
 
public class Tokenizer {

	public static class Keyword
	{
		public void extractkeywords(String strLine)
		{
			String s[]=strLine.split(" ");
			for(int i=0;i<s.length;i++)
			{
			Pattern p=Pattern.compile("[^a-zA-Z]int|class|if|import|do|float|char|while|short|byte|static|abstract|continue|boolean|break|case|catch|char|const|default|extends|final|finally|for|implements");
		Matcher m=p.matcher(s[i]);
		 boolean found = false;    
                while (m.find()) {    
			System.out.println(s[i]+" Is Keyword");  
                    found = true;    
                }    
                if(!found){    
                    //System.out.println("No match found.");    
                } 
		}  
		}
	}
	public static class Operator
	{
		public void extractoperator(String strLine)
		{
		String s[]=strLine.split("[A-Za-z]*");
		for(int i=0;i<s.length;i++)
		{
		Pattern p=Pattern.compile("[+|-|%|*]");
		Matcher m=p.matcher(s[i]);
		 boolean found = false;
		    
                while (m.find()) {    
			System.out.println(s[i]+" Is Operator");
                    found = true;    
                }    
                if(!found){    
                   
                }   
		}
		}
		
	}
	public static class Delimiter
	{
		public void extractdelimiter(String strLine)
		{
			String s[]=strLine.split("[A-Za-z]*");
			for(int i=0;i<s.length;i++)
			{
			Pattern p=Pattern.compile("[.|,|;|(|)|<|>]");
		Matcher m=p.matcher(s[i]);
		 boolean found = false;   
		
                while (m.find()) {    
			System.out.println(s[i]+"Is Delimiter");  
                    found = true;    
                }    
                if(!found){    
                    //System.out.println("No match found.");    
                }  
		} 	
		}
	}
	public static class Identifier
	{
		public void extractidentifier(String strLine)
		{
			Pattern p=Pattern.compile("(int [a-zA-Z]*[0-9]*)|(float [a-zA-Z]*[0-9]*)|(double [a-zA-Z]*[0-9]*)");
			Matcher m=p.matcher(strLine);
			boolean found=false;
			while(m.find())
			{
				String s=String.valueOf(m.group());
				String s1[]=s.split(" ");
				System.out.println(s1[1]+" Is Identifier");
                    found = true;
			}
		}
	}
	public static class Constant
	{
		public void extractconstant(String strLine)
		{
				Pattern p=Pattern.compile("(int [a-zA-Z]*[0-9]*=[0-9]+)|(float [a-zA-Z]*[0-9]*=[0-9]+\\.[0-9])|(double [a-zA-Z]*[0-9]*=[0-9]+\\.[0-9]+$)");
				Matcher m=p.matcher(strLine);
				boolean found=false;
			while(m.find())
			{
				String s=String.valueOf(m.group());
				String s1[]=s.split("=");
				System.out.println(s1[1] + " Is Constant");
				found=true;
			}
				
			//}		
				
		}
		
	}
 
    public static void main(String args[]){
        BufferedReader br = null;
        String strLine = "";
	String []a;
	Keyword k=new Keyword();
	Operator o=new Operator();
	Delimiter d=new Delimiter();
	Identifier i=new Identifier();
	Constant c=new Constant();
        try {
            br = new BufferedReader( new FileReader("Summation.java"));
            while( (strLine = br.readLine()) != null){
		k.extractkeywords(strLine);
		o.extractoperator(strLine);
		d.extractdelimiter(strLine);
		i.extractidentifier(strLine);
		c.extractconstant(strLine);
		 
            }
        } catch (FileNotFoundException e) {
            System.err.println("Unable to find the file: fileName");
        } catch (IOException e) {
            System.err.println("Unable to read the file: fileName");
        }
    }
}

