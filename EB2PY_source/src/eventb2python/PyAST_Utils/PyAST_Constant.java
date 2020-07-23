package eventb2python.PyAST_Utils;

import eventb2python.PyAST_Types.PyAST_Type;

public class PyAST_Constant {
	
	//Private Attributes
	
	//Public Attributes
	public String ConstantName;
	public PyAST_Type ConstantType;
	
	//OutputUtils
	public String ConstantTypeTranslation;
	public boolean ConstantTypeTranslated;
		
	//Constructor
	public PyAST_Constant(String constantName){
		ConstantName = constantName;
		ConstantType = new PyAST_Type();
		
		ConstantTypeTranslation = "";
		ConstantTypeTranslated = false;
	}
		
	//Methods

}
