package eventb2python.handlers;

import java.util.HashMap;
import java.util.LinkedList;

import org.eclipse.core.runtime.CoreException;
import org.eventb.core.ISCExtendsContext;
import org.eventb.core.ISCInternalContext;
import org.eventb.core.ISCRefinesMachine;
import org.eventb.core.basis.SCContextRoot;
import org.eventb.core.basis.SCMachineRoot;
import org.rodinp.core.IInternalElement;
import org.rodinp.core.IRodinElement;
import org.rodinp.core.IRodinFile;
import org.rodinp.core.IRodinProject;
import org.rodinp.core.RodinCore;
import org.rodinp.core.RodinDBException;

public class RodinHandler{
	
	//Private Attributes
	
	//Public Attributes
	
		//Important
	
			//General
			public String PathLocation;
			public IRodinProject[] RodinProjects;
			public int currentProjectID;
			
			public IRodinProject Project;
		
			//Machines
			public HashMap<String,SCMachineRoot> Machines;
			public HashMap<String,LinkedList<String>> MachinesInternalContexts;
			public LinkedList<String> MachineOrder;
			public HashMap<String,String> RefinementsRelation;
			public int currentMachineID;
			
			public SCMachineRoot Machine;
			public String MachineRefinement;
			public String MachineInternalContext;
			
			//Context
			public HashMap<String,SCContextRoot> Contexts;
			public LinkedList<String> ContextOrder;
			public HashMap<String,String> ExtensionsRelation;
			public int currentContextID;
			
			public SCContextRoot Context;
			public String ContextExtension;
	
		//Support
		public boolean AvailableProjects;
		public boolean AvailableMachines;
		public boolean AvailableContexts;
		
	//Constructor
	public RodinHandler() throws RodinDBException{
		//Obtain Projects in RodinDB. Check if available Projects.
		RodinProjects = RodinCore.getRodinDB().getRodinProjects();
		PathLocation = RodinCore.getRodinDB().getResource().getRawLocation().toString();
		
		if(RodinProjects.length == 0)AvailableProjects=false;
		else AvailableProjects=true;
		
		currentProjectID = 0;
	}
	
	//Methods
	
	//Fetch Machine
	public String FetchMachine() {
		String CurrentMachineName = MachineOrder.get(currentMachineID);
		Machine = Machines.get(CurrentMachineName);
		
		MachineRefinement = "";
		if(RefinementsRelation.containsKey(CurrentMachineName)) {
			MachineRefinement = RefinementsRelation.get(CurrentMachineName);
		}
		
		MachineInternalContext = "";
		
		boolean flag;
		for(String internalContext : MachinesInternalContexts.get(CurrentMachineName)) {
			flag = true;
			for(String internalContextCheck : MachinesInternalContexts.get(CurrentMachineName)) {
				if(ExtensionsRelation.containsKey(internalContextCheck)) {
					if(ExtensionsRelation.get(internalContextCheck).equals(internalContext)) {
						flag = false;
						break;
					}
				}
			}
			if(flag) {
				MachineInternalContext = internalContext;
				break;
			}
		}
		
		System.out.println("CurrentMachineName " + CurrentMachineName);
		System.out.println("MachineRefinement " + MachineRefinement);
		System.out.println("MachineInternalContext " + MachineInternalContext);
		
		return CurrentMachineName;
	}
	
	//Fetch Context
	public String FetchContext() {
		String CurrentContextName = ContextOrder.get(currentContextID);
		Context = Contexts.get(CurrentContextName);
		
		ContextExtension = "";
		if(ExtensionsRelation.containsKey(CurrentContextName)) {
			ContextExtension = ExtensionsRelation.get(CurrentContextName);
		}
		
		return CurrentContextName;
	}
	
	//Fetch Contexts
	public void FetchContexts() throws RodinDBException{
		AvailableContexts = false;
		currentContextID=0;
		
		Contexts = new HashMap<String,SCContextRoot>();
		ContextOrder=new LinkedList<String>();
		
		ExtensionsRelation = new HashMap<String,String>();
		
		for(IRodinElement ProjectChild : Project.getChildren()){
			IInternalElement internalElement = ((IRodinFile)ProjectChild).getRoot();
			if(internalElement instanceof SCContextRoot) {
				AvailableContexts=true;
				
				String nameOfContext = internalElement.getElementName();
				SCContextRoot contextRoot = (SCContextRoot) internalElement;
				Contexts.put(nameOfContext, contextRoot);
				
				for(ISCExtendsContext ExtendClause : contextRoot.getSCExtendsClauses()) {
					try {
						ExtensionsRelation.put(nameOfContext, ExtendClause.getAbstractSCContext().getComponentName());
					} catch (CoreException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
			}
			
		}
		//This section could be done with TopoSort Algorithm, but the optmization wouldn't be significant.
		System.out.println("TopoSort Contexts " + Contexts.size());
		while(ContextOrder.size() < Contexts.size()) {
			for(String getNameOfContext : Contexts.keySet()) {
				if((!ContextOrder.contains(getNameOfContext)) && 
						(!ExtensionsRelation.keySet().contains(getNameOfContext) || 
						(ExtensionsRelation.keySet().contains(getNameOfContext) && ContextOrder.contains(ExtensionsRelation.get(getNameOfContext))))) {
					ContextOrder.add(getNameOfContext);
				}
			}
		}
		System.out.println(ContextOrder);
		System.out.println(ExtensionsRelation);
	}
	
	//Fetch Machines
	public void FetchMachines() throws RodinDBException{
		AvailableMachines = false;
		currentMachineID=0;
		
		Machines = new HashMap<String,SCMachineRoot>();
		MachineOrder=new LinkedList<String>();
		
		MachinesInternalContexts = new HashMap<String,LinkedList<String>>();
		
		RefinementsRelation = new HashMap<String,String>();
		
		//HashMap<String,Integer>InDegree = new HashMap<String,Integer>();
		
		for(IRodinElement ProjectChild : Project.getChildren()){
			IInternalElement internalElement = ((IRodinFile)ProjectChild).getRoot();
			if(internalElement instanceof SCMachineRoot) {
				AvailableMachines=true;
				
				String nameOfMachine = internalElement.getElementName();
				SCMachineRoot machineRoot = (SCMachineRoot) internalElement;
				Machines.put(nameOfMachine, machineRoot);
				
				//Get Internal Context from every Machine
				LinkedList<String> InternalContexts=new LinkedList<String>();
				for(ISCInternalContext InternalContext : machineRoot.getChildrenOfType(ISCInternalContext.ELEMENT_TYPE)) {
					InternalContexts.add(InternalContext.getElementName());
				}
				MachinesInternalContexts.put(nameOfMachine, InternalContexts);
				
				//Get Refined Machines from every Machine
				for(ISCRefinesMachine RefineClause : machineRoot.getSCRefinesClauses()) {
					try {
						RefinementsRelation.put(nameOfMachine,RefineClause.getAbstractSCMachine().getBareName());
					} catch (CoreException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
			}
		}
		
		System.out.println("TopoSort Machines " + Machines.size());
		while(MachineOrder.size() < Machines.size()) {
			for(String getNameOfMachine : Machines.keySet()) {
				if((!MachineOrder.contains(getNameOfMachine)) && 
						(!RefinementsRelation.keySet().contains(getNameOfMachine) || 
						(RefinementsRelation.keySet().contains(getNameOfMachine) && MachineOrder.contains(RefinementsRelation.get(getNameOfMachine))))) {
					MachineOrder.add(getNameOfMachine);
				}
			}
		}
		System.out.println(MachineOrder);
		System.out.println(RefinementsRelation);
		
	}
	
	//Fetch Current Project to work with
	public void FetchProject() {
		Project = RodinProjects[currentProjectID];
	}
	
	//Get Name of Project
	public String getProjectName() {
		return Project.getElementName();
	}
}
