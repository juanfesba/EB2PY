package eventb2python.PyAST_Utils;

import java.util.HashMap;
import java.util.LinkedList;

import org.eventb.core.ast.Assignment;
import org.eventb.core.ast.AssociativeExpression;
import org.eventb.core.ast.AssociativePredicate;
import org.eventb.core.ast.AtomicExpression;
import org.eventb.core.ast.BecomesEqualTo;
import org.eventb.core.ast.BecomesMemberOf;
import org.eventb.core.ast.BecomesSuchThat;
import org.eventb.core.ast.BinaryExpression;
import org.eventb.core.ast.BinaryPredicate;
import org.eventb.core.ast.BoolExpression;
import org.eventb.core.ast.BoundIdentDecl;
import org.eventb.core.ast.BoundIdentifier;
import org.eventb.core.ast.Expression;
import org.eventb.core.ast.ExtendedExpression;
import org.eventb.core.ast.ExtendedPredicate;
import org.eventb.core.ast.Formula;
import org.eventb.core.ast.FormulaFactory;
import org.eventb.core.ast.FreeIdentifier;
import org.eventb.core.ast.IParseResult;
import org.eventb.core.ast.ISimpleVisitor2;
import org.eventb.core.ast.IntegerLiteral;
import org.eventb.core.ast.LiteralPredicate;
import org.eventb.core.ast.MultiplePredicate;
import org.eventb.core.ast.Predicate;
import org.eventb.core.ast.PredicateVariable;
import org.eventb.core.ast.QuantifiedExpression;
import org.eventb.core.ast.QuantifiedPredicate;
import org.eventb.core.ast.RelationalPredicate;
import org.eventb.core.ast.SetExtension;
import org.eventb.core.ast.SimplePredicate;
import org.eventb.core.ast.UnaryExpression;
import org.eventb.core.ast.UnaryPredicate;

import eventb2python.PyAST_Expressions.PyAST_AssociativeExpression;
import eventb2python.PyAST_Expressions.PyAST_AtomicExpression;
import eventb2python.PyAST_Expressions.PyAST_BinaryExpression;
import eventb2python.PyAST_Expressions.PyAST_BoundIdentifier;
import eventb2python.PyAST_Expressions.PyAST_Expression;
import eventb2python.PyAST_Expressions.PyAST_FreeIdentifier;
import eventb2python.PyAST_Expressions.PyAST_IntegerLiteral;
import eventb2python.PyAST_Expressions.PyAST_QuantifiedExpression;
import eventb2python.PyAST_Expressions.PyAST_SetExtension;
import eventb2python.PyAST_Expressions.PyAST_UnaryExpression;
import eventb2python.PyAST_Predicates.PyAST_Assignment;
import eventb2python.PyAST_Predicates.PyAST_AssociativePredicate;
import eventb2python.PyAST_Predicates.PyAST_BinaryPredicate;
import eventb2python.PyAST_Predicates.PyAST_LiteralPredicate;
import eventb2python.PyAST_Predicates.PyAST_MultiplePredicate;
import eventb2python.PyAST_Predicates.PyAST_Predicate;
import eventb2python.PyAST_Predicates.PyAST_QuantifiedPredicate;
import eventb2python.PyAST_Predicates.PyAST_RelationalPredicate;
import eventb2python.PyAST_Predicates.PyAST_SimplePredicate;
import eventb2python.PyAST_Predicates.PyAST_UnaryPredicate;
import eventb2python.PyAST_Types.PyAST_BinaryExpressionType;
import eventb2python.PyAST_Types.PyAST_Bool;
import eventb2python.PyAST_Types.PyAST_FreeIdentifierType;
import eventb2python.PyAST_Types.PyAST_Integer;
import eventb2python.PyAST_Types.PyAST_Type;
import eventb2python.PyAST_Types.PyAST_UnaryExpressionType;

public class PyAST_Visitor implements ISimpleVisitor2 {
	
	//Private Attributes
	
	//Public Attributes
		//General
	
			//General Support
			public String PreludeName;
	
			//ConstantType
			public boolean Task_GettingConstantType;
			public PyAST_Type CurrentConstantType;
		
			//Predicate
			public boolean Task_GettingPredicate;
			public PyAST_Predicate CurrentPredicate;
			public PyAST_Expression CurrentSupportExpression;
			
			//Context Extension
			public boolean HasContextExtension;
			public PyAST_Context ContextExtension;
			
			public boolean HasMachineRefinement;
			public PyAST_Machine MachineRefinement;
			
		//Supporting Variables
			
			//For CarrierSets
			public HashMap<String,Integer> CarrierSetsMetaData;
	
	
	public PyAST_Visitor() {
		Task_GettingConstantType = false;
		Task_GettingPredicate = false;
		PreludeName = "P";
		
		HasContextExtension = false;
		ContextExtension = new PyAST_Context();
		
		HasMachineRefinement = false;
		MachineRefinement = new PyAST_Machine();
		
		CarrierSetsMetaData = new HashMap<String, Integer>();
	}
	
	public PyAST_Expression getExpression(String expression) {
		
		//Only used for variants.
		
		Task_GettingPredicate = true;
		CurrentPredicate = new PyAST_Predicate();
		CurrentSupportExpression = new PyAST_Expression();
		
		FormulaFactory formulaFactory = FormulaFactory.getDefault();
        IParseResult parseResult = formulaFactory.parseExpression(expression, null);
        Expression parsedExpression = parseResult.getParsedExpression();
        
        System.out.print("assignment parsed pred: ");System.out.println(parsedExpression.toString());
		System.out.print("assignment syntax tree exp: ");System.out.println(parsedExpression.getSyntaxTree());
        
		parsedExpression.accept(this);
		Task_GettingPredicate = false;
		return CurrentSupportExpression;
	}
	
	public PyAST_Predicate getAssignment(String assignment) {
		
		Task_GettingPredicate = true;
		CurrentPredicate = new PyAST_Predicate();
		CurrentSupportExpression = new PyAST_Expression();
		
		FormulaFactory formulaFactory = FormulaFactory.getDefault();
        IParseResult parseResult = formulaFactory.parseAssignment(assignment, null);
        Assignment parsedAssignment = parseResult.getParsedAssignment();
        
        System.out.print("assignment parsed pred: ");System.out.println(parsedAssignment.toString());
		System.out.print("assignment syntax tree exp: ");System.out.println(parsedAssignment.getSyntaxTree());
        
		parsedAssignment.accept(this);
		Task_GettingPredicate = false;
		return CurrentPredicate;
	}
	
	public PyAST_Predicate getPredicate(String predicate) {
		
		Task_GettingPredicate = true;
		CurrentPredicate = new PyAST_Predicate();
		CurrentSupportExpression = new PyAST_Expression();
		
		FormulaFactory formulaFactory = FormulaFactory.getDefault();
        IParseResult parseResult = formulaFactory.parsePredicate(predicate, null);
        Predicate parsedPredicate = parseResult.getParsedPredicate();
        
        System.out.print("predicate parsed pred: ");System.out.println(parsedPredicate.toString());
		System.out.print("predicate syntax tree exp: ");System.out.println(parsedPredicate.getSyntaxTree());
        
		parsedPredicate.accept(this);
		Task_GettingPredicate = false;
		return CurrentPredicate;
	}
	
	public PyAST_Type getConstantType(String constantType) {
		
		Task_GettingConstantType = true;
		CurrentConstantType = new PyAST_Type();
		
		final FormulaFactory formulaFactory = FormulaFactory.getDefault();
		final IParseResult parseResult = formulaFactory.parseExpression(constantType, null);
		final Expression expression = parseResult.getParsedExpression();
		
		/* TODO FOR DEBUGGING: Shows Full Type, and then that same type in a Parse Tree with more information
		System.out.print("const parsed exp: ");System.out.println(expression.toString());
		System.out.print("const syntax tree exp: ");System.out.println(expression.getSyntaxTree());
		*/
		System.out.print("const parsed exp: ");System.out.println(expression.toString());
		System.out.print("const syntax tree exp: ");System.out.println(expression.getSyntaxTree());
		
		expression.accept(this);
		Task_GettingConstantType = false;
		return CurrentConstantType;
	}
	
	public void SetContextExtension(PyAST_Context contextExtension) {
		HasContextExtension = true;
		ContextExtension = contextExtension;
	}
	
	public void SetMachineRefinement(PyAST_Machine machineRefinement) {
		HasMachineRefinement = true;
		MachineRefinement = machineRefinement;
	}

	@Override
	public void visitBecomesEqualTo(BecomesEqualTo assignment) {
		System.out.println("visitBecomesEqualTo");
		// TODO Auto-generated method stub
		
		if(Task_GettingConstantType)CurrentConstantType=new PyAST_Type();
		if(Task_GettingPredicate) {
			CurrentPredicate = new PyAST_Predicate();
			CurrentSupportExpression=new PyAST_Expression();
		}
		
		PyAST_Assignment tmpAssignment = new PyAST_Assignment("BecomesEqualTo");
		
		//Assignments will only accept simple assignments (One FreeIdentifier, One Expression).
		
		assignment.getAssignedIdentifiers()[0].accept(this);
		PyAST_Expression assignmentFreeIdentifier = CurrentSupportExpression;
		
		assignment.getExpressions()[0].accept(this);
		PyAST_Expression assignmentExpression = CurrentSupportExpression;
		
		tmpAssignment.LeftSide = (PyAST_FreeIdentifier)assignmentFreeIdentifier;
		tmpAssignment.RightSide = assignmentExpression;
		
		CurrentPredicate = tmpAssignment;
	}

	@Override
	public void visitBecomesMemberOf(BecomesMemberOf assignment) {
		System.out.println("visitBecomesMemberOf");
		// TODO Auto-generated method stub

		if(Task_GettingConstantType)CurrentConstantType=new PyAST_Type();
		if(Task_GettingPredicate) {
			CurrentPredicate = new PyAST_Predicate();
			CurrentSupportExpression=new PyAST_Expression();
		}
		
		PyAST_Assignment tmpAssignment = new PyAST_Assignment("BecomesMemberOf");
		
		//Assignments will only accept simple assignments (One FreeIdentifier, One Expression).
		
		assignment.getAssignedIdentifiers()[0].accept(this);
		PyAST_Expression assignmentFreeIdentifier = CurrentSupportExpression;
		
		assignment.getSet().accept(this);
		PyAST_Expression assignmentExpression = CurrentSupportExpression;
		
		tmpAssignment.LeftSide = (PyAST_FreeIdentifier)assignmentFreeIdentifier;
		tmpAssignment.RightSide = assignmentExpression;
		
		CurrentPredicate = tmpAssignment;
	}

	@Override
	public void visitBecomesSuchThat(BecomesSuchThat assignment) {
		System.out.println("visitBecomesSuchThat");
		// TODO Auto-generated method stub
		
		if(Task_GettingPredicate) {
			CurrentSupportExpression = new PyAST_Expression();
			CurrentPredicate = new PyAST_Predicate();
		}
		
		System.out.println("Debug");
		System.out.println(assignment.getSyntaxTree());
		
		if(Task_GettingPredicate) {
			PyAST_Assignment bstAssignment =new PyAST_Assignment("BecomesSuchThat");
			
			assignment.getAssignedIdentifiers()[0].accept(this);
			bstAssignment.LeftSide = (PyAST_FreeIdentifier)CurrentSupportExpression;
			
			assignment.getCondition().accept(this);
			bstAssignment.PredicateSide = CurrentPredicate;
			CurrentPredicate = bstAssignment;
		}
		
	}

	@Override
	public void visitBoundIdentDecl(BoundIdentDecl boundIdentDecl) {
		System.out.println("visitBoundIdentDecl");
		System.out.println(boundIdentDecl.getName());
		// TODO Auto-generated method stub
	}

	@Override
	public void visitAssociativeExpression(AssociativeExpression expression) {
		System.out.println("visitAssociativeExpression");
		System.out.println(expression.getTag());
		// TODO Auto-generated method stub
		if(Task_GettingConstantType)CurrentConstantType=new PyAST_Type();
		if(Task_GettingPredicate)CurrentSupportExpression=new PyAST_Expression();
		
		int expressionTag = expression.getTag();
		int childrenAmount = expression.getChildCount();
		
		boolean no_default_error = true;
		
		PyAST_AssociativeExpression associativeExpression=new PyAST_AssociativeExpression("Unrecognized Associative Operation",childrenAmount);
		
		//Switch through Tag Cases.
		switch(expressionTag) {
		case Formula.BUNION: //301
			if(Task_GettingPredicate) {
				associativeExpression=new PyAST_AssociativeExpression("Union",childrenAmount);
			}
			break;
		case Formula.BINTER: //302
			if(Task_GettingPredicate) {
				associativeExpression=new PyAST_AssociativeExpression("Intersection",childrenAmount);
			}
			break;
		case Formula.BCOMP: //303
			if(Task_GettingPredicate) {
				associativeExpression=new PyAST_AssociativeExpression("BackwardComposition",childrenAmount);
			}
			break;
		case Formula.FCOMP: //304
			if(Task_GettingPredicate) {
				associativeExpression=new PyAST_AssociativeExpression("ForwardComposition",childrenAmount);
			}
			break;
		case Formula.OVR: //305
			if(Task_GettingPredicate) {
				associativeExpression=new PyAST_AssociativeExpression("Overriding",childrenAmount);
			}
			break;
		case Formula.PLUS: //306
			if(Task_GettingPredicate) {
				associativeExpression=new PyAST_AssociativeExpression("Addition",childrenAmount);
			}
			break;
		case Formula.MUL: //307
			if(Task_GettingPredicate) {
				associativeExpression=new PyAST_AssociativeExpression("Multiplication",childrenAmount);
			}
			break;
		default:
			if(Task_GettingConstantType)
				CurrentConstantType.CoreType += " ErrorVisitAssociativeExpression ";
			if(Task_GettingPredicate)
				CurrentSupportExpression.CoreExpression += " ErrorVisitAssociativeExpression ";
			no_default_error = false;
		}
		
		if(Task_GettingPredicate) {
			
			if(no_default_error) {
				int i = 0;
				for(Expression child : expression.getChildren()) {
					child.accept(this);
					associativeExpression.Children[i] = CurrentSupportExpression;
					i+=1;
				}
			}
			
			CurrentSupportExpression = associativeExpression;
		}
	}

	@Override
	public void visitAtomicExpression(AtomicExpression expression) {
		System.out.println("visitAtomicExpression");
		System.out.println(expression.getTag());
		// TODO Auto-generated method stub
		
		//Resetting Supporting Current Variables
		if(Task_GettingConstantType)CurrentConstantType=new PyAST_Type();
		if(Task_GettingPredicate)CurrentSupportExpression=new PyAST_Expression();
		
		int expressionTag = expression.getTag();
		
		//Switch through Tag Cases.
		switch(expressionTag) {
		case Formula.INTEGER: //401
			if(Task_GettingConstantType) {
				CurrentConstantType=new PyAST_Integer();
			}
			else if(Task_GettingPredicate) {
				CurrentSupportExpression=new PyAST_AtomicExpression("Integer");
			}
			break;
		case Formula.BOOL: //404
			if(Task_GettingConstantType) {
				CurrentConstantType=new PyAST_Bool();
			}
			else if(Task_GettingPredicate) {
				CurrentSupportExpression = new PyAST_AtomicExpression("Bool");
			}
			break;
		case Formula.TRUE: //405
			if(Task_GettingPredicate) {
				CurrentSupportExpression=new PyAST_AtomicExpression("True");
			}
			break;
		case Formula.FALSE: //406
			if(Task_GettingPredicate) {
				CurrentSupportExpression=new PyAST_AtomicExpression("False");
			}
			break;
		case Formula.NATURAL: //402
			if(Task_GettingPredicate) {
				CurrentSupportExpression=new PyAST_AtomicExpression("Natural");
			}
			break;
		case Formula.NATURAL1: //403
			if(Task_GettingPredicate) {
				CurrentSupportExpression=new PyAST_AtomicExpression("Natural1");
			}
			break;
		case Formula.EMPTYSET: //407
			if(Task_GettingPredicate) {
				CurrentSupportExpression=new PyAST_AtomicExpression("EmptySet");
			}
			break;
		case Formula.KID_GEN: //412
			if(Task_GettingPredicate) {
				CurrentSupportExpression=new PyAST_AtomicExpression("ID");
			}
			break;
		default:
			if(Task_GettingConstantType)
				CurrentConstantType.CoreType += " ErrorVisitAtomicExpression ";
			if(Task_GettingPredicate)
				CurrentSupportExpression.CoreExpression += " ErrorVisitAtomicExpression ";
		}
		
		/*
		System.out.println(expression.isATypeExpression()); true
		System.out.println(expression.getChildCount()); 0
		System.out.println(expression.toString()); BOOL
		System.out.println(expression.toStringFullyParenthesized()); BOOL
		System.out.println(expression.getWDPredicate().toStringWithTypes());
		System.out.println(expression.getPredicateVariables().length); 0
		System.out.println(expression.toStringWithTypes()); BOOL
		System.out.println(expression.getWDPredicate().getChildCount()); 0
		System.out.println(expression.getTag()); 404
		*/
	}

	@Override
	public void visitBinaryExpression(BinaryExpression expression) {
		System.out.println("visitBinaryExpression");
		System.out.println(expression.getTag());
		// TODO Auto-generated method stub
		if(Task_GettingConstantType)CurrentConstantType = new PyAST_Type();
		if(Task_GettingPredicate)CurrentSupportExpression = new PyAST_Expression();
		
		int expressionTag = expression.getTag();
		PyAST_BinaryExpression binaryExpression;
		PyAST_BinaryExpressionType binaryExpressionType;
		
		//Switch through Tag Cases.
		switch(expressionTag) {
		case Formula.MAPSTO: //201
			
			if(Task_GettingPredicate) {
				binaryExpression = new PyAST_BinaryExpression("Tuple");
				
				expression.getLeft().accept(this);
				binaryExpression.LeftSide = CurrentSupportExpression;
				
				expression.getRight().accept(this);
				binaryExpression.RightSide = CurrentSupportExpression;
				
				CurrentSupportExpression = binaryExpression;
			}
				
			break;
		case Formula.REL: //202
			
			if(Task_GettingPredicate) {
				binaryExpression = new PyAST_BinaryExpression("Relation");
				
				expression.getLeft().accept(this);
				binaryExpression.LeftSide = CurrentSupportExpression;
				
				expression.getRight().accept(this);
				binaryExpression.RightSide = CurrentSupportExpression;
				
				CurrentSupportExpression = binaryExpression;
			}
				
			break;
		case Formula.TREL: //203
			
			if(Task_GettingPredicate) {
				binaryExpression = new PyAST_BinaryExpression("TotalRelation");
				
				expression.getLeft().accept(this);
				binaryExpression.LeftSide = CurrentSupportExpression;
				
				expression.getRight().accept(this);
				binaryExpression.RightSide = CurrentSupportExpression;
				
				CurrentSupportExpression = binaryExpression;
			}
				
			break;
		case Formula.SREL: //204
		
			if(Task_GettingPredicate) {
				binaryExpression = new PyAST_BinaryExpression("SurjectiveRelation");
				
				expression.getLeft().accept(this);
				binaryExpression.LeftSide = CurrentSupportExpression;
				
				expression.getRight().accept(this);
				binaryExpression.RightSide = CurrentSupportExpression;
				
				CurrentSupportExpression = binaryExpression;
			}
				
			break;
		case Formula.STREL: //205
			
			if(Task_GettingPredicate) {
				binaryExpression = new PyAST_BinaryExpression("TotalSurjectiveRelation");
				
				expression.getLeft().accept(this);
				binaryExpression.LeftSide = CurrentSupportExpression;
				
				expression.getRight().accept(this);
				binaryExpression.RightSide = CurrentSupportExpression;
				
				CurrentSupportExpression = binaryExpression;
			}
				
			break;
		case Formula.PFUN: //206
			
			if(Task_GettingPredicate) {
				binaryExpression = new PyAST_BinaryExpression("PartialFunction");
				
				expression.getLeft().accept(this);
				binaryExpression.LeftSide = CurrentSupportExpression;
				
				expression.getRight().accept(this);
				binaryExpression.RightSide = CurrentSupportExpression;
				
				CurrentSupportExpression = binaryExpression;
			}
				
			break;
		case Formula.TFUN: //207
			
			if(Task_GettingPredicate) {
				binaryExpression = new PyAST_BinaryExpression("TotalFunction");
				
				expression.getLeft().accept(this);
				binaryExpression.LeftSide = CurrentSupportExpression;
				
				expression.getRight().accept(this);
				binaryExpression.RightSide = CurrentSupportExpression;
				
				CurrentSupportExpression = binaryExpression;
			}
				
			break;
		case Formula.PINJ: //208
			
			if(Task_GettingPredicate) {
				binaryExpression = new PyAST_BinaryExpression("PartialInjection");
				
				expression.getLeft().accept(this);
				binaryExpression.LeftSide = CurrentSupportExpression;
				
				expression.getRight().accept(this);
				binaryExpression.RightSide = CurrentSupportExpression;
				
				CurrentSupportExpression = binaryExpression;
			}
				
			break;
		case Formula.TINJ: //209
			
			if(Task_GettingPredicate) {
				binaryExpression = new PyAST_BinaryExpression("TotalInjection");
				
				expression.getLeft().accept(this);
				binaryExpression.LeftSide = CurrentSupportExpression;
				
				expression.getRight().accept(this);
				binaryExpression.RightSide = CurrentSupportExpression;
				
				CurrentSupportExpression = binaryExpression;
			}
				
			break;
		case Formula.PSUR: //210
			
			if(Task_GettingPredicate) {
				binaryExpression = new PyAST_BinaryExpression("PartialSurjection");
				
				expression.getLeft().accept(this);
				binaryExpression.LeftSide = CurrentSupportExpression;
				
				expression.getRight().accept(this);
				binaryExpression.RightSide = CurrentSupportExpression;
				
				CurrentSupportExpression = binaryExpression;
			}
				
			break;
		case Formula.TSUR: //211
			
			if(Task_GettingPredicate) {
				binaryExpression = new PyAST_BinaryExpression("TotalSurjection");
				
				expression.getLeft().accept(this);
				binaryExpression.LeftSide = CurrentSupportExpression;
				
				expression.getRight().accept(this);
				binaryExpression.RightSide = CurrentSupportExpression;
				
				CurrentSupportExpression = binaryExpression;
			}
				
			break;
		case Formula.TBIJ: //212
			
			if(Task_GettingPredicate) {
				binaryExpression = new PyAST_BinaryExpression("Bijection");
				
				expression.getLeft().accept(this);
				binaryExpression.LeftSide = CurrentSupportExpression;
				
				expression.getRight().accept(this);
				binaryExpression.RightSide = CurrentSupportExpression;
				
				CurrentSupportExpression = binaryExpression;
			}
				
			break;
		case Formula.SETMINUS: //213
			
			if(Task_GettingPredicate) {
				binaryExpression = new PyAST_BinaryExpression("Difference");
				
				expression.getLeft().accept(this);
				binaryExpression.LeftSide = CurrentSupportExpression;
				
				expression.getRight().accept(this);
				binaryExpression.RightSide = CurrentSupportExpression;
				
				CurrentSupportExpression = binaryExpression;
			}
				
			break;
		case Formula.CPROD: //214
			
			if(Task_GettingPredicate) {
				binaryExpression = new PyAST_BinaryExpression("CartesianProduct");
				
				expression.getLeft().accept(this);
				binaryExpression.LeftSide = CurrentSupportExpression;
				
				expression.getRight().accept(this);
				binaryExpression.RightSide = CurrentSupportExpression;
				
				CurrentSupportExpression = binaryExpression;
			}
			
			if(Task_GettingConstantType) {
				binaryExpressionType = new PyAST_BinaryExpressionType("CartesianProduct");
				
				expression.getLeft().accept(this);
				binaryExpressionType.LeftSide = CurrentConstantType;
				
				expression.getRight().accept(this);
				binaryExpressionType.RightSide = CurrentConstantType;
				
				CurrentConstantType = binaryExpressionType;
			}
			
			break;
		case Formula.DPROD: //215
			
			if(Task_GettingPredicate) {
				binaryExpression = new PyAST_BinaryExpression("DirectProduct");
				
				expression.getLeft().accept(this);
				binaryExpression.LeftSide = CurrentSupportExpression;
				
				expression.getRight().accept(this);
				binaryExpression.RightSide = CurrentSupportExpression;
				
				CurrentSupportExpression = binaryExpression;
			}
				
			break;
		case Formula.DOMRES: //217
			
			if(Task_GettingPredicate) {
				binaryExpression = new PyAST_BinaryExpression("DomainRestriction");
				
				expression.getLeft().accept(this);
				binaryExpression.LeftSide = CurrentSupportExpression;
				
				expression.getRight().accept(this);
				binaryExpression.RightSide = CurrentSupportExpression;
				
				CurrentSupportExpression = binaryExpression;
			}
				
			break;
		case Formula.DOMSUB: //218
			
			if(Task_GettingPredicate) {
				binaryExpression = new PyAST_BinaryExpression("DomainSubstraction");
				
				expression.getLeft().accept(this);
				binaryExpression.LeftSide = CurrentSupportExpression;
				
				expression.getRight().accept(this);
				binaryExpression.RightSide = CurrentSupportExpression;
				
				CurrentSupportExpression = binaryExpression;
			}
				
			break;
		case Formula.RANRES: //219
			
			if(Task_GettingPredicate) {
				binaryExpression = new PyAST_BinaryExpression("RangeRestriction");
				
				expression.getLeft().accept(this);
				binaryExpression.LeftSide = CurrentSupportExpression;
				
				expression.getRight().accept(this);
				binaryExpression.RightSide = CurrentSupportExpression;
				
				CurrentSupportExpression = binaryExpression;
			}
				
			break;
		case Formula.RANSUB: //220
			
			if(Task_GettingPredicate) {
				binaryExpression = new PyAST_BinaryExpression("RangeSubstraction");
				
				expression.getLeft().accept(this);
				binaryExpression.LeftSide = CurrentSupportExpression;
				
				expression.getRight().accept(this);
				binaryExpression.RightSide = CurrentSupportExpression;
				
				CurrentSupportExpression = binaryExpression;
			}
				
			break;
		case Formula.UPTO: //221
			
			if(Task_GettingPredicate) {
				binaryExpression = new PyAST_BinaryExpression("UpTo");
				
				expression.getLeft().accept(this);
				binaryExpression.LeftSide = CurrentSupportExpression;
				
				expression.getRight().accept(this);
				binaryExpression.RightSide = CurrentSupportExpression;
				
				CurrentSupportExpression = binaryExpression;
			}
				
			break;
		case Formula.MINUS: //222
			
			if(Task_GettingPredicate) {
				binaryExpression = new PyAST_BinaryExpression("Minus");
				
				expression.getLeft().accept(this);
				binaryExpression.LeftSide = CurrentSupportExpression;
				
				expression.getRight().accept(this);
				binaryExpression.RightSide = CurrentSupportExpression;
				
				CurrentSupportExpression = binaryExpression;
			}
				
			break;
		case Formula.DIV: //223
			
			if(Task_GettingPredicate) {
				binaryExpression = new PyAST_BinaryExpression("Division");
				
				expression.getLeft().accept(this);
				binaryExpression.LeftSide = CurrentSupportExpression;
				
				expression.getRight().accept(this);
				binaryExpression.RightSide = CurrentSupportExpression;
				
				CurrentSupportExpression = binaryExpression;
			}
				
			break;
		case Formula.MOD: //224
			
			if(Task_GettingPredicate) {
				binaryExpression = new PyAST_BinaryExpression("Mod");
				
				expression.getLeft().accept(this);
				binaryExpression.LeftSide = CurrentSupportExpression;
				
				expression.getRight().accept(this);
				binaryExpression.RightSide = CurrentSupportExpression;
				
				CurrentSupportExpression = binaryExpression;
			}
				
			break;
		case Formula.EXPN: //225
			
			if(Task_GettingPredicate) {
				binaryExpression = new PyAST_BinaryExpression("Exponentiation");
				
				expression.getLeft().accept(this);
				binaryExpression.LeftSide = CurrentSupportExpression;
				
				expression.getRight().accept(this);
				binaryExpression.RightSide = CurrentSupportExpression;
				
				CurrentSupportExpression = binaryExpression;
			}
				
			break;
		case Formula.FUNIMAGE: //226
			
			if(Task_GettingPredicate) {
				binaryExpression = new PyAST_BinaryExpression("Apply");
				
				expression.getLeft().accept(this);
				binaryExpression.LeftSide = CurrentSupportExpression;
				
				expression.getRight().accept(this);
				binaryExpression.RightSide = CurrentSupportExpression;
				
				CurrentSupportExpression = binaryExpression;
			}
				
			break;
		case Formula.RELIMAGE: //227
			
			if(Task_GettingPredicate) {
				binaryExpression = new PyAST_BinaryExpression("RelationalImage");
				
				expression.getLeft().accept(this);
				binaryExpression.LeftSide = CurrentSupportExpression;
				
				expression.getRight().accept(this);
				binaryExpression.RightSide = CurrentSupportExpression;
				
				CurrentSupportExpression = binaryExpression;
			}
				
			break;
		default:
			if(Task_GettingPredicate) {
				CurrentSupportExpression.CoreExpression += " ErrorVisitUnaryExpression ";
				CurrentPredicate.CorePredicate += " ErrorVisitUnaryExpression ";
			}
			if(Task_GettingConstantType)
				CurrentConstantType.CoreType += " ErrorVisitBinaryExpression ";
		}
	}

	@Override
	public void visitBoolExpression(BoolExpression expression) {
		System.out.println("visitBoolExpression");
		// TODO Auto-generated method stub
		
	}

	@Override
	public void visitIntegerLiteral(IntegerLiteral expression) {
		System.out.println("visitIntegerLiteral");
		// TODO Auto-generated method stub
		
		//Resetting Supporting Current Variables
		if(Task_GettingConstantType)CurrentConstantType = new PyAST_Type();
		if(Task_GettingPredicate)CurrentSupportExpression = new PyAST_Expression();
		
		if(Task_GettingPredicate) {
			CurrentSupportExpression = new PyAST_IntegerLiteral(expression.getValue().toString());
		}
		
	}

	@Override
	public void visitQuantifiedExpression(QuantifiedExpression expression) {
		System.out.println("visitQuantifiedExpression");
		// TODO Auto-generated method stub
		if(Task_GettingConstantType)CurrentConstantType=new PyAST_Type();
		if(Task_GettingPredicate) {
			CurrentSupportExpression = new PyAST_Expression();
			CurrentPredicate = new PyAST_Predicate();
		}
		
		int predicateTag = expression.getTag();
		int boundIdentDeclAmount = expression.getBoundIdentDecls().length;
		
		//Switch through Tag Cases.
		switch(predicateTag) {
		case Formula.CSET: //803
			if(Task_GettingPredicate) {
				PyAST_QuantifiedExpression quantifiedExpression=new PyAST_QuantifiedExpression(boundIdentDeclAmount);
	
				expression.getPredicate().accept(this);
				quantifiedExpression.InternalPredicate = CurrentPredicate;
				CurrentSupportExpression = quantifiedExpression;
			}
			break;
		default:
			if(Task_GettingConstantType)
				CurrentConstantType.CoreType += " ErrorVisitQuantifiedExpression ";
			if(Task_GettingPredicate) {
				CurrentSupportExpression.CoreExpression += " ErrorVisitQuantifiedExpression ";
				CurrentPredicate.CorePredicate += " ErrorVisitQuantifiedExpression ";
			}
		}
		
	}

	@Override
	public void visitSetExtension(SetExtension expression) {
		System.out.println("visitSetExtension");
		// TODO Auto-generated method stub
		if(Task_GettingConstantType)CurrentConstantType=new PyAST_Type();
		if(Task_GettingPredicate)CurrentSupportExpression=new PyAST_Expression();
		
		int membersAmount = expression.getMembers().length;
		
		if(Task_GettingPredicate) {
			PyAST_SetExtension setExtension=new PyAST_SetExtension(membersAmount);
			
			int i = 0;
			for(Expression element : expression.getMembers()) {
				element.accept(this);
				setExtension.Members[i] = CurrentSupportExpression;
				i+=1;
			}
			
			CurrentSupportExpression = setExtension;
		}
	}

	@Override
	public void visitUnaryExpression(UnaryExpression expression) {
		System.out.println("visitUnaryExpression");
		System.out.println(expression.getTag());
		// TODO Auto-generated method stub
		
		if(Task_GettingConstantType)CurrentConstantType=new PyAST_Type();
		if(Task_GettingPredicate) {
			CurrentSupportExpression = new PyAST_Expression();
			CurrentPredicate = new PyAST_Predicate();
		}
		
		int expressionTag = expression.getTag();
		
		//Switch through Tag Cases.
		switch(expressionTag) {
		case Formula.KCARD: //751
			if(Task_GettingPredicate) {
				PyAST_UnaryExpression unaryExpression=new PyAST_UnaryExpression("Cardinality");
				
				expression.getChild().accept(this);
				unaryExpression.InternalExpression = CurrentSupportExpression;
				
				CurrentSupportExpression = unaryExpression;
			}
			break;
		case Formula.POW: //752
			if(Task_GettingPredicate) {
				PyAST_UnaryExpression unaryExpression=new PyAST_UnaryExpression("PowerSet");
				
				expression.getChild().accept(this);
				unaryExpression.InternalExpression = CurrentSupportExpression;
				
				CurrentSupportExpression = unaryExpression;
			}
			if(Task_GettingConstantType) {
				PyAST_UnaryExpressionType unaryExpressionType=new PyAST_UnaryExpressionType("PowerSet");
				
				expression.getChild().accept(this);
				unaryExpressionType.InternalType = CurrentConstantType;
				
				//If the Internal Type of a Set is a Tuple, we can convert it to a PyRel.
				if(unaryExpressionType.InternalType.CoreType.equals("BinaryExpressionType")) {
					PyAST_BinaryExpressionType binaryInternalType = (PyAST_BinaryExpressionType) unaryExpressionType.InternalType;
					if(binaryInternalType.BinaryExpressionType.equals("CartesianProduct")) {
						PyAST_BinaryExpressionType relationConversion = new PyAST_BinaryExpressionType("Relation");
						
						relationConversion.LeftSide = binaryInternalType.LeftSide;
						relationConversion.RightSide = binaryInternalType.RightSide;
						
						CurrentConstantType = relationConversion;
					}
					else {
						CurrentConstantType = unaryExpressionType;
					}
				}
				else {
					CurrentConstantType = unaryExpressionType;
				}
			}
			break;
		case Formula.POW1: //753
			if(Task_GettingPredicate) {
				PyAST_UnaryExpression unaryExpression=new PyAST_UnaryExpression("PowerSet1");
				
				expression.getChild().accept(this);
				unaryExpression.InternalExpression = CurrentSupportExpression;
				
				CurrentSupportExpression = unaryExpression;
			}
			break;
		case Formula.KDOM: //756
			if(Task_GettingPredicate) {
				PyAST_UnaryExpression unaryExpression=new PyAST_UnaryExpression("Domain");
				
				expression.getChild().accept(this);
				unaryExpression.InternalExpression = CurrentSupportExpression;
				
				CurrentSupportExpression = unaryExpression;
			}
			break;
		case Formula.KRAN: //757
			if(Task_GettingPredicate) {
				PyAST_UnaryExpression unaryExpression=new PyAST_UnaryExpression("Range");
				
				expression.getChild().accept(this);
				unaryExpression.InternalExpression = CurrentSupportExpression;
				
				CurrentSupportExpression = unaryExpression;
			}
			break;
		case Formula.KMIN: //761
			if(Task_GettingPredicate) {
				PyAST_UnaryExpression unaryExpression=new PyAST_UnaryExpression("Minimum");
				
				expression.getChild().accept(this);
				unaryExpression.InternalExpression = CurrentSupportExpression;
				
				CurrentSupportExpression = unaryExpression;
			}
			break;
		case Formula.KMAX: //762
			if(Task_GettingPredicate) {
				PyAST_UnaryExpression unaryExpression=new PyAST_UnaryExpression("Maximum");
				
				expression.getChild().accept(this);
				unaryExpression.InternalExpression = CurrentSupportExpression;
				
				CurrentSupportExpression = unaryExpression;
			}
			break;
		case Formula.CONVERSE: //763
			if(Task_GettingPredicate) {
				PyAST_UnaryExpression unaryExpression=new PyAST_UnaryExpression("Inverse");
				
				expression.getChild().accept(this);
				unaryExpression.InternalExpression = CurrentSupportExpression;
				
				CurrentSupportExpression = unaryExpression;
			}
			break;
		case Formula.UNMINUS: //764
			if(Task_GettingPredicate) {
				PyAST_UnaryExpression unaryExpression=new PyAST_UnaryExpression("UnaryMinus");
				
				expression.getChild().accept(this);
				unaryExpression.InternalExpression = CurrentSupportExpression;
				
				CurrentSupportExpression = unaryExpression;
			}
			break;
		default:
			if(Task_GettingConstantType)
				CurrentConstantType.CoreType += " ErrorVisitUnaryExpression ";
			if(Task_GettingPredicate) {
				CurrentSupportExpression.CoreExpression += " ErrorVisitUnaryExpression ";
				CurrentPredicate.CorePredicate += " ErrorVisitUnaryExpression ";
			}
		}
	}

	@Override
	public void visitBoundIdentifier(BoundIdentifier identifierExpression) {
		System.out.println("visitBoundIdentifier");
		// TODO Auto-generated method stub
		
		//Resetting Supporting Current Variables
		if(Task_GettingConstantType)CurrentConstantType = new PyAST_Type();
		if(Task_GettingPredicate)CurrentSupportExpression = new PyAST_Expression();
		
		if(Task_GettingPredicate) {
			CurrentSupportExpression = new PyAST_BoundIdentifier(identifierExpression.getBoundIndex());
		}
	}
	
	public LinkedList<LinkedList<String>> SearchForContextDependencies(String identifierName, PyAST_Context contextExtension){
		
		LinkedList<LinkedList<String>> possibleDependencies = new LinkedList<LinkedList<String>>();
		
		LinkedList<String> tmp = new LinkedList<String>();
		tmp.add(contextExtension.Name);
		tmp.add("ContextDependency");
		possibleDependencies.add(tmp);
		
		if(contextExtension.Constants.containsKey(identifierName) || contextExtension.CarrierSets.containsKey(identifierName)) {
			//System.out.println("Included");
			return possibleDependencies;
		}
		if(contextExtension.HasContextExtension) {
			LinkedList<LinkedList<String>> tmpPossibleDependencies = SearchForContextDependencies(identifierName, contextExtension.ContextExtension);
			if(tmpPossibleDependencies.size()>0) {
				possibleDependencies.addAll(tmpPossibleDependencies);
				return possibleDependencies;
			}
		}
		
		return new LinkedList<LinkedList<String>>();
	}
	
	public LinkedList<LinkedList<String>> SearchForMachineDependencies(String identifierName, PyAST_Machine machineRefinement){

		LinkedList<LinkedList<String>> possibleDependencies = new LinkedList<LinkedList<String>>();
		
		LinkedList<String> tmp = new LinkedList<String>();
		tmp.add(machineRefinement.Name);
		tmp.add("MachineDependency");
		possibleDependencies.add(tmp);
		
		if(machineRefinement.Variables.containsKey(identifierName)) {
			return possibleDependencies;
		}
		if(machineRefinement.HasMachineRefinement) {
			return SearchForMachineDependencies(identifierName, machineRefinement.MachineRefinement);
		}
		
		return new LinkedList<LinkedList<String>>();
	}

	@Override
	public void visitFreeIdentifier(FreeIdentifier identifierExpression) {
		System.out.println("visitFreeIdentifier");
		// TODO Auto-generated method stub
		
		//Resetting Supporting Current Variables
		if(Task_GettingConstantType)CurrentConstantType = new PyAST_Type();
		if(Task_GettingPredicate)CurrentSupportExpression = new PyAST_Expression();
		
		String identifierName = identifierExpression.getName();
		
		if(Task_GettingConstantType) {
			CurrentConstantType = new PyAST_FreeIdentifierType(identifierName + "_CS");
		}
		else if(Task_GettingPredicate) {
			PyAST_FreeIdentifier freeIdentifier = new PyAST_FreeIdentifier(identifierName);
			
			LinkedList<LinkedList<String>> freeIdentifierDependencies = new LinkedList<LinkedList<String>>();
			if(HasContextExtension) {
				freeIdentifierDependencies = SearchForContextDependencies(identifierName,ContextExtension);
			}
			if(HasMachineRefinement && freeIdentifierDependencies.size() == 0) {
				freeIdentifierDependencies = SearchForMachineDependencies(identifierName, MachineRefinement);
			}
			
			freeIdentifier.IndentifierDependencies = freeIdentifierDependencies;
			//System.out.println("DebugDebug");
			//System.out.println(freeIdentifier.IdentifierName);
			//System.out.println(freeIdentifier.IndentifierDependencies);
			
			CurrentSupportExpression = freeIdentifier;
		}
	}

	@Override
	public void visitAssociativePredicate(AssociativePredicate predicate) {
		System.out.println("visitAssociativePredicate");
		System.out.println(predicate.getTag());
		// TODO Auto-generated method stub
		if(Task_GettingConstantType)CurrentConstantType = new PyAST_Type();
		if(Task_GettingPredicate) {
			CurrentSupportExpression = new PyAST_Expression();
			CurrentPredicate = new PyAST_Predicate();
		}
		
		int predicateTag = predicate.getTag();
		int childrenAmount = predicate.getChildCount();
		
		//Switch through Tag Cases.
		switch(predicateTag) {
		case Formula.LAND: //351
			if(Task_GettingPredicate) {
				PyAST_AssociativePredicate associativePredicate=new PyAST_AssociativePredicate("LogicalAND",childrenAmount);

				int i = 0;
				for(Predicate child : predicate.getChildren()) {
					child.accept(this);
					associativePredicate.Children[i] = CurrentPredicate;
					i+=1;
				}
				
				CurrentPredicate = associativePredicate;
			}
			break;
		case Formula.LOR: //352
			if(Task_GettingPredicate) {
				PyAST_AssociativePredicate associativePredicate=new PyAST_AssociativePredicate("LogicalOR",childrenAmount);

				int i = 0;
				for(Predicate child : predicate.getChildren()) {
					child.accept(this);
					associativePredicate.Children[i] = CurrentPredicate;
					i+=1;
				}
				
				CurrentPredicate = associativePredicate;
			}
			break;
		default:
			if(Task_GettingConstantType)
				CurrentConstantType.CoreType += " ErrorVisitAssociativePredicate ";
			if(Task_GettingPredicate) {
				CurrentSupportExpression.CoreExpression += " ErrorVisitAssociativePredicate ";
				CurrentPredicate.CorePredicate += " ErrorVisitAssociativePredicate ";
			}
		}
	}

	@Override
	public void visitBinaryPredicate(BinaryPredicate predicate) {
		System.out.println("visitBinaryPredicate");
		// TODO Auto-generated method stub
		
		if(Task_GettingConstantType)CurrentConstantType = new PyAST_Type();
		if(Task_GettingPredicate) {
			CurrentSupportExpression = new PyAST_Expression();
			CurrentPredicate = new PyAST_Predicate();
		}
		
		System.out.println(predicate.getTag());
		int predicateTag = predicate.getTag();
		
		switch(predicateTag) {
		case Formula.LIMP: //251
			if(Task_GettingPredicate) {
				
				PyAST_BinaryPredicate binaryPredicate = new PyAST_BinaryPredicate("LogicImplication");
				
				predicate.getLeft().accept(this);
				binaryPredicate.LeftSide = CurrentPredicate;
				predicate.getRight().accept(this);
				binaryPredicate.RightSide = CurrentPredicate;
				
				CurrentPredicate = binaryPredicate;
			}
			break;
		case Formula.LEQV: //252
			if(Task_GettingPredicate) {
				
				PyAST_BinaryPredicate binaryPredicate = new PyAST_BinaryPredicate("LogicEquivalence");
				
				predicate.getLeft().accept(this);
				binaryPredicate.LeftSide = CurrentPredicate;
				predicate.getRight().accept(this);
				binaryPredicate.RightSide = CurrentPredicate;
				
				CurrentPredicate = binaryPredicate;
			}
			break;
		default:
			if(Task_GettingConstantType)
				CurrentConstantType.CoreType += " ErrorVisitBinaryPredicate ";
			if(Task_GettingPredicate) {
				CurrentSupportExpression.CoreExpression += " ErrorVisitBinaryPredicate ";
				CurrentPredicate.CorePredicate += " ErrorVisitBinaryPredicate ";
			}
		}
		
	}

	@Override
	public void visitLiteralPredicate(LiteralPredicate predicate) {
		System.out.println("visitLiteralPredicate");
		// TODO Auto-generated method stub
		
		//Resetting Supporting Current Variables
		if(Task_GettingPredicate)CurrentPredicate = new PyAST_Predicate();
		
		int predicateTag = predicate.getTag();
		
		//Switch through Tag Cases.
		switch(predicateTag) {
		case Formula.BTRUE: //610
			CurrentPredicate = new PyAST_LiteralPredicate("True");
			break;
		case Formula.BFALSE: //611
			CurrentPredicate = new PyAST_LiteralPredicate("False");
			break;
		default:
			CurrentPredicate.CorePredicate += " ErrorVisitLiteralPredicate ";
		}
	}

	@Override
	public void visitMultiplePredicate(MultiplePredicate predicate) {
		System.out.println("visitMultiplePredicate");
		// TODO Auto-generated method stub
		if(Task_GettingPredicate) {
			CurrentSupportExpression = new PyAST_Expression();
			CurrentPredicate = new PyAST_Predicate();
		}
		
		int childrenAmount = predicate.getChildCount()-1;
		PyAST_MultiplePredicate multiplePredicate = new PyAST_MultiplePredicate(childrenAmount);
		PyAST_FreeIdentifier possibleCarrierSet;
		
		int i = -1;
		for(Expression child : predicate.getChildren()) {
			child.accept(this);
			
			if(i==-1) {
				multiplePredicate.SetToCheck = CurrentSupportExpression;
				//This is only to estimate the size of the CarrierSets
				if(CurrentSupportExpression.CoreExpression.equals("FreeIdentifier")) {
					possibleCarrierSet = (PyAST_FreeIdentifier)CurrentSupportExpression;
					CarrierSetsMetaData.put(possibleCarrierSet.IdentifierName, childrenAmount);
				}
			}
			else {
				multiplePredicate.Children[i] = CurrentSupportExpression;
			}
			i+=1;
		}
		
		CurrentPredicate = multiplePredicate;
	}

	@Override
	public void visitQuantifiedPredicate(QuantifiedPredicate predicate) {
		System.out.println("visitQuantifiedPredicate");
		System.out.println(predicate.getTag());
		// TODO Auto-generated method stub
		if(Task_GettingConstantType)CurrentConstantType=new PyAST_Type();
		if(Task_GettingPredicate) {
			CurrentSupportExpression = new PyAST_Expression();
			CurrentPredicate = new PyAST_Predicate();
		}
		
		int predicateTag = predicate.getTag();
		int boundIdentDeclAmount = predicate.getBoundIdentDecls().length;
		int boundIdentDeclIndex;
		
		//Switch through Tag Cases.
		switch(predicateTag) {
		case Formula.FORALL: //851
			if(Task_GettingPredicate) {
				PyAST_QuantifiedPredicate quantifiedPredicate=new PyAST_QuantifiedPredicate("FORALL",boundIdentDeclAmount);

				boundIdentDeclIndex = boundIdentDeclAmount-1;
				for(BoundIdentDecl boundIdentDecl : predicate.getBoundIdentDecls()) {
					//boundIdentDecl.accept(this);
					//boundIdentDeclName = boundIdentDecl.getName();
					
					Task_GettingPredicate = false;
					getConstantType(boundIdentDecl.getType().toString());
					Task_GettingPredicate = true;
					
					quantifiedPredicate.BoundIdentDeclsAndTypes[boundIdentDeclIndex] = CurrentConstantType;
					boundIdentDeclIndex -= 1;
				}
				
				predicate.getPredicate().accept(this);
				quantifiedPredicate.InternalPredicate = CurrentPredicate;
				CurrentPredicate = quantifiedPredicate;
			}
			break;
		case Formula.EXISTS: //852
			if(Task_GettingPredicate) {
				PyAST_QuantifiedPredicate quantifiedPredicate=new PyAST_QuantifiedPredicate("EXISTS",boundIdentDeclAmount);

				boundIdentDeclIndex = boundIdentDeclAmount-1;
				for(BoundIdentDecl boundIdentDecl : predicate.getBoundIdentDecls()) {
					boundIdentDecl.accept(this);
					//boundIdentDeclName = boundIdentDecl.getName();
					
					Task_GettingPredicate = false;
					getConstantType(boundIdentDecl.getType().toString());
					Task_GettingPredicate = true;
					
					quantifiedPredicate.BoundIdentDeclsAndTypes[boundIdentDeclIndex] = CurrentConstantType;
					boundIdentDeclIndex -= 1;
				}
				
				predicate.getPredicate().accept(this);
				quantifiedPredicate.InternalPredicate = CurrentPredicate;
				CurrentPredicate = quantifiedPredicate;
				
				//System.out.println("Debug");
				//System.out.println(quantifiedPredicate.BoundIdentDecls.values());
				//System.out.println(quantifiedPredicate.BoundIdentDecls.keySet());
			}
			break;
		default:
			if(Task_GettingConstantType)
				CurrentConstantType.CoreType += " ErrorVisitQuantifiedPredicate ";
			if(Task_GettingPredicate) {
				CurrentSupportExpression.CoreExpression += " ErrorVisitQuantifiedPredicate ";
				CurrentPredicate.CorePredicate += " ErrorVisitQuantifiedPredicate ";
			}
		}
	}

	@Override
	public void visitRelationalPredicate(RelationalPredicate predicate) {
		System.out.println("visitRelationalPredicate");
		System.out.println(predicate.getTag());
		// TODO Auto-generated method stub
		
		//Resetting Supporting Current Variables
		if(Task_GettingPredicate)CurrentPredicate = new PyAST_Predicate();
		
		int predicateTag = predicate.getTag();
		PyAST_RelationalPredicate relationalPredicate = new PyAST_RelationalPredicate("Undetermined");
		
		boolean no_default_error = true;
		
		//Switch through Tag Cases.
		switch(predicateTag) {
		case Formula.EQUAL: //101
			relationalPredicate = new PyAST_RelationalPredicate("Equal");
			break;
		case Formula.NOTEQUAL: //102
			relationalPredicate = new PyAST_RelationalPredicate("NotEqual");
			break;
		case Formula.LT: //103
			relationalPredicate = new PyAST_RelationalPredicate("LessThan");
			break;
		case Formula.LE: //104
			relationalPredicate = new PyAST_RelationalPredicate("LessOrEqual");
			break;
		case Formula.GT: //105
			relationalPredicate = new PyAST_RelationalPredicate("GreaterThan");
			break;
		case Formula.GE: //106
			relationalPredicate = new PyAST_RelationalPredicate("GreaterOrEqual");
			break;
		case Formula.IN: //107
			relationalPredicate = new PyAST_RelationalPredicate("In");
			break;
		case Formula.NOTIN: //108
			relationalPredicate = new PyAST_RelationalPredicate("NotIn");
			break;
		case Formula.SUBSET: //109
			relationalPredicate = new PyAST_RelationalPredicate("Subset");
			break;
		case Formula.NOTSUBSET: //110
			relationalPredicate = new PyAST_RelationalPredicate("NotSubset");
			break;
		case Formula.SUBSETEQ: //111
			relationalPredicate = new PyAST_RelationalPredicate("SubsetEq");
			break;
		case Formula.NOTSUBSETEQ: //112
			relationalPredicate = new PyAST_RelationalPredicate("NotSubsetEq");
			break;
		default:
			no_default_error = false;
			CurrentPredicate.CorePredicate += " ErrorVisitRelationalPredicate ";
		}
		
		if(no_default_error) {
			predicate.getLeft().accept(this);
			relationalPredicate.LeftSide = CurrentSupportExpression;
			
			predicate.getRight().accept(this);
			relationalPredicate.RightSide = CurrentSupportExpression;
		}
		
		CurrentPredicate = relationalPredicate;
		
	}

	@Override
	public void visitSimplePredicate(SimplePredicate predicate) {
		System.out.println("visitSimplePredicate");
		// TODO Auto-generated method stub
		
		//Resetting Supporting Current Variables
		if(Task_GettingPredicate) {
			CurrentPredicate = new PyAST_Predicate();
			CurrentSupportExpression = new PyAST_Expression();
		}
		
		int predicateTag = predicate.getTag();
		PyAST_SimplePredicate simplePredicate;
		
		//Switch through Tag Cases.
		switch(predicateTag) {
		case Formula.KFINITE: //620
			simplePredicate = new PyAST_SimplePredicate("Finite");
			
			predicate.getExpression().accept(this);
			simplePredicate.InternalExpression = CurrentSupportExpression;
			
			CurrentPredicate = simplePredicate;
			break;
		default:
			CurrentPredicate.CorePredicate += " ErrorVisitUnaryPredicate ";
		}
		
	}

	@Override
	public void visitUnaryPredicate(UnaryPredicate predicate) {
		System.out.println("visitUnaryPredicate");
		// TODO Auto-generated method stub
		
		//Resetting Supporting Current Variables
		if(Task_GettingPredicate)CurrentPredicate = new PyAST_Predicate();
		
		int predicateTag = predicate.getTag();
		PyAST_UnaryPredicate unaryPredicate;
		
		//Switch through Tag Cases.
		switch(predicateTag) {
		case Formula.NOT: //701
			unaryPredicate = new PyAST_UnaryPredicate("Not");
			
			predicate.getChild().accept(this);
			unaryPredicate.InternalPredicate = CurrentPredicate;
			
			CurrentPredicate = unaryPredicate;
			break;
		default:
			CurrentPredicate.CorePredicate += " ErrorVisitUnaryPredicate ";
		}
	}

	@Override
	public void visitExtendedExpression(ExtendedExpression expression) {
		System.out.println("visitExtendedExpression");
		// TODO Auto-generated method stub
		
	}

	@Override
	public void visitExtendedPredicate(ExtendedPredicate predicate) {
		System.out.println("visitExtendedPredicate");
		// TODO Auto-generated method stub
		
	}

	@Override
	public void visitPredicateVariable(PredicateVariable predVar) {
		System.out.println("visitPredicateVariable");
		// TODO Auto-generated method stub
		
	}

}
