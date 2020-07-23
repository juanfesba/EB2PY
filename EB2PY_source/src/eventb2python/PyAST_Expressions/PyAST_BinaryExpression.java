package eventb2python.PyAST_Expressions;

public class PyAST_BinaryExpression extends PyAST_Expression {
	
	//Private Attributes
	
	//Public Attributes
	public String BinaryOperation;
	public PyAST_Expression LeftSide;
	public PyAST_Expression RightSide;
	public String OperatorSymbol;
	
	//Constructor
	public PyAST_BinaryExpression(String binaryOperation){
		CoreExpression = "BinaryExpression";
		BinaryOperation = binaryOperation;
		LeftSide = new PyAST_Expression();
		RightSide = new PyAST_Expression();
		
		switch(binaryOperation) {
		case "Tuple":
			OperatorSymbol = ",";
			break;
		case "Relation":
			OperatorSymbol = "Relations";
			break;
		case "TotalRelation":
			OperatorSymbol = "TotalRelations";
			break;
		case "SurjectiveRelation":
			OperatorSymbol = "SurjectiveRelations";
			break;
		case "TotalSurjectiveRelation":
			OperatorSymbol = "TotalSurjectiveRelations";
			break;
		case "PartialFunction":
			OperatorSymbol = "PartialFunctions";
			break;
		case "TotalFunction":
			OperatorSymbol = "TotalFunctions";
			break;
		case "PartialInjection":
			OperatorSymbol = "PartialInjections";
			break;
		case "TotalInjection":
			OperatorSymbol = "TotalInjections";
			break;
		case "PartialSurjection":
			OperatorSymbol = "PartialSurjections";
			break;
		case "TotalSurjection":
			OperatorSymbol = "TotalSurjections";
			break;
		case "Bijection":
			OperatorSymbol = "Bijections";
			break;
		case "Difference":
			OperatorSymbol = ".PyDifference";
			break;
		case "CartesianProduct":
			OperatorSymbol = ".PyCartesianProduct";
			break;
		case "DirectProduct":
			OperatorSymbol = ".PyDirectProduct";
			break;
		case "DomainRestriction":
			OperatorSymbol = ".PyDomainRestriction";
			break;
		case "DomainSubstraction":
			OperatorSymbol = ".PyDomainSubstraction";
			break;
		case "RangeRestriction":
			OperatorSymbol = ".PyRangeRestriction";
			break;
		case "RangeSubstraction":
			OperatorSymbol = ".PyRangeSubstraction";
			break;
		case "UpTo":
			OperatorSymbol = ",";
			break;
		case "Minus":
			OperatorSymbol = "-";
			break;
		case "Division":
			OperatorSymbol = "//";
			break;
		case "Mod":
			OperatorSymbol = "%";
			break;
		case "Exponentiation":
			OperatorSymbol = "**";
			break;
		case "Apply":
			OperatorSymbol = "()";
			break;
		case "RelationalImage":
			OperatorSymbol = "[]";
			break;
		default:
			OperatorSymbol = "ErrorBinaryExpression";
		}
	}
}
