package eventb2python.PyAST_Utils;

import java.util.HashMap;

import org.eclipse.core.runtime.CoreException;
import org.eventb.core.IConvergenceElement.Convergence;
import org.eventb.core.ISCAction;
import org.eventb.core.ISCEvent;
import org.eventb.core.ISCGuard;
import org.eventb.core.ISCIdentifierElement;
import org.eventb.core.ISCInvariant;
import org.eventb.core.ISCParameter;
import org.eventb.core.ISCVariable;
import org.eventb.core.ISCVariant;
import org.eventb.core.ast.FormulaFactory;
import org.rodinp.core.RodinDBException;

import eventb2python.PyAST_Predicates.PyAST_Assignment;
import eventb2python.PyAST_Predicates.PyAST_Predicate;
import eventb2python.PyAST_Types.PyAST_Type;

public class PyAST_Machine {
	
	//Private Attributes
	
	//Public Attributes
	public String Name;
	public PyAST_Visitor Visitor;
	
	public PyAST_Variant EventVariant;
	public HashMap<String,PyAST_Variable> Variables;
	public HashMap<String,PyAST_Invariant> Invariants;
	public HashMap<String,PyAST_Event> Events;
	public PyAST_Event INITIALISATIONEvent;
	
	public boolean HasMachineRefinement;
	public PyAST_Machine MachineRefinement;
	
	public boolean HasMachineInternalContext;
	public PyAST_Context MachineInternalContext;
	
	//Constructor
	public PyAST_Machine(String MachineName){
		Name = MachineName;
		
		Visitor = new PyAST_Visitor();
		
		EventVariant = new PyAST_Variant(false);
		Variables = new HashMap<String,PyAST_Variable>();
		Invariants = new HashMap<String,PyAST_Invariant>();
		Events = new HashMap<String,PyAST_Event>();
		
		
		HasMachineRefinement = false;
		HasMachineInternalContext = false;
		
		MachineRefinement = new PyAST_Machine();
		MachineInternalContext = new PyAST_Context();
	}
	
	public PyAST_Machine() {
		HasMachineRefinement = false;
		HasMachineInternalContext = false;
	}
	
	//Methods
	
	//Add an Invariant to the Machine.
	public void AddEvent(ISCEvent event) throws CoreException {
		System.out.println("PyAST_Machine.AddEvent: " + event.getLabel());
		//Check if it already exists?
		
		int parametersAmount = event.getSCParameters().length;
		int guardsAmount = event.getSCGuards().length;
		int actionsAmount = event.getSCActions().length;
		
		String eventLabel = event.getLabel();
		
		PyAST_Event NewEvent = new PyAST_Event(eventLabel,parametersAmount,guardsAmount,actionsAmount);
		
		//Convergence
		Convergence eventConvergence = event.getConvergence();
		if(eventConvergence.equals(Convergence.ANTICIPATED))NewEvent.EventConvergence = "Anticipated";
		else if(eventConvergence.equals(Convergence.CONVERGENT))NewEvent.EventConvergence = "Convergent";
		
		//Parameters (any's)
		int i=0;
		PyAST_Variable tmpParameter;
		final FormulaFactory factory = FormulaFactory.getDefault();;
		for(ISCParameter parameter : event.getSCParameters()) {
			tmpParameter = new PyAST_Variable(parameter.getElementName());
			tmpParameter.VariableType = Visitor.getConstantType(((ISCIdentifierElement) parameter).getType(factory).toString());
			NewEvent.EventParameters[i] = tmpParameter;
			
			i+=1;
		}
		
		i=0;
		PyAST_Predicate tmpGuard;
		for(ISCGuard guard : event.getSCGuards()) {
			tmpGuard = Visitor.getPredicate(guard.getPredicateString());
			NewEvent.EventGuards[i] = tmpGuard;
			
			i+=1;
		}
		
		i=0;
		PyAST_Action tmpAction;
		PyAST_Predicate tmpPredicate;
		for(ISCAction action : event.getSCActions()) {
			tmpAction = new PyAST_Action(action.getLabel());
			tmpPredicate = Visitor.getAssignment(action.getAssignmentString());
			tmpAction.AssignmentAction = (PyAST_Assignment)tmpPredicate;
			NewEvent.EventActions[i] = tmpAction;
			
			i+=1;
		}
		
		if(NewEvent.EventLabel.equals("INITIALISATION"))INITIALISATIONEvent = NewEvent;
		else Events.put(eventLabel,NewEvent);
	}
	
	//Add an Variant to the Machine.
	public void AddVariant(ISCVariant variant) throws RodinDBException {
		System.out.println("PyAST_Machine.AddVariant");
		
		// TODO Delete System.out
		
		PyAST_Variant NewVariant = new PyAST_Variant(true);
		NewVariant.VariantExpression = Visitor.getExpression(variant.getExpressionString());
		
		EventVariant = NewVariant;
	}
	
	//Add an Invariant to the Machine.
	public void AddInvariant(ISCInvariant invariant) throws RodinDBException {
		System.out.println("PyAST_Machine.AddInvariant: " + invariant.getLabel());
		//Check if it already exists?
		
		String invariantLabel = invariant.getLabel();
		boolean isTheorem = invariant.isTheorem();
		
		PyAST_Invariant NewInvariant = new PyAST_Invariant(invariantLabel,isTheorem);
		
		PyAST_Predicate invariantPredicate = Visitor.getPredicate(invariant.getPredicateString());
		NewInvariant.InvariantPredicate = invariantPredicate;
		
		Invariants.put(invariantLabel,NewInvariant);
	}
	
	//Add a Variable to the Context.
	public void AddVariable(ISCVariable variable) throws CoreException {
		System.out.println("PyAST_Machine.AddVariable: " + variable.getElementName());
		//Check if it already exists?
		
		String variableName = variable.getElementName();
		PyAST_Variable NewVariable = new PyAST_Variable(variableName);
		
		final FormulaFactory factory = FormulaFactory.getDefault();
		
		//FOR DEBUGGING: This shows the full type of the variable (not parsed).
		//String firstType = ((ISCIdentifierElement) variable).getType(factory).toString();
		
		PyAST_Type variableType = Visitor.getConstantType(((ISCIdentifierElement) variable).getType(factory).toString());
		NewVariable.VariableType = variableType;
		
		Variables.put(variableName,NewVariable);
	}
	
	//Set Context Extension
	public void SetMachineInternalContext(PyAST_Context internalContext) {
		HasMachineInternalContext = true;
		MachineInternalContext = internalContext;
		Visitor.SetContextExtension(internalContext);
	}

	//Set Context Extension
	public void SetMachineRefinement(PyAST_Machine machineRefinement) {
		HasMachineRefinement = true;
		MachineRefinement = machineRefinement;
		Visitor.SetMachineRefinement(machineRefinement);
	}
}
