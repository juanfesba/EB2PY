package eventb2python.handlers;

import java.util.LinkedList;

import org.eclipse.core.runtime.CoreException;
import org.eventb.core.ISCAxiom;
import org.eventb.core.ISCCarrierSet;
import org.eventb.core.ISCConstant;
import org.eventb.core.ISCEvent;
import org.eventb.core.ISCInvariant;
import org.eventb.core.ISCVariable;
import org.eventb.core.ISCVariant;
import org.rodinp.core.RodinDBException;

import eventb2python.PyAST_Utils.PyAST_Context;
import eventb2python.PyAST_Utils.PyAST_Machine;

public class PyAST {
	
	//Private Attributes
	
	//Public Attributes
		//General
		public String ProjectName;
		
		public LinkedList<PyAST_Context>Contexts;
		public LinkedList<PyAST_Machine>Machines;
	
		//Current
		public PyAST_Context Context;
		public PyAST_Machine Machine;
	
	//Constructor
	public PyAST(){
		Contexts=new LinkedList<PyAST_Context>();
		Machines=new LinkedList<PyAST_Machine>();
	}
	
	//Methods
	
	//Add Event to Current Machine.
	public void Machine_AddEvent(ISCEvent event) throws RodinDBException {
		try {
			Machine.AddEvent(event);
		} catch (CoreException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	//Add Invariant to Current Machine.
	public void Machine_AddVariant(ISCVariant variant) throws RodinDBException {
		Machine.AddVariant(variant);
	}
	
	//Add Invariant to Current Machine.
	public void Machine_AddInvariant(ISCInvariant invariant) throws RodinDBException {
		Machine.AddInvariant(invariant);
	}
	
	//Add Variable to Current Machine.
	public void Machine_AddVariable(ISCVariable variable) throws CoreException{
		Machine.AddVariable(variable);
	}
	
	//Add Carrier Set to Current Context.
	public void Context_AddCarrierSet(ISCCarrierSet carrierSet) throws RodinDBException {
		Context.AddCarrierSet(carrierSet);
	}
	
	//Add Axiom to Current Context.
	public void Context_AddAxiom(ISCAxiom axiom) throws RodinDBException {
		Context.AddAxiom(axiom);
	}
	
	//Add Constant to Current Context.
	public void Context_AddConstant(ISCConstant constant) throws CoreException {
		Context.AddConstant(constant);
	}
	
	//Store Machine
	public void storeMachine() {
		Machines.add(Machine);
	}
	
	//Store Context
	public void storeContext() {
		Contexts.add(Context);
	}
	
	//Set New Machine
	public void setNewMachine(String machineName,String machineRefinement,String machineInternalContext) {
		
		PyAST_Machine possibleMachineRefinement = new PyAST_Machine();
		
		System.out.println("machineName : " + machineName);
		System.out.println("machineRefinement : " + machineRefinement);
		System.out.println("machineInternalContext : " + machineInternalContext);
		
		
		boolean flagRefinement = false;
		if(!machineRefinement.equals("")) {
			System.out.println("Entro Refinement");
			flagRefinement = true;
			for(PyAST_Machine previousMachine : Machines) {
				if(previousMachine.Name.equals(machineRefinement)) {
					possibleMachineRefinement = previousMachine;
				}
			}
		}
		
		PyAST_Context possibleInternalContext = new PyAST_Context();
		
		boolean flagExtension = false;
		if(!machineInternalContext.equals("")) {
			System.out.println("Entro InternalContext");
			flagExtension = true;
			for(PyAST_Context previousContext : Contexts) {
				if(previousContext.Name.equals(machineInternalContext)) {
					possibleInternalContext = previousContext;
				}
			}
		}
			
		Machine = new PyAST_Machine(machineName);
		
		if(flagRefinement)Machine.SetMachineRefinement(possibleMachineRefinement);
		if(flagExtension)Machine.SetMachineInternalContext(possibleInternalContext);
	}
	
	//Set New Context
	public void setNewContext(String contextName,String contextExtension) {
		PyAST_Context possibleContextExtension = new PyAST_Context();
		
		boolean flag = false;
		if(!contextExtension.equals("")) {
			flag = true;
			for(PyAST_Context previousContext : Contexts) {
				if(previousContext.Name.equals(contextExtension)) {
					possibleContextExtension = previousContext;
				}
			}
		}
		
		Context = new PyAST_Context(contextName);
		
		if(flag)Context.SetContextExtension(possibleContextExtension);
	}
	
	//Set Name of the Project.
	public void setProjectName(String projectName) {
		ProjectName = projectName;
	}
}