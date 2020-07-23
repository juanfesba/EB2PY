package eventb2python.PyAST_Utils;

import eventb2python.PyAST_Predicates.PyAST_Assignment;

public class PyAST_Action {
	//Private Attributes
	
	//Public Attributes
	public String ActionLabel;
	public PyAST_Assignment AssignmentAction;
		
	//Constructor
	public PyAST_Action(String label){
		ActionLabel = label;
		AssignmentAction = new PyAST_Assignment();
	}
		
	//Methods

}
