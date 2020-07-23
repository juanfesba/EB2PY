package eventb2python.PyAST_Expressions;

import eventb2python.PyAST_Predicates.PyAST_Predicate;

public class PyAST_QuantifiedExpression extends PyAST_Expression {
	
	//Private Attributes
	
	//Public Attributes
	public String QuantifiedPredicate;
	public PyAST_Predicate InternalPredicate;
	public int BoundIdentDeclAmount;
	
	//Constructor
	public PyAST_QuantifiedExpression(int boundIdentDeclAmount){
		CoreExpression = "QuantifiedExpression";
		InternalPredicate = new PyAST_Predicate();
		BoundIdentDeclAmount = boundIdentDeclAmount;
	}
}