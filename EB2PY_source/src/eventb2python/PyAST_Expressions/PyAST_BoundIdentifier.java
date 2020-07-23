package eventb2python.PyAST_Expressions;

public class PyAST_BoundIdentifier extends PyAST_Expression {
	
	//Private Attributes
	
	//Public Attributes
	public int BoundIdentifierIndex;
	
	//Constructor
	public PyAST_BoundIdentifier(int boundIdentifierIndex){
		CoreExpression = "BoundIdentifier";
		BoundIdentifierIndex = boundIdentifierIndex;
	}
}
