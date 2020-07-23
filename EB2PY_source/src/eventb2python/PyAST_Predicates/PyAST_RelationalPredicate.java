package eventb2python.PyAST_Predicates;

import eventb2python.PyAST_Expressions.PyAST_Expression;

public class PyAST_RelationalPredicate extends PyAST_Predicate {
	
	//Private Attributes
	
	//Public Attributes
	public String RelationType;
	public PyAST_Expression LeftSide;
	public PyAST_Expression RightSide;
	
	//Constructor
	public PyAST_RelationalPredicate(String relationType){
		CorePredicate = "RelationalPredicate";
		RelationType = relationType;
		LeftSide = new PyAST_Expression();
		RightSide = new PyAST_Expression();
	}
}
