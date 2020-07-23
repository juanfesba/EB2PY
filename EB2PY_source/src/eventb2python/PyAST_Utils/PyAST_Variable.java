package eventb2python.PyAST_Utils;

import eventb2python.PyAST_Types.PyAST_Type;

public class PyAST_Variable {
	
	//Private Attributes
	
	//Public Attributes
	public String VariableName;
	public PyAST_Type VariableType;
	
	//OutputUtils
	public String VariableTypeTranslation;
	public boolean VariableTypeTranslated;
		
	//Constructor
	public PyAST_Variable(String variableName){
		VariableName = variableName;
		VariableType = new PyAST_Type();
		
		VariableTypeTranslation = "";
		VariableTypeTranslated = false;
	}
		
	//Methods

}