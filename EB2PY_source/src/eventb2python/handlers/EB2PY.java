package eventb2python.handlers;

import java.io.File;
import java.io.IOException;

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

public class EB2PY {
	
	//Private Attributes
	
	
	//Public Attributes
	
		//Important
		public RodinHandler rodinHandler;
		public PyAST pyAST;
		public OutputHandler outputHandler;
		public String OutputLocation;
		
		//Supporting
		public boolean AvailableProjects;
	
	//Constructor
	public EB2PY() throws RodinDBException {
		//Create the Handler to access RodinSoftware.
		rodinHandler = new RodinHandler();
		String pathLocation = rodinHandler.PathLocation;
		
		OutputLocation = pathLocation + File.separator + ".." + File.separator;
		new File(OutputLocation + "Output_EB2PY").mkdir();
		OutputLocation += "Output_EB2PY" + File.separator;
		
		AvailableProjects=rodinHandler.AvailableProjects;
	}
	
	//Methods
	
	//Process Machine
	public void processMachine(String machineName, String machineRefinement, String machineInternalContext) throws RodinDBException {
		System.out.println("EB2PY.processMachine: " + machineName + " Refinement: " + machineRefinement + " Internal Context: " + machineInternalContext);
		//Initialize PyAST Machine with CurrentMachineName
		
		pyAST.setNewMachine(machineName,machineRefinement,machineInternalContext);
		
		//Process Variant
		ISCVariant[] variants = rodinHandler.Machine.getSCVariants();
		for(ISCVariant variant : variants) {
			pyAST.Machine_AddVariant(variant);
		}
		
		//Process Variables
		ISCVariable[] variables = rodinHandler.Machine.getSCVariables();
		for(ISCVariable variable : variables) {
			try {
				pyAST.Machine_AddVariable(variable);
			} catch (CoreException e) {
				e.printStackTrace();
			}
		}
		
		//Process Invariants
		ISCInvariant[] invariants = rodinHandler.Machine.getSCInvariants();
		for(ISCInvariant invariant  : invariants) {
			pyAST.Machine_AddInvariant(invariant);
		}
		
		//Process Invariants
		ISCEvent[] events = rodinHandler.Machine.getSCEvents();
		for(ISCEvent event  : events) {
			pyAST.Machine_AddEvent(event);
		}
		
		pyAST.storeMachine();
	}
	
	//Process Context
	public void processContext(String contextName,String contextExtension) throws RodinDBException {
		System.out.println("EB2PY.processContext: " + contextName + " Extension: " + contextExtension);
		//Initialize PyAST Context with Current Context

		pyAST.setNewContext(contextName,contextExtension);
		
		//Process Constants
		ISCConstant[] constants = rodinHandler.Context.getSCConstants();
		for(ISCConstant constant : constants) {
			try {
				pyAST.Context_AddConstant(constant);
			} catch (CoreException e) {
				e.printStackTrace();
			}
		}
		
		//Process Axioms
		ISCAxiom[] axioms = rodinHandler.Context.getSCAxioms();
		for(ISCAxiom axiom  : axioms) {
			pyAST.Context_AddAxiom(axiom);
		}
		//int[] debug = new int[1];
		//System.out.println(debug[7]);
		//TODO Keep the above commented.
		
		//Process Carrier Sets
		ISCCarrierSet[] carrierSets = rodinHandler.Context.getSCCarrierSets();
		for(ISCCarrierSet carrierSet : carrierSets) {
			pyAST.Context_AddCarrierSet(carrierSet);
		}
		
		pyAST.storeContext();
	}
	
	//Process Machines
	public void processMachines() throws RodinDBException {
		if(rodinHandler.AvailableMachines) {
			//Traverse Machines and build PyAST
			while(rodinHandler.currentMachineID<rodinHandler.MachineOrder.size()) {
				String machineName = rodinHandler.FetchMachine(); //This also fetches Extensions and Refinements
				processMachine(machineName,rodinHandler.MachineRefinement,rodinHandler.MachineInternalContext);
				
				rodinHandler.currentMachineID+=1;
			}
		}
	}
	
	//Process Contexts
	public void processContexts() throws RodinDBException {
		if(rodinHandler.AvailableContexts) {
			//Traverse Contexts and build PyAST
			while(rodinHandler.currentContextID<rodinHandler.ContextOrder.size()) {
				
				String contextName = rodinHandler.FetchContext(); //This also fetches the Context Extension
				processContext(contextName,rodinHandler.ContextExtension);
				
				rodinHandler.currentContextID+=1;
			}
		}
	}
	
	//Translation of a project.
	public void TranslateProject() throws RodinDBException {
		System.out.println("EB2PY.TranslateProject: " + pyAST.ProjectName);
		
		rodinHandler.FetchContexts();
		rodinHandler.FetchMachines();
		
		processContexts();
		processMachines();
		
		//Traverse Contexts to Translate them.
		for(PyAST_Context context :  pyAST.Contexts) {
			try {
				outputHandler.translateContext(context);
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
		
		//Traverse Machines to Translate them.
		for(PyAST_Machine machine : pyAST.Machines) {
			try {
				outputHandler.translateMachine(machine);
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
	}
	
	//Traverse projects in RodinDB and translate them.
	public void TranslateProjects() throws RodinDBException {
		try {
			outputHandler = new OutputHandler(OutputLocation);
		} catch (IOException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}
		while(rodinHandler.currentProjectID<rodinHandler.RodinProjects.length) {
			rodinHandler.FetchProject();
			pyAST = new PyAST();
			pyAST.setProjectName(rodinHandler.getProjectName());
			outputHandler = new OutputHandler(OutputLocation,rodinHandler.getProjectName());
			try {
				outputHandler.MypyPathDependencies();
			} catch (IOException e) {
				e.printStackTrace();
			}
			if(outputHandler.DirectoryCreatedSuccesfully) {
				TranslateProject();
			}
			
			rodinHandler.currentProjectID+=1;
		}
	}
}
