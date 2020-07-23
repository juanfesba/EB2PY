package eventb2python.PyAST_Expressions;

public class PyAST_AssociativeExpression extends PyAST_Expression {
	
	//Private Attributes
	
	//Public Attributes
	public String AssociativeExpression;
	public PyAST_Expression[] Children;
	public int ChildrenAmount;
	public String OperatorSymbol;
	
	//Constructor
	public PyAST_AssociativeExpression(String associativeExpression,int childrenAmount){
		CoreExpression = "AssociativeExpression";
		AssociativeExpression = associativeExpression;
		Children = new PyAST_Expression[childrenAmount];
		ChildrenAmount = childrenAmount;
		
		switch (associativeExpression) {
		case "Union":
			OperatorSymbol = "PyUnion";
			break;
		case "Intersection":
			OperatorSymbol = "PyIntersection";
			break;
		case "BackwardComposition":
			OperatorSymbol = "PyBackwardComposition";
			break;
		case "ForwardComposition":
			OperatorSymbol = "PyComposition";
			break;
		case "Overriding":
			OperatorSymbol = "PyOverriding";
			break;
		case "Addition":
			OperatorSymbol = "+";
			break;
		case "Multiplication":
			OperatorSymbol = "*";
			break;
		default:
			OperatorSymbol = "ErrorAssociativeExpression";
		}
	}
}
