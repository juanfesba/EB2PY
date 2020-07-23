package eventb2python.PyAST_Utils;

import eventb2python.PyAST_Expressions.PyAST_Expression;

public class PyAST_Variant {
	//Private Attributes
	
	//Public Attributes
	public PyAST_Expression VariantExpression;
	public boolean DeterminedVariant;
		
	//Constructor
	public PyAST_Variant(boolean determinedVariant){
		VariantExpression = new PyAST_Expression();
		DeterminedVariant = determinedVariant;
	}
		
	//Methods

}

