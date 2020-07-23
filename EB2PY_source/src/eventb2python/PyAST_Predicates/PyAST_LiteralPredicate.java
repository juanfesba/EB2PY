package eventb2python.PyAST_Predicates;

public class PyAST_LiteralPredicate extends PyAST_Predicate {
	
	//Private Attributes
	
	//Public Attributes
	public String LiteralType;
	
	//Constructor
	public PyAST_LiteralPredicate(String literalType){
		CorePredicate = "LiteralPredicate";
		LiteralType = literalType;
	}
}
