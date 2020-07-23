package eventb2python.PyAST_Predicates;

import eventb2python.PyAST_Types.PyAST_Type;

public class PyAST_QuantifiedPredicate extends PyAST_Predicate {
	
	//Private Attributes
	
	//Public Attributes
	public String QuantifiedPredicate;
	public PyAST_Predicate InternalPredicate;
	public PyAST_Type[] BoundIdentDeclsAndTypes;
	public int BoundIdentDeclAmount;
	public String OperatorSymbol;
	
	//Constructor
	public PyAST_QuantifiedPredicate(String quantifiedPredicate,int boundIdentDeclAmount){
		CorePredicate = "QuantifiedPredicate";
		InternalPredicate = new PyAST_Predicate();
		QuantifiedPredicate = quantifiedPredicate;
		BoundIdentDeclsAndTypes = new PyAST_Type[boundIdentDeclAmount];
		BoundIdentDeclAmount = boundIdentDeclAmount;
		
		switch (quantifiedPredicate) {
		case "FORALL":
			OperatorSymbol = "QuantifiedForAll";
			break;
		case "EXISTS":
			OperatorSymbol = "QuantifiedExists";
			break;
		default:
			OperatorSymbol = "ErrorQuantifiedPredicate";
		}
	}
}
