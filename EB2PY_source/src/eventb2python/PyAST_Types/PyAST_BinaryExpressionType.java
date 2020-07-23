package eventb2python.PyAST_Types;

public class PyAST_BinaryExpressionType extends PyAST_Type {
	
	//Private Attributes
	
	//Public Attributes
	public String BinaryExpressionType;
	public PyAST_Type LeftSide;
	public PyAST_Type RightSide;
	public String TypeSymbolInterpretation;
	
	//Constructor
	public PyAST_BinaryExpressionType(String binaryExpressionType){
		CoreType = "BinaryExpressionType";
		BinaryExpressionType = binaryExpressionType;
		LeftSide = new PyAST_Type();
		RightSide = new PyAST_Type();
		
		switch(binaryExpressionType) {
		case "CartesianProduct":
			TypeSymbolInterpretation = "Tuple";
			break;
		case "Relation":
			TypeSymbolInterpretation = "PyRel";
			break;
		default:
			TypeSymbolInterpretation = "ErrorBinaryExpressionType";
		}
	}
}