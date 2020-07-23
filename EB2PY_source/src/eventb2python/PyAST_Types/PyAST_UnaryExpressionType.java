package eventb2python.PyAST_Types;

public class PyAST_UnaryExpressionType extends PyAST_Type {
	
	//Private Attributes
	
	//Public Attributes
	public String UnaryExpression;
	public PyAST_Type InternalType;
	public String InternalTypeInterpretation;
	
	//Constructor
	public PyAST_UnaryExpressionType(String unaryExpressionType){
		CoreType = "UnaryExpressionType";
		UnaryExpression = unaryExpressionType;
		InternalType = new PyAST_Type();
		
		switch(unaryExpressionType) {
		case "PowerSet":
			InternalTypeInterpretation = "PySet";
			break;
		default:
			InternalTypeInterpretation = "ErrorUnaryExpressionType";
		}
	}
}
