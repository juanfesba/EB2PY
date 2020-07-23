package eventb2python.PyAST_Predicates;

import eventb2python.PyAST_Expressions.PyAST_Expression;

public class PyAST_MultiplePredicate extends PyAST_Predicate {
	
	//Private Attributes
	
	//Public Attributes
	public PyAST_Expression SetToCheck;
	public PyAST_Expression[] Children;
	public int ChildrenAmount;
	
	//Constructor
	public PyAST_MultiplePredicate(int childrenAmount){
		CorePredicate = "MultiplePredicate";
		Children = new PyAST_Expression[childrenAmount];
		ChildrenAmount = childrenAmount;
		SetToCheck = new PyAST_Expression();
	}
}