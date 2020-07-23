package eventb2python.PyAST_Utils;

import java.util.HashMap;

import org.eclipse.core.runtime.CoreException;
import org.eventb.core.ISCAxiom;
import org.eventb.core.ISCCarrierSet;
import org.eventb.core.ISCConstant;
import org.eventb.core.ISCIdentifierElement;
import org.eventb.core.ast.FormulaFactory;
import org.rodinp.core.RodinDBException;

import eventb2python.PyAST_Predicates.PyAST_Predicate;
import eventb2python.PyAST_Types.PyAST_Type;

public class PyAST_Context {
	
	//Private Attributes
	
	//Public Attributes
	public String Name;
	public PyAST_Visitor Visitor;
	
	public HashMap<String,PyAST_Constant> Constants;
	public HashMap<String,PyAST_Axiom> Axioms;
	public HashMap<String,PyAST_CarrierSet> CarrierSets;
	
	public boolean HasContextExtension;
	public PyAST_Context ContextExtension;
	
	//Constructor
	public PyAST_Context(String contextName){
		Name = contextName;
		Visitor = new PyAST_Visitor();
		
		Constants = new HashMap<String,PyAST_Constant>();
		Axioms = new HashMap<String,PyAST_Axiom>();
		CarrierSets = new HashMap<String,PyAST_CarrierSet>();
		
		HasContextExtension = false;
		ContextExtension = new PyAST_Context();
	}
	
	public PyAST_Context() {
		HasContextExtension = false;
	}
	
	//Methods
	
	//Add a Carrier Set to the Context.
	public void AddCarrierSet(ISCCarrierSet carrierSet) throws RodinDBException {
		System.out.println("PyAST_Context.AddCarrierSet: " + carrierSet.getElementName());
		//Check if it already exists?
		
		String carrierSetName = carrierSet.getElementName();
		PyAST_CarrierSet NewCarrierSet = new PyAST_CarrierSet(carrierSetName);
		if(Visitor.CarrierSetsMetaData.containsKey(NewCarrierSet.CarrierSetName)) {
			NewCarrierSet.EstimatedSize = Visitor.CarrierSetsMetaData.get(NewCarrierSet.CarrierSetName);
		}
		
		CarrierSets.put(carrierSetName,NewCarrierSet);
	}
	
	//Add an Axiom to the Context.
	public void AddAxiom(ISCAxiom axiom) throws RodinDBException {
		System.out.println("PyAST_Context.AddAxiom: " + axiom.getLabel());
		//Check if it already exists?
		
		String axiomLabel = axiom.getLabel();
		boolean isTheorem = axiom.isTheorem();
		PyAST_Axiom NewAxiom = new PyAST_Axiom(axiomLabel,isTheorem);
		
		PyAST_Predicate axiomPredicate = Visitor.getPredicate(axiom.getPredicateString());
		NewAxiom.AxiomPredicate = axiomPredicate;
		
		Axioms.put(axiomLabel,NewAxiom);
	}
	
	//Add a Constant to the Context.
	public void AddConstant(ISCConstant constant) throws CoreException {
		System.out.println("PyAST_Context.AddConstant: " + constant.getElementName());
		//Check if it already exists?
		
		String constantName = constant.getElementName();
		PyAST_Constant NewConstant = new PyAST_Constant(constantName);
		
		final FormulaFactory factory = FormulaFactory.getDefault();
		
		//FOR DEBUGGING: This shows the full type of the constant (not parsed).
		//String firstType = ((ISCIdentifierElement) constant).getType(factory).toString();
		
		PyAST_Type constantType = Visitor.getConstantType(((ISCIdentifierElement) constant).getType(factory).toString());
		NewConstant.ConstantType = constantType;
		
		Constants.put(constantName,NewConstant);
	}
	
	//Set Context Extension
	public void SetContextExtension(PyAST_Context contextExtension) {
		HasContextExtension = true;
		ContextExtension = contextExtension;
		Visitor.SetContextExtension(contextExtension);
	}
}
