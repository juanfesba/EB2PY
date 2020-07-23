package eventb2python.PyAST_Expressions;

import java.util.LinkedList;

public class PyAST_FreeIdentifier extends PyAST_Expression {
	
	//Private Attributes
	
	//Public Attributes
	public String IdentifierName;
	public LinkedList<LinkedList<String>> IndentifierDependencies;
	
	//Constructor
	public PyAST_FreeIdentifier(String identifierName){
		CoreExpression = "FreeIdentifier";
		IdentifierName = identifierName;
		IndentifierDependencies = new LinkedList<LinkedList<String>>();
	}
}
