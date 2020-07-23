package eventb2python.PyAST_Predicates;

public class PyAST_UnaryPredicate extends PyAST_Predicate {
	
	//Private Attributes
	
	//Public Attributes
	public String UnaryType;
	public PyAST_Predicate InternalPredicate;
	
	//Constructor
	public PyAST_UnaryPredicate(String unaryType){
		CorePredicate = "UnaryPredicate";
		UnaryType = unaryType;
		InternalPredicate = new PyAST_Predicate();
	}
}