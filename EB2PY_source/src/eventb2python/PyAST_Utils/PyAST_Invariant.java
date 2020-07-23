package eventb2python.PyAST_Utils;

import eventb2python.PyAST_Predicates.PyAST_Predicate;

public class PyAST_Invariant {
	//Private Attributes
	
	//Public Attributes
	public String InvariantLabel;
	public PyAST_Predicate InvariantPredicate;
	public boolean IsTheorem;
		
	//Constructor
	public PyAST_Invariant(String label,boolean isTheorem){
		InvariantLabel = label;
		InvariantPredicate = new PyAST_Predicate();
		IsTheorem = isTheorem;
	}
		
	//Methods

}
