package eventb2python.PyAST_Utils;

import eventb2python.PyAST_Predicates.PyAST_Predicate;

public class PyAST_Axiom {
	//Private Attributes
	
	//Public Attributes
	public String AxiomLabel;
	public PyAST_Predicate AxiomPredicate;
	public boolean IsTheorem;
		
	//Constructor
	public PyAST_Axiom(String label,boolean isTheorem){
		AxiomLabel = label;
		AxiomPredicate = new PyAST_Predicate();
		IsTheorem = isTheorem;
	}
		
	//Methods
}
