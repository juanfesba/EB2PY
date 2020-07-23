package eventb2python.PyAST_Types;

public class PyAST_FreeIdentifierType extends PyAST_Type{
	
	//Private Attributes
	
	//Public Attributes
	public String IdentifierName;
	
	//Constructor
	public PyAST_FreeIdentifierType(String identifierName){
		CoreType = "FreeIdentifierType";
		IdentifierName = identifierName;
	}
		
}
