package eventb2python.PyAST_Predicates;

import eventb2python.PyAST_Expressions.PyAST_Expression;

public class PyAST_SimplePredicate extends PyAST_Predicate {
	
	//Private Attributes
	
	//Public Attributes
	public String SimpleType;
	public PyAST_Expression InternalExpression;
	
	//Constructor
	public PyAST_SimplePredicate(String simpleType){
		CorePredicate = "SimplePredicate";
		SimpleType = simpleType;
		InternalExpression = new PyAST_Expression();
	}
}