package eventb2python.PyAST_Predicates;

public class PyAST_AssociativePredicate extends PyAST_Predicate {
	
	//Private Attributes
	
	//Public Attributes
	public String AssociativePredicate;
	public PyAST_Predicate[] Children;
	public int ChildrenAmount;
	public String OperatorSymbol;
	
	//Constructor
	public PyAST_AssociativePredicate(String associativePredicate,int childrenAmount){
		CorePredicate = "AssociativePredicate";
		AssociativePredicate = associativePredicate;
		Children = new PyAST_Predicate[childrenAmount];
		ChildrenAmount = childrenAmount;
		
		switch (associativePredicate) {
		case "LogicalOR":
			OperatorSymbol = "or";
			break;
		case "LogicalAND":
			OperatorSymbol = "and";
			break;
		default:
			OperatorSymbol = "ErrorAssociativePredicate";
		}
	}
}
