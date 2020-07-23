package eventb2python.handlers;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Random;
import java.util.Set;
import java.util.Stack;

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
import eventb2python.PyAST_Types.PyAST_FreeIdentifierType;
import eventb2python.PyAST_Types.PyAST_Type;
import eventb2python.PyAST_Types.PyAST_UnaryExpressionType;
import eventb2python.PyAST_Utils.PyAST_Action;
import eventb2python.PyAST_Utils.PyAST_Axiom;
import eventb2python.PyAST_Utils.PyAST_CarrierSet;
import eventb2python.PyAST_Utils.PyAST_Constant;
import eventb2python.PyAST_Utils.PyAST_Context;
import eventb2python.PyAST_Utils.PyAST_Event;
import eventb2python.PyAST_Utils.PyAST_Invariant;
import eventb2python.PyAST_Utils.PyAST_Machine;
import eventb2python.PyAST_Utils.PyAST_Variable;

public class OutputHandler {
	
	//Private Attributes
	
	//Public Attributes
		//Important
			//General
			public String OutputLocation;
			public String ProjectName;
			public boolean DirectoryCreatedSuccesfully;
			
			FileWriter Writer;
			
			//Context Support
			
			//Machine Support
			public HashMap<String,String>VariableTypesDP;
			
		//General Support
		public int IDENTATION;
		public int MAX_PROJECT_VERSIONS; //one more than specified
		public Comparator<PyAST_Axiom> AxiomComparator; //To Output organized Axioms when possible.
		public Comparator<PyAST_Constant> ConstantComparator; //To Output organized Constants when possible.
		public Comparator<PyAST_CarrierSet> CarrierSetComparator; //To Output organized CarrierSets when possible.
		public Comparator<PyAST_Invariant> InvariantComparator; //To Output organized Invariants when possible.
		public Comparator<PyAST_Variable> VariableComparator; //To Output organized Variables when possible.
		public Random RandomNumberGenerator; //To provide more diversity to the Outputs.
		public int MAX_CARRIERSET_INITIALELEMENTS;
		public String PreludeName;
		public String PreludeClassName;
		public String QuantifiedBoundIdentifiersName;
		
			//Support for Quantified Expressions/Predicates
			public Stack<Integer> CurrentQuantified;
		
	//Constructor
	public OutputHandler(String outputLocation, String projectName) {
		
		/*
		IBundleGroupProvider[] xx = Platform.getBundleGroupProviders();
		for(IBundleGroupProvider x : xx) {
			System.out.println(x.getName());
		}
		*/
		
		IDENTATION = 3;
		MAX_PROJECT_VERSIONS = 15;
		
		OutputLocation = outputLocation;
		ProjectName = projectName;
		
		int i = 0;
		DirectoryCreatedSuccesfully = new File(OutputLocation + projectName + "_Project_" + String.valueOf(i)).mkdir();
		while(!DirectoryCreatedSuccesfully) {
			
			if(i==MAX_PROJECT_VERSIONS) {
				break;
			}
			i+=1;
			DirectoryCreatedSuccesfully = new File(OutputLocation + projectName + "_Project_" + String.valueOf(i)).mkdir();
		}

		OutputLocation += projectName + "_Project_" + String.valueOf(i) + File.separator;
		
		//Support Initialization -- Only for better Formatted Output
		AxiomComparator = new Comparator<PyAST_Axiom>() {
			public int compare(PyAST_Axiom ax1, PyAST_Axiom ax2) {
				return ax1.AxiomLabel.compareTo(ax2.AxiomLabel);
			}
		};
		
		ConstantComparator = new Comparator<PyAST_Constant>() {
			public int compare(PyAST_Constant cnst1, PyAST_Constant cnst2) {
				return cnst1.ConstantName.compareTo(cnst2.ConstantName);
			}
		};
		
		CarrierSetComparator = new Comparator<PyAST_CarrierSet>() {
			public int compare(PyAST_CarrierSet cs1, PyAST_CarrierSet cs2) {
				return cs1.CarrierSetName.compareTo(cs2.CarrierSetName);
			}
		};
		
		InvariantComparator = new Comparator<PyAST_Invariant>() {
			public int compare(PyAST_Invariant inv1, PyAST_Invariant inv2) {
				return inv1.InvariantLabel.compareTo(inv2.InvariantLabel);
			}
		};
		
		VariableComparator = new Comparator<PyAST_Variable>() {
			public int compare(PyAST_Variable var1, PyAST_Variable var2) {
				return var1.VariableName.compareTo(var2.VariableName);
			}
		};
		
		//Support Randomness Generator Initialization and other supporting variables.
		RandomNumberGenerator = new Random();
		MAX_CARRIERSET_INITIALELEMENTS = 3;
		
		//Machine Support
		VariableTypesDP = new HashMap<String,String>();
		
		//Other
		PreludeName = "P";
		PreludeClassName = "PyPrelude";
		QuantifiedBoundIdentifiersName = "boundIdentifiers";
		
		//Extra Support
		CurrentQuantified = new Stack<Integer>();
	}
	
	public OutputHandler(String outputLocation) throws IOException {
		
		IDENTATION = 3;
		
		OutputLocation = outputLocation;
		
		DirectoryCreatedSuccesfully = new File(OutputLocation + "Py_Preludes").mkdir();

		OutputLocation += "Py_Preludes" + File.separator;
		
		File contextFile = new File(OutputLocation + "__init__.py");
		boolean FileCreatedSuccessfully=contextFile.createNewFile();
		
		//Write Dependencies if the File was created successfully.
		if(FileCreatedSuccessfully) {
			
			Writer = new FileWriter(contextFile);
			
			WriteLine("from Py_Preludes.PyUtils_Prelude2 import *", 0);
			
			Writer.close();
		}
		
		contextFile = new File(OutputLocation + "PyUtils_Prelude2.py");
		FileCreatedSuccessfully=contextFile.createNewFile();
		
		//Write Dependencies if the File was created successfully.
		if(FileCreatedSuccessfully) {
			
			Writer = new FileWriter(contextFile);
		
			WriteLine("#imports Enum\nfrom enum import Enum,auto,unique\n\n#imports Typing\nfrom typing import Set,TypeVar,Generic,Any,Callable,cast,Iterator,Tuple,Any,Dict,Type,List,Optional\n\n#imports Utils\nfrom copy import deepcopy\n\n#imports Random\nfrom random import randint,choice\n\n#Supporting Imports\nfrom math import log2\n\n#Supporting Variables\n\nT = TypeVar(\'T\')\nD = TypeVar(\'D\')\nR = TypeVar(\'R\')\n\nclass PyBaseFunc():\n\n   @staticmethod\n   def Unspecified_FuncBool0() -> bool:\n      #print(\'Test_PreludeBaseFunc.Unspecified_FuncBool0\')\n      raise Exception(\'No special Bool Function 0 args was set for this object\')\n\n   @staticmethod\n   def Unspecified_FuncInt0() -> int:\n      #print(\'Test_PreludeBaseFunc.Unspecified_FuncInt0\')\n      raise Exception(\'No special Int Function 0 args was set for this object\')\n\n   @staticmethod\n   def Unspecified_FuncBool1(element : Any) -> bool:\n      #print(\'Test_PreludeBaseFunc.Unspecified_FuncBool1\')\n      raise Exception(\'No special Bool Function 1 arg was set for this object\')\n\n   @staticmethod\n   def Unspecified_FuncInt1(element : Any) -> int:\n      #print(\'Test_PreludeBaseFunc.Unspecified_FuncInt1\')\n      raise Exception(\'No special Int Function 1 arg was set for this object\')\n\n   @staticmethod\n   def Unspecified_FuncPySet0() -> \'PySet\':\n      #print(\'Test_PreludeBaseFunc.Unspecified_FuncPySet0\')\n      raise Exception(\'No special PySet Function 0 arg was set for this object\')\n\n   @staticmethod\n   def Unspecified_FuncPySet1(element : Any) -> \'PySet\':\n      #print(\'Test_PreludeBaseFunc.Unspecified_FuncPySet1\')\n      raise Exception(\'No special PySet Function 1 arg was set for this object\')\n\n   @staticmethod\n   def ReturnFalse0() -> bool:\n      #print(\'Test_PreludeBaseFunc.ReturnFalse0\')\n      return False\n\n   @staticmethod\n   def ReturnFalse1(element : Any) -> bool:\n      #print(\'Test_PreludeBaseFunc.ReturnFalse1\')\n      return False\n\n   @staticmethod\n   def ReturnTrue0() -> bool:\n      #print(\'Test_PreludeBaseFunc.ReturnTrue0\')\n      return True\n\n   @staticmethod\n   def ReturnTrue1(element : Any) -> bool:\n      #print(\'Test_PreludeBaseFunc.ReturnTrue1\')\n      return True\n\n   @staticmethod\n   def NAT_ContainsFunc(element : int) -> bool:\n      #print(\'Test_PreludeBaseFunc.NAT_ContainsFunc\')\n      if isinstance(element,int) and element >=0:\n         return True\n      return False\n   \n   @staticmethod\n   def NAT1_ContainsFunc(element : int) -> bool:\n      #print(\'Test_PreludeBaseFunc.NAT1_ContainsFunc\')\n      if isinstance(element,int) and element >0:\n         return True\n      return False\n\n   @staticmethod\n   def INT_ContainsFunc(element : int) -> bool:\n      #print(\'Test_PreludeBaseFunc.INT_ContainsFunc\')\n      if isinstance(element,int):\n         return True\n      return False\n\n   @staticmethod\n   def PNAT_ContainsFunc(int_set : \'PySet[int]\') -> bool:\n      #print(\'Test_PreludeBaseFunc.PNAT_ContainsFunc\')\n      for element in int_set:\n         if not PyBaseFunc.NAT_ContainsFunc(element):\n            return False\n      return True\n   \n   @staticmethod\n   def PNAT1_ContainsFunc(int_set : \'PySet[int]\') -> bool:\n      #print(\'Test_PreludeBaseFunc.PNAT1_ContainsFunc\')\n      for element in int_set:\n         if not PyBaseFunc.NAT1_ContainsFunc(element):\n            return False\n      return True\n\n   @staticmethod\n   def PINT_ContainsFunc(int_set : \'PySet[int]\') -> bool:\n      #print(\'Test_PreludeBaseFunc.PINT_ContainsFunc\')\n      for element in int_set:\n         if not PyBaseFunc.INT_ContainsFunc(element):\n            return False\n      return True\n\n   @staticmethod\n   def P1NAT_ContainsFunc(int_set : \'PySet[int]\') -> bool:\n      #print(\'Test_PreludeBaseFunc.P1NAT_ContainsFunc\')\n      for element in int_set:\n         if not PyBaseFunc.NAT_ContainsFunc(element):\n            return False\n      if len(int_set)>0:\n         return True\n      return False\n   \n   @staticmethod\n   def P1NAT1_ContainsFunc(int_set : \'PySet[int]\') -> bool:\n      #print(\'Test_PreludeBaseFunc.P1NAT1_ContainsFunc\')\n      for element in int_set:\n         if not PyBaseFunc.NAT1_ContainsFunc(element):\n            return False\n      if len(int_set)>0:\n         return True\n      return False\n\n   @staticmethod\n   def P1INT_ContainsFunc(int_set : \'PySet[int]\') -> bool:\n      #print(\'Test_PreludeBaseFunc.P1INT_ContainsFunc\')\n      for element in int_set:\n         if not PyBaseFunc.INT_ContainsFunc(element):\n            return False\n      if len(int_set)>0:\n         return True\n      return False\n\n   @staticmethod\n   def PNATXNAT_ContainsFunc(natxnat_set : \'PyRel[int,int]\') -> bool:\n      #print(\'Test_PreludeBaseFunc.PNATXNAT_ContainsFunc\')\n      for left_ele,right_ele in natxnat_set:\n         if not PyBaseFunc.NAT_ContainsFunc(left_ele) or not PyBaseFunc.NAT_ContainsFunc(right_ele):\n            return False\n      return True\n   \n   @staticmethod\n   def PINTXINT_ContainsFunc(intxint_set : \'PyRel[int,int]\') -> bool:\n      #print(\'Test_PreludeBaseFunc.PINTXINT_ContainsFunc\')\n      for left_ele,right_ele in intxint_set:\n         if not PyBaseFunc.INT_ContainsFunc(left_ele) or not PyBaseFunc.INT_ContainsFunc(right_ele):\n            return False\n      return True\n\n   @staticmethod\n   def PINTXNAT_ContainsFunc(intxnat_set : \'PyRel[int,int]\') -> bool:\n      #print(\'Test_PreludeBaseFunc.PINTXNAT_ContainsFunc\')\n      for left_ele,right_ele in intxnat_set:\n         if not PyBaseFunc.INT_ContainsFunc(left_ele) or not PyBaseFunc.NAT_ContainsFunc(right_ele):\n            return False\n      return True\n\n   @staticmethod\n   def P1NATXNAT_ContainsFunc(natxnat_set : \'PyRel[int,int]\') -> bool:\n      #print(\'Test_PreludeBaseFunc.P1NATXNAT_ContainsFunc\')\n      for left_ele,right_ele in natxnat_set:\n         if not PyBaseFunc.NAT_ContainsFunc(left_ele) or not PyBaseFunc.NAT_ContainsFunc(right_ele):\n            return False\n      if len(natxnat_set)>0:\n         return True\n      return False\n   \n   @staticmethod\n   def P1INTXINT_ContainsFunc(intxint_set : \'PyRel[int,int]\') -> bool:\n      #print(\'Test_PreludeBaseFunc.P1INTXINT_ContainsFunc\')\n      for left_ele,right_ele in intxint_set:\n         if not PyBaseFunc.INT_ContainsFunc(left_ele) or not PyBaseFunc.INT_ContainsFunc(right_ele):\n            return False\n      if len(intxint_set)>0:\n         return True\n      return False\n\n   @staticmethod\n   def P1INTXNAT_ContainsFunc(intxnat_set : \'PyRel[int,int]\') -> bool:\n      #print(\'Test_PreludeBaseFunc.P1INTXNAT_ContainsFunc\')\n      for left_ele,right_ele in intxnat_set:\n         if not PyBaseFunc.INT_ContainsFunc(left_ele) or not PyBaseFunc.NAT_ContainsFunc(right_ele):\n            return False\n      if len(intxnat_set)>0:\n         return True\n      return False\n\n   ###Debug Method\n   @staticmethod\n   def test(element:int) -> bool:\n      #print(\'Test_PreludesBaseFunc.test\')\n      if element < -80 and element > -100:\n         return True\n      return False\n\n   @staticmethod\n   def ReturnEmptySet0() -> \'PySet\':\n      #print(\'Test_PreludeBaseFunc.ReturnEmptySet0\')\n      return PySet()\n   \n   @staticmethod\n   def ReturnEmptySet1(set_elems : \'PySet\') -> \'PySet\':\n      #print(\'Test_PreludeBaseFunc.ReturnEmptySet0\')\n      return PySet()\n\n   @staticmethod\n   def ReturnPyNAT_0() -> \'PyNAT\':\n      return PyNAT()\n\n   @staticmethod\n   def ReturnPyINT_0() -> \'PyINT\':\n      return PyINT()\n\n   @staticmethod\n   def ReturnPyNAT_1(int_set : \'PySet[int]\') -> \'PyNAT\':\n      return PyNAT()\n\n   @staticmethod\n   def ReturnPyINT_1(int_set : \'PySet[int]\') -> \'PyINT\':\n      return PyINT()\n\n   @staticmethod\n   def ReturnPyNAT_NAT(nat_set : \'PySet[int]\') -> \'PySet[int]\':\n      for nat_ele in nat_set:\n         if PyBaseFunc.NAT_ContainsFunc(nat_ele):\n            return PyNAT()\n      return PySet()\n\n   @staticmethod\n   def ReturnPyNAT_INT(nat_set : \'PySet[int]\') -> \'PySet[int]\':\n      for nat_ele in nat_set:\n         if PyBaseFunc.NAT_ContainsFunc(nat_ele):\n            return PyINT()\n      return PySet()\n\n   @staticmethod\n   def ID_Rel_Func(any_set : \'PySet\') -> \'PySet\':\n      return any_set\n\n   ###Debug Method\n   @staticmethod\n   def test2(dom_elements : \'PySet[int]\') -> \'PySet[int]\':\n      #print(\'Test_PreludesBaseFunc.test2\')\n      ans_set : Set[int] = set()\n      for dom_ele in dom_elements:\n         if dom_ele == 1:\n            ans_set.update({10,100})\n         elif dom_ele == 2:\n            ans_set.update({20,200})\n         elif dom_ele == 3:\n            ans_set.update({3,4,7})\n      return PySet(ans_set)\n\n\n@unique\nclass PyFamilyTypes(Enum):\n\n   UndeterminedFamilyType = auto()\n   Relations = auto()\n   TotalRelations = auto()\n   SurjectiveRelations = auto()\n   TotalSurjectiveRelations = auto()\n   PartialFunctions = auto()\n   TotalFunctions = auto()\n   PartialInjections = auto()\n   TotalInjections = auto()\n   PartialSurjections = auto()\n   TotalSurjections = auto()\n   Bijections = auto()\n\n\nclass GuardsViolated(Exception):\n   pass\n\n\nclass PyBaseIter():\n\n   def __iter__(self) -> Iterator:\n      return self\n   \n   def __next__(self):\n      raise Exception(\'No special __next__ Function was specified for this object\')\n\nclass PyNAT_Iter(PyBaseIter):\n\n   def __iter__(self) -> Iterator:\n      self.boundary : int = P.FINITE_SPECIAL_SETS_LIMIT()\n      self.iterator : int = -1\n      return self\n   \n   def __next__(self) -> int:\n      if P.USE_FINITE_SPECIAL_SETS():\n         self.iterator += 1\n         if self.iterator > self.boundary:\n            raise StopIteration\n         return self.iterator\n         \n      raise Exception(\'You cannot traverse an infinite set. Set the Prelude Parameter USE_FINITE_SPECIAL_SETS to True.\')\n\nclass PyNAT1_Iter(PyBaseIter):\n\n   def __iter__(self) -> Iterator:\n      self.boundary : int = P.FINITE_SPECIAL_SETS_LIMIT()\n      self.iterator : int = 0\n      return self\n   \n   def __next__(self) -> int:\n      if P.USE_FINITE_SPECIAL_SETS():\n         self.iterator += 1\n         if self.iterator > self.boundary:\n            raise StopIteration\n         return self.iterator\n         \n      raise Exception(\'You cannot traverse an infinite set. Set the Prelude Parameter USE_FINITE_SPECIAL_SETS to True.\')\n\nclass PyINT_Iter(PyBaseIter):\n\n   def __iter__(self) -> Iterator:\n      self.boundary : int = P.FINITE_SPECIAL_SETS_LIMIT()\n      self.iterator : int = - self.boundary - 1\n      return self\n   \n   def __next__(self) -> int:\n      if P.USE_FINITE_SPECIAL_SETS():\n         self.iterator += 1\n         if self.iterator > self.boundary:\n            raise StopIteration\n         return self.iterator\n      raise Exception(\'You cannot traverse an infinite set. Set the Prelude Parameter USE_FINITE_SPECIAL_SETS to True.\')\n\nclass PySet(Generic[T]):\n\n   def __init__(self, initialElements : Set[T] = set()) -> None:\n      #print(\'Test_PySet.__init__\')\n      self.__FiniteInclusion : Set[T] = initialElements\n\n   def FiniteInclusion(self) -> Set[T]:\n      return self.__FiniteInclusion.copy()\n\n   def __str__(self) -> str:\n      return \'PySet(\' + self.__FiniteInclusion.__str__() + \')\'\n\n   def __repr__(self) -> str:\n      return \'PySet(\' + self.__FiniteInclusion.__repr__() + \')\'\n\n   def __len__(self) -> int:\n      return len(self.__FiniteInclusion)\n\n   def __iter__(self) -> Iterator: #Necessary to be able to override __contains__\n      return self.__FiniteInclusion.__iter__()\n\n   def __eq__(self,other) -> bool:\n      if isinstance(other,PyCondSet) or isinstance(other,PyCondRel):\n         raise Exception(\'Operation not supported for implicit Sets\')\n      if isinstance(other,PySet) or isinstance(other,PyRel):\n         return self.__FiniteInclusion.__eq__(other.FiniteInclusion())\n      raise Exception(\'Operation only supported for PySet\')\n\n   def __hash__(self):\n      return hash(frozenset(self.__FiniteInclusion))\n\n   def __contains__(self,element : object) -> bool: #Liskov Principle\n      raise Exception(\'Due to the Liskov Principle, TypeCheck will not work, use PyContains instead.\')\n\n   def PyContains(self,element : T) -> bool:\n      #O(1)\n      #print(\'Test_PySet.PyContains\')\n      return self.__FiniteInclusion.__contains__(element)\n\n   def PyNotContains(self,element : T) -> bool:\n      #O(1)\n      #print(\'Test_PySet.PyNotContains\')\n      return not self.PyContains(element)\n\n   def PyUnion(self, other : \'PySet[T]\') -> \'PySet[T]\':\n      #O(m+n) between PySets.\n      #print(\'Test_PySet.PyUnion\')\n\n      if isinstance(other, PyCondSet_TreeExt):\n         return other.PyUnion(self)\n      elif isinstance(other, PyCondSet_Ext):\n         new_finite_inclusion : Set = other.FiniteInclusion().union(self.__FiniteInclusion)\n         return PyCondSet_Ext(other.FuncContains(), new_finite_inclusion, other.FiniteExclusion().difference(new_finite_inclusion))\n      elif isinstance(other, PyCondSet):\n         return PyCondSet_Ext(other.FuncContains(), self.FiniteInclusion())\n      return PySet(self.__FiniteInclusion.union(other.FiniteInclusion()))\n\n   def PyIntersection(self, other : \'PySet[T]\') -> \'PySet[T]\':\n      #O(m) between PySets.\n      #print(\'Test_PySet.PyIntersection\')\n      \n      if isinstance(other, PyCondSet):\n         intersection_set : Set = set()\n         for element in self:\n            if other.PyContains(element):\n               intersection_set.add(element)\n         return PySet(intersection_set)\n      return PySet(self.__FiniteInclusion.intersection(other.FiniteInclusion()))\n\n   def PyDifference(self, other : \'PySet[T]\') -> \'PySet[T]\':\n      #O(m) between PySets.\n      #print(\'Test_PySet.PyDifference\')\n\n      if isinstance(other, PyCondSet):\n         difference_set : Set = self.FiniteInclusion()\n         for element in self:\n            if other.PyContains(element):\n               difference_set.discard(element)\n         return PySet(difference_set)\n      return PySet(self.__FiniteInclusion.difference(other.FiniteInclusion()))\n\n   def PyCartesianProduct(self, other : \'PySet\') -> \'PyRel[T,Any]\':\n      #O(m*n) between PySets.\n      #print(\'Test_PySet.PyCartesianProduct\')\n      if isinstance(other, PyCondSet_Ext):\n         raise Exception(\'Operation only supported between iterable PySets\')\n      cartesian_product : Set[Tuple[T,Any]] = set()\n      for self_ele in self:\n         for other_ele in other:\n            cartesian_product.add((self_ele, other_ele))\n      return PyRel(cartesian_product)\n\n   def PyIsSubset(self, other : \'PySet[T]\') -> bool:\n      #O(n)\n      #print(\'Test_PySet.PyIsSubset\')\n      for element in self:\n         if not(other.PyContains(element)):\n            return False\n      return True\n\n   def PyNotSubset(self, other : \'PySet[T]\') -> bool:\n      #O(n)\n      #print(\'Test_PySet.PyNotSubset\')\n      return not self.PyIsSubset(other)\n\n   def PyIsProperSubset(self, other : \'PySet[T]\') -> bool:\n      #O(n)\n      #print(\'Test_PySet.PyIsProperSubset\')\n      if len(self)==len(other):\n         return False\n      return self.PyIsSubset(other)\n\n   def PyNotProperSubset(self, other : \'PySet[T]\') -> bool:\n      #O(n)\n      #print(\'Test_PySet.PyNotProperSubset\')\n      return not self.PyIsProperSubset(other)\n\n   def PyFinite(self) -> bool:\n      #O(1)\n      #print(\'Test_PySet.PyFinite\')\n      return True\n\n   def PyPartition(self, partition_sets : \'List[PySet[T]]\') -> bool:\n      #print(\'Test_PySet.PyPartition\')\n      checking_set : PySet[T] = PySet()\n      for partition_set in partition_sets:\n         if isinstance(partition_set, PyCondSet):\n            raise Exception(\'Operation only supported between PySets\')\n         if len(checking_set.PyIntersection(partition_set)) > 0:\n            return False\n         checking_set = checking_set.PyUnion(partition_set)\n      if checking_set.__eq__(self):\n         return True\n      return False\n\n   def PyPowerSet(self) -> \'PySet[PySet[T]]\':\n      #print(\'Test_PySet.PyPowerSet\')\n      elements_list : List[T] = list(self.FiniteInclusion())\n      power_set : Set[PySet[T]] = set()\n      for set_picker in range(2**len(self)):\n         current_set : Set[T] = set()\n         for i in range(len(self)):\n            if set_picker & 1<<i != 0:\n               current_set.add(elements_list[i])\n         power_set.add(PySet(current_set))\n      return PySet(power_set)\n\n   def PyPowerSet1(self) -> \'PySet[PySet[T]]\':\n      #print(\'Test_PySet.PyPowerSet1\')\n      elements_list : List[T] = list(self.FiniteInclusion())\n      power_set : Set[PySet[T]] = set()\n      for set_picker in range(1,2**len(self)):\n         current_set : Set[T] = set()\n         for i in range(len(self)):\n            if set_picker & 1<<i != 0:\n               current_set.add(elements_list[i])\n         power_set.add(PySet(current_set))\n      return PySet(power_set)\n\n   def PyChoice(self) -> T:\n      #print(\'Test_PySet.PyChoice\')\n      return choice(list(self.__FiniteInclusion))\n\n   def PyDomain(self) -> \'PySet[D]\':\n      #print(\'Test_PySet.PyDomain\')\n      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)\n      return tmp_pyrel.PyDomain()\n\n   def PyRange(self) -> \'PySet[R]\':\n      #print(\'Test_PySet.PyRange\')\n      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)\n      return tmp_pyrel.PyRange()\n\n   def PyComposition(self, other : \'PyRel[R,T]\') -> \'PyRel[D,T]\':\n      #print(\'Test_PySet.PyComposition\')\n      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)\n      return tmp_pyrel.PyComposition(other)\n\n   def PyBackwardComposition(self, other : \'PyRel[T,D]\') -> \'PyRel[T,R]\':\n      #print(\'Test_PySet.PyBackwardComposition\')\n      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)\n      return tmp_pyrel.PyBackwardComposition(other)\n\n   def PyDomainRestriction(self, other : \'PySet[D]\') -> \'PyRel[D,R]\':\n      #print(\'Test_PySet.PyDomainRestriction\')\n      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)\n      return tmp_pyrel.PyDomainRestriction(other)\n\n   def PyRangeRestriction(self, other : \'PySet[R]\') -> \'PyRel[D,R]\':\n      #print(\'Test_PySet.PyRangeRestriction\')\n      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)\n      return tmp_pyrel.PyRangeRestriction(other)\n\n   def PyDomainSubstraction(self, other : \'PySet[D]\') -> \'PyRel[D,R]\':\n      #print(\'Test_PySet.PyDomainSubstraction\')\n      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)\n      return tmp_pyrel.PyDomainSubstraction(other)\n\n   def PyRangeSubstraction(self, other : \'PySet[R]\') -> \'PyRel[D,R]\':\n      #print(\'Test_PySet.PyRangeSubstraction\')\n      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)\n      return tmp_pyrel.PyRangeSubstraction(other)\n\n   def __invert__(self) -> \'PyRel[R,D]\': #Inverse Relation method\n      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)\n      return tmp_pyrel.__invert__()\n\n   def __getitem__(self, keys : \'PySet[D]\') -> \'PySet[R]\': #Relational Image method\n      #O(range)\n      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)\n      return tmp_pyrel.__getitem__(keys)\n\n   def PyOverriding(self, other : \'PyRel[D,R]\') -> \'PyRel[D,R]\':\n      #print(\'Test_PySet.PyOverriding\')\n      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)\n      return tmp_pyrel.PyOverriding(other)\n\n   def PyDirectProduct(self, other : \'PyRel[D,T]\') -> \'PyRel[D,Tuple[R,T]]\':\n      #print(\'Test_PySet.PyDirectProduct\')\n      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)\n      return tmp_pyrel.PyDirectProduct(other)\n\n   def PyIsTotal(self, domain_set : \'PySet[D]\') -> bool:\n      #print(\'Test_PySet.PyIsTotal\')\n      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)\n      return tmp_pyrel.PyIsTotal(domain_set)\n\n   def PyIsSurjection(self, range_set : \'PySet[R]\') -> bool:\n      #print(\'Test_PySet.PyIsSurjection\')\n      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)\n      return tmp_pyrel.PyIsSurjection(range_set)\n\n   def PyIsRelation(self, domain_set : \'PySet[D]\', range_set : \'PySet[R]\') -> bool:\n      #print(\'Test_PySet.PyIsRelation\')\n      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)\n      return tmp_pyrel.PyIsRelation(domain_set,range_set)\n\n   def PyIsTotalRelation(self, domain_set : \'PySet[D]\', range_set : \'PySet[R]\') -> bool:\n      #print(\'Test_PySet.PyIsTotalRelation\')\n      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)\n      return tmp_pyrel.PyIsTotalRelation(domain_set,range_set)\n\n   def PyIsSurjectiveRelation(self, domain_set : \'PySet[D]\', range_set : \'PySet[R]\') -> bool:\n      #print(\'Test_PySet.PyIsSurjectiveRelation\')\n      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)\n      return tmp_pyrel.PyIsSurjectiveRelation(domain_set,range_set)\n\n   def PyIsTotalSurjectiveRelation(self, domain_set : \'PySet[D]\', range_set : \'PySet[R]\') -> bool:\n      #print(\'Test_PySet.PyIsTotalSurjectiveRelation\')\n      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)\n      return tmp_pyrel.PyIsTotalSurjectiveRelation(domain_set,range_set)\n\n   def PyIsWellDefined(self) -> bool:\n      #print(\'Test_PySet.PyIsWellDefined\')\n      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)\n      return tmp_pyrel.PyIsWellDefined()\n\n   def PyIsFunction(self, domain_set : \'PySet[D]\', range_set : \'PySet[R]\') -> bool:\n      #print(\'Test_PySet.PyIsFunction\')\n      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)\n      return tmp_pyrel.PyIsFunction(domain_set,range_set)\n\n   def PyIsPartialFunction(self, domain_set : \'PySet[D]\', range_set : \'PySet[R]\') -> bool:\n      #print(\'Test_PySet.PyIsPartialFunction\')\n      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)\n      return tmp_pyrel.PyIsPartialFunction(domain_set,range_set)\n\n   def PyIsTotalFunction(self, domain_set : \'PySet[D]\', range_set : \'PySet[R]\') -> bool:\n      #print(\'Test_PySet.PyIsTotalFunction\')\n      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)\n      return tmp_pyrel.PyIsTotalFunction(domain_set,range_set)\n\n   def PyIsInjection(self) -> bool:\n      #print(\'Test_PySet.PyIsInjection\')\n      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)\n      return tmp_pyrel.PyIsInjection()\n\n   def PyIsPartialInjection(self, domain_set : \'PySet[D]\', range_set : \'PySet[R]\') -> bool:\n      #print(\'Test_PySet.PyIsPartialInjection\')\n      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)\n      return tmp_pyrel.PyIsPartialInjection(domain_set,range_set)\n\n   def PyIsTotalInjection(self, domain_set : \'PySet[D]\', range_set : \'PySet[R]\') -> bool:\n      #print(\'Test_PySet.PyIsTotalInjection\')\n      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)\n      return tmp_pyrel.PyIsTotalInjection(domain_set,range_set)\n\n   def PyIsPartialSurjection(self, domain_set : \'PySet[D]\', range_set : \'PySet[R]\') -> bool:\n      #print(\'Test_PySet.PyIsPartialSurjection\')\n      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)\n      return tmp_pyrel.PyIsPartialSurjection(domain_set,range_set)\n\n   def PyIsTotalSurjection(self, domain_set : \'PySet[D]\', range_set : \'PySet[R]\') -> bool:\n      #print(\'Test_PySet.PyIsTotalSurjection\')\n      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)\n      return tmp_pyrel.PyIsTotalSurjection(domain_set,range_set)\n\n   def PyIsBijection(self, domain_set : \'PySet[D]\', range_set : \'PySet[R]\') -> bool:\n      #print(\'Test_PySet.PyIsBijection\')\n      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)\n      return tmp_pyrel.PyIsBijection(domain_set,range_set)\n\n   def __call__(self, domain_element : D) -> R: #Apply method\n      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)\n      return tmp_pyrel.__call__(domain_element)\n\n\nclass PyCondSet(PySet[T]):\n\n   def __init__(self, funcContains : Callable[[T],bool] = PyBaseFunc.Unspecified_FuncBool1,\n                iterator_class : PyBaseIter = PyBaseIter(),\n                length_func : Callable[[],int] = PyBaseFunc.Unspecified_FuncInt0,\n                finite_func : Callable[[],bool] = PyBaseFunc.Unspecified_FuncBool0) -> None:\n      #print(\'Test_PyCondSet.__init__\')\n      self.__FuncContains : Callable[[T],bool] = funcContains\n      self.__IteratorClass : PyBaseIter = iterator_class\n      self.__LengthFunc : Callable[[],int] = length_func\n      self.__FiniteFunc : Callable[[],bool] = finite_func\n\n   def FuncContains(self) -> Callable[[T],bool]:\n      return self.__FuncContains\n\n   def IteratorClass(self) -> PyBaseIter:\n      return self.__IteratorClass\n\n   def LengthFunc(self) -> Callable[[],int]:\n      return self.__LengthFunc\n\n   def FiniteFunc(self) -> Callable[[],bool]:\n      return self.__FiniteFunc\n\n   def __str__(self) -> str:\n      return \'PyCondSet(\' + self.__FuncContains.__str__() + \')\'\n\n   def __repr__(self) -> str:\n      return \'PyCondSet(\' + self.__FuncContains.__str__() + \')\'\n\n   def __len__(self) -> int:\n      return self.__LengthFunc()\n\n   def __iter__(self) -> Iterator: #Necessary to be able to override __contains__\n      return self.__IteratorClass.__iter__()\n\n   def __eq__(self,other) -> bool:\n      if isinstance(other, PyCondSet_TreeExt):\n         raise Exception(\'Can not determine the result\')\n      elif isinstance(other, PyCondSet_Ext):\n         if other.FuncContains() == self.__FuncContains and len(other.FiniteInclusion()) == 0 and len(other.FiniteExclusion()) == 0:\n            return True\n      elif isinstance(other, PyCondSet):\n         if other.FuncContains() == self.__FuncContains:\n            return True\n      raise Exception(\'Can not determine the result\')\n\n   def __hash__(self):\n      return hash(self.__FuncContains)\n\n   # >> def __contains__(self,element : object) -> bool: #Inherited\n\n   def PyContains(self,element : T) -> bool:\n      #O(self.__FuncContains)\n      #print(\'Test_PyCondSet.PyContains\')\n      return self.__FuncContains(element)\n\n   # >> def PyNotContains(self,element : T) -> bool: #Inherited\n\n   def PyUnion(self, other : \'PySet[T]\') -> \'PySet[T]\':\n      #print(\'Test_PyCondSet.PyUnion\')\n\n      if isinstance(other, PyCondSet_TreeExt):\n         return other.PyUnion(self)\n      elif isinstance(other, PyCondSet_Ext):\n         return PyCondSet_TreeExt(funcContains = self.FuncContains()).PyUnion(other)\n      elif isinstance(other, PyCondSet):\n         return PyCondSet_TreeExt(funcContains = self.FuncContains()).PyUnion(other)\n      return other.PyUnion(self)\n\n   def PyIntersection(self, other : \'PySet[T]\') -> \'PySet[T]\':\n      #print(\'Test_PyCondSet.PyIntersection\')\n      \n      if isinstance(other, PyCondSet_TreeExt):\n         return other.PyIntersection(self)\n      elif isinstance(other, PyCondSet_Ext):\n         return PyCondSet_TreeExt(funcContains = self.FuncContains()).PyIntersection(other)\n      elif isinstance(other, PyCondSet):\n         return PyCondSet_TreeExt(funcContains = self.FuncContains()).PyIntersection(other)\n      return other.PyIntersection(self)\n\n   def PyDifference(self, other : \'PySet[T]\') -> \'PySet[T]\':\n      #print(\'Test_PyCondSet.PyDifference\')\n\n      if isinstance(other, PyCondSet_TreeExt):\n         return other.PyDifference(self)\n      elif isinstance(other, PyCondSet_Ext):\n         return PyCondSet_TreeExt(funcContains = self.FuncContains()).PyDifference(other)\n      elif isinstance(other, PyCondSet):\n         return PyCondSet_TreeExt(funcContains = self.FuncContains()).PyDifference(other)\n      return PyCondSet_TreeExt(funcContains = self.FuncContains(),finiteExclusion = other.FiniteInclusion())\n\n   # >> def PyCartesianProduct(self, other : \'PySet\') -> \'PyRel[T,Any]\': #Inherited + __iter__\n\n   # >> def PyIsSubset(self, other : \'PySet[T]\') -> bool: #Inherited + __iter__\n\n   # >> def PyNotSubset(self, other : \'PySet[T]\') -> bool: #Inherited + __iter__\n\n   # >> def PyIsProperSubset(self, other : \'PySet[T]\') -> bool: #Inherited + __iter__ + __len__\n\n   # >> def PyNotProperSubset(self, other : \'PySet[T]\') -> bool: #Inherited + __iter__ + __len__\n\n   def PyFinite(self) -> bool:\n      return self.__FiniteFunc()\n\n   def PyPartition(self, partition_sets : \'List[PySet[T]]\') -> bool:\n      raise Exception(\'Operation not supported for Implicit Sets\')\n\n   def PyPowerSet(self) -> PySet[PySet[T]]: #Unsupported\n      raise Exception(\'Operation not supported for Implicit Sets\')\n\n   def PyPowerSet1(self) -> PySet[PySet[T]]: #Unsupported\n      raise Exception(\'Operation not supported for Implicit Sets\')\n\n   def PyChoice(self) -> T: #Unsupported\n      #print(\'Test_PyCondSet.PyChoice\')\n      raise Exception(\'Operation not supported for Implicit Sets\')\n\n\nclass PyNAT(PyCondSet[int]):\n\n   def __init__(self) -> None:\n      #print(\'Test_PyNAT.__init__\')\n      self._PyCondSet__FuncContains : Callable[[int],bool] = PyBaseFunc.NAT_ContainsFunc\n      self._PyCondSet__IteratorClass : PyBaseIter = PyNAT_Iter()\n\n   def __str__(self) -> str:\n      return \'PyNAT()\'\n\n   def __repr__(self) -> str:\n      return \'PyNAT()\'\n\n   def __len__(self) -> int: #Unsupported\n      raise Exception(\'This set has no finite cardinality.\')\n\n   # >> def __iter__(self) -> Iterator: #Inherited\n\n   # >> def __eq__(self,other) -> bool: #Inherited\n\n   # >> def __hash__(self): #Inherited\n\n   # >> def __contains__(self,element : object) -> bool: #Inherited\n\n   # >> def PyContains(self,element : int) -> bool: #Inherited\n\n   # >> def PyNotContains(self,element : int) -> bool: #Inherited\n\n   def PyUnion(self, other : PySet[int]) -> PySet[int]:\n      #print(\'Test_PyNAT.PyUnion\')\n      if isinstance(other, PyNAT):\n         return PyNAT()\n      if isinstance(other, PyNAT1):\n         return PyNAT()\n      if isinstance(other, PyINT):\n         return PyINT()\n      return super().PyUnion(other)\n\n   def PyIntersection(self, other : PySet[int]) -> PySet[int]:\n      #print(\'Test_PyNAT.PyIntersection\')\n      if isinstance(other, PyNAT):\n         return PyNAT()\n      if isinstance(other, PyNAT1):\n         return PyNAT1()\n      if isinstance(other, PyINT):\n         return PyNAT()\n      return super().PyIntersection(other)\n\n   def PyDifference(self, other : PySet[int]) -> PySet[int]:\n      #print(\'Test_PyNAT.PyDifference\')\n      if isinstance(other, PyNAT):\n         return PySet()\n      if isinstance(other, PyNAT1):\n         return PySet({0})\n      if isinstance(other, PyINT):\n         return PySet()\n      return super().PyDifference(other)\n\n   def PyCartesianProduct(self, other : PySet[int]) -> \'PyRel[int,int]\':\n      #print(\'Test_PyNAT.PyCartesianProduct\')\n      if isinstance(other, PyNAT):\n         return PyNATXNAT()\n      return super().PyCartesianProduct(other)\n\n   def PyIsSubset(self, other : PySet[int]) -> bool:\n      #print(\'Test_PyNAT.PyIsSubset\')\n      if isinstance(other, PyNAT):\n         return True\n      if isinstance(other, PyNAT1):\n         return False\n      if isinstance(other, PyINT):\n         return True\n      if other.PyFinite():\n         return False\n      return super().PyIsSubset(other)\n\n   # >> def PyNotSubset(self, other : \'PySet[int]\') -> bool: #Inherited\n\n   def PyIsProperSubset(self, other : PySet[int]) -> bool:\n      #print(\'Test_PyNAT.PyIsProperSubset\')\n      if isinstance(other, PyNAT):\n         return False\n      if isinstance(other, PyNAT1):\n         return False\n      if isinstance(other, PyINT):\n         return True\n      if other.PyFinite():\n         return False\n      raise Exception(\'Can not determine the result\')\n\n   # >> def PyNotProperSubset(self, other : \'PySet[int]\') -> bool: #Inherited\n\n   def PyFinite(self) -> bool:\n      return False\n\n   # >> def PyPartition(self, partition_sets : \'List[PySet[int]]\') -> bool: #Inherited #Unsupported\n\n   def PyPowerSet(self) -> PySet[PySet[int]]:\n      return PyCondSet(PyBaseFunc.PNAT_ContainsFunc, finite_func = PyBaseFunc.ReturnFalse0)\n\n   def PyPowerSet1(self) -> PySet[PySet[int]]:\n      return PyCondSet(PyBaseFunc.P1NAT_ContainsFunc, finite_func = PyBaseFunc.ReturnFalse0)\n\n   def PyChoice(self) -> int:\n      #print(\'Test_PyNAT.PyChoice\')\n      return randint(0,P.RAND_INT_RANGE()[1])\n\n\nclass PyNAT1(PyCondSet[int]):\n\n   def __init__(self) -> None:\n      #print(\'Test_PyNAT1.__init__\')\n      self._PyCondSet__FuncContains : Callable[[int],bool] = PyBaseFunc.NAT1_ContainsFunc\n      self._PyCondSet__IteratorClass : PyBaseIter = PyNAT1_Iter()\n\n   def __str__(self) -> str:\n      return \'PyNAT1()\'\n\n   def __repr__(self) -> str:\n      return \'PyNAT1()\'\n\n   def __len__(self) -> int: #Unsupported\n      raise Exception(\'This set has no finite cardinality.\')\n\n   # >> def __iter__(self) -> Iterator: #Inherited\n\n   # >> def __eq__(self,other) -> bool: #Inherited\n\n   # >> def __hash__(self): #Inherited\n\n   # >> def __contains__(self,element : object) -> bool: #Inherited\n\n   # >> def PyContains(self,element : int) -> bool: #Inherited\n\n   # >> def PyNotContains(self,element : int) -> bool: #Inherited\n\n   def PyUnion(self, other : PySet[int]) -> PySet[int]:\n      #print(\'Test_PyNAT1.PyUnion\')\n      if isinstance(other, PyNAT):\n         return PyNAT()\n      if isinstance(other, PyNAT1):\n         return PyNAT1()\n      if isinstance(other, PyINT):\n         return PyINT()\n      return super().PyUnion(other)\n\n   def PyIntersection(self, other : PySet[int]) -> PySet[int]:\n      #print(\'Test_PyNAT1.PyIntersection\')\n      if isinstance(other, PyNAT):\n         return PyNAT1()\n      if isinstance(other, PyNAT1):\n         return PyNAT1()\n      if isinstance(other, PyINT):\n         return PyNAT1()\n      return super().PyIntersection(other)\n\n   def PyDifference(self, other : PySet[int]) -> PySet[int]:\n      #print(\'Test_PyNAT1.PyDifference\')\n      if isinstance(other, PyNAT):\n         return PySet()\n      if isinstance(other, PyNAT1):\n         return PySet()\n      if isinstance(other, PyINT):\n         return PySet()\n      return super().PyDifference(other)\n\n   # >> PyCartesianProduct(self, other : \'PySet\') -> \'PyRel[T,Any]\': #Inherited\n\n   def PyIsSubset(self, other : PySet[int]) -> bool:\n      #print(\'Test_PyNAT1.PyIsSubset\')\n      if isinstance(other, PyNAT):\n         return True\n      if isinstance(other, PyNAT1):\n         return True\n      if isinstance(other, PyINT):\n         return True\n      if other.PyFinite():\n         return False\n      return super().PyIsSubset(other)\n\n   # >> def PyNotSubset(self, other : \'PySet[int]\') -> bool: #Inherited\n\n   def PyIsProperSubset(self, other : PySet[int]) -> bool:\n      #print(\'Test_PyNAT1.PyIsProperSubset\')\n      if isinstance(other, PyNAT):\n         return True\n      if isinstance(other, PyNAT1):\n         return False\n      if isinstance(other, PyINT):\n         return True\n      if other.PyFinite():\n         return False\n      raise Exception(\'Can not determine the result\')\n\n   # >> def PyNotProperSubset(self, other : \'PySet[int]\') -> bool: #Inherited\n\n   def PyFinite(self) -> bool:\n      return False\n\n   # >> def PyPartition(self, partition_sets : \'List[PySet[int]]\') -> bool: #Inherited #Unsupported\n\n   def PyPowerSet(self) -> PySet[PySet[int]]:\n      return PyCondSet(PyBaseFunc.PNAT1_ContainsFunc, finite_func = PyBaseFunc.ReturnFalse0)\n\n   def PyPowerSet1(self) -> PySet[PySet[int]]:\n      return PyCondSet(PyBaseFunc.P1NAT1_ContainsFunc, finite_func = PyBaseFunc.ReturnFalse0)\n\n   def PyChoice(self) -> int:\n      #print(\'Test_PyNAT1.PyChoice\')\n      return randint(1,P.RAND_INT_RANGE()[1])\n\n\nclass PyINT(PyCondSet[int]):\n\n   def __init__(self) -> None:\n      #print(\'Test_PyINT.__init__\')\n      self._PyCondSet__FuncContains : Callable[[int],bool] = PyBaseFunc.INT_ContainsFunc\n      self._PyCondSet__IteratorClass : PyBaseIter = PyINT_Iter()\n\n   def __str__(self) -> str:\n      return \'PyINT()\'\n\n   def __repr__(self) -> str:\n      return \'PyINT()\'\n\n   def __len__(self) -> int: #Unsupported\n      raise Exception(\'This set has no finite cardinality.\')\n\n   # >> def __iter__(self) -> Iterator: #Inherited\n\n   # >> def __eq__(self,other) -> bool: #Inherited\n\n   # >> def __hash__(self): #Inherited\n\n   # >> def __contains__(self,element : object) -> bool: #Inherited\n\n   # >> def PyContains(self,element : int) -> bool: #Inherited\n\n   # >> def PyNotContains(self,element : int) -> bool: #Inherited\n\n   def PyUnion(self, other : PySet[int]) -> PySet[int]:\n      #print(\'Test_PyINT.PyUnion\')\n      if isinstance(other, PyNAT):\n         return PyINT()\n      if isinstance(other, PyNAT1):\n         return PyINT()\n      if isinstance(other, PyINT):\n         return PyINT()\n      return super().PyUnion(other)\n\n   def PyIntersection(self, other : PySet[int]) -> PySet[int]:\n      #print(\'Test_PyINT.PyIntersection\')\n      if isinstance(other, PyNAT):\n         return PyNAT()\n      if isinstance(other, PyNAT1):\n         return PyNAT1()\n      if isinstance(other, PyINT):\n         return PyINT()\n      return super().PyIntersection(other)\n\n   def PyDifference(self, other : PySet[int]) -> PySet[int]:\n      #print(\'Test_PyINT.PyDifference\')\n      if isinstance(other, PyINT):\n         return PySet()\n      return super().PyDifference(other)\n\n   def PyCartesianProduct(self, other : PySet[int]) -> \'PyRel[int,int]\':\n      #print(\'Test_PyINT.PyCartesianProduct\')\n      if isinstance(other, PyINT):\n         return PyINTXINT()\n      if isinstance(other, PyNAT):\n         return PyINTXNAT()\n      return super().PyCartesianProduct(other)\n\n   def PyIsSubset(self, other : PySet[int]) -> bool:\n      #print(\'Test_PyINT.PyIsSubset\')\n      if isinstance(other, PyNAT):\n         return False\n      if isinstance(other, PyNAT1):\n         return False\n      if isinstance(other, PyINT):\n         return True\n      if other.PyFinite():\n         return False\n      return super().PyIsSubset(other)\n\n   # >> def PyNotSubset(self, other : \'PySet[T]\') -> bool: #Inherited\n\n   def PyIsProperSubset(self, other : PySet[int]) -> bool:\n      #print(\'Test_PyINT.PyIsProperSubset\')\n      if isinstance(other, PyNAT):\n         return False\n      if isinstance(other, PyNAT1):\n         return False\n      if isinstance(other, PyINT):\n         return False\n      if other.PyFinite():\n         return False\n      raise Exception(\'Can not determine the result\')\n\n   # >> def PyNotProperSubset(self, other : \'PySet[int]\') -> bool: #Inherited\n\n   def PyFinite(self) -> bool:\n      return False\n\n   # >> def PyPartition(self, partition_sets : \'List[PySet[int]]\') -> bool: #Inherited #Unsupported\n\n   def PyPowerSet(self) -> PySet[PySet[int]]:\n      return PyCondSet(PyBaseFunc.PINT_ContainsFunc, finite_func = PyBaseFunc.ReturnFalse0)\n\n   def PyPowerSet1(self) -> PySet[PySet[int]]:\n      return PyCondSet(PyBaseFunc.P1INT_ContainsFunc, finite_func = PyBaseFunc.ReturnFalse0)\n\n   def PyChoice(self) -> int:\n      #print(\'Test_PyINT.PyChoice\')\n      return randint(P.RAND_INT_RANGE()[0],P.RAND_INT_RANGE()[1])\n\n\nclass PyCondSet_Ext(PyCondSet[T]):\n\n   def __init__(self, funcContains : Callable[[T],bool] = PyBaseFunc.Unspecified_FuncBool1,\n                finiteInclusion : Set[T] = set(),\n                finiteExclusion : Set[T] = set()) -> None:\n      #print(\'Test_PyCondSet_Ext.__init__\')\n      self._PyCondSet__FuncContains : Callable[[T],bool] #Necessary for mypy to recognize the attribute.\n      super().__init__(funcContains)\n      self.__FiniteInclusion : Set[T] = finiteInclusion\n      self.__FiniteExclusion : Set[T] = finiteExclusion\n\n   def FiniteInclusion(self) -> Set[T]:\n      return self.__FiniteInclusion.copy()\n\n   def FiniteExclusion(self) -> Set[T]:\n      return self.__FiniteExclusion.copy()\n\n   def __str__(self) -> str:\n      return \'PyCondSet_Ext(\' + self._PyCondSet__FuncContains.__str__() + \' \\nFiniteInclusion(\' + self.__FiniteInclusion.__str__() + \')\\nFiniteExclusion(\' + self.__FiniteExclusion.__str__() +\'}))\'\n\n   def __repr__(self) -> str:\n      return \'PyCondSet_Ext(\' + self._PyCondSet__FuncContains.__str__() + \' \\nFiniteInclusion(\' + self.__FiniteInclusion.__str__() + \')\\nFiniteExclusion(\' + self.__FiniteExclusion.__str__() +\'}))\'\n\n   def __len__(self) -> int: #Unsupported\n      raise Exception(\'Unsupported Operation for PyCondSet_Ext\')\n\n   def __iter__(self) -> Iterator: #Unsupported\n      raise Exception(\'Unsupported Operation for PyCondSet_Ext\')\n\n   def __eq__(self,other) -> bool:\n      if isinstance(other, PyCondSet_TreeExt):\n         raise Exception(\'Can not determine the result\')\n      elif isinstance(other, PyCondSet_Ext):\n         if other.FuncContains() == self._PyCondSet__FuncContains and other.FiniteInclusion() == self.__FiniteInclusion and other.FiniteExclusion() == self.__FiniteExclusion:\n            return True\n      elif isinstance(other, PyCondSet):\n         if other.FuncContains() == self._PyCondSet__FuncContains and len(self.__FiniteInclusion) == 0 and len(self.__FiniteExclusion) == 0:\n            return True\n      raise Exception(\'Can not determine the result\')\n\n   def __hash__(self): #Unsupported\n      raise Exception(\'Unsupported Operation for PyCondSet_Ext\')\n\n   # >> def __contains__(self,element : object) -> bool: #Inherited #Unsupported\n\n   def PyContains(self,element : T) -> bool:\n      #print(\'Test_PyCondSet_Ext.PyContains\')\n      #O(self.__FuncContains) + O(n)\n      if element in self.__FiniteInclusion:\n         return True\n      if element in self.__FiniteExclusion:\n         return False\n      return self._PyCondSet__FuncContains(element)\n\n   # >> def PyNotContains(self,element : T) -> bool: #Inherited\n\n   def PyUnion(self, other : \'PySet[T]\') -> \'PySet[T]\':\n      #print(\'Test_PyCondSet_Ext.PyUnion\')\n\n      if isinstance(other, PyCondSet_TreeExt):\n         return other.PyUnion(self)\n      elif isinstance(other, PyCondSet_Ext):\n         return PyCondSet_TreeExt(funcContains = self.FuncContains(),finiteInclusion = self.FiniteInclusion(),finiteExclusion = self.FiniteExclusion()).PyUnion(other)\n      elif isinstance(other, PyCondSet):\n         return other.PyUnion(self)\n      return other.PyUnion(self)\n\n   def PyIntersection(self, other : \'PySet[T]\') -> \'PySet[T]\':\n      #print(\'Test_PyCondSet_Ext.PyIntersection\')\n      \n      if isinstance(other, PyCondSet_TreeExt):\n         return other.PyIntersection(self)\n      elif isinstance(other, PyCondSet_Ext):\n         return PyCondSet_TreeExt(funcContains = self.FuncContains(),finiteInclusion = self.FiniteInclusion(),finiteExclusion = self.FiniteExclusion()).PyIntersection(other)\n      elif isinstance(other, PyCondSet):\n         return other.PyIntersection(self)\n      return other.PyIntersection(self)\n\n   def PyDifference(self, other : \'PySet[T]\') -> \'PySet[T]\':\n      #print(\'Test_PyCondSet_Ext.PyDifference\')\n\n      if isinstance(other, PyCondSet_TreeExt):\n         return other.PyDifference(self)\n      elif isinstance(other, PyCondSet_Ext):\n         return PyCondSet_TreeExt(funcContains = self.FuncContains(),finiteInclusion = self.FiniteInclusion(),finiteExclusion = self.FiniteExclusion()).PyDifference(other)\n      elif isinstance(other, PyCondSet):\n         return other.PyDifference(self)\n      return PyCondSet_TreeExt(self.FuncContains(),self.FiniteInclusion().difference(other.FiniteInclusion()),self.FiniteExclusion().union(other.FiniteInclusion()))\n\n   def PyCartesianProduct(self, other : \'PySet\') -> \'PyRel[T,Any]\': #Unsupported\n      raise Exception(\'Unsupported Operation for PyCondSet_Ext\')\n\n   def PyIsSubset(self, other : \'PySet[T]\') -> bool: #Unsupported\n      raise Exception(\'Unsupported Operation for PyCondSet_Ext\')\n\n   def PyNotSubset(self, other : \'PySet[T]\') -> bool: #Unsupported\n      raise Exception(\'Unsupported Operation for PyCondSet_Ext\')\n\n   def PyIsProperSubset(self, other : \'PySet[T]\') -> bool: #Unsupported\n      raise Exception(\'Unsupported Operation for PyCondSet_Ext\')\n\n   def PyNotProperSubset(self, other : \'PySet[T]\') -> bool: #Unsupported\n      raise Exception(\'Unsupported Operation for PyCondSet_Ext\')\n\n   def PyFinite(self) -> bool: #Unsupported\n      raise Exception(\'Unsupported Operation for PyCondSet_Ext\')\n\n   # >> def PyPartition(self, partition_sets : \'List[PySet[T]]\') -> bool: #Inherited #Unsupported\n\n   # >> def PyPowerSet(self) -> \'PySet[PySet[T]]\': #Inherited #Unsupported\n\n   # >> def PyPowerSet1(self) -> \'PySet[PySet[T]]\': #Inherited #Unsupported\n\n   # >> def PyChoice(self) -> T: #Inherited #Unsupported\n\n\nclass PyTreeNode_Default(Generic[T]):\n\n   def __init__(self, funcContains : Callable[[T],bool] = PyBaseFunc.Unspecified_FuncBool1,\n                finiteInclusion : Set[T] = set(),\n                finiteExclusion : Set[T] = set()) -> None:\n      #print(\'Test_PyTreeNode_Default.__init__\')\n      self.__NodePyCondSetExt : PyCondSet_Ext[T] = PyCondSet_Ext(funcContains,finiteInclusion,finiteExclusion)\n\n   def __str__(self) -> str:\n      return \'NodeDefault(\' + self.__NodePyCondSetExt.__str__() + \')\'\n\n   def __repr__(self) -> str:\n      return \'NodeDefault(\' + self.__NodePyCondSetExt.__str__() + \')\'\n\n   def PyContains(self,element : T) -> bool:\n      #O(self.__NodePyCondSetExt.PyContains)\n      #print(\'Test_PyTreeNode_Default.PyContains\')\n      return self.__NodePyCondSetExt.PyContains(element)\n\n\nclass PyTreeNode_Union(PyTreeNode_Default[T]):\n\n   def __init__(self, pyTreeNode_Left : PyTreeNode_Default[T],pyTreeNode_Right : PyTreeNode_Default) -> None:\n      #print(\'Test_PyTreeNode_Union.__init__\')\n      self.__PyTreeNode_Left : PyTreeNode_Default[T] = pyTreeNode_Left\n      self.__PyTreeNode_Right : PyTreeNode_Default[T] = pyTreeNode_Right\n\n   def __str__(self) -> str:\n      return \'NodeUnion(\' + self.__PyTreeNode_Left.__str__() + \'\\nUnion\\n\' + self.__PyTreeNode_Right.__str__() + \')\'\n\n   def __repr__(self) -> str:\n      return \'NodeUnion(\' + self.__PyTreeNode_Left.__str__() + \'\\nUnion\\n\' + self.__PyTreeNode_Right.__str__() + \')\'\n\n   def PyContains(self,element : T) -> bool:\n      #O(self.__PyTreeNode_Left.PyContains + self.__PyTreeNode_Right.PyContains)\n      #print(\'Test_PyTreeNode_Union.PyContains\')\n      return self.__PyTreeNode_Left.PyContains(element) or self.__PyTreeNode_Right.PyContains(element)\n\n\nclass PyTreeNode_Intersection(PyTreeNode_Default[T]):\n\n   def __init__(self, pyTreeNode_Left : PyTreeNode_Default[T], pyTreeNode_Right : PyTreeNode_Default) -> None:\n      #print(\'Test_PyTreeNode_Intersection.__init__\')\n      self.__PyTreeNode_Left : PyTreeNode_Default[T] = pyTreeNode_Left\n      self.__PyTreeNode_Right : PyTreeNode_Default[T] = pyTreeNode_Right\n\n   def __str__(self) -> str:\n      return \'NodeIntersection(\' + self.__PyTreeNode_Left.__str__() + \'\\nIntersection\\n\' + self.__PyTreeNode_Right.__str__() + \')\'\n\n   def __repr__(self) -> str:\n      return \'NodeIntersection(\' + self.__PyTreeNode_Left.__str__() + \'\\nIntersection\\n\' + self.__PyTreeNode_Right.__str__() + \')\'\n\n   def PyContains(self,element : T) -> bool:\n      #O(self.__PyTreeNode_Left.PyContains + self.__PyTreeNode_Right.PyContains)\n      #print(\'Test_PyTreeNode_Intersection.PyContains\')\n      return self.__PyTreeNode_Left.PyContains(element) and self.__PyTreeNode_Right.PyContains(element)\n\n\nclass PyTreeNode_Difference(PyTreeNode_Default[T]):\n\n   def __init__(self, pyTreeNode_Left : PyTreeNode_Default[T], pyTreeNode_Right : PyTreeNode_Default) -> None:\n      #print(\'Test_PyTreeNode_Difference.__init__\')\n      self.__PyTreeNode_Left : PyTreeNode_Default[T] = pyTreeNode_Left\n      self.__PyTreeNode_Right : PyTreeNode_Default[T] = pyTreeNode_Right\n\n   def __str__(self) -> str:\n      return \'NodeDifference(\' + self.__PyTreeNode_Left.__str__() + \'\\nDifference\\n\' + self.__PyTreeNode_Right.__str__() + \')\'\n\n   def __repr__(self) -> str:\n      return \'NodeDifference(\' + self.__PyTreeNode_Left.__str__() + \'\\nDifference\\n\' + self.__PyTreeNode_Right.__str__() + \')\'\n\n   def PyContains(self,element : T) -> bool:\n      #O(self.__PyTreeNode_Left.PyContains + self.__PyTreeNode_Right.PyContains)\n      #print(\'Test_PyTreeNode_Difference.PyContains\')\n      return self.__PyTreeNode_Left.PyContains(element) and not self.__PyTreeNode_Right.PyContains(element)\n\n\nclass PyCondSet_TreeExt(PyCondSet_Ext[T]):\n\n   def __init__(self, funcContains : Callable[[T],bool] = PyBaseFunc.Unspecified_FuncBool1,\n                finiteInclusion : Set[T] = set(),\n                finiteExclusion : Set[T] = set()) -> None:\n      #print(\'Test_PyCondSet_TreeExt.__init__\')\n      self.__TreeRoot : PyTreeNode_Default = PyTreeNode_Default(funcContains,finiteInclusion,finiteExclusion)\n\n   def TreeRoot(self) -> PyTreeNode_Default:\n      return deepcopy(self.__TreeRoot)\n\n   def __str__(self) -> str:\n      return \'PyCondSet_TreeExt(\' + self.__TreeRoot.__str__() + \')\'\n\n   def __repr__(self) -> str:\n      return \'PyCondSet_TreeExt(\' + self.__TreeRoot.__str__() + \')\'\n\n   def __len__(self) -> int: #Unsupported\n      raise Exception(\'Unsupported Operation for PyCondSet_TreeExt\')\n\n   def __iter__(self) -> Iterator: #Unsupported\n      raise Exception(\'Unsupported Operation for PyCondSet_TreeExt\')\n\n   def __eq__(self,other) -> bool:\n      if isinstance(other, PyCondSet_TreeExt):\n         return self.__TreeRoot == other.TreeRoot()\n      raise Exception(\'Can not determine the result\')\n\n   def __hash__(self): #Unsupported\n      raise Exception(\'Unsupported Operation for PyCondSet_TreeExt\')\n\n   # >> def __contains__(self,element : object) -> bool: #Inherited #Unsupported\n\n   def PyContains(self,element : T) -> bool:\n      #O(self.__TreeRoot.PyContains)\n      #print(\'Test_PyCondSet_TreeExt.PyContains\')\n      return self.__TreeRoot.PyContains(element)\n\n   # >> def PyNotContains(self,element : T) -> bool: #Inherited\n\n   def PyUnion(self, setRight : PySet[T]) -> PySet[T]:\n      #O()\n      #print(\'Test_PyCondSet_TreeExt.PyUnion\')\n\n      ans : PyCondSet_TreeExt[T]\n      nodeLeft : PyTreeNode_Default[T] = deepcopy(self.__TreeRoot)\n      nodeRight : PyTreeNode_Default[T]\n\n      if isinstance(setRight,PyCondSet_TreeExt):\n         nodeRight = deepcopy(setRight.__TreeRoot)\n\n      elif isinstance(setRight,PyCondSet_Ext):\n         nodeRight = PyTreeNode_Default(setRight.FuncContains(),setRight.FiniteInclusion(),setRight.FiniteExclusion())\n\n      elif isinstance(setRight,PyCondSet):\n         nodeRight = PyTreeNode_Default(setRight.FuncContains())\n\n      else:\n         nodeRight = PyTreeNode_Default(finiteInclusion = setRight.FiniteInclusion())\n\n      newNode : PyTreeNode_Union[T] = PyTreeNode_Union(nodeLeft,nodeRight)\n\n      ans = PyCondSet_TreeExt()\n      ans.setTreeRoot(newNode)\n\n      return ans\n\n   def PyIntersection(self, setRight : PySet[T]) -> PySet[T]:\n      #O()\n      #print(\'Test_PyCondSet_TreeExt.PyIntersection\')\n\n      ans : PyCondSet_TreeExt[T]\n      nodeLeft : PyTreeNode_Default[T]\n      nodeRight : PyTreeNode_Default[T]\n\n      if isinstance(setRight,PyCondSet_TreeExt):\n         \n         nodeLeft = deepcopy(self.__TreeRoot)\n         nodeRight = deepcopy(setRight.__TreeRoot)\n\n      elif isinstance(setRight,PyCondSet_Ext):\n\n         nodeLeft = deepcopy(self.__TreeRoot)\n         nodeRight = PyTreeNode_Default(setRight.FuncContains(),setRight.FiniteInclusion(),setRight.FiniteExclusion())\n\n      elif isinstance(setRight,PyCondSet):\n\n         nodeLeft = deepcopy(self.__TreeRoot)\n         nodeRight = PyTreeNode_Default(setRight.FuncContains())\n\n      else:\n\n         nodeLeft = deepcopy(self.__TreeRoot)\n         nodeRight = PyTreeNode_Default(finiteInclusion = setRight.FiniteInclusion())\n\n      newNode : PyTreeNode_Intersection[T] = PyTreeNode_Intersection(nodeLeft,nodeRight)\n\n      ans = PyCondSet_TreeExt()\n      ans.setTreeRoot(newNode)\n\n      return ans\n\n   def PyDifference(self, setRight : PySet[T]) -> PySet[T]:\n      #O()\n      #print(\'Test_PyCondSet_TreeExt.PyDifference\')\n\n      ans : PyCondSet_TreeExt[T]\n      nodeLeft : PyTreeNode_Default[T]\n      nodeRight : PyTreeNode_Default[T]\n\n      if isinstance(setRight,PyCondSet_TreeExt):\n         \n         nodeLeft = deepcopy(self.__TreeRoot)\n         nodeRight = deepcopy(setRight.__TreeRoot)\n\n      elif isinstance(setRight,PyCondSet_Ext):\n\n         nodeLeft = deepcopy(self.__TreeRoot)\n         nodeRight = PyTreeNode_Default(setRight.FuncContains(),setRight.FiniteInclusion(),setRight.FiniteExclusion())\n\n      elif isinstance(setRight,PyCondSet):\n\n         nodeLeft = deepcopy(self.__TreeRoot)\n         nodeRight = PyTreeNode_Default(setRight.FuncContains())\n\n      else:\n\n         nodeLeft = deepcopy(self.__TreeRoot)\n         nodeRight = PyTreeNode_Default(finiteInclusion = setRight.FiniteInclusion())\n\n      newNode : PyTreeNode_Difference[T] = PyTreeNode_Difference(nodeLeft,nodeRight)\n\n      ans = PyCondSet_TreeExt()\n      ans.setTreeRoot(newNode)\n\n      return ans\n\n   def PyCartesianProduct(self, other : \'PySet\') -> \'PyRel[T,Any]\': #Unsupported\n      raise Exception(\'Unsupported Operation for PyCondSet_TreeExt\')\n\n   def PyIsSubset(self, other : \'PySet[T]\') -> bool: #Unsupported\n      raise Exception(\'Unsupported Operation for PyCondSet_TreeExt\')\n\n   def PyNotSubset(self, other : \'PySet[T]\') -> bool: #Unsupported\n      raise Exception(\'Unsupported Operation for PyCondSet_TreeExt\')\n\n   def PyIsProperSubset(self, other : \'PySet[T]\') -> bool: #Unsupported\n      raise Exception(\'Unsupported Operation for PyCondSet_TreeExt\')\n\n   def PyNotProperSubset(self, other : \'PySet[T]\') -> bool: #Unsupported\n      raise Exception(\'Unsupported Operation for PyCondSet_TreeExt\')\n\n   def PyFinite(self) -> bool: #Unsupported\n      raise Exception(\'Unsupported Operation for PyCondSet_TreeExt\')\n\n   # >> def PyPartition(self, partition_sets : \'List[PySet[T]]\') -> bool: #Inherited #Unsupported\n\n   # >> def PyPowerSet(self) -> \'PySet[PySet[T]]\': #Inherited #Unsupported\n\n   # >> def PyPowerSet1(self) -> \'PySet[PySet[T]]\': #Inherited #Unsupported\n\n   # >> def PyChoice(self) -> T: #Inherited #Unsupported\n\n   def setTreeRoot(self, newRoot : PyTreeNode_Default[T]) -> None:\n      #O(1)\n      #print(\'Test_PyCondSet_TreeExt.setTreeRoot\')\n      self.__TreeRoot = newRoot\n\n\nclass PyRel(Generic[D,R]):\n\n   def __init__(self, initialElements : Set[Tuple[D,R]] = set())->None:\n      #print(\'Test_PyRel.__init__\')\n      self.__FiniteInclusion : Set[Tuple[D,R]] = initialElements\n\n   def FiniteInclusion(self) -> Set[Tuple[D,R]]:\n      return self.__FiniteInclusion.copy()\n\n   def __str__(self) -> str:\n      return \'PyRel(\' + self.__FiniteInclusion.__str__() + \')\'\n\n   def __repr__(self) -> str:\n      return \'PyRel(\' + self.__FiniteInclusion.__repr__() + \')\'\n\n   def __len__(self) -> int:\n      return len(self.__FiniteInclusion)\n\n   def __iter__(self) -> Iterator:\n      return self.__FiniteInclusion.__iter__()\n\n   def __eq__(self,other) -> bool:\n      if isinstance(other,PyCondRel) or isinstance(other,PyCondSet):\n         raise Exception(\'Operation not supported for implicit Rels\')\n      if isinstance(other,PyRel) or isinstance(other,PySet):\n         return self.__FiniteInclusion.__eq__(other.FiniteInclusion())\n      raise Exception(\'PySets should not operate with PyRels in this Operation\')\n\n   def __hash__(self):\n      return hash(frozenset(self.__FiniteInclusion))\n\n   def __contains__(self,element : object) -> bool: #Liskov Principle\n      raise Exception(\'Due to the Liskov Principle, TypeCheck will not work, use PyContains instead.\')\n\n   def PyContains(self,element : Tuple[D,R]) -> bool:\n      #O(1)\n      #print(\'Test_PyRel.PyContains\')\n      return self.__FiniteInclusion.__contains__(element)\n\n   def PyNotContains(self,element : Tuple[D,R]) -> bool:\n      #O(1)\n      #print(\'Test_PyRel.PyContains\')\n      return not self.PyContains(element)\n\n   def PyUnion(self, other : \'PyRel[D,R]\') -> \'PyRel[D,R]\':\n      #O(m+n) between PyRels.\n      #print(\'Test_PyRel.PyUnion\')\n      \n      if isinstance(other, PyCondRel):\n         raise Exception(\'Operation not supported for implicit PyRels\')\n      return PyRel(self.__FiniteInclusion.union(other.FiniteInclusion()))\n\n   def PyIntersection(self, other : \'PyRel[D,R]\') -> \'PyRel[D,R]\':\n      #O(n) when other is PyCondRel\n      #O(m+n) between PyRels.\n      #print(\'Test_PyRel.PyIntersection\')\n      \n      if isinstance(other, PyCondRel):\n         intersection_set : Set[Tuple[D,R]] = set()\n         for element in self:\n            if other.PyContains(element):\n               intersection_set.add(element)\n         return PyRel(intersection_set)\n      return PyRel(self.__FiniteInclusion.intersection(other.FiniteInclusion()))\n\n   def PyDifference(self, other : \'PyRel[D,R]\') -> \'PyRel[D,R]\':\n      #O(n) between PyRels.\n      #print(\'Test_PyRel.PyDifference\')\n\n      if isinstance(other, PyCondRel):\n         difference_set : Set[Tuple[D,R]] = self.FiniteInclusion()\n         for element in self:\n            if other.PyContains(element):\n               difference_set.discard(element)\n         return PyRel(difference_set)\n      return PyRel(self.__FiniteInclusion.difference(other.FiniteInclusion()))\n\n   def PyCartesianProduct(self, other : PySet) -> \'PyRel[Tuple[D,R],Any]\':\n      #O(m*n) between PySets.\n      #print(\'Test_PyRel.PyCartesianProduct\')\n      if isinstance(other, PyCondSet):\n         raise Exception(\'Operation only supported between iterable PySets\')\n      cartesian_product : Set[Tuple[Tuple[D,R],Any]] = set()\n      for self_ele in self:\n         for other_ele in other:\n            cartesian_product.add((self_ele, other_ele))\n      return PyRel(cartesian_product)\n\n   def PyIsSubset(self, other : \'PyRel[D,R]\') -> bool:\n      #O(n)\n      #print(\'Test_PyRel.PyIsSubset\')\n      for element in self:\n         if not(other.PyContains(element)):\n            return False\n      return True\n\n   def PyNotSubset(self, other : \'PyRel[D,R]\') -> bool:\n      #O(n)\n      #print(\'Test_PyRel.PyNotSubset\')\n      return not self.PyIsSubset(other)\n\n   def PyIsProperSubset(self, other : \'PyRel[D,R]\') -> bool:\n      #O(n)\n      #print(\'Test_PyRel.PyIsProperSubset\')\n      if len(self)==len(other):\n         return False\n      return self.PyIsSubset(other)\n\n   def PyNotProperSubset(self, other : \'PyRel[D,R]\') -> bool:\n      #O(n)\n      #print(\'Test_PyRel.PyNotProperSubset\')\n      return not self.PyIsProperSubset(other)\n\n   def PyFinite(self) -> bool:\n      #O(1)\n      #print(\'Test_PyRel.PyFinite\')\n      return True\n\n   def PyPartition(self, partition_rels : \'List[PyRel[D,R]]\') -> bool:\n      #print(\'Test_PyRel.PyPartition\')\n      checking_rel : PyRel[D,R] = PyRel()\n      for partition_rel in partition_rels:\n         if isinstance(partition_rel, PyCondRel):\n            raise Exception(\'Operation only supported between PyRels\')\n         if len(checking_rel.PyIntersection(partition_rel)) > 0:\n            return False\n         checking_rel = checking_rel.PyUnion(partition_rel)\n      if checking_rel.__eq__(self):\n         return True\n      return False\n\n   def PyPowerSet(self) -> \'PySet[PyRel[D,R]]\':\n      #print(\'Test_PyRel.PyPowerSet\')\n      elements_list : List[Tuple[D,R]] = list(self.FiniteInclusion())\n      power_set : Set[PyRel[D,R]] = set()\n      for rel_picker in range(2**len(self)):\n         current_rel : Set[Tuple[D,R]] = set()\n         for i in range(len(self)):\n            if rel_picker & 1<<i != 0:\n               current_rel.add(elements_list[i])\n         power_set.add(PyRel(current_rel))\n      return PySet(power_set)\n\n   def PyPowerSet1(self) -> \'PySet[PyRel[D,R]]\':\n      #print(\'Test_PyRel.PyPowerSet1\')\n      elements_list : List[Tuple[D,R]] = list(self.FiniteInclusion())\n      power_set : Set[PyRel[D,R]] = set()\n      for rel_picker in range(1,2**len(self)):\n         current_rel : Set[Tuple[D,R]] = set()\n         for i in range(len(self)):\n            if rel_picker & 1<<i != 0:\n               current_rel.add(elements_list[i])\n         power_set.add(PyRel(current_rel))\n      return PySet(power_set)\n\n   def PyChoice(self) -> Tuple[D,R]:\n      #print(\'Test_PySet.PyChoice\')\n      return choice(list(self.__FiniteInclusion))\n\n   def PyDomain(self) -> PySet[D]:\n      #print(\'Test_PyRel.PyDomain\')\n      domain_set : Set[D] = set()\n      for dom_ele,_ran_ele in self:\n         domain_set.add(dom_ele)\n      return PySet(domain_set)\n\n   def PyRange(self) -> PySet[R]:\n      #print(\'Test_PyRel.PyRange\')\n      range_set : Set[R] = set()\n      for _dom_ele,ran_ele in self:\n         range_set.add(ran_ele)\n      return PySet(range_set)\n\n   def PyComposition(self, other : \'PyRel[R,T]\') -> \'PyRel[D,T]\':\n      #print(\'Test_PyRel.PyComposition\')\n      new_relation : Set[Tuple[D,T]] = set()\n      for left_ele,right_ele in self:\n         relational_image : PySet[T] = other[PySet({right_ele})]\n         for range_element in relational_image:\n            new_relation.add((left_ele,range_element))\n      return PyRel(new_relation)\n\n   def PyBackwardComposition(self, other : \'PyRel[T,D]\') -> \'PyRel[T,R]\':\n      #print(\'Test_PyRel.PyBackwardComposition\')\n      return other.PyComposition(self)\n\n   def PyDomainRestriction(self, other : PySet[D]) -> \'PyRel[D,R]\':\n      #print(\'Test_PyRel.PyDomainRestriction\')\n      domain_restriction : Set[Tuple[D,R]] = set()\n      for tuple_element in self:\n         if other.PyContains(tuple_element[0]):\n            domain_restriction.add(tuple_element)\n      return PyRel(domain_restriction)\n\n   def PyRangeRestriction(self, other : PySet[R]) -> \'PyRel[D,R]\':\n      #print(\'Test_PyRel.PyRangeRestriction\')\n      range_restriction : Set[Tuple[D,R]] = set()\n      for tuple_element in self:\n         if other.PyContains(tuple_element[1]):\n            range_restriction.add(tuple_element)\n      return PyRel(range_restriction)\n\n   def PyDomainSubstraction(self, other : PySet[D]) -> \'PyRel[D,R]\':\n      #print(\'Test_PyRel.PyDomainSubstraction\')\n      domain_substraction : Set[Tuple[D,R]] = set()\n      for tuple_element in self:\n         if other.PyNotContains(tuple_element[0]):\n            domain_substraction.add(tuple_element)\n      return PyRel(domain_substraction)\n\n   def PyRangeSubstraction(self, other : PySet[R]) -> \'PyRel[D,R]\':\n      #print(\'Test_PyRel.PyRangeSubstraction\')\n      range_substraction : Set[Tuple[D,R]] = set()\n      for tuple_element in self:\n         if other.PyNotContains(tuple_element[1]):\n            range_substraction.add(tuple_element)\n      return PyRel(range_substraction)\n\n   def __invert__(self) -> \'PyRel[R,D]\': #Inverse Relation method\n      inverse_relation : Set[Tuple[R,D]] = set()\n      for dom_ele,ran_ele in self:\n         inverse_relation.add((ran_ele,dom_ele))\n      return PyRel(inverse_relation)\n\n   def __getitem__(self, keys : PySet[D]) -> PySet[R]: #Relational Image method\n      #O(range)\n      relational_image : Set[R] = set()\n      for left_ele,right_ele in self:\n         if keys.PyContains(left_ele):\n            relational_image.add(right_ele)\n      return PySet(relational_image)\n\n   def PyOverriding(self, other : \'PyRel[D,R]\') -> \'PyRel[D,R]\':\n      #print(\'Test_PyRel.PyOverriding\')\n      return other.PyUnion(self.PyDomainSubstraction(other.PyDomain()))\n\n   def PyDirectProduct(self, other : \'PyRel[D,T]\') -> \'PyRel[D,Tuple[R,T]]\':\n      #print(\'Test_PyRel.PyDirectProduct\')\n      direct_product : Set[Tuple[D,Tuple[R,T]]] = set()\n      for domain_element in self.PyDomain():\n         self_image : PySet[R] = self[PySet({domain_element})]\n         other_image : PySet[T] = other[PySet({domain_element})]\n         cartesian_product = self_image.PyCartesianProduct(other_image)\n         for cart_prod_tuple in cartesian_product:\n            direct_product.add((domain_element,cart_prod_tuple))\n      return PyRel(direct_product)\n\n   def PyIsTotal(self, domain_set : PySet[D]) -> bool:\n      #print(\'Test_PyRel.PyIsTotal\')\n      return self.PyDomain() == domain_set\n\n   def PyIsSurjection(self, range_set : PySet[R]) -> bool:\n      #print(\'Test_PyRel.PyIsSurjection\')\n      return self.PyRange() == range_set\n\n   def PyIsRelation(self, domain_set : PySet[D], range_set : PySet[R]) -> bool:\n      #print(\'Test_PyRel.PyIsRelation\')\n      return self.PyDomain().PyIsSubset(domain_set) and self.PyRange().PyIsSubset(range_set)\n\n   def PyIsTotalRelation(self, domain_set : PySet[D], range_set : PySet[R]) -> bool:\n      #print(\'Test_PyRel.PyIsTotalRelation\')\n      return self.PyIsRelation(domain_set,range_set) and self.PyIsTotal(domain_set)\n\n   def PyIsSurjectiveRelation(self, domain_set : PySet[D], range_set : PySet[R]) -> bool:\n      #print(\'Test_PyRel.PyIsSurjectiveRelation\')\n      return self.PyIsRelation(domain_set,range_set) and self.PyIsSurjection(range_set)\n\n   def PyIsTotalSurjectiveRelation(self, domain_set : PySet[D], range_set : PySet[R]) -> bool:\n      #print(\'Test_PyRel.PyIsTotalSurjectiveRelation\')\n      return self.PyIsTotalRelation(domain_set,range_set) and self.PyIsSurjection(range_set)\n\n   def PyIsWellDefined(self) -> bool:\n      #print(\'Test_PyRel.PyIsWellDefined\')\n      domain_elements : PySet[D] = self.PyDomain()\n      for dom_ele in domain_elements:\n         image_elements : PySet[R] = self[PySet({dom_ele})]\n         if len(image_elements)!=1:\n            return False\n      return True\n\n   def PyIsFunction(self, domain_set : PySet[D], range_set : PySet[R]) -> bool:\n      #print(\'Test_PyRel.PyIsFunction\')\n      return self.PyIsWellDefined() and self.PyIsRelation(domain_set, range_set)\n\n   def PyIsPartialFunction(self, domain_set : PySet[D], range_set : PySet[R]) -> bool:\n      #print(\'Test_PyRel.PyIsPartialFunction\')\n      return self.PyIsFunction(domain_set, range_set)\n\n   def PyIsTotalFunction(self, domain_set : PySet[D], range_set : PySet[R]) -> bool:\n      #print(\'Test_PyRel.PyIsTotalFunction\')\n      return self.PyIsFunction(domain_set, range_set) and self.PyIsTotal(domain_set)\n\n   def PyIsInjection(self) -> bool:\n      #print(\'Test_PyRel.PyIsInjection\')\n      inverse_rel = ~self\n      return inverse_rel.PyIsWellDefined()\n\n   def PyIsPartialInjection(self, domain_set : PySet[D], range_set : PySet[R]) -> bool:\n      #print(\'Test_PyRel.PyIsPartialInjection\')\n      return self.PyIsInjection() and self.PyIsPartialFunction(domain_set, range_set)\n\n   def PyIsTotalInjection(self, domain_set : PySet[D], range_set : PySet[R]) -> bool:\n      #print(\'Test_PyRel.PyIsTotalInjection\')\n      return self.PyIsInjection() and self.PyIsTotalFunction(domain_set, range_set)\n\n   def PyIsPartialSurjection(self, domain_set : PySet[D], range_set : PySet[R]) -> bool:\n      #print(\'Test_PyRel.PyIsPartialSurjection\')\n      return self.PyIsPartialFunction(domain_set, range_set) and self.PyIsSurjection(range_set)\n\n   def PyIsTotalSurjection(self, domain_set : PySet[D], range_set : PySet[R]) -> bool:\n      #print(\'Test_PyRel.PyIsTotalSurjection\')\n      return self.PyIsTotalFunction(domain_set, range_set) and self.PyIsSurjection(range_set)\n\n   def PyIsBijection(self, domain_set : PySet[D], range_set : PySet[R]) -> bool:\n      #print(\'Test_PyRel.PyIsBijection\')\n      return self.PyIsInjection() and self.PyIsTotalSurjection(domain_set,range_set)\n\n   def __call__(self, domain_element : D) -> R: #Apply method\n      for dom_elem, ran_elem in self:\n         if dom_elem == domain_element:\n            return ran_elem\n      raise Exception(\'This element had no image!\')\n\n\nclass PyCondRel(PyRel[D,R]):\n   \n   def __init__(self, relation_func : Callable[[PySet[D]],PySet[R]] = PyBaseFunc.Unspecified_FuncPySet1,\n                domain_set : PySet[D] = PyCondSet(),\n                range_set : PySet[R] = PyCondSet(),\n                inverse_func : Callable[[PySet[R]],PySet[D]] = PyBaseFunc.Unspecified_FuncPySet1) -> None:\n      #print(\'Test_PyCondRel.__init__\')\n      self.__RelationFunc : Callable[[PySet[D]],PySet[R]] = relation_func\n      self.__DomainSet : PySet[D] = domain_set\n      self.__RangeSet : PySet[R] = range_set\n      self.__InverseFunc : Callable[[PySet[R]],PySet[D]] = inverse_func\n\n   def RelationFunc(self) -> Callable[[PySet[D]],PySet[R]]:\n      return self.__RelationFunc\n\n   def DomainSet(self) -> PySet[D]:\n      return self.__DomainSet\n\n   def RangeSet(self) -> PySet[R]:\n      return self.__RangeSet\n\n   def InverseFunc(self) -> Callable[[PySet[R]],PySet[D]]:\n      return self.__InverseFunc\n\n   def __str__(self) -> str:\n      return \'PyCondRel(\' + self.__RelationFunc.__str__() + \' \\nDomainSet(\' + self.__DomainSet.__str__() + \')\\nRangeSet(\' + self.__RangeSet.__str__() +  \')\\nInverseFunc(\' + self.__InverseFunc.__str__() +\'))\'\n\n   def __repr__(self) -> str:\n      return \'PyCondRel(\' + self.__RelationFunc.__str__() + \' \\nDomainSet(\' + self.__DomainSet.__str__() + \')\\nRangeSet(\' + self.__RangeSet.__str__() +  \')\\nInverseFunc(\' + self.__InverseFunc.__str__() +\'))\'\n\n   def __len__(self) -> int: # + domain + relfunc\n      rel_length = 0\n      for dom_ele in self.PyDomain():\n         image_elems : PySet[R] = self[PySet({dom_ele})]\n         rel_length += len(image_elems)\n      return rel_length\n\n   def __iter__(self) -> Iterator: # + domain + relfunc\n      all_tuples : Set[Tuple[D,R]] = set()\n      for dom_ele in self.PyDomain():\n         image_elems : PySet[R] = self[PySet({dom_ele})]\n         for image_elem in image_elems:\n            all_tuples.add((dom_ele,image_elem))\n      return all_tuples.__iter__()\n\n   def __eq__(self,other) -> bool: # + all\n      if isinstance(other, PyCondRel):\n         if other.RelationFunc() == self.__RelationFunc and other.DomainSet() == self.__DomainSet and other.RangeSet() == self.__RangeSet:\n            return True\n      raise Exception(\'Can not determine the result\')\n\n   def __hash__(self):\n      return hash(self.__RelationFunc)\n\n   # >> def __contains__(self,element : object) -> bool: #Inherited\n\n   def PyContains(self,tuple_element : Tuple[D,R]) -> bool:\n      #O(self.__RelationFunc + len(domain_set))\n      #print(\'Test_PyCondRel.PyContains\')\n      preimage_element : D = tuple_element[0]\n      image_element : R = tuple_element[1]\n      image_elements : PySet[R] = self[PySet({preimage_element})]\n      return image_elements.PyContains(image_element)\n\n   # >> def PyNotContains(self,element : Tuple[D,R]) -> bool: #Inherited\n\n   def PyUnion(self, other : PyRel[D,R]) -> PyRel[D,R]: #Unsupported\n      raise Exception(\'Operation only supported between PyRels.\')\n\n   def PyIntersection(self, other : PyRel[D,R]) -> PyRel[D,R]: #Unsupported\n      if isinstance(other,PyCondRel):\n         raise Exception(\'Operation not supported between implicit PyRels!\')\n      return other.PyIntersection(self)\n\n   def PyDifference(self, other : PyRel[D,R]) -> PyRel[D,R]: #Unsupported\n      raise Exception(\'Operation only supported between PyRels.\')\n\n   # >> def PyCartesianProduct(self, other : PySet) -> PyRel[Tuple[D,R],Any]: #Inherited + __iter__\n\n   # >> def PyIsSubset(self, other : PyRel[D,R]) -> bool: #Inherited + __iter__\n\n   # >> def PyNotSubset(self, other : PyRel[D,R]) -> bool: #Inherited + __iter__\n\n   # >> def PyIsProperSubset(self, other : PyRel[D,R]) -> bool: #Inherited + __iter__ + __len__\n\n   # >> def PyNotProperSubset(self, other : PyRel[D,R]) -> bool: #Inherited + __iter__ + __len__\n\n   def PyFinite(self) -> bool:\n      return self.PyDomain().PyFinite() and self.PyRange().PyFinite()\n\n   def PyPartition(self, partition_rels : List[PyRel[D,R]]) -> bool: #Unsupported\n      raise Exception(\'Operation not supported for Implicit Rels\')\n\n   def PyPowerSet(self) -> PySet[PyRel[D,R]]: #Unsupported\n      raise Exception(\'Operation not supported for Implicit Rels\')\n\n   def PyPowerSet1(self) -> PySet[PyRel[D,R]]: #Unsupported\n      raise Exception(\'Operation not supported for Implicit Rels\')\n\n   def PyChoice(self) -> Tuple[D,R]: #Unsupported\n      #print(\'Test_PyCondRel.PyChoice\')\n      raise Exception(\'Operation not supported for Implicit Sets\')\n\n   def PyDomain(self) -> PySet[D]:\n      #O(1)\n      #print(\'Test_PyCondRel.PyDomain\')\n      return self.__DomainSet\n\n   def PyRange(self) -> PySet[R]:\n      #O(1)\n      #print(\'Test_PyCondRel.PyRange\')\n      return self.__RangeSet\n\n   # >> def PyComposition(self, other : \'PyRel[R,T]\') -> \'PyRel[D,T]\': #Inherited\n\n   # >> def PyBackwardComposition(self, other : \'PyRel[T,D]\') -> \'PyRel[T,R]\' #Inherited\n\n   # >> def PyDomainRestriction(self, other : PySet[D]) -> \'PyRel[D,R]\': #Inherited\n\n   # >> def PyRangeRestriction(self, other : PySet[R]) -> \'PyRel[D,R]\': #Inherited\n\n   # >> def PyDomainSubstraction(self, other : PySet[D]) -> \'PyRel[D,R]\': #Inherited\n\n   # >> def PyRangeSubstraction(self, other : PySet[R]) -> \'PyRel[D,R]\': #Inherited\n\n   def __invert__(self) -> \'PyCondRel[R,D]\': #Inverse Relation method\n      return PyCondRel(self.__InverseFunc,self.__RangeSet,self.__DomainSet,self.__RelationFunc)\n\n   def __getitem__(self, keys : PySet[D]) -> PySet[R]: #Relational Image method\n      #O(self.__RelationFunc)\n      return self.__RelationFunc(keys)\n\n   # >> def PyOverriding(self, other : \'PyRel[D,R]\') -> \'PyRel[D,R]\': #Inherited\n\n   # >> def PyDirectProduct(self, other : \'PyRel[D,T]\') -> \'PyRel[D,Tuple[R,T]]\': #Inherited\n\n   # >> def PyIsTotal(self, domain_set : PySet[D]) -> bool: #Inherited\n\n   # >> def PyIsSurjection(self, range_set : PySet[R]) -> bool: #Inherited\n\n   # >> def PyIsRelation(self, domain_set : PySet[D], range_set : PySet[R]) -> bool: #Inherited\n\n   # >> def PyIsTotalRelation(self, domain_set : PySet[D], range_set : PySet[R]) -> bool: #Inherited\n\n   # >> def PyIsSurjectiveRelation(self, domain_set : PySet[D], range_set : PySet[R]) -> bool: #Inherited\n\n   # >> def PyIsTotalSurjectiveRelation(self, domain_set : PySet[D], range_set : PySet[R]) -> bool: #Inherited\n\n   # >> def PyIsWellDefined(self) -> bool: #Inherited\n\n   # >> def PyIsFunction(self, domain_set : PySet[D], range_set : PySet[R]) -> bool: #Inherited\n\n   # >> def PyIsPartialFunction(self, domain_set : PySet[D], range_set : PySet[R]) -> bool: #Inherited\n\n   # >> def PyIsTotalFunction(self, domain_set : PySet[D], range_set : PySet[R]) -> bool: #Inherited\n\n   # >> def PyIsInjection(self) -> bool: #Inherited\n\n   # >> def PyIsPartialInjection(self, domain_set : PySet[D], range_set : PySet[R]) -> bool: #Inherited\n\n   # >> def PyIsTotalInjection(self, domain_set : PySet[D], range_set : PySet[R]) -> bool: #Inherited\n\n   # >> def PyIsPartialSurjection(self, domain_set : PySet[D], range_set : PySet[R]) -> bool: #Inherited\n\n   # >> def PyIsTotalSurjection(self, domain_set : PySet[D], range_set : PySet[R]) -> bool: #Inherited\n\n   # >> def PyIsBijection(self, domain_set : PySet[D], range_set : PySet[R]) -> bool: #Inherited\n\n   def __call__(self, domain_element : D) -> R: #Apply method\n      element_images : PySet[R] = self[PySet({domain_element})]\n      if len(element_images)==0:\n         raise Exception(\'This element has no images related to it\')\n      return list(element_images)[0]\n\n\nclass PyNATXNAT(PyCondRel[int,int]):\n\n   def __init__(self) -> None:\n      #print(\'Test_NATXNAT.__init__\')\n      self._PyCondRel__RelationFunc : Callable[[PySet[int]],PySet[int]] = PyBaseFunc.ReturnPyNAT_NAT\n      self._PyCondRel__DomainSet : PySet[int] = PyNAT()\n      self._PyCondRel__RangeSet : PySet[int] = PyNAT()\n      self._PyCondRel__InverseFunc : Callable[[PySet[int]],PySet[int]] = PyBaseFunc.ReturnPyNAT_NAT\n\n   def __str__(self) -> str:\n      return \'PyNATXNAT()\'\n   \n   def __repr__(self) -> str:\n      return \'PyNATXNAT()\'\n\n   def __len__(self) -> int: #Unsupported\n      raise Exception(\'This set has no finite cardinality.\')\n\n   # >> def __iter__(self) -> Iterator: #Inherited\n\n   # >> def __eq__(self,other) -> bool: #Inherited\n\n   # >> def __hash__(self): #Inherited\n\n   # >> def __contains__(self,element : object) -> bool: #Inherited\n\n   def PyContains(self,tuple_element : Tuple[int,int]) -> bool:\n      #O(1)\n      #print(\'Test_PyNATXNAT.PyContains\')\n      if tuple_element[0] >= 0 and tuple_element[1] >=0:\n         return True\n      return False\n\n   # >> def PyNotContains(self,element : Tuple[int,int]) -> bool: #Inherited\n\n   def PyUnion(self, other : PyRel[int,int]) -> PyRel[int,int]:\n      #print(\'Test_PyNATXNAT.PyUnion\')\n      if isinstance(other, PyNATXNAT):\n         return PyNATXNAT()\n      if isinstance(other, PyINTXINT):\n         return PyINTXINT()\n      if isinstance(other, PyINTXNAT):\n         return PyINTXNAT()\n      raise Exception(\'Can not determine the result\')\n\n   def PyIntersection(self, other : PyRel[int,int]) -> PyRel[int,int]:\n      #print(\'Test_PyNATXNAT.PyIntersection\')\n      if isinstance(other, PyNATXNAT):\n         return PyNATXNAT()\n      if isinstance(other, PyINTXINT):\n         return PyNATXNAT()\n      if isinstance(other, PyINTXNAT):\n         return PyNATXNAT()\n      return super().PyIntersection(other)\n\n   def PyDifference(self, other : PyRel[int,int]) -> PyRel[int,int]:\n      #print(\'Test_PyNATXNAT.PyDifference\')\n      if isinstance(other, PyNATXNAT):\n         return PyRel()\n      if isinstance(other, PyINTXINT):\n         return PyRel()\n      if isinstance(other, PyINTXNAT):\n         return PyRel()\n      raise Exception(\'Can not determine the result\')\n\n   # >> def PyCartesianProduct(self, other : PySet) -> PyRel[Tuple[int,int],Any]: #Inherited\n\n   def PyIsSubset(self, other : PyRel[int,int]) -> bool:\n      #print(\'Test_PyNATXNAT.PyIsSubset\')\n      if isinstance(other, PyNATXNAT):\n         return True\n      if isinstance(other, PyINTXINT):\n         return True\n      if isinstance(other, PyINTXNAT):\n         return True\n      if other.PyFinite():\n         return False\n      return super().PyIsSubset(other)\n\n   # >> def PyNotSubset(self, other : PyRel[int,int]) -> bool: #Inherited\n\n   def PyIsProperSubset(self, other : PyRel[int,int]) -> bool:\n      #print(\'Test_PyNATXNAT.PyIsProperSubset\')\n      if isinstance(other, PyNATXNAT):\n         return False\n      if isinstance(other, PyINTXINT):\n         return True\n      if isinstance(other, PyINTXNAT):\n         return True\n      if other.PyFinite():\n         return False\n      raise Exception(\'Can not determine the result\')\n\n   # >> def PyNotProperSubset(self, other : PyRel[int,int]) -> bool: #Inherited\n\n   def PyFinite(self) -> bool:\n      return False\n\n   # >> def PyPartition(self, partition_sets : List[PyRel[int,int]]) -> bool: #Inherited #Unsupported\n\n   def PyPowerSet(self) -> PySet[PyRel[int,int]]:\n      return PyCondSet(PyBaseFunc.PNATXNAT_ContainsFunc, finite_func = PyBaseFunc.ReturnFalse0)\n\n   def PyPowerSet1(self) -> PySet[PyRel[int,int]]:\n      return PyCondSet(PyBaseFunc.P1NATXNAT_ContainsFunc, finite_func = PyBaseFunc.ReturnFalse0)\n\n   def PyChoice(self) -> Tuple[int,int]:\n      #print(\'Test_PyNATXNAT.PyChoice\')\n      return (randint(0,P.RAND_INT_RANGE()[1]),randint(0,P.RAND_INT_RANGE()[1]))\n\n   # >> def PyDomain(self) -> PySet[int]: #Inherited\n\n   # >> def PyRange(self) -> PySet[int]: #Inherited\n\n   # >> def PyComposition(self, other : \'PyRel[int,int]\') -> \'PyRel[int,int]\': #Inherited\n\n   # >> def PyBackwardComposition(self, other : \'PyRel[int,int]\') -> \'PyRel[int,int]\' #Inherited\n\n   # >> def PyDomainRestriction(self, other : PySet[int]) -> \'PyRel[int,int]\': #Inherited\n\n   # >> def PyRangeRestriction(self, other : PySet[int]) -> \'PyRel[int,int]\': #Inherited\n\n   # >> def PyDomainSubstraction(self, other : PySet[int]) -> \'PyRel[int,int]\': #Inherited\n\n   # >> def PyRangeSubstraction(self, other : PySet[int]) -> \'PyRel[int,int]\': #Inherited\n\n   # >> def __invert__(self) -> \'PyCondRel[int,int]\': #Inherited\n\n   # >> def __getitem__(self, keys : PySet[int]) -> PySet[R]: #Inherited\n\n   # >> def PyOverriding(self, other : \'PyRel[int,int]\') -> \'PyRel[int,int]\': #Inherited\n\n   # >> def PyDirectProduct(self, other : \'PyRel[int,int]\') -> \'PyRel[int,Tuple[int,int]]\': #Inherited\n\n   # >> def PyIsTotal(self, domain_set : PySet[int]) -> bool: #Inherited\n\n   # >> def PyIsSurjection(self, range_set : PySet[int]) -> bool: #Inherited\n\n   # >> def PyIsRelation(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited\n\n   # >> def PyIsTotalRelation(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited\n\n   # >> def PyIsSurjectiveRelation(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited\n\n   # >> def PyIsTotalSurjectiveRelation(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited\n\n   def PyIsWellDefined(self) -> bool:\n      return False\n\n   # >> def PyIsFunction(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited\n\n   # >> def PyIsPartialFunction(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited\n\n   # >> def PyIsTotalFunction(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited\n\n   def PyIsInjection(self) -> bool:\n      return False\n\n   # >> def PyIsPartialInjection(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited\n\n   # >> def PyIsTotalInjection(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited\n\n   # >> def PyIsPartialSurjection(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited\n\n   # >> def PyIsTotalSurjection(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited\n\n   # >> def PyIsBijection(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited\n\n   # >> def __call__(self, domain_element : int) -> R: #Inherited\n\n\nclass PyINTXINT(PyCondRel[int,int]):\n\n   def __init__(self) -> None:\n      #print(\'Test_INTXINT.__init__\')\n      self._PyCondRel__RelationFunc : Callable[[PySet[int]],PySet[int]] = PyBaseFunc.ReturnPyINT_1\n      self._PyCondRel__DomainSet : PySet[int] = PyINT()\n      self._PyCondRel__RangeSet : PySet[int] = PyINT()\n      self._PyCondRel__InverseFunc : Callable[[PySet[int]],PySet[int]] = PyBaseFunc.ReturnPyINT_1\n\n   def __str__(self) -> str:\n      return \'PyINTXINT()\'\n\n   def __repr__(self) -> str:\n      return \'PyINTXINT()\'\n\n   def __len__(self) -> int: #Unsupported\n      raise Exception(\'This set has no finite cardinality.\')\n\n   # >> def __iter__(self) -> Iterator: #Inherited\n\n   # >> def __eq__(self,other) -> bool: #Inherited\n\n   # >> def __hash__(self): #Inherited\n\n   # >> def __contains__(self,element : object) -> bool: #Inherited\n\n   def PyContains(self,tuple_element : Tuple[int,int]) -> bool:\n      #O(1)\n      #print(\'Test_PyINTXINT.PyContains\')\n      if isinstance(tuple_element[0],int) and isinstance(tuple_element[1],int):\n         return True\n      return False\n\n   # >> def PyNotContains(self,element : Tuple[int,int]) -> bool: #Inherited\n\n   def PyUnion(self, other : PyRel[int,int]) -> PyRel[int,int]:\n      #print(\'Test_PyINTXINT.PyUnion\')\n      if isinstance(other, PyNATXNAT):\n         return PyINTXINT()\n      if isinstance(other, PyINTXINT):\n         return PyINTXINT()\n      if isinstance(other, PyINTXNAT):\n         return PyINTXINT()\n      raise Exception(\'Can not determine the result\')\n\n   def PyIntersection(self, other : PyRel[int,int]) -> PyRel[int,int]:\n      #print(\'Test_PyINTXINT.PyIntersection\')\n      if isinstance(other, PyNATXNAT):\n         return PyNATXNAT()\n      if isinstance(other, PyINTXINT):\n         return PyINTXINT()\n      if isinstance(other, PyINTXNAT):\n         return PyINTXNAT()\n      return super().PyIntersection(other)\n\n   def PyDifference(self, other : PyRel[int,int]) -> PyRel[int,int]:\n      #print(\'Test_PyINTXINT.PyDifference\')\n      if isinstance(other, PyINTXINT):\n         return PyRel()\n      raise Exception(\'Can not determine the result\')\n\n   # >> def PyCartesianProduct(self, other : PySet) -> PyRel[Tuple[int,int],Any]: #Inherited\n\n   def PyIsSubset(self, other : PyRel[int,int]) -> bool:\n      #print(\'Test_PyINTXINT.PyIsSubset\')\n      if isinstance(other, PyNATXNAT):\n         return False\n      if isinstance(other, PyINTXINT):\n         return True\n      if isinstance(other, PyINTXNAT):\n         return False\n      if other.PyFinite():\n         return False\n      return super().PyIsSubset(other)\n\n   # >> def PyNotSubset(self, other : PyRel[int,int]) -> bool: #Inherited\n\n   def PyIsProperSubset(self, other : PyRel[int,int]) -> bool:\n      #print(\'Test_PyINTXINT.PyIsProperSubset\')\n      if isinstance(other, PyNATXNAT):\n         return False\n      if isinstance(other, PyINTXINT):\n         return False\n      if isinstance(other, PyINTXNAT):\n         return False\n      if other.PyFinite():\n         return False\n      raise Exception(\'Can not determine the result\')\n\n   # >> def PyNotProperSubset(self, other : PyRel[int,int]) -> bool: #Inherited\n\n   def PyFinite(self) -> bool:\n      return False\n\n   # >> def PyPartition(self, partition_sets : List[PyRel[int,int]]) -> bool: #Inherited #Unsupported\n\n   def PyPowerSet(self) -> PySet[PyRel[int,int]]:\n      return PyCondSet(PyBaseFunc.PINTXINT_ContainsFunc, finite_func = PyBaseFunc.ReturnFalse0)\n\n   def PyPowerSet1(self) -> PySet[PyRel[int,int]]:\n      return PyCondSet(PyBaseFunc.P1INTXINT_ContainsFunc, finite_func = PyBaseFunc.ReturnFalse0)\n\n   def PyChoice(self) -> Tuple[int,int]:\n      #print(\'Test_PyINTXINT.PyChoice\')\n      return (randint(P.RAND_INT_RANGE()[0],P.RAND_INT_RANGE()[1]),randint(P.RAND_INT_RANGE()[0],P.RAND_INT_RANGE()[1]))\n\n   # >> def PyDomain(self) -> PySet[int]: #Inherited\n\n   # >> def PyRange(self) -> PySet[int]: #Inherited\n\n   # >> def PyComposition(self, other : \'PyRel[int,int]\') -> \'PyRel[int,int]\': #Inherited\n\n   # >> def PyBackwardComposition(self, other : \'PyRel[int,int]\') -> \'PyRel[int,int]\' #Inherited\n\n   # >> def PyDomainRestriction(self, other : PySet[int]) -> \'PyRel[int,int]\': #Inherited\n\n   # >> def PyRangeRestriction(self, other : PySet[int]) -> \'PyRel[int,int]\': #Inherited\n\n   # >> def PyDomainSubstraction(self, other : PySet[int]) -> \'PyRel[int,int]\': #Inherited\n\n   # >> def PyRangeSubstraction(self, other : PySet[int]) -> \'PyRel[int,int]\': #Inherited\n\n   # >> def __invert__(self) -> \'PyCondRel[int,int]\': #Inherited\n\n   # >> def __getitem__(self, keys : PySet[int]) -> PySet[R]: #Inherited\n\n   # >> def PyOverriding(self, other : \'PyRel[int,int]\') -> \'PyRel[int,int]\': #Inherited\n\n   # >> def PyDirectProduct(self, other : \'PyRel[int,int]\') -> \'PyRel[int,Tuple[int,int]]\': #Inherited\n\n   # >> def PyIsTotal(self, domain_set : PySet[int]) -> bool: #Inherited\n\n   # >> def PyIsSurjection(self, range_set : PySet[int]) -> bool: #Inherited\n\n   # >> def PyIsRelation(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited\n\n   # >> def PyIsTotalRelation(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited\n\n   # >> def PyIsSurjectiveRelation(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited\n\n   # >> def PyIsTotalSurjectiveRelation(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited\n\n   def PyIsWellDefined(self) -> bool:\n      return False\n\n   # >> def PyIsFunction(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited\n\n   # >> def PyIsPartialFunction(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited\n\n   # >> def PyIsTotalFunction(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited\n\n   def PyIsInjection(self) -> bool:\n      return False\n\n   # >> def PyIsPartialInjection(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited\n\n   # >> def PyIsTotalInjection(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited\n\n   # >> def PyIsPartialSurjection(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited\n\n   # >> def PyIsTotalSurjection(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited\n\n   # >> def PyIsBijection(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited\n\n   # >> def __call__(self, domain_element : int) -> R: #Inherited\n\n\nclass PyINTXNAT(PyCondRel[int,int]):\n\n   def __init__(self) -> None:\n      #print(\'Test_INTXNAT.__init__\')\n      self._PyCondRel__RelationFunc : Callable[[PySet[int]],PySet[int]] = PyBaseFunc.ReturnPyNAT_1\n      self._PyCondRel__DomainSet : PySet[int] = PyINT()\n      self._PyCondRel__RangeSet : PySet[int] = PyNAT()\n      self._PyCondRel__InverseFunc : Callable[[PySet[int]],PySet[int]] = PyBaseFunc.ReturnPyNAT_INT\n\n   def __str__(self) -> str:\n      return \'PyINTXNAT()\'\n\n   def __repr__(self) -> str:\n      return \'PyINTXNAT()\'\n\n   def __len__(self) -> int: #Unsupported\n      raise Exception(\'This set has no finite cardinality.\')\n\n   # >> def __iter__(self) -> Iterator: #Inherited\n\n   # >> def __eq__(self,other) -> bool: #Inherited\n\n   # >> def __hash__(self): #Inherited\n\n   # >> def __contains__(self,element : object) -> bool: #Inherited\n\n   def PyContains(self,tuple_element : Tuple[int,int]) -> bool:\n      #O(1)\n      #print(\'Test_PyINTXNAT.PyContains\')\n      if isinstance(tuple_element[0],int) and tuple_element[1] >=0:\n         return True\n      return False\n\n   # >> def PyNotContains(self,element : Tuple[int,int]) -> bool: #Inherited\n\n   def PyUnion(self, other : PyRel[int,int]) -> PyRel[int,int]:\n      #print(\'Test_PyINTXNAT.PyUnion\')\n      if isinstance(other, PyNATXNAT):\n         return PyINTXNAT()\n      if isinstance(other, PyINTXINT):\n         return PyINTXINT()\n      if isinstance(other, PyINTXNAT):\n         return PyINTXNAT()\n      raise Exception(\'Can not determine the result\')\n\n   def PyIntersection(self, other : PyRel[int,int]) -> PyRel[int,int]:\n      #print(\'Test_PyINTXNAT.PyIntersection\')\n      if isinstance(other, PyNATXNAT):\n         return PyNATXNAT()\n      if isinstance(other, PyINTXINT):\n         return PyINTXNAT()\n      if isinstance(other, PyINTXNAT):\n         return PyINTXNAT()\n      return super().PyIntersection(other)\n\n   def PyDifference(self, other : PyRel[int,int]) -> PyRel[int,int]:\n      #print(\'Test_PyINTXNAT.PyDifference\')\n      if isinstance(other, PyINTXINT):\n         return PyRel()\n      if isinstance(other, PyINTXNAT):\n         return PyRel()\n      raise Exception(\'Can not determine the result\')\n\n   def PyCartesianProduct(self, other : PySet) -> PyRel[Tuple[int,int],Any]: #Unsupported\n      raise Exception(\'Operation not supported\')\n\n   def PyIsSubset(self, other : PyRel[int,int]) -> bool:\n      #print(\'Test_PyINTXNAT.PyIsSubset\')\n      if isinstance(other, PyNATXNAT):\n         return False\n      if isinstance(other, PyINTXINT):\n         return True\n      if isinstance(other, PyINTXNAT):\n         return True\n      if other.PyFinite():\n         return False\n      return super().PyIsSubset(other)\n\n   # >> def PyNotSubset(self, other : PyRel[int,int]) -> bool: #Inherited\n\n   def PyIsProperSubset(self, other : PyRel[int,int]) -> bool:\n      #print(\'Test_PyINTXNAT.PyIsProperSubset\')\n      if isinstance(other, PyNATXNAT):\n         return False\n      if isinstance(other, PyINTXINT):\n         return True\n      if isinstance(other, PyINTXNAT):\n         return False\n      if other.PyFinite():\n         return False\n      raise Exception(\'Can not determine the result\')\n\n   # >> def PyNotProperSubset(self, other : PyRel[int,int]) -> bool: #Inherited\n\n   def PyFinite(self) -> bool:\n      return False\n\n   # >> def PyPartition(self, partition_sets : List[PyRel[int,int]]) -> bool: #Inherited #Unsupported\n\n   def PyPowerSet(self) -> PySet[PyRel[int,int]]:\n      return PyCondSet(PyBaseFunc.PINTXNAT_ContainsFunc, finite_func = PyBaseFunc.ReturnFalse0)\n\n   def PyPowerSet1(self) -> PySet[PyRel[int,int]]:\n      return PyCondSet(PyBaseFunc.P1INTXNAT_ContainsFunc, finite_func = PyBaseFunc.ReturnFalse0)\n\n   def PyChoice(self) -> Tuple[int,int]:\n      #print(\'Test_PyINTXNAT.PyChoice\')\n      return (randint(P.RAND_INT_RANGE()[0],P.RAND_INT_RANGE()[1]),randint(0,P.RAND_INT_RANGE()[1]))\n\n   # >> def PyDomain(self) -> PySet[int]: #Inherited\n\n   # >> def PyRange(self) -> PySet[int]: #Inherited\n\n   # >> def PyComposition(self, other : \'PyRel[int,int]\') -> \'PyRel[int,int]\': #Inherited\n\n   # >> def PyBackwardComposition(self, other : \'PyRel[int,int]\') -> \'PyRel[int,int]\' #Inherited\n\n   # >> def PyDomainRestriction(self, other : PySet[int]) -> \'PyRel[int,int]\': #Inherited\n\n   # >> def PyRangeRestriction(self, other : PySet[int]) -> \'PyRel[int,int]\': #Inherited\n\n   # >> def PyDomainSubstraction(self, other : PySet[int]) -> \'PyRel[int,int]\': #Inherited\n\n   # >> def PyRangeSubstraction(self, other : PySet[int]) -> \'PyRel[int,int]\': #Inherited\n\n   # >> def __invert__(self) -> \'PyCondRel[int,int]\': #Inherited\n\n   # >> def __getitem__(self, keys : PySet[int]) -> PySet[R]: #Inherited\n\n   # >> def PyOverriding(self, other : \'PyRel[int,int]\') -> \'PyRel[int,int]\': #Inherited\n\n   # >> def PyDirectProduct(self, other : \'PyRel[int,int]\') -> \'PyRel[int,Tuple[int,int]]\': #Inherited\n\n   # >> def PyIsTotal(self, domain_set : PySet[int]) -> bool: #Inherited\n\n   # >> def PyIsSurjection(self, range_set : PySet[int]) -> bool: #Inherited\n\n   # >> def PyIsRelation(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited\n\n   # >> def PyIsTotalRelation(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited\n\n   # >> def PyIsSurjectiveRelation(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited\n\n   # >> def PyIsTotalSurjectiveRelation(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited\n\n   def PyIsWellDefined(self) -> bool:\n      return False\n\n   # >> def PyIsFunction(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited\n\n   # >> def PyIsPartialFunction(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited\n\n   # >> def PyIsTotalFunction(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited\n\n   def PyIsInjection(self) -> bool:\n      return False\n\n   # >> def PyIsPartialInjection(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited\n\n   # >> def PyIsTotalInjection(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited\n\n   # >> def PyIsPartialSurjection(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited\n\n   # >> def PyIsTotalSurjection(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited\n\n   # >> def PyIsBijection(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited\n\n   # >> def __call__(self, domain_element : int) -> R: #Inherited\n\n\nclass PyID(PyCondRel):\n\n   def __init__(self) -> None:\n      #print(\'Test_ID.__init__\')\n      self._PyCondRel__RelationFunc : Callable[[PySet],PySet] = PyBaseFunc.ID_Rel_Func\n      self._PyCondRel__DomainSet : PySet = PyCondSet()\n      self._PyCondRel__RangeSet : PySet = PyCondSet()\n      self._PyCondRel__InverseFunc : Callable[[PySet],PySet] = PyBaseFunc.ID_Rel_Func\n\n   def __str__(self) -> str:\n      return \'PyID()\'\n   \n   def __repr__(self) -> str:\n      return \'PyID()\'\n\n   def __len__(self) -> int: #Unsupported\n      raise Exception(\'Unsupported Operation for PyID.\')\n\n   def __iter__(self) -> Iterator: #Unsupported\n      raise Exception(\'Unsupported Operation for PyID.\')\n\n   def __eq__(self,other) -> bool: #Unsupported\n      raise Exception(\'Unsupported Operation for PyID.\')\n\n   def __hash__(self): #Unsupported\n      raise Exception(\'Unsupported Operation for PyID.\')\n\n   # >> def __contains__(self,element : object) -> bool: #Inherited\n\n   def PyContains(self,tuple_element : Tuple) -> bool:\n      #O(1)\n      #print(\'Test_PyID.PyContains\')\n      if tuple_element[0] == tuple_element[1]:\n         return True\n      return False\n\n   # >> def PyNotContains(self,element : Tuple) -> bool: #Inherited\n\n   def PyUnion(self, other : PyRel) -> PyRel: #Unsupported\n      raise Exception(\'Can not determine the result\')\n\n   def PyIntersection(self, other : PyRel) -> PyRel:\n      return super().PyIntersection(other)\n\n   def PyDifference(self, other : PyRel) -> PyRel: #Unsupported\n      raise Exception(\'Can not determine the result\')\n\n   def PyCartesianProduct(self, other : PySet) -> PyRel[Tuple[Any,Any],Any]: #Unsupported\n      raise Exception(\'Can not determine the result\')\n\n   def PyIsSubset(self, other : PyRel) -> bool: #Unsupported\n      raise Exception(\'Can not determine the result\')\n\n   # >> def PyNotSubset(self, other : PyRel) -> bool: #Inherited #Unsupported\n\n   def PyIsProperSubset(self, other : PyRel) -> bool: #Unsupported\n      raise Exception(\'Can not determine the result\')\n\n   # >> def PyNotProperSubset(self, other : PyRel) -> bool: #Inherited #Unsupported\n\n   def PyFinite(self) -> bool:\n      return False\n\n   # >> def PyPartition(self, partition_sets : List[PyRel]) -> bool: #Inherited #Unsupported\n\n   def PyPowerSet(self) -> PySet[PyRel]: #Unsupported\n      raise Exception(\'Can not determine the result\')\n\n   def PyPowerSet1(self) -> PySet[PyRel]: #Unsupported\n      raise Exception(\'Can not determine the result\')\n\n   # >> def PyChoice(self) -> Tuple: #Inherited #Unsupported\n\n   def PyDomain(self) -> PySet[D]: #Unsupported\n      raise Exception(\'Unsupported Operation for PyID.\')\n\n   def PyRange(self) -> PySet[R]: #Unsupported\n      raise Exception(\'Unsupported Operation for PyID.\')\n\n   def PyComposition(self, other : PyRel) -> PyRel: #Unsupported\n      raise Exception(\'Unsupported Operation for PyID.\')\n\n   def PyBackwardComposition(self, other : PyRel) -> PyRel: #Unsupported\n      raise Exception(\'Unsupported Operation for PyID.\')\n\n   def PyDomainRestriction(self, other : PySet) -> PyRel:\n      restricted_id : Set[Tuple[Any,Any]] = set()\n      for element in other:\n         restricted_id.add((element,element))\n      return PyRel(restricted_id)\n\n   def PyRangeRestriction(self, other : PySet) -> PyRel:\n      restricted_id : Set[Tuple[Any,Any]] = set()\n      for element in other:\n         restricted_id.add((element,element))\n      return PyRel(restricted_id)\n\n   def PyDomainSubstraction(self, other : PySet) -> PyRel: #Unsupported\n      raise Exception(\'Unsupported Operation for PyID.\')\n\n   def PyRangeSubstraction(self, other : PySet) -> PyRel: #Unsupported\n      raise Exception(\'Unsupported Operation for PyID.\')\n\n   def __invert__(self) -> \'PyID\': #Inverse Relation method\n      return PyID()\n\n   # >> def __getitem__(self, keys : PySet) -> PySet: #Inherited\n\n   def PyOverriding(self, other : PyRel) -> PyRel: #Unsupported\n      raise Exception(\'Unsupported Operation for PyID.\')\n\n   # >> def PyDirectProduct(self, other : PyRel) -> PyRel[Any,Tuple[Any,Any]]: #Inherited #Unsupported\n\n   # >> def PyIsTotal(self, domain_set : PySet) -> bool: #Inherited #Unsupported\n\n   # >> def PyIsSurjection(self, range_set : PySet) -> bool: #Inherited #Unsupported\n\n   # >> def PyIsRelation(self, domain_set : PySet, range_set : PySet) -> bool: #Inherited #Unsupported\n\n   # >> def PyIsTotalRelation(self, domain_set : PySet, range_set : PySet) -> bool: #Inherited #Unsupported\n\n   # >> def PyIsSurjectiveRelation(self, domain_set : PySet, range_set : PySet) -> bool: #Inherited #Unsupported\n\n   # >> def PyIsTotalSurjectiveRelation(self, domain_set : PySet, range_set : PySet) -> bool: #Inherited #Unsupported\n\n   def PyIsWellDefined(self) -> bool:\n      return False\n\n   # >> def PyIsFunction(self, domain_set : PySet, range_set : PySet) -> bool: #Inherited #Unsupported\n\n   # >> def PyIsPartialFunction(self, domain_set : PySet, range_set : PySet) -> bool: #Inherited #Unsupported\n\n   # >> def PyIsTotalFunction(self, domain_set : PySet, range_set : PySet) -> bool: #Inherited #Unsupported\n\n   def PyIsInjection(self) -> bool:\n      return True\n\n   # >> def PyIsPartialInjection(self, domain_set : PySet, range_set : PySet) -> bool: #Inherited #Unsupported\n\n   # >> def PyIsTotalInjection(self, domain_set : PySet, range_set : PySet) -> bool: #Inherited #Unsupported\n\n   # >> def PyIsPartialSurjection(self, domain_set : PySet, range_set : PySet) -> bool: #Inherited #Unsupported\n\n   # >> def PyIsTotalSurjection(self, domain_set : PySet, range_set : PySet) -> bool: #Inherited #Unsupported\n\n   # >> def PyIsBijection(self, domain_set : PySet, range_set : PySet) -> bool: #Inherited #Unsupported\n\n   # >> def __call__(self, domain_element : Any) -> Any: #Apply method #Inherited\n\n\nclass PyFamilies(Generic[D,R]):\n\n   def __init__(self, familyType : PyFamilyTypes = PyFamilyTypes.UndeterminedFamilyType,\n                domain_set : PySet[D] = PySet(),\n                range_set : PySet[R] = PySet()) -> None:\n      #print(\'Test_PyFamilies.__init__\')\n      self.__FamilyType : PyFamilyTypes = familyType\n      self.__DomainSet : PySet[D] = domain_set\n      self.__RangeSet : PySet[R] = range_set\n\n   def FamilyType(self) -> PyFamilyTypes:\n      return self.__FamilyType\n\n   def DomainSet(self) -> PySet[D]:\n      return self.__DomainSet\n\n   def RangeSet(self) -> PySet[R]:\n      return self.__RangeSet\n\n   def __str__(self) -> str:\n      return \'PyFamilies(\' + self.__FamilyType.__str__() + \' \\nDomainSet(\' + self.__DomainSet.__str__() +  \')\\nRangeSet(\' + self.__RangeSet.__str__() + \'))\'\n\n   def __repr__(self) -> str:\n      return \'PyFamilies(\' + self.__FamilyType.__str__() + \' \\nDomainSet(\' + self.__DomainSet.__str__() +  \')\\nRangeSet(\' + self.__RangeSet.__str__() + \'))\'\n\n   def PyContains(self,relation : PyRel[D,R]) -> bool:\n      #print(\'Test_PyFamilies.PyContains\')\n      if self.__FamilyType == PyFamilyTypes.Relations:\n         return relation.PyIsRelation(self.__DomainSet,self.__RangeSet)\n      if self.__FamilyType == PyFamilyTypes.TotalRelations:\n         return relation.PyIsTotalRelation(self.__DomainSet,self.__RangeSet)\n      if self.__FamilyType == PyFamilyTypes.SurjectiveRelations:\n         return relation.PyIsSurjectiveRelation(self.__DomainSet,self.__RangeSet)\n      if self.__FamilyType == PyFamilyTypes.TotalSurjectiveRelations:\n         return relation.PyIsTotalSurjectiveRelation(self.__DomainSet,self.__RangeSet)\n      if self.__FamilyType == PyFamilyTypes.PartialFunctions:\n         return relation.PyIsPartialFunction(self.__DomainSet,self.__RangeSet)\n      if self.__FamilyType == PyFamilyTypes.TotalFunctions:\n         return relation.PyIsTotalFunction(self.__DomainSet,self.__RangeSet)\n      if self.__FamilyType == PyFamilyTypes.PartialInjections:\n         return relation.PyIsPartialInjection(self.__DomainSet,self.__RangeSet)\n      if self.__FamilyType == PyFamilyTypes.TotalInjections:\n         return relation.PyIsTotalInjection(self.__DomainSet,self.__RangeSet)\n      if self.__FamilyType == PyFamilyTypes.PartialSurjections:\n         return relation.PyIsPartialSurjection(self.__DomainSet,self.__RangeSet)\n      if self.__FamilyType == PyFamilyTypes.TotalSurjections:\n         return relation.PyIsTotalSurjection(self.__DomainSet,self.__RangeSet)\n      if self.__FamilyType == PyFamilyTypes.Bijections:\n         return relation.PyIsBijection(self.__DomainSet,self.__RangeSet)\n      raise Exception(\'Family Type unrecognized.\')\n\n   def PyNotContains(self,relation : PyRel[D,R]) -> bool:\n      #print(\'Test_PyFamilies.PyNotContains\')\n      return not self.PyContains(relation)\n\n   def PyChoice(self) -> PyRel[D,R]:\n      #print(\'Test_PyFamilies.PyChoice\')\n      tfunc_tuples : Set[Tuple[D,R]] = set()\n      if self.__FamilyType == PyFamilyTypes.TotalFunctions:\n         for dom_ele in self.__DomainSet:\n            tfunc_tuples.add((dom_ele,self.__RangeSet.PyChoice()))\n         return PyRel(tfunc_tuples)\n      if self.__FamilyType == PyFamilyTypes.TotalInjections:\n         if isinstance(self.__RangeSet,PyCondSet_Ext):\n            raise Exception(\'Operation not supported for PyCondSet_Ext in TotalInjections.\')\n         if isinstance(self.__RangeSet,PyCondSet):\n            visited_range_set : Set[R] = set()\n            for dom_ele in self.__DomainSet:\n               if self.__RangeSet.PyFinite() and len(visited_range_set) == len(self.__RangeSet):\n                  raise Exception(\'It was not possible to create a TotalInjective Relation\')\n               img_ele = self.__RangeSet.PyChoice()\n               while(img_ele in visited_range_set):\n                     img_ele = self.__RangeSet.PyChoice()\n               tfunc_tuples.add((dom_ele,img_ele))\n               visited_range_set.add(img_ele)\n            return PyRel(tfunc_tuples)\n         if isinstance(self.__RangeSet,PySet):\n            non_visited_range_set : Set[R] = self.__RangeSet.FiniteInclusion()\n            for dom_ele in self.__DomainSet:\n               if len(non_visited_range_set) == 0:\n                  raise Exception(\'It was not possible to create a TotalInjective Relation\')\n               img_ele = choice(list(non_visited_range_set))\n               tfunc_tuples.add((dom_ele,img_ele))\n               non_visited_range_set.discard(img_ele)\n            return PyRel(tfunc_tuples)\n      raise Exception(\'Operation only supported for TotalFunctions or TotalInjections.\')\n\n\nclass PyPrelude():\n\n   def __init__(self) -> None:\n\n      ###Special Pararmeters###\n\n      # Amount of times that the Prelude will try to generate valid values\n      #    for the parameters of an event.\n      self.__lowMaxRandomGenAttempts : int = 5\n      \n      # Amount of times that the Prelude will try to generate valid values\n      #    for the constants of a context.\n      self.__highMaxRandomGenAttempts : int = 10\n\n      # Flag to activate or deactivate all the contracts.\n      self.__DESIGN_BY_CONTRACT_ENABLED : bool = True\n      \n      # Amount of times that the Prelude will try to choose an enabled event\n      #    from a machine and execute it.\n      self.__MaxAutoExecuteAttempts : int = 10\n      \n      # When True, the Prelude will traverse infinite Sets (like the natural numbers set) by traversing a finite set that represents that infinite set.\n      #    This parameter NEEDS to be True so that the Prelude can execute predicates that require the traversing of infinite sets (for example, when there is a\n      #    quantified predicate where the bound variable is type \'int\'.\n      self.__USE_FINITE_SPECIAL_SETS : bool = False\n\n      # Value that defines the size of the finite sets that represent infinite setes when USE_FINITE_SPECIAL_SETS is True. For example, if this parameter = 10,\n      #    then the integers will go from -10 to 10, the natural number will go from 0 to 10, and the natural numbers without the 0 will go from 1 to 10.\n      self.__FINITE_SPECIAL_SETS_LIMIT : int = 10\n\n      # PyRandValGen will generate random integer values within this range.\n      self.__RAND_INT_RANGE : Tuple[int,int] = (-100,100)\n\n      # PyRandValGen will generate random sets (PySet) of at most this amount of elements.\n      self.__RAND_SET_SIZE : int = 5\n\n      # PyRandValGen will generate random relations (PyRel) of at most this amount of elements.\n      self.__RAND_REL_SIZE : int = 5\n\n      ###PyRandValGen CarrierSets###\n      self.__CarrierSetClasses : Dict[str,Type[Enum]] = dict()\n      self.__CarrierSets : Dict[str,PySet[Enum]] = dict()\n      self.__CarrierSetsIters : Dict[str,int] = dict()\n\n   #This method exists to avoid Optional[ ] Typings.\n   def NoParam(self) -> Any:\n      return None\n      \n   def BOOL(self) -> PySet[bool]:\n      return PySet({True,False})\n\n   def NAT(self) -> PyNAT:\n      return PyNAT()\n\n   def NAT1(self) -> PyNAT1:\n      return PyNAT1()\n\n   def INT(self) -> PyINT:\n      return PyINT()\n\n   def PNAT(self) -> PyCondSet[PySet[int]]:\n      return PyCondSet(PyBaseFunc.PNAT_ContainsFunc, finite_func = PyBaseFunc.ReturnFalse0)\n\n   def PNAT1(self) -> PyCondSet[PySet[int]]:\n      return PyCondSet(PyBaseFunc.PNAT1_ContainsFunc, finite_func = PyBaseFunc.ReturnFalse0)\n\n   def PINT(self) -> PyCondSet[PySet[int]]:\n      return PyCondSet(PyBaseFunc.PINT_ContainsFunc, finite_func = PyBaseFunc.ReturnFalse0)\n\n   def P1NAT(self) -> PyCondSet[PySet[int]]:\n      return PyCondSet(PyBaseFunc.P1NAT_ContainsFunc, finite_func = PyBaseFunc.ReturnFalse0)\n\n   def P1NAT1(self) -> PyCondSet[PySet[int]]:\n      return PyCondSet(PyBaseFunc.P1NAT1_ContainsFunc, finite_func = PyBaseFunc.ReturnFalse0)\n\n   def P1INT(self) -> PyCondSet[PySet[int]]:\n      return PyCondSet(PyBaseFunc.P1INT_ContainsFunc, finite_func = PyBaseFunc.ReturnFalse0)\n\n   def NATXNAT(self) -> PyNATXNAT:\n      return PyNATXNAT()\n\n   def INTXINT(self) -> PyINTXINT:\n      return PyINTXINT()\n\n   def INTXNAT(self) -> PyINTXNAT:\n      return PyINTXNAT()\n\n   def ID(self) -> PyID:\n      return PyID()\n\n   def LOWMAXGENATTEMPTS(self) -> int:\n      return self.__lowMaxRandomGenAttempts\n\n   def HIGHMAXGENATTEMPTS(self) -> int:\n      return self.__highMaxRandomGenAttempts\n\n   def MaxAutoExecuteAttempts(self) -> int:\n      return self.__MaxAutoExecuteAttempts\n\n   def DESIGN_BY_CONTRACT_ENABLED(self) -> bool:\n      return self.__DESIGN_BY_CONTRACT_ENABLED\n\n   def USE_FINITE_SPECIAL_SETS(self) -> bool:\n      return self.__USE_FINITE_SPECIAL_SETS\n\n   def RAND_INT_RANGE(self) -> Tuple[int,int]:\n      return self.__RAND_INT_RANGE\n\n   def RAND_SET_SIZE(self) -> int:\n      return self.__RAND_SET_SIZE\n\n   def RAND_REL_SIZE(self) -> int:\n      return self.__RAND_REL_SIZE\n\n   def FINITE_SPECIAL_SETS_LIMIT(self) -> int:\n      return self.__FINITE_SPECIAL_SETS_LIMIT\n\n   def setLowMaxGenAttempts(self, newLowMaxAttempts: int) -> None:\n      assert(newLowMaxAttempts>=0)\n      self.__lowMaxRandomGenAttempts = newLowMaxAttempts\n\n   def setHighMaxGenAttempts(self, newHighMaxAttempts: int) -> None:\n      assert(newHighMaxAttempts>=0)\n      self.__highMaxRandomGenAttempts = newHighMaxAttempts\n\n   def setDESIGN_BY_CONTRACT_ENABLED(self, newDESIGN_BY_CONTRACT : bool) -> None:\n      self.__DESIGN_BY_CONTRACT_ENABLED = newDESIGN_BY_CONTRACT\n\n   def setUSE_FINITE_SPECIAL_SETS(self, newUSE_FINITE_SPECIAL_SETS : bool) -> None:\n      self.__USE_FINITE_SPECIAL_SETS = newUSE_FINITE_SPECIAL_SETS\n\n   def setRAND_INT_RANGE(self, newRAND_INT_RANGE: Tuple[int,int]) -> None:\n      assert(newRAND_INT_RANGE[0]<=newRAND_INT_RANGE[1])\n      self.__RAND_INT_RANGE = newRAND_INT_RANGE\n\n   def setRAND_SET_SIZE(self, newRAND_SET_SIZE: int) -> None:\n      assert(newRAND_SET_SIZE > 0)\n      self.__RAND_SET_SIZE = newRAND_SET_SIZE\n\n   def setRAND_REL_SIZE(self, newRAND_REL_SIZE: int) -> None:\n      assert(newRAND_REL_SIZE > 0)\n      self.__RAND_REL_SIZE = newRAND_REL_SIZE\n\n   def setFINITE_SPECIAL_SETS_LIMIT(self, newFINITE_SPECIAL_SETS_LIMIT: int) -> None:\n      assert(newFINITE_SPECIAL_SETS_LIMIT > 0)\n      self.__FINITE_SPECIAL_SETS_LIMIT = newFINITE_SPECIAL_SETS_LIMIT\n\n   #PY RANDOM VALUE GENERATOR #Weak Typechecking\n\n   def PyRandIntGen(self) -> int:\n      return randint(P.RAND_INT_RANGE()[0],P.RAND_INT_RANGE()[1])\n\n   def PyRandBoolGen(self) -> bool:\n      return choice((True,False))\n\n   def PyRandPySetGen(self, pyType : str) -> PySet:\n      tmp : Set = set()\n      for e in range(P.RAND_SET_SIZE()):\n         tmp.add(self.PyRandValGen(pyType[6:-1]))\n      return PySet(tmp)\n\n   def PyRandEnumGen(self, pyType : str) -> Enum:\n      EnumType : Type[Enum] = self.__CarrierSetClasses[pyType]\n      self.__CarrierSetsIters[pyType] += 1\n      if self.__CarrierSetsIters[pyType] > len(EnumType):\n         self.__CarrierSetsIters[pyType] = 1\n      return EnumType(self.__CarrierSetsIters[pyType])\n\n   def PyRandTupleGen(self, pyType : str) -> Tuple:\n\n      parenthesis_count : int = 0\n      i_index : int = 6\n      for char in pyType[6:]:\n         if char == \',\' and parenthesis_count == 0:\n            break\n         if char == \'[\':\n            parenthesis_count += 1\n         if char == \']\':\n            parenthesis_count -= 1\n         i_index += 1\n         \n      return ( self.PyRandValGen(pyType[6:i_index]), self.PyRandValGen(pyType[i_index+1:-1]) )\n\n   def PyRandPyRelGen(self, pyType : str) -> PyRel:\n      return PyRel( self.PyRandValGen( \'PySet[Tuple[\' + pyType[6:] + \']\').FiniteInclusion() )\n\n   def PyRandValGen(self, pyType : str ) -> Any:\n      if pyType == \'bool\':\n         return self.PyRandBoolGen()\n      elif pyType == \'int\':\n         return self.PyRandIntGen()\n      elif pyType[:5] == \'PySet\':\n         return self.PyRandPySetGen(pyType)\n      elif pyType in self.__CarrierSets:\n         return self.PyRandEnumGen(pyType)\n      elif pyType[:5] == \'Tuple\':\n         return self.PyRandTupleGen(pyType)\n      elif pyType[:5] == \'PyRel\':\n         return self.PyRandPyRelGen(pyType)\n      else:\n         raise Exception(\'Error PyPrelude.PyRandValGen\')\n\n   def PyCarrierSetGet(self, carrierSetName : str ) -> PySet[Any]:\n      return self.__CarrierSets[carrierSetName]\n\n   def AddCarrierSet(self, carrierSetName : str, carrierSetClassType : Type[Enum]) -> None:\n      self.__CarrierSetClasses[carrierSetName] = carrierSetClassType\n\n      tmp : Set[Enum] = set()\n      for element in carrierSetClassType:\n         tmp.add(element)  \n      self.__CarrierSets[carrierSetName] = PySet(tmp)\n      self.__CarrierSetsIters[carrierSetName] = 0\n\n   def getCarrierSets(self) -> Dict[str,PySet[Enum]]:\n      return self.__CarrierSets\n\n   def getCarrierSetClasses(self) -> Dict[str,Type[Enum]]:\n      return self.__CarrierSetClasses\n\n   def getCarrierSetsIters(self) -> Dict[str,int]:\n      return self.__CarrierSetsIters\n\n   @staticmethod\n   def LogicImplication(left : bool,right : bool) -> bool:\n      if left == True and right == False:\n         return False\n      return True\n\n   @staticmethod\n   def LogicEquivalence(left : bool,right : bool) -> bool:\n      if (left == True and right == True) or (left == False and right == False):\n         return True\n      return False\n\n   @staticmethod\n   def Minimum(int_set : PySet[int]) -> int:\n      if isinstance(int_set, PyCondSet):\n         raise Exception(\'Minimum operation is not supported for implicit sets.\')\n      return min(int_set.FiniteInclusion())\n\n   @staticmethod\n   def Maximum(int_set : PySet[int]) -> int:\n      if isinstance(int_set, PyCondSet):\n         raise Exception(\'Maximum operation is not supported for implicit sets.\')\n      return max(int_set.FiniteInclusion())\n\n   def ObtainSetFromTuple(self, pyType : str) -> PyRel:\n\n      parenthesis_count : int = 0\n      i_index : int = 6\n      for char in pyType[6:]:\n         if char == \',\' and parenthesis_count == 0:\n            break\n         if char == \'[\':\n            parenthesis_count += 1\n         if char == \']\':\n            parenthesis_count -= 1\n         i_index += 1\n         \n      return self.ObtainSetFromType(pyType[6:i_index]).PyCartesianProduct(self.ObtainSetFromType(pyType[i_index+1:-1]))\n\n   def ObtainSetFromSet(self, pyType : str) -> PySet[PySet]:\n      return self.ObtainSetFromType(pyType[6:-1]).PyPowerSet()\n\n   def ObtainSetFromType(self, pyType : str) -> Any:\n      \n      if pyType == \'bool\':\n         return PySet({True,False})\n      elif pyType == \'int\':\n         return PyINT()\n      elif pyType[:5] == \'PySet\':\n         return self.ObtainSetFromSet(pyType)\n      elif pyType in self.__CarrierSets:\n         return self.__CarrierSets[pyType]\n      elif pyType[:5] == \'Tuple\':\n         return self.ObtainSetFromTuple(pyType)\n      elif pyType[:5] == \'PyRel\':\n         return self.ObtainSetFromTuple(pyType).PyPowerSet()\n      else:\n         raise Exception(\'Error PyPrelude.ObtainSetFromType\')\n\n   def BecomesSuchThat(self,\n                       predicate : Callable[[List[Any]],bool],\n                       BoundIdentType : str) -> Any:\n      set_to_iter = self.ObtainSetFromType(BoundIdentType)\n      possible_values : Set = set()\n\n      for possible_value in set_to_iter:\n         try:\n            if predicate(possible_value):\n               possible_values.add(possible_value)\n         except:\n            pass\n\n      if len(possible_values) == 0:\n         raise Exception(\'No value managed to accomplish the given predicate!\')\n      return PySet(possible_values).PyChoice()\n\n      \n   def QuantifiedForAll(self, predicate : Callable[[List[Any]],bool] , BoundIdentDeclsAndTypes : List[Tuple[int,str]]) -> bool:\n\n      boundIdentifiersAmount : int = len(BoundIdentDeclsAndTypes)\n\n      #Create Array Of Sets\n      boundIdentifiersSets : List[Any] = [ None for e in range(boundIdentifiersAmount) ]\n\n      #Obtain Sets from Types\n      for BoundIdentDeclAndType in BoundIdentDeclsAndTypes:\n         boundIdentifiersSets[BoundIdentDeclAndType[0]] = self.ObtainSetFromType( BoundIdentDeclAndType[1] )\n\n      #Create Array of Iters\n      boundIdentifiersIters : List[Iterator] = [ iter(boundIdentifiersSets[i]) for i in range(boundIdentifiersAmount) ]\n\n      #Create and Initialize Array of lambda Parameters\n      boundIdentifiersValues : List[Any] = [ None for e in range(boundIdentifiersAmount) ]\n      for i in range(boundIdentifiersAmount):\n         try:\n            boundIdentifiersValues[i] = next(boundIdentifiersIters[i])\n         except StopIteration:\n            return True #chrome-extension://oemmndcbldboiebfnladdacbdfmadadm/http://cse.unl.edu/~cbourke/CSCE235/notes/PredicatesQuantifiers-HandoutNoNotes.pdf\n\n      #Try al possibilities\n      indexIterator : int = boundIdentifiersAmount-1\n      while(indexIterator>=0):\n         \n         try:\n            if predicate(boundIdentifiersValues) == False:\n               return False\n         except:\n            pass\n         \n         try:\n            boundIdentifiersValues[indexIterator] = next(boundIdentifiersIters[indexIterator])\n         except StopIteration:\n            boundIdentifiersIters[indexIterator] = iter(boundIdentifiersSets[indexIterator])\n            boundIdentifiersValues[indexIterator] = next(boundIdentifiersIters[indexIterator])\n            indexIterator-=1\n            flag : bool = True\n            while(flag and indexIterator>=0):\n               try:\n                  boundIdentifiersValues[indexIterator] = next(boundIdentifiersIters[indexIterator])\n                  indexIterator = boundIdentifiersAmount-1\n                  flag = False\n               except StopIteration:\n                  boundIdentifiersIters[indexIterator] = iter(boundIdentifiersSets[indexIterator])\n                  boundIdentifiersValues[indexIterator] = next(boundIdentifiersIters[indexIterator])\n                  indexIterator-=1\n      \n      return True\n\n   def QuantifiedExists(self, predicate : Callable[[List[Any]],bool] , BoundIdentDeclsAndTypes : List[Tuple[int,str]]) -> bool:\n\n      boundIdentifiersAmount : int = len(BoundIdentDeclsAndTypes)\n\n      #Create Array Of Sets\n      boundIdentifiersSets : List[Any] = [ None for e in range(boundIdentifiersAmount) ]\n\n      #Obtain Sets from Types\n      for BoundIdentDeclAndType in BoundIdentDeclsAndTypes:\n         boundIdentifiersSets[BoundIdentDeclAndType[0]] = self.ObtainSetFromType( BoundIdentDeclAndType[1] )\n\n      #Create Array of Iters\n      boundIdentifiersIters : List[Iterator] = [ iter(boundIdentifiersSets[i]) for i in range(boundIdentifiersAmount) ]\n\n      #Create and Initialize Array of lambda Parameters\n      boundIdentifiersValues : List[Any] = [ None for e in range(boundIdentifiersAmount) ]\n      for i in range(boundIdentifiersAmount):\n         try:\n            boundIdentifiersValues[i] = next(boundIdentifiersIters[i])\n         except StopIteration:\n            return False #chrome-extension://oemmndcbldboiebfnladdacbdfmadadm/http://cse.unl.edu/~cbourke/CSCE235/notes/PredicatesQuantifiers-HandoutNoNotes.pdf\n\n      #Try al possibilities\n      indexIterator : int = boundIdentifiersAmount-1\n      while(indexIterator>=0):\n\n         try:\n            if predicate(boundIdentifiersValues) == True:\n               return True\n         except:\n            pass\n         \n         try:\n            boundIdentifiersValues[indexIterator] = next(boundIdentifiersIters[indexIterator])\n         except StopIteration:\n            boundIdentifiersIters[indexIterator] = iter(boundIdentifiersSets[indexIterator])\n            boundIdentifiersValues[indexIterator] = next(boundIdentifiersIters[indexIterator])\n            indexIterator-=1\n            flag : bool = True\n            while(flag and indexIterator>=0):\n               try:\n                  boundIdentifiersValues[indexIterator] = next(boundIdentifiersIters[indexIterator])\n                  indexIterator = boundIdentifiersAmount-1\n                  flag = False\n               except StopIteration:\n                  boundIdentifiersIters[indexIterator] = iter(boundIdentifiersSets[indexIterator])\n                  boundIdentifiersValues[indexIterator] = next(boundIdentifiersIters[indexIterator])\n                  indexIterator-=1\n      \n      return False\n\n   def DebugArray(self, pyrel_as_arr : PyRel[int,Any]) -> List[Any]:\n      if isinstance(pyrel_as_arr,PyCondRel):\n         raise Exception(\'Operation not supported for implicit Rels.\')\n      converted_array : List[Any] = list(pyrel_as_arr.FiniteInclusion())\n      converted_array.sort(key= lambda tuple_in_arr:tuple_in_arr[0])\n      return [element[1] for element in converted_array]\n\n\nP : PyPrelude = PyPrelude()\n\n# Methods to deal with Mypy inconsistencies.\n\ndef MypyPySetCastPyRel(pyset_to_cast : PySet) -> PyRel:\n   return PyRel(pyset_to_cast.FiniteInclusion())\n\ndef MypyPyCondSet(lambda_func : Callable) -> PyCondSet:\n   return PyCondSet(lambda_func)\n\n\'\'\'\n#PENDING\n   #Discuss OR Check\n      #Create Special Class for PyNat, PyNat1, etc.\n      #SubSet with finite element is possible.\n      #Operations return duplicates\n      #Operate with &\n\n\n##### TEST FOR SIMPLE PYSET\nt10 : PySet[int] = PySet({3,4})\nt11 : PySet[int] = PySet({4,3})\nt12 : PySet[int] = PySet({7})\nprint(t12.PyContains(7))\nprint(t12.PyNotContains(7))\n\n##### TEST FOR SPECIAL PYSET\nt13 : PySet[int] = PySet({3,4})\nt14 : PySet[int] = PySet({0,3,4})\nt15 : PySet[int] = PySet({-1,3,4})\nprint(P.PNAT().PyContains(t13))\nprint(P.PNAT().PyContains(t14))\nprint(P.PNAT().PyContains(t15))\nprint(P.PNAT1().PyContains(t13))\nprint(P.PNAT1().PyContains(t14))\nprint(P.PNAT1().PyContains(t15))\nprint(P.PINT().PyContains(t13))\nprint(P.PINT().PyContains(t14))\nprint(P.PINT().PyContains(t15))\n\n##### TEST FOR PYSET OF PYSETS\nt20 : PySet[PySet[int]] = PySet({PySet({3,4}),PySet({4,3}),PySet(),PySet({7})})\nt21 : PySet[PySet[int]]= PySet({PyCondSet(),PyCondSet(PyBaseFunc.NAT_ContainsFunc)})\n\n##### TEST FOR PYUNION AND PYINTERSECTION AND PYDIFFERENCE\nt30 : PySet[int] = PySet({3,4,10})\nt31 : PySet[int] = t30.PyUnion(t12)\nt34 : PySet[int] = PySet({3,4,20})\nprint(t30.PyIntersection(t34))\nprint(t30.PyDifference(t34))\n\n##### TEST FOR PYCARTESIANPRODUCT\nt23 : PyRel[int,int] = t30.PyCartesianProduct(t34)\nprint(t23)\n\n##### TEST FOR PYISSUBSET\nt32 : PySet[int] = PySet({-3, 4, 10})\nt33 : PySet[int] = PySet({-3, 4, 5})\nprint(t32.PyIsSubset(PyNAT()))\nprint(t32.PyIsSubset(PyINT()))\nprint(t32.PyIsSubset(t33))\nprint(t32.PyNotSubset(t33))\n\n##### TEST FOR PYPARTITION\nt35 : PySet[int] = PySet({1, 2, 3, 4, 5})\nt36 : PySet[int] = PySet({1, 2})\nt37 : PySet[int] = PySet({3})\nt38 : PySet[int] = PySet({4, 5})\nt39 : PySet[int] = PySet({4, 5, 7})\nprint(t35.PyPartition([t36,t37]))\nprint(t35.PyPartition([t36,t37,t38]))\nprint(t35.PyPartition([t36,t37,t39]))\n\n##### TEST FOR PYPOWERSET +1\nt22 : PySet[int] = PySet({1,2,3})\nprint(t22.PyPowerSet())\nprint(len(t22.PyPowerSet()))\nprint(t22.PyPowerSet1())\nprint(len(t22.PyPowerSet1()))\n\n##### TEST PYCONDSET and PyNAT\nt40 : PySet[int] = PyCondSet(PyBaseFunc.NAT_ContainsFunc)\nt40.PyContains(4)\nt41 : PySet[int] = PyNAT()\nprint(t41.PyContains(7))\nprint(t41.PyUnion(t32))\n\nt42 : PySet[int] = PyINT()\nprint(t41.PyUnion(t42))\nt43 : PySet[int] = PyNAT1()\nprint(t41.PyUnion(t42))\n# Test PyUnion and PyIntersection and PyDifference on PyCondSet (PySet)\nprint(t11.PyUnion(t41))\nprint(t32.PyIntersection(t41))\nprint(t32.PyDifference(t41))\nP.setUSE_FINITE_SPECIAL_SETS(True)\nprint(t22.PyCartesianProduct(P.NAT()))\nprint(P.NAT().PyCartesianProduct(t22))\nP.setUSE_FINITE_SPECIAL_SETS(False)\n\n##### TEST PYCONDSET_EXT\nt50 : PySet[int] = PyCondSet_Ext(PyBaseFunc.NAT_ContainsFunc,{-3,-7},{90})\nprint(t50.PyContains(10))\nprint(t50.PyContains(-7))\nprint(t50.PyContains(90))\n# Test PyUnion and PyIntersection and PyDifference on PyCondSet_Ext (PySet)\nprint(t11.PyUnion(t50))\nprint(t32.PyIntersection(t50))\nprint(t32.PyDifference(t50))\n\n##### TEST PYCONDSET_TREEEXT\nt60 : PySet[int] = PyCondSet_TreeExt(PyBaseFunc.NAT_ContainsFunc,{-5,-7,-95},{90})\nt61 : PySet[int] = PyCondSet_TreeExt(PyBaseFunc.test,{50},{22})\nt62 = t60.PyUnion(t61)\nprint(t62.PyContains(90))\nt63 = t60.PyIntersection(t61)\nprint(t63.PyContains(90))\nprint(t63.PyContains(-5))\nprint(t63.PyContains(-95))\nt64 = t60.PyDifference(t61)\nprint(t64.PyContains(90))\nprint(t64.PyContains(-5))\nprint(t64.PyContains(-95))\n# Test PyUnion and PyIntersection and PyDifference on PyCondSet_TreeExt (PySet)\nprint(t11.PyUnion(t60))\nprint(t32.PyIntersection(t60))\nprint(t32.PyDifference(t60))\n# Test PyUnion and PyIntersection and PyDifference on PyCondSet_TreeExt (PyCondSet)\nprint(t40.PyUnion(t60))\nprint(t42.PyIntersection(t60))\nprint(t40.PyDifference(t60))\n\n##### TEST PYRANDVALGEN\nt70 : PySet[PySet[int]] = P.PyRandValGen(\'PySet[PySet[int]]\')\nt71 : Tuple[int,Tuple[Tuple[int,int],int]] = P.PyRandValGen(\'Tuple[int,Tuple[Tuple[int,int],int]]\')\nprint(t71)\n\n##### TEST PYREL: PYCONTAINS\nt81 : PyRel[int,int] = PyRel({(3,4),(4,7)})\nt82 : PyRel[int,int] = PyRel({(4,3),(4,7)})\nt83 : PyCondRel[int,int] = PyCondRel(PyBaseFunc.test2,PySet({1,2,3}),PySet({3,4,7,10,20,100,200}))\nt84 : PySet[int] = PySet({-3, 4, 10})\nt85 : PyCondRel[int,int] = P.NATXNAT()\n\nprint(t81.PyContains((4,3)))\nprint(t81.PyNotContains((4,3)))\nprint(t83.PyContains((1,100)))\nprint(t83.PyContains((2,100)))\nprint(t83.PyNotContains((3,3)))\n\n##### TEST PYREL: PYUNION AND PYINTERSECTION AND PYDIFFERENCE AND CARTESIANPRODUCT\nprint(t81.PyUnion(t82))\nprint(t81.PyIntersection(t82))\nprint(t81.PyIntersection(t83))\nprint(t81.PyIntersection(PyINTXINT()))\nprint(PyINTXINT().PyIntersection(t81))\nprint(t81.PyIntersection(PyID()))\nprint(PyID().PyIntersection(t81.PyUnion(PyRel({(7,7)}))))\nprint(t81.PyDifference(t83))\nprint(t81.PyCartesianProduct(t84))\n#P.setUSE_FINITE_SPECIAL_SETS(True)\n#print(t85.PyCartesianProduct(t81))\n#P.setUSE_FINITE_SPECIAL_SETS(False)\n\n##### TEST PYREL: PYISSUBSET AND PYNOTSUBSET AND PYISPROPERSUBSET AND PYNOTPROPERSUBSET AND PYFINITE AND PYPARTITION AND PYPOWERSET AND PYFINITE\nt90 : PyRel[int,int] = PyRel({(3,4),(4,7)})\nt91 : PyRel[int,int] = PyRel({(3,4),(4,7),(7,9),(4,9),(2,1),(2,2),(2,2)})\nt92 : PyRel[int,int] = PyRel({(7,9)})\nt93 : PyRel[int,int] = PyRel({(2,2),(7,10),(3,5),(8,2)})\nt94 : PyCondRel[int,int] = PyCondRel(PyBaseFunc.test2,PySet({1,2,3}),PySet({3,4,7,10,20,100,200}))\nt95 : PyRel[int,int] = PyRel({(2,2),(7,10),(3,5),(8,7)})\nprint(t90.PyIsSubset(t91))\nprint(t82.PyIsSubset(t91))\nprint(t90.PyNotSubset(t91))\nprint(t82.PyNotSubset(t91))\nprint(t81.PyIsProperSubset(t90))\nprint(t90.PyIsProperSubset(t91))\nprint(t81.PyNotProperSubset(t90))\nprint(t90.PyFinite())\nprint(t91.PyFinite())\nprint(t91.PyPartition([t90,t92]))\nprint(t91.PyPartition([t90,t93]))\nprint(t91.PyPartition([t91,PyRel()]))\nprint(t92.PyPowerSet())\nprint(len(t91.PyPowerSet()))\nprint(t91.PyPowerSet1())\nprint(len(t91.PyPowerSet1()))\nprint(t94.PyFinite()) #####################################################TESTS HERE\nprint(t94.PyDomain())\n\n##### TEST PYREL: PYDOMAIN AND PYRANGE AND PYCOMPOSITION AND PYDOMAIN|RANGE RESTRICTION|SUBSTRACTION AND INVERSE AND RELIMAGE AND PYOVERRIDING AND PYDIRECTPRODUCT\n#        AND PY ISRELATION | ISTOTALRELATION | ISSURJECTIVERELATION | ISTOTALSURJECTIVERELATION | ISWELLDEFINED | ALL INJECTSURJECTBIJECTION FUNCTIONS\nprint(t82.PyDomain())\nprint(t82.PyRange())\nprint(t91.PyComposition(t93))\nprint(t91.PyBackwardComposition(t95))\nprint(t93.PyDomainRestriction(PySet({7,2,37})))\nprint(t93.PyRangeRestriction(PySet({7,9,2,10})))\nprint(t93.PyDomainSubstraction(PySet({7,2,37})))\nprint(t93.PyRangeSubstraction(PySet({7,9,2,10})))\nprint(~t93)\nprint(t93[PySet({2,7})])\nprint(t91.PyOverriding(t93))\nprint(t91.PyDirectProduct(t93))\nprint(t90.PyIsRelation(PySet({3,4,5}),PySet({3,4,5})))\nprint(t90.PyIsRelation(PySet({3,4,5}),PySet({4,7})))\nprint(t90.PyIsTotalRelation(PySet({3,4,5}),PySet({7,3,4,5})))\nprint(t90.PyIsTotalRelation(PySet({3,4}),PySet({7,3,4,5})))\nprint(t90.PyIsSurjectiveRelation(PySet({3,4,5}),PySet({3,4,7})))\nprint(t90.PyIsSurjectiveRelation(PySet({3,4,5}),PySet({4,7})))\nprint(t90.PyIsTotalSurjectiveRelation(PySet({3,4,5}),PySet({3,4,7})))\nprint(t90.PyIsTotalSurjectiveRelation(PySet({3,4}),PySet({4,7})))\nprint(t94.PyIsTotalRelation(PySet({1,2,3}),PySet({3,4,7,10,20,100,200})))\nprint(t94.PyIsTotalFunction(PySet({1,2,3}),PySet({3,4,7,10,20,100,200})))\n\nprint(t90.PyIsWellDefined())\nprint(t91.PyIsWellDefined())\nprint(t90.PyIsTotal(PySet({3,4})))\nprint(t90.PyIsTotal(PySet({3,4,5})))\nprint(t90.PyIsTotalFunction(PySet({3,4}),PySet({4,7,9})))\nprint(t90.PyIsTotalFunction(PySet({3,4,5}),PySet({4,7,9})))\nprint(t90.PyIsInjection())\nprint(t93.PyIsInjection())\nprint(t90.PyIsSurjection(PySet({4,7})))\nprint(t90.PyIsSurjection(PySet({7,4,9})))\nprint(t93.PyIsBijection(PySet({2,7,3,8}),PySet({2,5,10})))\nprint(t93.PyIsTotalSurjection(PySet({2,7,3,8}),PySet({2,5,10})))\nprint(t95.PyIsBijection(PySet({2,7,3,8}),PySet({2,5,10,7})))\nprint(t93[PySet({2,7})])\nprint(t90(3))\nprint(t95(7))\nprint(t91(4))\n\n##### TEST PYNATXNAT AND SIMILARS\nprint(P.ID().PyDomainRestriction(PySet({3,4,5})))\nprint(PyRel({(0,-3),(3,7)}).PyIsSubset(P.INTXINT()))\n\n##### FAMILYOF\nfamily_of_relations0 : PyFamilies = PyFamilies(PyFamilyTypes.Relations,PySet({3,4,5}),PySet({3,4,5}))\nprint(family_of_relations0.PyContains(t90))\nfamily_of_relations1 : PyFamilies = PyFamilies(PyFamilyTypes.Relations,PySet({3,4,5}),PySet({4,7}))\nprint(family_of_relations1.PyContains(t90))\nfamily_of_relations2 : PyFamilies = PyFamilies(PyFamilyTypes.TotalSurjectiveRelations,PySet({3,4,5}),PySet({3,4,7}))\nprint(family_of_relations2.PyContains(t90))\nfamily_of_relations3 : PyFamilies = PyFamilies(PyFamilyTypes.TotalSurjectiveRelations,PySet({3,4}),PySet({4,7}))\nprint(family_of_relations3.PyContains(t90))\n\n### PYCHOICE AND OBTAINSETFROMTYPE\nprint(PySet({10,20,37,40,50}).PyChoice())\nprint(P.NAT1().PyChoice())\nprint(t91.PyChoice())\nprint(P.NATXNAT().PyChoice())\nprint(P.ObtainSetFromType(\'Tuple[bool,bool]\'))\nprint(PyFamilies(PyFamilyTypes.TotalFunctions,PySet({1,2,3,4,5}),PySet({\'a\',\'b\',\'c\',\'d\'})).PyChoice())\nprint(PyFamilies(PyFamilyTypes.TotalInjections,PySet({1,2,3,4,5}),PySet({\'a\',\'b\',\'c\',\'d\',\'e\',\'f\',\'g\'})).PyChoice())\n\n### OTHER TESTS\nt100 = MypyPyCondSet(lambda boundIdentifiers : True if ((( boundIdentifiers[0] ) > 5) and (( boundIdentifiers[1] ) < 10)) else False)\nprint(t100.PyContains((7,7)))\nt101 = MypyPyCondSet(lambda boundIdentifiers : True if (P.NAT().PyContains(boundIdentifiers)) else False)\n\'\'\'\n",0);
			
			Writer.close();
		}
	}
	
	//Methods
	
	//MyPy Path Dependencies
	public void MypyPathDependencies() throws IOException {
		//Generate mypy.ini File
		
		File contextFile = new File(OutputLocation + "mypy.ini");
		boolean FileCreatedSuccessfully=contextFile.createNewFile();
		
		//Write Dependencies if the File was created successfully.
		if(FileCreatedSuccessfully) {
			
			Writer = new FileWriter(contextFile);
			
			WriteLine("[mypy]", 0);
			WriteLine("mypy_path = ..", 0);
			
			Writer.close();
		}
	}
	
	//Translate a Context
	public void translateMachine(PyAST_Machine machine) throws IOException {
		//Generate proper Output Context File.

		File machineFile = new File(OutputLocation + machine.Name + "_mch.py");
		boolean FileCreatedSuccessfully=machineFile.createNewFile();
		
		//Initiate Translation if the File was created successfully.
		if(FileCreatedSuccessfully) {
			
			Writer = new FileWriter(machineFile);
			
			//Introduction and Declaration of a Context
			translateMachineIntro(machine,0);
			
			//Translate Constructor (Variables Declaration)
			translateMachineConstructor(machine,1);
			
			//Translate Machine Get Methods
			translateMachineGetMethods(machine,1);
			
			//Translate Variant Method
			translateVariant(machine,1);
			
			//Translate Invariants Methods
			translateInvariants(machine,1);
			
			//Translate CheckAllInvariants Method
			translateCheckAllInvariantsMethod(machine,1);
			
			//Translate Events
			translateEvents(machine,1);
			
			//Translate User/Debugging Functions
			translateUserDebuggingFunctions(null, machine,1);
			
			Writer.close();
		}
	}
	
	//Translate a Context
	public void translateContext(PyAST_Context context) throws IOException {
		//Generate proper Output Context File.

		File contextFile = new File(OutputLocation + context.Name + "_ctx.py");
		boolean FileCreatedSuccessfully=contextFile.createNewFile();
		
		//Initiate Translation if the File was created successfully.
		if(FileCreatedSuccessfully) {
			
			Writer = new FileWriter(contextFile);
			
			//Introduction and Declaration of a Context
			translateContextIntro(context,0);
			
			//Translate Constructor (Constants Declaration)
			translateContextConstructor(context,1);
			
			//Translate Context Get Methods
			translateContextGetSetMethods(context,1);
			
			//Translate Axioms Methods
			translateAxioms(context,1);
			
			//Translate Initialization Methods
			translateContextInitializationMethods(context, 1);
			
			//Translate User/Debugging Functions
			translateUserDebuggingFunctions(context, null, 1);
			
			Writer.close();
		}
	}
	
	public String translatePredicate(PyAST_Predicate currentPredicate) throws IOException {
		StringBuilder predicate = new StringBuilder();
		
		switch(currentPredicate.CorePredicate) {
		case "Assignment":
			PyAST_Assignment assignmentPredicate = (PyAST_Assignment) currentPredicate;
			
			switch(assignmentPredicate.AssignmentType) {
			case "BecomesEqualTo":
				predicate.append(translateExpression(assignmentPredicate.LeftSide));
				predicate.append(" = ");
				predicate.append(translateExpression(assignmentPredicate.RightSide));
				break;
			case "BecomesMemberOf":
				predicate.append(translateExpression(assignmentPredicate.LeftSide));
				predicate.append(" = ");
				
				if(!FlagIfParenthesis(assignmentPredicate.RightSide.CoreExpression))
					predicate.append("(");
				predicate.append(translateExpression(assignmentPredicate.RightSide));
				if(!FlagIfParenthesis(assignmentPredicate.RightSide.CoreExpression))
					predicate.append(")");
				
				predicate.append(".PyChoice()");
				break;
			case "BecomesSuchThat":
				CurrentQuantified.add(1); 
				predicate.append(translateExpression(assignmentPredicate.LeftSide));
				predicate.append(" = ");
				
				predicate.append(PreludeName + ".BecomesSuchThat");
				predicate.append("((lambda " + QuantifiedBoundIdentifiersName + " : ");
				predicate.append(translatePredicate(assignmentPredicate.PredicateSide));
				predicate.append(") , \"");
				
				predicate.append(VariableTypesDP.get(assignmentPredicate.LeftSide.IdentifierName));
				
				predicate.append("\") ");

				CurrentQuantified.pop(); 
				break;
			default:
				predicate.append(" ErrorOutputHandlerTranslatePredicateAssignment ");
			}
			
			break;
		case "BinaryPredicate":
			PyAST_BinaryPredicate binaryPredicate = (PyAST_BinaryPredicate) currentPredicate;
			
			predicate.append(PreludeClassName + "." + binaryPredicate.BinaryPredicate);
			predicate.append("(");
			predicate.append(translatePredicate(binaryPredicate.LeftSide));
			predicate.append(", ");
			predicate.append(translatePredicate(binaryPredicate.RightSide));
			predicate.append(")");
			
			break;
		case "SimplePredicate":
			PyAST_SimplePredicate simplePredicate = (PyAST_SimplePredicate)currentPredicate;
			
			switch(simplePredicate.SimpleType) {
			case "Finite":
				
				if(!FlagIfParenthesis(simplePredicate.InternalExpression.CoreExpression))
					predicate.append("(");
				predicate.append(translateExpression(simplePredicate.InternalExpression));
				if(!FlagIfParenthesis(simplePredicate.InternalExpression.CoreExpression))
					predicate.append(")");
				predicate.append(".PyFinite()");
				
				break;
			default:
				predicate.append(" ErrorOutputHandlerTranslatePredicateSimplePredicate ");
			}
			
			break;
		case "UnaryPredicate":
			PyAST_UnaryPredicate unaryPredicate = (PyAST_UnaryPredicate)currentPredicate;
			
			switch(unaryPredicate.UnaryType) {
			case "Not":
				predicate.append("not(");
				predicate.append(translatePredicate(unaryPredicate.InternalPredicate));
				predicate.append(")");
				break;
			default:
				predicate.append(" ErrorOutputHandlerTranslatePredicateUnaryPredicate ");
			}
			
			break;
		case "LiteralPredicate":
			PyAST_LiteralPredicate literalPredicate = (PyAST_LiteralPredicate)currentPredicate;
			
			switch(literalPredicate.LiteralType) {
			case "True":
				predicate.append("True");
				break;
			case "False":
				predicate.append("False");
				break;
			default:
				predicate.append(" ErrorOutputHandlerTranslatePredicateLiteralPredicate ");
			}
			
			break;
		case "MultiplePredicate":
			PyAST_MultiplePredicate multiplePredicate = (PyAST_MultiplePredicate)currentPredicate;
			
			if(!FlagIfParenthesis(multiplePredicate.SetToCheck.CoreExpression))
				predicate.append("(");
			predicate.append(translateExpression(multiplePredicate.SetToCheck));
			if(!FlagIfParenthesis(multiplePredicate.SetToCheck.CoreExpression))
				predicate.append(")");
			
			predicate.append(".PyPartition([");
			
			boolean firstPartition=true;
			for(PyAST_Expression child : multiplePredicate.Children) {
				if(firstPartition) {
					firstPartition=false;
					predicate.append(translateExpression(child));
				}
				else {
					predicate.append(", ");
					predicate.append(translateExpression(child));
				}
			}
			
			predicate.append("])");
			
			break;
		case "RelationalPredicate":
			PyAST_RelationalPredicate relationalPredicate = (PyAST_RelationalPredicate)currentPredicate;
			
			switch(relationalPredicate.RelationType) {
			case "Equal":
				if(!FlagIfParenthesis(relationalPredicate.LeftSide.CoreExpression))
					predicate.append("(");
				predicate.append(translateExpression(relationalPredicate.LeftSide));
				if(!FlagIfParenthesis(relationalPredicate.LeftSide.CoreExpression))
					predicate.append(")");
				predicate.append(" == ");
				if(!FlagIfParenthesis(relationalPredicate.RightSide.CoreExpression))
					predicate.append("(");
				predicate.append(translateExpression(relationalPredicate.RightSide));
				if(!FlagIfParenthesis(relationalPredicate.RightSide.CoreExpression))
					predicate.append(")");
				break;
			case "NotEqual":
				if(!FlagIfParenthesis(relationalPredicate.LeftSide.CoreExpression))
					predicate.append("(");
				predicate.append(translateExpression(relationalPredicate.LeftSide));
				if(!FlagIfParenthesis(relationalPredicate.LeftSide.CoreExpression))
					predicate.append(")");
				predicate.append(" != ");
				if(!FlagIfParenthesis(relationalPredicate.RightSide.CoreExpression))
					predicate.append("(");
				predicate.append(translateExpression(relationalPredicate.RightSide));
				if(!FlagIfParenthesis(relationalPredicate.RightSide.CoreExpression))
					predicate.append(")");
				break;
			case "LessThan":
				if(!FlagIfParenthesis(relationalPredicate.LeftSide.CoreExpression))
					predicate.append("(");
				predicate.append(translateExpression(relationalPredicate.LeftSide));
				if(!FlagIfParenthesis(relationalPredicate.LeftSide.CoreExpression))
					predicate.append(")");
				predicate.append(" < ");
				if(!FlagIfParenthesis(relationalPredicate.RightSide.CoreExpression))
					predicate.append("(");
				predicate.append(translateExpression(relationalPredicate.RightSide));
				if(!FlagIfParenthesis(relationalPredicate.RightSide.CoreExpression))
					predicate.append(")");
				break;
			case "LessOrEqual":
				if(!FlagIfParenthesis(relationalPredicate.LeftSide.CoreExpression))
					predicate.append("(");
				predicate.append(translateExpression(relationalPredicate.LeftSide));
				if(!FlagIfParenthesis(relationalPredicate.LeftSide.CoreExpression))
					predicate.append(")");
				predicate.append(" <= ");
				if(!FlagIfParenthesis(relationalPredicate.RightSide.CoreExpression))
					predicate.append("(");
				predicate.append(translateExpression(relationalPredicate.RightSide));
				if(!FlagIfParenthesis(relationalPredicate.RightSide.CoreExpression))
					predicate.append(")");
				break;
			case "GreaterThan":
				if(!FlagIfParenthesis(relationalPredicate.LeftSide.CoreExpression))
					predicate.append("(");
				predicate.append(translateExpression(relationalPredicate.LeftSide));
				if(!FlagIfParenthesis(relationalPredicate.LeftSide.CoreExpression))
					predicate.append(")");
				predicate.append(" > ");
				if(!FlagIfParenthesis(relationalPredicate.RightSide.CoreExpression))
					predicate.append("(");
				predicate.append(translateExpression(relationalPredicate.RightSide));
				if(!FlagIfParenthesis(relationalPredicate.RightSide.CoreExpression))
					predicate.append(")");
				break;
			case "GreaterOrEqual":
				if(!FlagIfParenthesis(relationalPredicate.LeftSide.CoreExpression))
					predicate.append("(");
				predicate.append(translateExpression(relationalPredicate.LeftSide));
				if(!FlagIfParenthesis(relationalPredicate.LeftSide.CoreExpression))
					predicate.append(")");
				predicate.append(" >= ");
				if(!FlagIfParenthesis(relationalPredicate.RightSide.CoreExpression))
					predicate.append("(");
				predicate.append(translateExpression(relationalPredicate.RightSide));
				if(!FlagIfParenthesis(relationalPredicate.RightSide.CoreExpression))
					predicate.append(")");
				break;
			case "In":
				predicate.append(translateExpression(relationalPredicate.RightSide));
				predicate.append(".PyContains(");
				predicate.append(translateExpression(relationalPredicate.LeftSide));
				predicate.append(")");
				break;
			case "NotIn":
				predicate.append(translateExpression(relationalPredicate.RightSide));
				predicate.append(".PyNotContains(");
				predicate.append(translateExpression(relationalPredicate.LeftSide));
				predicate.append(")");
				break;
			case "Subset":
				predicate.append(translateExpression(relationalPredicate.LeftSide));
				predicate.append(".PyIsProperSubset(");
				predicate.append(translateExpression(relationalPredicate.RightSide));
				predicate.append(")");
				break;
			case "NotSubset":
				predicate.append(translateExpression(relationalPredicate.LeftSide));
				predicate.append(".PyNotProperSubset(");
				predicate.append(translateExpression(relationalPredicate.RightSide));
				predicate.append(")");
				break;
			case "SubsetEq":
				predicate.append(translateExpression(relationalPredicate.LeftSide));
				predicate.append(".PyIsSubset(");
				predicate.append(translateExpression(relationalPredicate.RightSide));
				predicate.append(")");
				break;
			case "NotSubsetEq":
				predicate.append(translateExpression(relationalPredicate.LeftSide));
				predicate.append(".PyNotSubset(");
				predicate.append(translateExpression(relationalPredicate.RightSide));
				predicate.append(")");
				break;
			default:
				predicate.append(relationalPredicate.RelationType + " ErrorTranslatePredicate ");
			}
			
			break;
		case "QuantifiedPredicate":
			PyAST_QuantifiedPredicate quantifiedPredicate = (PyAST_QuantifiedPredicate) currentPredicate;
			CurrentQuantified.add(0); 
			
			predicate.append(PreludeName + "." + quantifiedPredicate.OperatorSymbol);
			predicate.append("( (lambda " + QuantifiedBoundIdentifiersName + " : ");
			predicate.append(translatePredicate(quantifiedPredicate.InternalPredicate));
			predicate.append(") , [ ");
			
			//predicate.append(translateConstantType(binaryPredicate.));
			for( int i = 0; i < quantifiedPredicate.BoundIdentDeclAmount; i++) {
				if(i==0) {
					predicate.append("(" + String.valueOf(i) + ",\"" + translateConstantType(quantifiedPredicate.BoundIdentDeclsAndTypes[i]) + "\")");
				}
				else {
					predicate.append(" , (" + String.valueOf(i) + ",\"" + translateConstantType(quantifiedPredicate.BoundIdentDeclsAndTypes[i]) + "\")");
				}
			}
			
			predicate.append(" ] ) ");
			
			CurrentQuantified.pop();
			break;
		case "AssociativePredicate":
			PyAST_AssociativePredicate associativePredicate = (PyAST_AssociativePredicate)currentPredicate;

			predicate.append("(");
			boolean firstChild=true;
			for(PyAST_Predicate child : associativePredicate.Children) {
				if(firstChild) {
					firstChild=false;
					
					//The if is only to make the Output more readable.
					if(FlagIfParenthesis(child.CorePredicate))
						predicate.append(translatePredicate(child));
					else
						predicate.append("(" + translatePredicate(child) + ")");
				}
				else {
					predicate.append(" " + associativePredicate.OperatorSymbol + " ");
					
					//This is only to make the Output more readable.
					if(FlagIfParenthesis(child.CorePredicate))
						predicate.append(translatePredicate(child));
					else
						predicate.append("(" + translatePredicate(child) + ")");
				}
			}
			predicate.append(")");
			break;
		default:
			predicate.append(" ErrorTranslatePredicate ");
		}
		
		return predicate.toString();
	}
	
	public String translateExpression(PyAST_Expression currentExpression) throws IOException {
		StringBuilder expression = new StringBuilder();
		
		switch(currentExpression.CoreExpression) {
		case "AtomicExpression":
			PyAST_AtomicExpression atomicExpression = (PyAST_AtomicExpression)currentExpression;
			expression.append(atomicExpression.AtomicExpressionTranslation);
			break;
		case "FreeIdentifier":
			PyAST_FreeIdentifier freeIdentifier = (PyAST_FreeIdentifier)currentExpression;
			
			if(freeIdentifier.IndentifierDependencies.size()==0)
				expression.append("self." + freeIdentifier.IdentifierName);
			else {
				expression.append("self.");
				for(LinkedList<String> dependency : freeIdentifier.IndentifierDependencies) {
					if(dependency.get(1).equals("ContextDependency"))
						expression.append(dependency.get(0) + "_get().");
					//else unnecessary since the attributes handling won't be OOP, rather properties
					//else if(dependency.get(1).equals("MachineDependency"))
						//expression.append("_" + dependency.get(0) + ".");
				}
				expression.append(freeIdentifier.IdentifierName);
			}
			break;
		case "IntegerLiteral":
			PyAST_IntegerLiteral integerLiteral = (PyAST_IntegerLiteral)currentExpression;
			expression.append(integerLiteral.IntegerValue);
			break;
		case "UnaryExpression":
			PyAST_UnaryExpression unaryExpression = (PyAST_UnaryExpression)currentExpression;
			
			if(unaryExpression.UnaryExpression.equals("Cardinality") || unaryExpression.UnaryExpression.equals("Minimum") || unaryExpression.UnaryExpression.equals("Maximum")) {
				expression.append(unaryExpression.OperatorSymbol + "(");
				expression.append(translateExpression(unaryExpression.InternalExpression));
				expression.append(")");
			}
			else if(unaryExpression.UnaryExpression.equals("Inverse") || unaryExpression.UnaryExpression.equals("UnaryMinus")) {
				if(FlagIfParenthesis(unaryExpression.InternalExpression.CoreExpression)) {
					expression.append(unaryExpression.OperatorSymbol);
					expression.append(translateExpression(unaryExpression.InternalExpression));
				}
				else {
					expression.append(unaryExpression.OperatorSymbol + "(");
					expression.append(translateExpression(unaryExpression.InternalExpression));
					expression.append(")");
				}
			}
			else {
				expression.append(translateExpression(unaryExpression.InternalExpression));
				expression.append(unaryExpression.OperatorSymbol);
			}
				
			break;
		case "QuantifiedExpression":
			PyAST_QuantifiedExpression quantifiedExpression = (PyAST_QuantifiedExpression)currentExpression;
			CurrentQuantified.add(quantifiedExpression.BoundIdentDeclAmount); 
			
			expression.append("MypyPyCondSet(");
			expression.append("lambda " + QuantifiedBoundIdentifiersName + " : True if (");
			expression.append(translatePredicate(quantifiedExpression.InternalPredicate));
			expression.append(") else False)");
			
			CurrentQuantified.pop();
			break;
		case "BinaryExpression":
			PyAST_BinaryExpression binaryExpression = (PyAST_BinaryExpression)currentExpression;
			
			String bin_exp_op = binaryExpression.BinaryOperation;
			
			if(bin_exp_op.equals("Tuple")) {
				expression.append("(");
				expression.append(translateExpression(binaryExpression.LeftSide));
				expression.append(binaryExpression.OperatorSymbol + " ");
				expression.append(translateExpression(binaryExpression.RightSide));
				expression.append(")");
			}
			else if(bin_exp_op.equals("DomainRestriction") ||
					bin_exp_op.equals("DomainSubstraction")) {
				
				
				if(FlagIfParenthesis(binaryExpression.RightSide.CoreExpression))
					expression.append(translateExpression(binaryExpression.RightSide));
				else
					expression.append("(" + translateExpression(binaryExpression.RightSide) + ")");
				
				
				expression.append(binaryExpression.OperatorSymbol + "(");
				expression.append(translateExpression(binaryExpression.LeftSide));
				expression.append(")");
			}
			else if(bin_exp_op.equals("Difference") ||
					bin_exp_op.equals("CartesianProduct") ||
					bin_exp_op.equals("DirectProduct") ||
					bin_exp_op.equals("RangeRestriction") ||
					bin_exp_op.equals("RangeSubstraction")) {
				
				
				if(FlagIfParenthesis(binaryExpression.LeftSide.CoreExpression))
					expression.append(translateExpression(binaryExpression.LeftSide));
				else
					expression.append("(" + translateExpression(binaryExpression.LeftSide) + ")");
				
				
				expression.append(binaryExpression.OperatorSymbol + "(");
				expression.append(translateExpression(binaryExpression.RightSide));
				expression.append(")");
			}
			else if(bin_exp_op.equals("UpTo")) {
				expression.append("PySet({int_range for int_range in range(");
				expression.append(translateExpression(binaryExpression.LeftSide));
				expression.append(binaryExpression.OperatorSymbol + " ");
				expression.append(translateExpression(binaryExpression.RightSide));
				expression.append("+1)})");
			}
			else if(bin_exp_op.equals("Minus") ||
					bin_exp_op.equals("Division") ||
					bin_exp_op.equals("Mod") ||
					bin_exp_op.equals("Exponentiation")) {
				
				expression.append("(");
				expression.append(translateExpression(binaryExpression.LeftSide));
				expression.append(" " + binaryExpression.OperatorSymbol + " ");
				expression.append(translateExpression(binaryExpression.RightSide));
				expression.append(")");
				
				/*
				if(FlagIfParenthesis(binaryExpression.LeftSide.CoreExpression))
					expression.append(translateExpression(binaryExpression.LeftSide));
				else
					expression.append("(" + translateExpression(binaryExpression.LeftSide) + ")");
				
				expression.append(" " + binaryExpression.OperatorSymbol + " ");
				
				if(FlagIfParenthesis(binaryExpression.RightSide.CoreExpression))
					expression.append(translateExpression(binaryExpression.RightSide));
				else
					expression.append("(" + translateExpression(binaryExpression.RightSide) + ")");
				*/
			}
			else if(bin_exp_op.equals("Apply")) {
				if(FlagIfParenthesis(binaryExpression.LeftSide.CoreExpression))
					expression.append(translateExpression(binaryExpression.LeftSide));
				else
					expression.append("(" + translateExpression(binaryExpression.LeftSide) + ")");
				
				expression.append("(");
				expression.append(translateExpression(binaryExpression.RightSide));
				expression.append(")");
			}
			else if(bin_exp_op.equals("RelationalImage")) {
				if(FlagIfParenthesis(binaryExpression.LeftSide.CoreExpression))
					expression.append(translateExpression(binaryExpression.LeftSide));
				else
					expression.append("(" + translateExpression(binaryExpression.LeftSide) + ")");
				
				expression.append("[");
				expression.append(translateExpression(binaryExpression.RightSide));
				expression.append("]");
			}
			else {
				expression.append("PyFamilies(PyFamilyTypes.");
				expression.append(binaryExpression.OperatorSymbol);
				expression.append(", ");
				expression.append(translateExpression(binaryExpression.LeftSide));
				expression.append(", ");
				expression.append(translateExpression(binaryExpression.RightSide));
				expression.append(")");
			}

			break;
		case "BoundIdentifier":
			PyAST_BoundIdentifier boundIdentifier = (PyAST_BoundIdentifier) currentExpression;
			expression.append(QuantifiedBoundIdentifiersName);
			
			Integer current_quantified = CurrentQuantified.peek();
			if(current_quantified==0) {
				expression.append("[" + String.valueOf(boundIdentifier.BoundIdentifierIndex) + "]");
			}
			else {
				if(current_quantified==2) {
					expression.append("[" + String.valueOf(1-boundIdentifier.BoundIdentifierIndex) + "]");
				}
			}
			
			break;
		case "SetExtension":
			PyAST_SetExtension setExtension = (PyAST_SetExtension)currentExpression;
			
			boolean flag_if_relation = false;
			
			PyAST_BinaryExpression inner_bin_exp;
			for(int i = 0; i<setExtension.MembersAmount; i++) {
				if(setExtension.Members[i].CoreExpression.equals("BinaryExpression")) {
					inner_bin_exp = (PyAST_BinaryExpression)setExtension.Members[i];
					if(inner_bin_exp.BinaryOperation.equals("Tuple")) {
						flag_if_relation = true;
						break;
					}
				}
			}
			
			if(flag_if_relation) {
				expression.append("PyRel({");
			}
			else {
				expression.append("PySet({");
			}
			
			for(int i = 0; i<setExtension.MembersAmount; i++) {
				if(i==0) {
					expression.append(translateExpression(setExtension.Members[i]));
				}
				else {
					expression.append(", ");
					expression.append(translateExpression(setExtension.Members[i]));
				}
			}
			
			expression.append("})");
			
			break;
		case "AssociativeExpression":
			PyAST_AssociativeExpression associativeExpression = (PyAST_AssociativeExpression)currentExpression;
			if(associativeExpression.AssociativeExpression.equals("Addition") || associativeExpression.AssociativeExpression.equals("Multiplication")) {
				expression.append("(");
			}

			boolean firstChild=true;
			for(PyAST_Expression child : associativeExpression.Children) {
				if(firstChild) {
					firstChild=false;
					
					//This is is only to make the Output more readable.
					if(FlagIfParenthesis(child.CoreExpression))
						expression.append(translateExpression(child));
					else
						expression.append("(" + translateExpression(child) + ")");
				}
				else {
					
					if(associativeExpression.AssociativeExpression.equals("Addition") || associativeExpression.AssociativeExpression.equals("Multiplication")) {
					
						expression.append(" " + associativeExpression.OperatorSymbol + " ");
						
						//This is only to make the Output more readable.
						if(FlagIfParenthesis(child.CoreExpression))
							expression.append(translateExpression(child));
						else
							expression.append("(" + translateExpression(child) + ")");
					}
					else {
						expression.append("." + associativeExpression.OperatorSymbol + "(");
						expression.append(translateExpression(child));
						expression.append(")");
					}
				}
			}
			if(associativeExpression.AssociativeExpression.equals("Addition") || associativeExpression.AssociativeExpression.equals("Multiplication")) {
				expression.append(")");
			}
			break;
		default:
			expression.append(currentExpression.CoreExpression + "ErrorTranslateExpression");
		}
		
		return expression.toString();
	}
	
	public void translateMachineGetMethods(PyAST_Machine machine,int identation) throws IOException {
		
		//Include Get Method of Context Extension if there is one.
		if(machine.HasMachineInternalContext) {
			BlankLines(1);
			WriteLine("#Internal Context Dependency Object Get Method",identation);
			
			BlankLines(1);
			WriteLine("def " + machine.MachineInternalContext.Name + "_get(self) -> " + machine.MachineInternalContext.Name + "_class:",identation);
			WriteLine("return self.__" + machine.MachineInternalContext.Name,identation+1);
		}
		
		//Variables Get/Set Methods
		BlankLines(1);
		WriteLine("#Variables Get/Set Methods",identation);
		
		ArrayList<PyAST_Variable> orderedVariables = new ArrayList<PyAST_Variable>(machine.Variables.values());
		Collections.sort(orderedVariables,VariableComparator);
		for(PyAST_Variable variable : orderedVariables) {
			
			//Check whether the Type of the Variable was already translated (surely it did).
			String translationVariableType;
			if(variable.VariableTypeTranslated) translationVariableType = variable.VariableTypeTranslation;
			else {
				translationVariableType = translateConstantType(variable.VariableType);
				variable.VariableTypeTranslated=true;
				variable.VariableTypeTranslation = translationVariableType;
			}
			
			BlankLines(1);
			WriteLine("@property",identation);
			WriteLine("def " + variable.VariableName + "(self) -> " + translationVariableType +":",identation);
			WriteLine("return self.__" + variable.VariableName,identation+1);
			BlankLines(1);
			WriteLine("@" + variable.VariableName +".setter",identation);
			WriteLine("def " + variable.VariableName + "(self, " + variable.VariableName + "_userIn : " + translationVariableType +") -> None:",identation);
			WriteLine("self.__" + variable.VariableName + " : " + translationVariableType + " = " + variable.VariableName + "_userIn",identation+1);
		}
		
		BlankLines(1);
		WriteLine("#End Variables Get Methods",identation);
	}
	
	public void translateContextGetSetMethods(PyAST_Context context,int identation) throws IOException {
		
		//Include Get/Set Method of Context Extension if there is one.
		if(context.HasContextExtension) {
			BlankLines(1);
			WriteLine("#Context Extended Dependency Object Get Method",identation);
			
			BlankLines(1);
			WriteLine("def " + context.ContextExtension.Name + "_get(self) -> " + context.ContextExtension.Name + "_class:",identation);
			WriteLine("return self.__" + context.ContextExtension.Name,identation+1);
		}
		
		//Initialized_Context Flag Attribute Get Method
		BlankLines(1);
		WriteLine("#Initialized_Context Flag Attribute Get Method",identation);
		WriteLine("def Initialized_ContextGetMethod(self) -> bool:",identation);
		WriteLine("return self.__Initialized_Context",identation+1);
		
		//CarrierSets Get/Set Methods
		BlankLines(1);
		WriteLine("#CarrierSets Get/Set Methods",identation);
		
		ArrayList<PyAST_CarrierSet> orderedCarrierSets = new ArrayList<PyAST_CarrierSet>(context.CarrierSets.values());
		Collections.sort(orderedCarrierSets,CarrierSetComparator);
		for(PyAST_CarrierSet carrierSet : orderedCarrierSets) {
			
			BlankLines(1);
			WriteLine("@property",identation);
			WriteLine("def " + carrierSet.CarrierSetName + "(self) -> PySet[" + carrierSet.CarrierSetName +"_CS]:",identation);
			WriteLine("return self.__" + carrierSet.CarrierSetName,identation+1);
			BlankLines(1);
			WriteLine("@" + carrierSet.CarrierSetName +".setter",identation);
			WriteLine("def " + carrierSet.CarrierSetName + "(self, " + carrierSet.CarrierSetName + "_userIn : PySet[" + carrierSet.CarrierSetName +"_CS]) -> None:",identation);
			WriteLine("if self.__Attributes_SetFlag == False: raise Exception(\"Changing the state of this Context is disabled.\")",identation+1);
			WriteLine("self.__" + carrierSet.CarrierSetName + " : " + "PySet[" + carrierSet.CarrierSetName +"_CS]" + " = " + carrierSet.CarrierSetName + "_userIn",identation+1);
		}
		
		BlankLines(1);
		WriteLine("#End CarrierSets Get/Set Methods",identation);
		
		//Constants Get/Set Methods
		BlankLines(1);
		WriteLine("#Constants Get/Set Methods",identation);
		
		ArrayList<PyAST_Constant> orderedConstants = new ArrayList<PyAST_Constant>(context.Constants.values());
		Collections.sort(orderedConstants,ConstantComparator);
		for(PyAST_Constant constant : orderedConstants) {
			
			//Check whether the Type of the Constant was already translated (surely it did).
			String translationConstantType;
			if(constant.ConstantTypeTranslated) translationConstantType = constant.ConstantTypeTranslation;
			else {
				translationConstantType = translateConstantType(constant.ConstantType);
				constant.ConstantTypeTranslated=true;
				constant.ConstantTypeTranslation = translationConstantType;
			}
			
			BlankLines(1);
			WriteLine("@property",identation);
			WriteLine("def " + constant.ConstantName + "(self) -> " + translationConstantType +":",identation);
			WriteLine("return self.__" + constant.ConstantName,identation+1);
			BlankLines(1);
			WriteLine("@" + constant.ConstantName +".setter",identation);
			WriteLine("def " + constant.ConstantName + "(self, " + constant.ConstantName + "_userIn : " + translationConstantType +") -> None:",identation);
			WriteLine("if self.__Attributes_SetFlag == False: raise Exception(\"Changing the state of this Context is disabled.\")",identation+1);
			WriteLine("self.__" + constant.ConstantName + " : " + translationConstantType + " = " + constant.ConstantName + "_userIn",identation+1);
		}
		
		BlankLines(1);
		WriteLine("#End Constants Get Methods",identation);
	}
	
	public void translateContextInitializationMethods(PyAST_Context context,int identation) throws IOException {
		
		BlankLines(1);
		WriteLine("#Checked Initialization Method",identation);
		
		//CHECKED INIT
		
		WriteSomething("def checkedInit(self", identation);
		
		//Include Context Extension if it exists.
		if(context.HasContextExtension)
			WriteSomething(" , " + context.ContextExtension.Name + "_userIn : " + context.ContextExtension.Name + "_class = " + context.ContextExtension.Name + "_class()",0);
		
		//Ordered Constants
		ArrayList<PyAST_Constant> orderedConstants = new ArrayList<PyAST_Constant>(context.Constants.values());
		Collections.sort(orderedConstants,ConstantComparator);
		
		//Constant Parameters
		for(PyAST_Constant constant : orderedConstants) {
			
			//Check whether the Type of the Constant was already translated (surely it did).
			String currentConstantTypeTranslation;
			if(constant.ConstantTypeTranslated)currentConstantTypeTranslation=constant.ConstantTypeTranslation;
			else {
				currentConstantTypeTranslation = translateConstantType(constant.ConstantType);
				constant.ConstantTypeTranslated = true;
				constant.ConstantTypeTranslation = currentConstantTypeTranslation;
			}
			WriteSomething(", " + constant.ConstantName + "_userIn : " + currentConstantTypeTranslation + " = " + PreludeName + ".NoParam()", 0);
		}
		
		WriteLine(" ) -> None:", 0);
		
		//PyRandValGen for every parameter that had no value specified.
		BlankLines(1);
		for(PyAST_Constant constant : orderedConstants) {
			WriteLine("if " + constant.ConstantName + "_userIn is None:",identation+1);
			WriteLine(constant.ConstantName + "_userIn = " + PreludeName + ".PyRandValGen(\"" + constant.ConstantTypeTranslation + "\")", identation+2);
		}
		
		//Avoid Initializing more than once
		BlankLines(1);
		WriteLine("if self.__Initialized_Context: raise Exception(\"Context already initialized!\")",identation+1);
		WriteLine("self.__Initialized_Context = True", identation+1);
		
		//Enable Attributes Set Method
		BlankLines(1);
		WriteLine("#Enable Attributes Set Method", identation+1);
		WriteLine("self.__Attributes_SetFlag = True",identation+1);
		
		
		//Assign Parameters to Constants
		
		if(context.HasContextExtension) {
			BlankLines(1);
			WriteLine("#Assign Parameter to Context Extended Dependency Object",identation+1);
			WriteLine("self.__" + context.ContextExtension.Name + " = " + context.ContextExtension.Name + "_userIn",identation+1);
			WriteLine("if not(self.__" + context.ContextExtension.Name + ".Initialized_ContextGetMethod()):",identation+1);
			WriteLine("self.__" + context.ContextExtension.Name + ".checkedInit()",identation+2);
		}
		
		BlankLines(1);
		for(PyAST_Constant constant : orderedConstants) {
			WriteLine("self." + constant.ConstantName + " = " + constant.ConstantName + "_userIn",identation+1);
		}
		
		// DESING BY CONTRACT
		
		BlankLines(1);
		WriteLine("if P.DESIGN_BY_CONTRACT_ENABLED():", identation+1);
		WriteLine("attempt_Count : int = 0", identation+2);
		WriteLine("while not(self.checkAllAxioms()):",identation+2);
		
		for(PyAST_Constant constant : orderedConstants) {
			WriteLine("self." + constant.ConstantName + " = " + PreludeName + ".PyRandValGen(\"" + constant.ConstantTypeTranslation + "\")",identation+3);
		}
		
		WriteLine("if attempt_Count == " + PreludeName + ".HIGHMAXGENATTEMPTS():",identation+3);
		WriteLine("raise Exception(\"Initialization could not satisfy the Axioms!\")",identation+4);
		WriteLine("attempt_Count += 1", identation+3);
		
		//Disable Attributes Set Method
		BlankLines(1);
		WriteLine("#Disable Attributes Set Method", identation+1);
		WriteLine("self.__Attributes_SetFlag = False",identation+1);
	}
	
	public void translateEvents(PyAST_Machine machine,int identation) throws IOException {
		
		//Support Variables
		boolean flagFirst;
		String[] actionsList;
		String[] actionsLeftList;
		String[] actionsRightList;

		BlankLines(1);
		WriteLine("#Events",identation);
		
		ArrayList<PyAST_Event> events = new ArrayList<PyAST_Event>(machine.Events.values());
		for(PyAST_Event event : events) {
			
			BlankLines(1);
			WriteLine("#" + event.EventLabel + " - Event",identation);
			
			//EVENT GUARDS
			
			BlankLines(1);
			WriteSomething("def " + event.EventLabel + "_eventGuards(self",identation);
			
			for(PyAST_Variable parameter : event.EventParameters)
				WriteSomething(", " + parameter.VariableName + "_userIn : " + translateConstantType(parameter.VariableType),0);
			
			WriteLine(") -> bool:",0);
			
			WriteLine("guard_ans : bool = True",identation+1);
			
			//SET PARAMETERS AS AN ATTRIBUTE
			BlankLines(1);
			WriteLine("#Set Parameters as an Attribute.",identation+1);
			for(PyAST_Variable parameter : event.EventParameters)
				WriteLine("self." + parameter.VariableName + " : " + translateConstantType(parameter.VariableType) + " = " + parameter.VariableName + "_userIn",identation+1);
			
			//CHECK PRECONDITIONS
			BlankLines(1);
			WriteLine("#Check Event PreConditions.",identation+1);
			WriteLine("if " + PreludeName + ".DESIGN_BY_CONTRACT_ENABLED():",identation+1);
			
			WriteLine("try:",identation+2);
			
			WriteSomething("if True",identation+3);
			for(PyAST_Predicate guard : event.EventGuards)
				WriteSomething(" and (" + translatePredicate(guard) + ")",0);
			WriteLine(":",0);
			
			WriteLine("guard_ans = True",identation+4);
			WriteLine("else:",identation+3);
			WriteLine("guard_ans = False",identation+4);
			
			WriteLine("except:",identation+2);
			WriteLine("guard_ans = False",identation+3);
			
			
			WriteLine("else:",identation+1);
			WriteLine("guard_ans = True",identation+2);
			
			//DELETE PARAMETERS AND RETURN GUARD RESULT
			BlankLines(1);
			for(PyAST_Variable parameter : event.EventParameters)
				WriteLine("del(self." + parameter.VariableName + ")",identation+1);
			
			WriteLine("return guard_ans",identation+1);
			
			//EVENT ACTIONS
			
			BlankLines(1);
			
			//SHOW CONVERGENCE IF IT IS DIFFERENT TO 'ORDINARY'
			if(event.EventConvergence.equals("Anticipated"))WriteLine("#Anticipated Event!",identation);
			else if(event.EventConvergence.equals("Convergent"))WriteLine("#Convergent Event!",identation);
			
			WriteSomething("def " + event.EventLabel + "_eventActions(self",identation);
			for(PyAST_Variable parameter : event.EventParameters)
				WriteSomething(", " + parameter.VariableName + "_userIn : " + translateConstantType(parameter.VariableType) + " = " + PreludeName + ".NoParam()",0);
			
			WriteLine(") -> None:",0);
			
			//PyRandValGen for every parameter that had no value specified.
			if(event.EventParameters.length > 0)BlankLines(1);
			for(PyAST_Variable parameter : event.EventParameters) {
				WriteLine("if " + parameter.VariableName + "_userIn is None:",identation+1);
				WriteLine(parameter.VariableName + "_userIn = " + PreludeName + ".PyRandValGen(\"" + translateConstantType(parameter.VariableType) + "\")", identation+2);
			}
			
			//CALL GUARDS AND CHECK THEM
			BlankLines(1);
			
			if(event.EventGuards.length==0) {
				WriteSomething("if not(self." + event.EventLabel + "_eventGuards(",identation+1);
				flagFirst = true;
				for(PyAST_Variable parameter : event.EventParameters) {
					if(flagFirst) {
						WriteSomething(parameter.VariableName + "_userIn",0);
						flagFirst = false;
					}
					else WriteSomething(", " + parameter.VariableName + "_userIn",0);
				}
				WriteLine(")):",0);
				
				WriteLine("raise GuardsViolated(\"Guards of the Event could not be fulfilled.\")",identation+2);
			}
			else {
				WriteLine("attempt_Count : int = 0",identation+1);
				WriteSomething("while not(self." + event.EventLabel + "_eventGuards(",identation+1);
				flagFirst = true;
				for(PyAST_Variable parameter : event.EventParameters) {
					if(flagFirst) {
						WriteSomething(parameter.VariableName + "_userIn",0);
						flagFirst = false;
					}
					else WriteSomething(", " + parameter.VariableName + "_userIn",0);
				}
				WriteLine(")):",0);
				
				for(PyAST_Variable parameter : event.EventParameters)
					WriteLine(parameter.VariableName + "_userIn = " + PreludeName + ".PyRandValGen(\"" + translateConstantType(parameter.VariableType) + "\")",identation+2);
				
				WriteLine("if attempt_Count == " + PreludeName + ".LOWMAXGENATTEMPTS():",identation+2);
				WriteLine("raise GuardsViolated(\"Guards of the Event could not be fulfilled.\")",identation+3);
				WriteLine("attempt_Count += 1",identation+2);
			}
			
			//SET PARAMETERS AS AN ATTRIBUTE
			BlankLines(1);
			WriteLine("#Set Parameters as an Attribute.",identation+1);
			for(PyAST_Variable parameter : event.EventParameters)
				WriteLine("self." + parameter.VariableName + " = " + parameter.VariableName + "_userIn",identation+1);
			
			//ACTIONS
			BlankLines(1);
			WriteLine("#Event Actions",identation+1);
			
			if(event.EventConvergence.equals("Convergent")) {
				BlankLines(1);
				WriteLine("#Convergent Event: Value of the variant before the actions.",identation+1);
				WriteLine("tmp_variant_value : int = self.PyMachineVariant()",identation+1);	
			}
			
			if(event.EventActions.length>0) {
				
				BlankLines(1);
				
				actionsList = new String[event.EventActions.length];
				actionsLeftList = new String[event.EventActions.length];
				actionsRightList = new String[event.EventActions.length];
				int i=0;
				
				//Create List of Actions for Parallel Assignment.
				for(PyAST_Action action : event.EventActions) {
					actionsList[i] = translatePredicate(action.AssignmentAction);
					i+=1;
				}
				i=0;

				//Split List of Actions.
				for(String action : actionsList) {
					actionsLeftList[i] = action.split(" = ")[0];
					actionsRightList[i] = action.split(" = ")[1];
					i+=1;
				}
				
				flagFirst = true;
				for(String leftAction : actionsLeftList) {
					if(flagFirst) {
						WriteSomething(leftAction,identation+1);
						flagFirst = false;
					}
					else WriteSomething(", " + leftAction,0);
				}
				WriteSomething(" = ",0);
				
				flagFirst = true;
				for(String rightAction : actionsRightList) {
					if(flagFirst) {
						WriteSomething(rightAction,0);
						flagFirst = false;
					}
					else WriteSomething(", " + rightAction,0);
				}
				
				BlankLines(1);
			}
			
			if(event.EventConvergence.equals("Convergent")) {
				BlankLines(1);
				WriteLine("#Convergent Event: Check that the Variant decreased.",identation+1);
				WriteLine("if tmp_variant_value <= self.PyMachineVariant():",identation+1);
				WriteLine("raise Exception(\"The Variant did not decrease!\")",identation+2);
			}
			
			
			//CHECK INVARIANTS IN THE END
			BlankLines(1);
			WriteLine("#Check Invariants after the actions are executed.",identation+1);
			
			if(event.EventActions.length>0) {

				WriteLine("if " + PreludeName + ".DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):",identation+1);
				
				/*
				flagFirst = true;
				TranslatingPostCondition = true;
				for(PyAST_Action action : event.EventActions)
					if(flagFirst) {
						WriteSomething(translatePredicate(action.AssignmentAction) + ")",0);
						flagFirst = false;
					}
					else WriteSomething(" and (" + translatePredicate(action.AssignmentAction) + ")",0);
				TranslatingPostCondition = false;
				*/

				WriteLine("raise Exception(\"PostConditions of the Event could not be fulfilled.\")",identation+2);	
			}
			
			BlankLines(1);
			for(PyAST_Variable parameter : event.EventParameters)
				WriteLine("del(self." + parameter.VariableName + ")",identation+1);
			
			BlankLines(1);
			WriteLine("#End Event",identation);
		}
	}
	
	public void translateCheckAllInvariantsMethod(PyAST_Machine machine,int identation) throws IOException{
		
		BlankLines(1);
		WriteLine("#Check ALL Invariants",identation);
		BlankLines(1);
		WriteLine("def checkAllInvariants(self) -> bool:",identation);
		WriteLine("checkedAns_local : bool = True",identation+1);
		WriteLine("allInvariants_local : List[str] = " + translateSetToList(machine.Invariants.keySet()),identation+1);
		
		BlankLines(1);
		WriteLine("for Invariant_local in allInvariants_local:",identation+1);
		WriteLine("InvariantMethod_local = getattr(self,Invariant_local + \"_invariantCheck\")",identation+2);
		WriteLine("checkedAns_local = checkedAns_local and InvariantMethod_local()",identation+2);
		
		BlankLines(1);
		WriteLine("return checkedAns_local",identation+1);
		
		BlankLines(1);
		WriteLine("#End Check ALL Invariants Method",identation);
	}
	
	public void translateVariant(PyAST_Machine machine,int identation) throws IOException {
		if(machine.EventVariant.DeterminedVariant) {
			BlankLines(1);
			WriteLine("#Variant Method",identation);
			WriteLine("def PyMachineVariant(self) -> int:",identation);
			WriteSomething("return ",identation+1);
			WriteSomething(translateExpression(machine.EventVariant.VariantExpression),0);
			BlankLines(1);
		}
	}
	
	public void translateInvariants(PyAST_Machine machine,int identation) throws IOException {

		BlankLines(1);
		WriteLine("#Invariants Check Methods",identation);
		
		ArrayList<PyAST_Invariant> orderedInvariants = new ArrayList<PyAST_Invariant>(machine.Invariants.values());
		Collections.sort(orderedInvariants,InvariantComparator);
		for(PyAST_Invariant invariant : orderedInvariants) {
			BlankLines(1);
			
			if(invariant.IsTheorem)WriteLine("#This Invariant is a Theorem.",identation);
			
			WriteLine("def " + invariant.InvariantLabel + "_invariantCheck(self) -> bool:",identation);
			WriteLine("return " + translatePredicate(invariant.InvariantPredicate),identation+1);
		}
	}
	
	public void translateAxioms(PyAST_Context context,int identation) throws IOException {
		
		BlankLines(1);
		WriteLine("#Axiom Check Methods",identation);
		
		ArrayList<PyAST_Axiom> orderedAxioms = new ArrayList<PyAST_Axiom>(context.Axioms.values());
		Collections.sort(orderedAxioms,AxiomComparator);
		for(PyAST_Axiom axiom : orderedAxioms) {
			BlankLines(1);
			
			if(axiom.IsTheorem)WriteLine("#This Axiom is a Theorem.",identation);
			
			WriteLine("def " + axiom.AxiomLabel + "_axiomCheck(self) -> bool:",identation);
			WriteLine("return " + translatePredicate(axiom.AxiomPredicate),identation+1);
		}
		
		BlankLines(1);
		WriteLine("#End Axiom Check Methods",identation);
		
		BlankLines(1);
		WriteLine("#Check ALL Axioms",identation);
		BlankLines(1);
		WriteLine("def checkAllAxioms(self) -> bool:",identation);
		WriteLine("checkedAns_local : bool = True",identation+1);
		WriteLine("allAxioms_local : List[str] = " + translateSetToList(context.Axioms.keySet()),identation+1);
		
		BlankLines(1);
		WriteLine("for Axiom_local in allAxioms_local:",identation+1);
		WriteLine("AxiomMethod_local = getattr(self,Axiom_local + \"_axiomCheck\")",identation+2);
		WriteLine("checkedAns_local = checkedAns_local and AxiomMethod_local()",identation+2);
		
		BlankLines(1);
		WriteLine("return checkedAns_local",identation+1);
		
		BlankLines(1);
		WriteLine("#End Check ALL Axioms",identation);
	}
	
	public void translateUserDebuggingFunctions(PyAST_Context context, PyAST_Machine machine,int identation) throws IOException {
		
		BlankLines(1);
		WriteLine("#User/Debugging Functions", identation);
		
		//Printing Status
		BlankLines(1);
		WriteLine("def __str__(self) -> str:", identation);
		WriteLine("tmp_values : List[str] = list()", identation+1);
		
		if(context != null) {
			BlankLines(1);
			WriteLine("#Print Constants", identation+1);
			WriteLine("tmp_values.append(\"###\")", identation+1);
			WriteLine("tmp_values.append(\"" + context.Name + " Constants\")", identation+1);
			
			//Constants Declaration
			ArrayList<PyAST_Constant> orderedConstants = new ArrayList<PyAST_Constant>(context.Constants.values());
			Collections.sort(orderedConstants,ConstantComparator);
			BlankLines(1);
			for(PyAST_Constant constant : orderedConstants) {
				WriteSomething("tmp_values.append(\"",identation+1);
				WriteSomething(constant.ConstantName,0);
				WriteSomething(" ==> \" + str(self.",0);
				WriteSomething(constant.ConstantName,0);
				WriteSomething("))",0);
				BlankLines(1);
			}
			
			if(context.HasContextExtension) {
				BlankLines(1);
				WriteLine("#Print Extended Context Constants", identation+1);
				WriteLine("tmp_values.append(self.__" + context.ContextExtension.Name + ".__str__())", identation+1);
			}
		}
		
		if(machine != null) {
			if(machine.HasMachineInternalContext) {
				BlankLines(1);
				WriteLine("#Print Internal Context Constants", identation+1);
				WriteLine("tmp_values.append(self.__" + machine.MachineInternalContext.Name + ".__str__())", identation+1);
			}
			
			BlankLines(1);
			WriteLine("#Print Variables", identation+1);
			WriteLine("tmp_values.append(\"###\")", identation+1);
			WriteLine("tmp_values.append(\"Variables\")", identation+1);
			
			//Ordered Variables
			ArrayList<PyAST_Variable> orderedVariables = new ArrayList<PyAST_Variable>(machine.Variables.values());
			Collections.sort(orderedVariables,VariableComparator);
			BlankLines(1);
			for(PyAST_Variable variable : orderedVariables) {
				WriteSomething("tmp_values.append(\"",identation+1);
				WriteSomething(variable.VariableName,0);
				WriteSomething(" ==> \" + str(self.",0);
				WriteSomething(variable.VariableName,0);
				WriteSomething("))",0);
				BlankLines(1);
			}
		}
		
		BlankLines(1);
		WriteLine("return \"\\n\".join(tmp_values)", identation+1);
		
		BlankLines(1);
		WriteLine("def __repr__(self) -> str:", identation);
		WriteLine("return self.__str__()", identation+1);
		
		// PYGUARDSSTATE
		if(machine != null) {
			BlankLines(1);
			WriteLine("def PyGuardsState(self) -> None:", identation);
			WriteLine("#This method will show which events (with no parameters) can be executed.", identation+1);
			WriteLine("tmp_values : List[str] = list()",identation+1);
			
			WriteSomething("list_events_noparams : List[str] = [",identation+1);
			ArrayList<PyAST_Event> events = new ArrayList<PyAST_Event>(machine.Events.values());
			boolean firstEvent = true;
			for(PyAST_Event event : events) {
				if(event.EventParameters.length == 0) {
					if(firstEvent) {
						firstEvent = false;
						WriteSomething("\"" + event.EventLabel +"\"",0);
					}
					else WriteSomething(", \"" + event.EventLabel +"\"",0);
				}
			}
			WriteSomething("]",0);
			BlankLines(1);
			
			WriteSomething("list_events_params : List[Tuple[str,List[str]]] = [",identation+1);
			firstEvent = true;
			boolean firstParameter;
			for(PyAST_Event event : events) {
				firstParameter = true;
				if(event.EventParameters.length > 0) {
					if(firstEvent) {
						firstEvent = false;
						WriteSomething("(\"" + event.EventLabel +"\",[",0);
					}
					else WriteSomething(", (\"" + event.EventLabel +"\",[",0);
						
					for(PyAST_Variable parameter : event.EventParameters) {
						if(firstParameter) {
							firstParameter = false;
							WriteSomething("\"" + translateConstantType(parameter.VariableType) +"\"",0);
						}
						else WriteSomething(", \"" + translateConstantType(parameter.VariableType) +"\"",0);
					}
					
					WriteSomething("])",0);
				}
			}
			WriteSomething("]",0);
			BlankLines(1);
			
			WriteLine("tmp_values.append(\"State of the Guards of every event!\")",identation+1);
			WriteLine("for event_name in list_events_noparams:",identation+1);
			WriteLine("guards_to_check = getattr(self,event_name + \"_eventGuards\")",identation+2);
			WriteLine("tmp_values.append(event_name + \" ==> \" + str(guards_to_check()))",identation+2);
			WriteLine("for event_name,params_type in list_events_params:",identation+1);
			WriteLine("if len(params_type)>1:",identation+2);
			WriteLine("tmp_values.append(event_name + \" ==> Undetermined\")",identation+3);
			WriteLine("continue",identation+3);
			WriteLine("guards_to_check = getattr(self,event_name + \"_eventGuards\")",identation+2);
			WriteLine("guards_state = False",identation+2);
			WriteLine("for possible_any in P.ObtainSetFromType(params_type[0]):",identation+2);
			WriteLine("try:",identation+3);
			WriteLine("guards_state = guards_to_check(possible_any)",identation+4);
			WriteLine("except:",identation+3);
			WriteLine("continue",identation+4);
			WriteLine("if guards_state:",identation+3);
			WriteLine("tmp_values.append(event_name + \" ==> \" + str(guards_state) + \", e.g. with param = \" + str(possible_any))",identation+4);
			WriteLine("break",identation+4);
			WriteLine("if not guards_state:",identation+2);
			WriteLine("tmp_values.append(event_name + \" ==> \" + str(guards_state))",identation+3);
			WriteLine("print(\"\\n\".join(tmp_values))",identation+1);
		}
		
		// PYAUTOEXECUTE
		if(machine != null) {
			BlankLines(1);
			WriteLine("def PyAutoExecute(self) -> None:", identation);
			WriteLine("#This method will try to find an event to execute.", identation+1);
			
			WriteSomething("list_events_strs : List[str] = [",identation+1);
			ArrayList<PyAST_Event> events = new ArrayList<PyAST_Event>(machine.Events.values());
			boolean firstEvent = true;
			for(PyAST_Event event : events) {
				if(firstEvent) {
					firstEvent = false;
					WriteSomething("\"" + event.EventLabel +"\"",0);
				}
				else WriteSomething(", \"" + event.EventLabel +"\"",0);
			}
			WriteSomething("]",0);
			BlankLines(1);
			
			WriteLine("amount_of_events : int = len(list_events_strs)", identation+1);
			WriteLine("attempt_count : int = 0", identation+1);
			WriteLine("while(attempt_count < P.MaxAutoExecuteAttempts()):", identation+1);
			WriteLine("event_iter : int = randint(0,amount_of_events-1)", identation+2);
			WriteLine("event_name : str = list_events_strs[event_iter]", identation+2);
			WriteLine("try:", identation+2);
			WriteLine("event_to_attempt = getattr(self,event_name + \"_eventActions\")", identation+3);
			WriteLine("event_to_attempt()", identation+3);
			WriteLine("print(event_name + \" succesfully executed!!!\")", identation+3);
			WriteLine("print(self)", identation+3);
			WriteLine("return", identation+3);
			WriteLine("except GuardsViolated:", identation+2);
			WriteLine("attempt_count += 1", identation+3);
			WriteLine("print(\"No event could be AutoExecuted\")", identation+1);
		}
	}
	
	public void translateMachineConstructor(PyAST_Machine machine,int identation) throws IOException {
		
		//Declaration of Constructor of the Context Class
		BlankLines(1);
		WriteSomething("def __init__( self", identation);
		
		if(machine.HasMachineInternalContext)
			WriteSomething(" , " + machine.MachineInternalContext.Name + "_userIn : " + machine.MachineInternalContext.Name + "_class = " + machine.MachineInternalContext.Name + "_class()",0);
		
		WriteSomething(" ) -> None:",0);
		BlankLines(1);
		
		//Assign Parameters to Constants
		
		if(machine.HasMachineInternalContext) {
			BlankLines(1);
			WriteLine("#Assign Parameter to Context Extended Dependency Object",identation+1);
			WriteLine("self.__" + machine.MachineInternalContext.Name + " : " + machine.MachineInternalContext.Name + "_class = " + machine.MachineInternalContext.Name + "_userIn",identation+1);
			WriteLine("if not(self.__" + machine.MachineInternalContext.Name + ".Initialized_ContextGetMethod()):",identation+1);
			WriteLine("self.__" + machine.MachineInternalContext.Name + ".checkedInit()",identation+2);
		}
		
		BlankLines(1);
		WriteLine("#Variables",identation+1);
		
		//Ordered Variables
		ArrayList<PyAST_Variable> orderedVariables = new ArrayList<PyAST_Variable>(machine.Variables.values());
		Collections.sort(orderedVariables,VariableComparator);
		for(PyAST_Variable variable : orderedVariables) {
			//Check whether the Type of the Variable was already translated (surely not).
			String currentVariableTypeTranslation;
			if(variable.VariableTypeTranslated)currentVariableTypeTranslation=variable.VariableTypeTranslation;
			else {
				currentVariableTypeTranslation = translateConstantType(variable.VariableType);
				variable.VariableTypeTranslated = true;
				variable.VariableTypeTranslation = currentVariableTypeTranslation;
			}
			
			WriteLine("self." + variable.VariableName + " : " + variable.VariableTypeTranslation,identation+1);
			
			VariableTypesDP.put(variable.VariableName, variable.VariableTypeTranslation);
		}
		
		WriteLine("#EndVariables",identation+1);
		
		
		//INITIALISATION Event
		BlankLines(1);
		WriteLine("#INITIALISATION of variables",identation+1);
		for(PyAST_Action initialisationAction : machine.INITIALISATIONEvent.EventActions)
			WriteLine(translatePredicate(initialisationAction.AssignmentAction),identation+1);
		
		//Check ALL Invariants.
		BlankLines(1);
		WriteLine("#Check ALL Invariants if enabled.",identation+1);
		WriteLine("if " + PreludeName + ".DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):",identation+1);
		WriteLine("raise Exception(\"Invariants violated after INITIALISATION.\")",identation+2);
		
	}
	
	public void translateContextConstructor(PyAST_Context context,int identation) throws IOException {
		
		//Declaration of Constructor of the Context Class
		BlankLines(1);
		WriteLine("def __init__(self) -> None:",identation);
		
		//Context Utilities
		BlankLines(1);
		WriteLine("#Context Utils", identation+1);
		WriteLine("self.__Initialized_Context = False",identation+1);
		WriteLine("self.__Attributes_SetFlag : bool = True",identation+1);
		
		//Include Context Extension Dependency Object if there is one.
		if(context.HasContextExtension) {
			BlankLines(1);
			WriteLine("#Context Extended Dependency Object",identation+1);
			WriteLine("self.__" + context.ContextExtension.Name + " : " + context.ContextExtension.Name + "_class", identation+1);
		}
		
		//Carrier Sets Declaration Comment
		BlankLines(1);
		WriteLine("#CarrierSets", identation+1);
		
		//Carrier Sets Declaration
		ArrayList<PyAST_CarrierSet> orderedCarrierSets = new ArrayList<PyAST_CarrierSet>(context.CarrierSets.values());
		Collections.sort(orderedCarrierSets,CarrierSetComparator);
		for(PyAST_CarrierSet carrierSet : orderedCarrierSets) {
			WriteLine("self." + carrierSet.CarrierSetName + " : PySet[" + carrierSet.CarrierSetName + "_CS] = " + PreludeName + ".PyCarrierSetGet(\"" + carrierSet.CarrierSetName + "_CS\")",identation+1);
		}
		WriteLine("#EndCarrierSets", identation+1);
		WriteLine("self.__Attributes_SetFlag = False",identation+1);
		
		//Constants Declaration Comment
		BlankLines(1);
		WriteLine("#Constants",identation+1);
		
		String currentConstantTypeTranslation;
		
		//Constants Declaration
		ArrayList<PyAST_Constant> orderedConstants = new ArrayList<PyAST_Constant>(context.Constants.values());
		Collections.sort(orderedConstants,ConstantComparator);
		for(PyAST_Constant constant : orderedConstants) {
			
			//Check whether the Type of the Constant was already translated.
			if(constant.ConstantTypeTranslated)currentConstantTypeTranslation=constant.ConstantTypeTranslation;
			else {
				currentConstantTypeTranslation = translateConstantType(constant.ConstantType);
				constant.ConstantTypeTranslated=true;
				constant.ConstantTypeTranslation = currentConstantTypeTranslation;
			}
			
			WriteLine("self." + constant.ConstantName + " : " + currentConstantTypeTranslation,identation+1);
			
		}
		
		WriteLine("#EndConstants",identation+1);
		BlankLines(1);
	}
	
	//Translate a Constant Type of a Context.
	public String translateConstantType(PyAST_Type currentConstantType) {
		
		StringBuilder constantType = new StringBuilder();
		
		switch(currentConstantType.CoreType) {
			case "Bool":
				constantType.append("bool");
				break;
			case "Integer":
				constantType.append("int");
				break;
			case "FreeIdentifierType":
				PyAST_FreeIdentifierType currentFreeIdentifierType = (PyAST_FreeIdentifierType)currentConstantType;
				constantType.append(currentFreeIdentifierType.IdentifierName);
				break;
			case "UnaryExpressionType":
				PyAST_UnaryExpressionType unaryExpressionType = (PyAST_UnaryExpressionType) currentConstantType;
				
				constantType.append(unaryExpressionType.InternalTypeInterpretation);
				constantType.append("[");
				constantType.append(translateConstantType(unaryExpressionType.InternalType));
				constantType.append("]");
				break;
			case "BinaryExpressionType":
				PyAST_BinaryExpressionType binaryExpressionType = (PyAST_BinaryExpressionType) currentConstantType;
				
				constantType.append(binaryExpressionType.TypeSymbolInterpretation);
				constantType.append("[");
				constantType.append(translateConstantType(binaryExpressionType.LeftSide));
				constantType.append(",");
				constantType.append(translateConstantType(binaryExpressionType.RightSide));
				constantType.append("]");
				break;
			default:
				constantType.append(currentConstantType.CoreType + " ErrorTranslateConstant ");
		}
		
		return constantType.toString();
	}
	
	public void translateCarrierSetTypes(PyAST_Context context,int identation) throws IOException {
		
		WriteLine("#CarrierSet Types Declarations", identation);
		
		ArrayList<PyAST_CarrierSet> orderedCarrierSets = new ArrayList<PyAST_CarrierSet>(context.CarrierSets.values());
		Collections.sort(orderedCarrierSets,CarrierSetComparator);
		for(PyAST_CarrierSet carrierSet : orderedCarrierSets) {
			
			BlankLines(1);
			WriteLine("@unique", identation);
			WriteLine("class " + carrierSet.CarrierSetName + "_CS(Enum):", identation);
			BlankLines(1);
			WriteLine("# CUSTOM USER CODE BEGIN: Increase or decrease the amount of finite elements as you wish!", identation+1);
			
			BlankLines(1);
			if(carrierSet.EstimatedSize==0) {
				for(int i=0; i<(RandomNumberGenerator.nextInt(MAX_CARRIERSET_INITIALELEMENTS)+1); i++)
					WriteLine(carrierSet.CarrierSetName + String.valueOf(i) + " = auto()",identation+1);
			}
			else {
				for(int i=0; i<carrierSet.EstimatedSize; i++)
					WriteLine(carrierSet.CarrierSetName + String.valueOf(i) + " = auto()",identation+1);
			}
			
			BlankLines(1);
			WriteLine("# CUSTOM USER CODE END", identation+1);
			
			BlankLines(1);
			WriteLine("#Include this new Type in the Prelude.",identation);
			WriteLine(PreludeName + ".AddCarrierSet(\"" + carrierSet.CarrierSetName + "_CS\"," + carrierSet.CarrierSetName + "_CS)",identation);
		}
	}
	
	public void translateMachineIntro(PyAST_Machine machine,int identation) throws IOException {
		
		//Imports
		//BlankLines(1);
		WriteLine("#DEPENDENCIES", identation);
		
		//Allow Path Access to the Prelude's Directory
		BlankLines(1);
		WriteLine("#Allow Path Access to the Prelude's Directory", identation);
		BlankLines(1);
		WriteLine("import sys", identation);
		WriteLine("if not(\"..\" in sys.path):",identation);
		WriteLine("sys.path.append(\"..\")", identation+1);
		
		//Import Utilities
		BlankLines(1);
		WriteLine("#Utilities Dependencies",identation);
		WriteLine("from Py_Preludes import *", identation);
		
		//Import Typing
		BlankLines(1);
		WriteLine("#Typing Dependencies", identation);
		WriteLine("from typing import List", identation);
		
		//Import Machine Refinement if there is one.
		if(machine.HasMachineRefinement) {
			BlankLines(1);
			WriteLine("#Machine Refinement Dependencies",identation);
			WriteLine("from " + machine.MachineRefinement.Name + "_mch import *",identation);
		}
		
		//Import Machine Internal Context if there is one.
		if(machine.HasMachineInternalContext) {
			BlankLines(1);
			WriteLine("#Machine Internal Context Dependencies",identation);
			WriteLine("from " + machine.MachineInternalContext.Name + "_ctx import *",identation);
		}
		
		//Head and Introductory Comments about the Context.
		BlankLines(2);
		WriteLine("#Translation of Machine: " + machine.Name,identation);
		
		//Include Comment if there is a Machine Refinement.
		if(machine.HasMachineRefinement)
			WriteLine("#This machine refines the following machine: " + machine.MachineRefinement.Name + "_class",identation);
		
		//Include Comment if this machine sees a Context.
		if(machine.HasMachineInternalContext)
			WriteLine("#This machine sees the following context: " + machine.MachineInternalContext.Name + "_class",identation);
		
		//Declaration of Context Class
		BlankLines(2);
		if(machine.HasMachineRefinement){
			//Introduction and Declaration of a Machine
			WriteLine("class " + machine.Name + "_class(" + machine.MachineRefinement.Name + "_class):",identation);
		}
		else{
			//Introduction and Declaration of a Machine
			WriteLine("class " + machine.Name + "_class():",identation);
		}
	}
	
	public void translateContextIntro(PyAST_Context context,int identation) throws IOException {
		
		//Imports
		//BlankLines(1);
		WriteLine("#DEPENDENCIES", identation);
		
		//Allow Path Access to the Prelude's Directory
		BlankLines(1);
		WriteLine("#Allow Path Access to the Prelude's Directory", identation);
		BlankLines(1);
		WriteLine("import sys", identation);
		WriteLine("if not(\"..\" in sys.path):",identation);
		WriteLine("sys.path.append(\"..\")", identation+1);
		
		//Import Utilities
		BlankLines(1);
		WriteLine("#Utilities Dependencies",identation);
		WriteLine("from Py_Preludes import *", identation);
		
		//Import Typing
		BlankLines(1);
		WriteLine("#Typing Dependencies", identation);
		WriteLine("from typing import List", identation);
		
		//Import Enumeration
		BlankLines(1);
		WriteLine("#Enum Dependencies",identation);
		WriteLine("from enum import Enum,auto,unique",identation);
		
		//Import Context Extensions
		if(context.HasContextExtension) {
			BlankLines(1);
			WriteLine("#Context Extension Dependencies",identation);
			WriteLine("from " + context.ContextExtension.Name + "_ctx import *",identation);
		}
		
		//Create Carrier Set Types.
		BlankLines(2);
		translateCarrierSetTypes(context,identation);
		
		//Head and Introductory Comments about the Context.
		BlankLines(2);
		WriteLine("#Translation of Context: " + context.Name,identation);
		
		//Include Comment if there is a Context Extension.
		if(context.HasContextExtension)
			WriteLine("#This context extends the following context: " + context.ContextExtension.Name + "_class",identation);
		
		//Declaration of Context Class
		BlankLines(2);
		WriteLine("class " + context.Name + "_class():",identation);
	}
	
	public boolean FlagIfParenthesis(String expressionCore) {
		return true;
		/*if(expressionCore.equals("FreeIdentifier") || expressionCore.equals("IntegerLiteral") || expressionCore.equals("UnaryExpression") || expressionCore.equals("LiteralPredicate") || expressionCore.equals("AtomicExpression"))
			return true;
		else
			return false;*/
	}
	
	public String translateSetToList(Set<String> set) {
		
		StringBuilder newList = new StringBuilder();
		
		newList.append("[");
		
		boolean firstElement=true;
		ArrayList<String> orderedSet = new ArrayList<String>(set);
		Collections.sort(orderedSet);
		for(String element : orderedSet) {
			if(firstElement) {
				firstElement = false;
				newList.append(" \"" + element + "\"");
			}
			else newList.append(" , \"" + element + "\"");
		}
		newList.append(" ]");
		return newList.toString();
	}
	
	public void WriteSomething(String something,int identation) throws IOException {
		
		identation*=IDENTATION;
		StringBuilder newLine = new StringBuilder();
		
		for(int i=0;i<identation;i++) {
			newLine.append(' ');
		}
		
		newLine.append(something);
		
		Writer.write(newLine.toString());
	}
	
	public void WriteLine(String line, int identation) throws IOException {
		
		identation *= IDENTATION;
		StringBuilder newLine = new StringBuilder();
		
		for(int i=0;i<identation;i++) {
			newLine.append(' ');
		}
		
		newLine.append(line);
		newLine.append('\n');
		
		Writer.write(newLine.toString());
		
	}
	
	public void BlankLines(int amount) throws IOException {
		StringBuilder blankLines = new StringBuilder();
		for(int i=0;i<amount;i++) {
			blankLines.append('\n');
		}
		Writer.write(blankLines.toString());
	}
}
