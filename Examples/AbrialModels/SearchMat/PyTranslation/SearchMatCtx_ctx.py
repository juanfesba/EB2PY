#DEPENDENCIES

#Allow Path Access to the Prelude's Directory

import sys
if not(".." in sys.path):
   sys.path.append("..")

#Utilities Dependencies
from Py_Preludes import *

#Typing Dependencies
from typing import List

#Enum Dependencies
from enum import Enum,auto,unique


#CarrierSet Types Declarations


#Translation of Context: SearchMatCtx


class SearchMatCtx_class():

   def __init__(self) -> None:

      #Context Utils
      self.__Initialized_Context = False
      self.__Attributes_SetFlag : bool = True

      #CarrierSets
      #EndCarrierSets
      self.__Attributes_SetFlag = False

      #Constants
      self.f : PyRel[Tuple[int,int],int]
      self.m : int
      self.n : int
      self.s : PySet[int]
      #EndConstants


   #Initialized_Context Flag Attribute Get Method
   def Initialized_ContextGetMethod(self) -> bool:
      return self.__Initialized_Context

   #CarrierSets Get/Set Methods

   #End CarrierSets Get/Set Methods

   #Constants Get/Set Methods

   @property
   def f(self) -> PyRel[Tuple[int,int],int]:
      return self.__f

   @f.setter
   def f(self, f_userIn : PyRel[Tuple[int,int],int]) -> None:
      if self.__Attributes_SetFlag == False: raise Exception("Changing the state of this Context is disabled.")
      self.__f : PyRel[Tuple[int,int],int] = f_userIn

   @property
   def m(self) -> int:
      return self.__m

   @m.setter
   def m(self, m_userIn : int) -> None:
      if self.__Attributes_SetFlag == False: raise Exception("Changing the state of this Context is disabled.")
      self.__m : int = m_userIn

   @property
   def n(self) -> int:
      return self.__n

   @n.setter
   def n(self, n_userIn : int) -> None:
      if self.__Attributes_SetFlag == False: raise Exception("Changing the state of this Context is disabled.")
      self.__n : int = n_userIn

   @property
   def s(self) -> PySet[int]:
      return self.__s

   @s.setter
   def s(self, s_userIn : PySet[int]) -> None:
      if self.__Attributes_SetFlag == False: raise Exception("Changing the state of this Context is disabled.")
      self.__s : PySet[int] = s_userIn

   #End Constants Get Methods

   #Axiom Check Methods

   def ax0_axiomCheck(self) -> bool:
      return P.NAT1().PyContains(self.m)

   def ax1_axiomCheck(self) -> bool:
      return P.NAT1().PyContains(self.n)

   def ax2_axiomCheck(self) -> bool:
      return self.s == PySet({int_range for int_range in range(101, 116+1)})

   def ax3_axiomCheck(self) -> bool:
      return PyFamilies(PyFamilyTypes.TotalFunctions, PySet({int_range for int_range in range(1, self.m+1)}).PyCartesianProduct(PySet({int_range for int_range in range(1, self.n+1)})), self.s).PyContains(self.f)

   def ax4_axiomCheck(self) -> bool:
      return P.INT().PyCartesianProduct(P.INT()).PyPowerSet().PyContains(self.f.PyDomain())

   #End Axiom Check Methods

   #Check ALL Axioms

   def checkAllAxioms(self) -> bool:
      checkedAns_local : bool = True
      allAxioms_local : List[str] = [ "ax0" , "ax1" , "ax2" , "ax3" , "ax4" ]

      for Axiom_local in allAxioms_local:
         AxiomMethod_local = getattr(self,Axiom_local + "_axiomCheck")
         checkedAns_local = checkedAns_local and AxiomMethod_local()

      return checkedAns_local

   #End Check ALL Axioms

   #Checked Initialization Method
   def checkedInit(self, f_userIn : PyRel[Tuple[int,int],int] = P.NoParam(), m_userIn : int = P.NoParam(), n_userIn : int = P.NoParam(), s_userIn : PySet[int] = P.NoParam() ) -> None:

      if f_userIn is None:
         f_userIn = P.PyRandValGen("PyRel[Tuple[int,int],int]")
      if m_userIn is None:
         m_userIn = P.PyRandValGen("int")
      if n_userIn is None:
         n_userIn = P.PyRandValGen("int")
      if s_userIn is None:
         s_userIn = P.PyRandValGen("PySet[int]")

      if self.__Initialized_Context: raise Exception("Context already initialized!")
      self.__Initialized_Context = True

      #Enable Attributes Set Method
      self.__Attributes_SetFlag = True

      self.f = f_userIn
      self.m = m_userIn
      self.n = n_userIn
      self.s = s_userIn

      if P.DESIGN_BY_CONTRACT_ENABLED():
         attempt_Count : int = 0
         while not(self.checkAllAxioms()):
            self.f = P.PyRandValGen("PyRel[Tuple[int,int],int]")
            self.m = P.PyRandValGen("int")
            self.n = P.PyRandValGen("int")
            self.s = P.PyRandValGen("PySet[int]")
            if attempt_Count == P.HIGHMAXGENATTEMPTS():
               raise Exception("Initialization could not satisfy the Axioms!")
            attempt_Count += 1

      #Disable Attributes Set Method
      self.__Attributes_SetFlag = False

   #User/Debugging Functions

   def __str__(self) -> str:
      tmp_values : List[str] = list()

      #Print Constants
      tmp_values.append("###")
      tmp_values.append("SearchMatCtx Constants")

      tmp_values.append("f ==> " + str(self.f))
      tmp_values.append("m ==> " + str(self.m))
      tmp_values.append("n ==> " + str(self.n))
      tmp_values.append("s ==> " + str(self.s))

      return "\n".join(tmp_values)

   def __repr__(self) -> str:
      return self.__str__()
