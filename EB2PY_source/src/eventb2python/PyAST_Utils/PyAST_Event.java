package eventb2python.PyAST_Utils;

import eventb2python.PyAST_Predicates.PyAST_Predicate;

public class PyAST_Event {
	//Private Attributes
	
	//Public Attributes
	public String EventLabel;
	public PyAST_Variable[] EventParameters;
	public PyAST_Predicate[] EventGuards;
	public PyAST_Action[] EventActions;
	public String EventConvergence;
		
	//Constructor
	public PyAST_Event(String label, int parametersAmount, int guardsAmount, int actionsAmount){
		EventLabel = label;
		EventParameters = new PyAST_Variable[parametersAmount];
		EventGuards = new PyAST_Predicate[guardsAmount];
		EventActions = new PyAST_Action[actionsAmount];
		EventConvergence = "Ordinary";
	}
		
	//Methods

}