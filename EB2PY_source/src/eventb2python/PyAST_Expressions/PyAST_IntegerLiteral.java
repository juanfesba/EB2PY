package eventb2python.PyAST_Expressions;

public class PyAST_IntegerLiteral extends PyAST_Expression {
	
	//Private Attributes
	
	//Public Attributes
	public String IntegerValue;
	
	//Constructor
	public PyAST_IntegerLiteral(String integerValue){
		CoreExpression = "IntegerLiteral";
		IntegerValue = integerValue;
	}
}
