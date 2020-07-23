package eventb2python.PyAST_Expressions;

public class PyAST_SetExtension extends PyAST_Expression {
	
	//Private Attributes
	
	//Public Attributes
	public String SetExtension;
	public PyAST_Expression[] Members;
	public int MembersAmount;
	
	//Constructor
	public PyAST_SetExtension(int membersAmount){
		CoreExpression = "SetExtension";
		Members = new PyAST_Expression[membersAmount];
		MembersAmount = membersAmount;
	}
}