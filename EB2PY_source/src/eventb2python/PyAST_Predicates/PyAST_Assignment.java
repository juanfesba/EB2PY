package eventb2python.PyAST_Predicates;

import eventb2python.PyAST_Expressions.PyAST_Expression;
import eventb2python.PyAST_Expressions.PyAST_FreeIdentifier;

public class PyAST_Assignment extends PyAST_Predicate {
	
	//Private Attributes
	
	//Public Attributes
		//General Attributes.
		public String AssignmentType;
		public PyAST_FreeIdentifier LeftSide;
		public PyAST_Expression RightSide;
	
		//BecomesSuchThat Special Attributes.
		public PyAST_Predicate PredicateSide;
	
	
	//Constructor
	public PyAST_Assignment(){
		CorePredicate = "Assignment";
		AssignmentType = "UndeterminedAssignmentType";
		LeftSide = new PyAST_FreeIdentifier("UndeterminedLeftSide");
		RightSide = new PyAST_Expression();
		PredicateSide = new PyAST_Predicate();
	}
	
	public PyAST_Assignment(String assignmentType){
		CorePredicate = "Assignment";
		AssignmentType = assignmentType;
		LeftSide = new PyAST_FreeIdentifier("UndeterminedLeftSide");
		RightSide = new PyAST_Expression();
		PredicateSide = new PyAST_Predicate();
	}
}

