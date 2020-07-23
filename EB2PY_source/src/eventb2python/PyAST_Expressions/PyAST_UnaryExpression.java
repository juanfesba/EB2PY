package eventb2python.PyAST_Expressions;

public class PyAST_UnaryExpression extends PyAST_Expression {
	
	//Private Attributes
	
	//Public Attributes
	public String UnaryExpression;
	public PyAST_Expression InternalExpression;
	public String OperatorSymbol;
	public String PreludeName;
	
	//Constructor
	public PyAST_UnaryExpression(String unaryExpression){
		CoreExpression = "UnaryExpression";
		UnaryExpression = unaryExpression;
		InternalExpression = new PyAST_Expression();
		PreludeName = "P";
		
		switch(unaryExpression) {
		case "Cardinality":
			OperatorSymbol = "len";
			break;
		case "PowerSet":
			OperatorSymbol = ".PyPowerSet()";
			break;
		case "PowerSet1":
			OperatorSymbol = ".PyPowerSet1()";
			break;
		case "Domain":
			OperatorSymbol = ".PyDomain()";
			break;
		case "Range":
			OperatorSymbol = ".PyRange()";
			break;
		case "Minimum":
			OperatorSymbol = PreludeName + ".Minimum";
			break;
		case "Maximum":
			OperatorSymbol = PreludeName + ".Maximum";
			break;
		case "Inverse":
			OperatorSymbol = "~";
			break;
		case "UnaryMinus":
			OperatorSymbol = "-";
			break;
		default:
			OperatorSymbol = "ErrorUnaryExpression";
		}
	}
}
