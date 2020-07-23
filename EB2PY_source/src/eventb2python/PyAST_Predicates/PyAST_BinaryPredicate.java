package eventb2python.PyAST_Predicates;

public class PyAST_BinaryPredicate extends PyAST_Predicate {
	
	//Private Attributes
	
	//Public Attributes
	public String BinaryPredicate;
	public PyAST_Predicate LeftSide;
	public PyAST_Predicate RightSide;
	
	//Constructor
	public PyAST_BinaryPredicate(String binaryPredicate){
		CorePredicate = "BinaryPredicate";
		BinaryPredicate = binaryPredicate;
		LeftSide = new PyAST_Predicate();
		RightSide = new PyAST_Predicate();
	}
}

