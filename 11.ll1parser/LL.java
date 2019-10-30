import java.util.*;
import java.io.*;
/**
   Implements the <code>LL(1)</code> top-down analysis. 
   Usage:<br>
   <code>java LL "input" grammar</code>.
   The normal execution shows the evolution of the stack ended by the
   message "input accepted".
   If the grammar is not <code>LL(1)</code>, an error message 
   "The grammar is not LL(1)" is issued. The message also indicates
   which rules generate the conflict. If the input is not correct, an
   error message "Syntax error" or "Syntax error: end of input" is issued.
*/
public class LL {
   /**
       The expression to analyze.
    */
    public char[] expression; 
    /**
       The current index.
    */   
    public int position; 
    /**
       The stack used to store the LR states.
    */       
    public Stack stack;
    /**
       The current context-free grammar.
    */
    public Grammar G;
    /**
       The input alphabet;
    */
    public Alphabet alphabet;
    /**
       The LL(1) table.
    */
    int[][] LLTable;
   /**
       Advance one character to the right on input.
    */
   public void advance(){
	position++;
    }
   /**
       Returns the current token of the input. Discards possible
       space characters.
    */
    public short current(){
	while(expression[position] == ' ')
	    advance();
	char c = expression[position];
	return (Character.isDigit(c))? 
	    alphabet.toShort('c') : alphabet.toShort(c);
    }
    /**
       Pop the left side of production <code>n</code> and push the right side .
    */
    public void push(int n){
	stack.pop();
	Production[] P = G.productionsArray;
	short[] right = alphabet.toShort(P[n].right);
	int le = right.length;
	for(int i = le - 1; i >= 0; i--)
	    stack.push(new Short(right[i]));
    }
    /**
       Cancels the current character with the top of stack.
    */
    public void cancel(){
	advance();
	stack.pop();
    }
    /**
       True if the input has been read completely.
    */
    public boolean endOfInput(){
	return position == expression.length;
    }
    /**
       Creates the <code>LLTable</code> and initializes the stack.
    */
    public LL(String exp, Grammar grammar){
	G = grammar;
	alphabet = G.alphabet;
	try{
	    LLTable = LLTable();
	} catch (Exception e){
	    System.out.println(e);
	    System.exit(1);
	}
	expression = exp.toCharArray();
	stack = new Stack();
	char v = G.productionsArray[G.initial].left;
	stack.push(new Short(alphabet.toShort(v)));
    }
  /**
       The LL(1) table analysis. The entry <code>table[v][c]</code>
       is the rule to
       apply if the variable <code>v</code> is on the stack and 
       <code>v</code> is the lookahead value.
       @return the LL(1) table
    */
    public int[][] LLTable() throws Exception {   
	int[][] table=new int[G.variables.size()][G.terminals.size()];
	    //initialize LL table
	for(int i = 0; i < G.variables.size(); i++)
	    for(int j = 0; j < G.terminals.size(); j++)
		table[i][j] = -1; 
	for(int i = 0; i < G.nbProductions; i++){
	    short[] r = G.alphabet.toShort(G.productionsArray[i].right);
	    short v = G.variables.toShort(G.productionsArray[i].left);
	    if(r.length > 0){
		Set s = G.first(r);
		for(Iterator it = s.iterator(); it.hasNext(); ) {
		    int u = ((Short) it.next()).shortValue();
		    if(table[v][u] != -1){
			System.out.print("Conflict between rules" +i+" and "+ 
					 table[v][u]);
			throw new Exception("The grammar is not LL(1)");
		    }
		    else
			table[v][u] = i;
		}
	    }
	    if(r.length == 0) {      //rule i is an epsilon rule
		Set f = G.follow(v);
		for(Iterator it = f.iterator(); it.hasNext(); ){
		    short u = ((Short) it.next()).shortValue();
		    if(table[v][u] != -1){
			System.out.print("Conflict between rules " +i+" and "+ 
					 table[v][u] + "for u =" 
					 +G.terminals.toChar(u));
			throw new Exception("The grammar is not LL(1)");
		    }
		    else
			table[v][u] = i;
		}
	    }
	}
	return table;   

    }
    /**
       Parses the input expression using the LL(1) analysis alpgorithm.
    */
    public void lLParse() throws Exception {
	System.out.println(stack);
	while(true){
	    if(stack.isEmpty())
		if(endOfInput()){
		    System.out.println("input accepted\n");
		    break;
		}
		else
		    throw new Exception("Syntax error: end of input");
	    short c = current();
	    short v = ((Short) stack.peek()).shortValue();
	    if(G.terminals.isIn(alphabet.toChar(v)))
		if(v == c) {
		    cancel();
		    System.out.println(stack);
		}
		else throw new Exception("Syntax error");
	    else {
		v = G.alphabet.convert(G.variables, v);
		int n = LLTable[v][alphabet.convert(G.terminals,c)];
		if(n != -1){
		    push(n);
		    System.out.println(stack);
		}
		else throw new Exception("Syntax error");
	    }
	}
    }
   static void printTable(String s,int[][] table){
	System.out.println(s);
	for(int i = 0; i < table.length; i++){
	    System.out.print(i+" ");
	    for(int j = 0; j < table[i].length; j++)
		System.out.print(table[i][j]+" ");
	    System.out.println();
	}
    }
    public static void main(String[] args) throws IOException {
	String exp = args[0]+'$';
	LL input = new LL(exp, Grammar.fromFile(args[1]));
	try{
	    input.lLParse();
	}catch(Exception e){
	    System.out.println(e);
	    System.exit(1);
	}
    }
}
