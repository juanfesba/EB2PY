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


#Translation of Context: CommonNumberCtx


class CommonNumberCtx_class():

   def __init__(self) -> None:

      #Context Utils
      self.__Initialized_Context = False
      self.__Attributes_SetFlag : bool = True

      #CarrierSets
      #EndCarrierSets
      self.__Attributes_SetFlag = False

      #Constants
      self.f : PyRel[int,int]
      self.g : PyRel[int,int]
      self.m : int
      self.n : int
      #EndConstants


   #Initialized_Context Flag Attribute Get Method
   def Initialized_ContextGetMethod(self) -> bool:
      return self.__Initialized_Context

   #CarrierSets Get/Set Methods

   #End CarrierSets Get/Set Methods

   #Constants Get/Set Methods

   @property
   def f(self) -> PyRel[int,int]:
      return self.__f

   @f.setter
   def f(self, f_userIn : PyRel[int,int]) -> None:
      if self.__Attributes_SetFlag == False: raise Exception("Changing the state of this Context is disabled.")
      self.__f : PyRel[int,int] = f_userIn

   @property
   def g(self) -> PyRel[int,int]:
      return self.__g

   @g.setter
   def g(self, g_userIn : PyRel[int,int]) -> None:
      if self.__Attributes_SetFlag == False: raise Exception("Changing the state of this Context is disabled.")
      self.__g : PyRel[int,int] = g_userIn

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

   #End Constants Get Methods

   #Axiom Check Methods

   def ax0_axiomCheck(self) -> bool:
      return P.NAT1().PyContains(self.m)

   def ax1_axiomCheck(self) -> bool:
      return P.NAT1().PyContains(self.n)

   def ax2_axiomCheck(self) -> bool:
      return PyFamilies(PyFamilyTypes.TotalInjections, PySet({int_range for int_range in range(1, self.m+1)}), P.NAT()).PyContains(self.f)

   def ax3_axiomCheck(self) -> bool:
      return PyFamilies(PyFamilyTypes.TotalInjections, PySet({int_range for int_range in range(1, self.n+1)}), P.NAT()).PyContains(self.g)

   def ax4_axiomCheck(self) -> bool:
      return P.QuantifiedForAll( (lambda boundIdentifiers : PyPrelude.LogicImplication((self.f.PyDomain().PyContains(boundIdentifiers[1]) and self.f.PyDomain().PyContains(boundIdentifiers[0]) and boundIdentifiers[1] <= boundIdentifiers[0]), self.f(boundIdentifiers[1]) <= self.f(boundIdentifiers[0]))) , [ (0,"int") , (1,"int") ] ) 

   def ax5_axiomCheck(self) -> bool:
      return P.QuantifiedForAll( (lambda boundIdentifiers : PyPrelude.LogicImplication((self.g.PyDomain().PyContains(boundIdentifiers[1]) and self.g.PyDomain().PyContains(boundIdentifiers[0]) and boundIdentifiers[1] <= boundIdentifiers[0]), self.g(boundIdentifiers[1]) <= self.g(boundIdentifiers[0]))) , [ (0,"int") , (1,"int") ] ) 

   def ax6_axiomCheck(self) -> bool:
      return self.f.PyRange().PyIntersection(self.g.PyRange()) != PySet()

   #End Axiom Check Methods

   #Check ALL Axioms

   def checkAllAxioms(self) -> bool:
      checkedAns_local : bool = True
      allAxioms_local : List[str] = [ "ax0" , "ax1" , "ax2" , "ax3" , "ax4" , "ax5" , "ax6" ]

      for Axiom_local in allAxioms_local:
         AxiomMethod_local = getattr(self,Axiom_local + "_axiomCheck")
         checkedAns_local = checkedAns_local and AxiomMethod_local()

      return checkedAns_local

   #End Check ALL Axioms

   #Checked Initialization Method
   def checkedInit(self, f_userIn : PyRel[int,int] = P.NoParam(), g_userIn : PyRel[int,int] = P.NoParam(), m_userIn : int = P.NoParam(), n_userIn : int = P.NoParam() ) -> None:

      if f_userIn is None:
         f_userIn = P.PyRandValGen("PyRel[int,int]")
      if g_userIn is None:
         g_userIn = P.PyRandValGen("PyRel[int,int]")
      if m_userIn is None:
         m_userIn = P.PyRandValGen("int")
      if n_userIn is None:
         n_userIn = P.PyRandValGen("int")

      if self.__Initialized_Context: raise Exception("Context already initialized!")
      self.__Initialized_Context = True

      #Enable Attributes Set Method
      self.__Attributes_SetFlag = True

      self.f = f_userIn
      self.g = g_userIn
      self.m = m_userIn
      self.n = n_userIn

      if P.DESIGN_BY_CONTRACT_ENABLED():
         attempt_Count : int = 0
         while not(self.checkAllAxioms()):
            self.f = P.PyRandValGen("PyRel[int,int]")
            self.g = P.PyRandValGen("PyRel[int,int]")
            self.m = P.PyRandValGen("int")
            self.n = P.PyRandValGen("int")
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
      tmp_values.append("CommonNumberCtx Constants")

      tmp_values.append("f ==> " + str(self.f))
      tmp_values.append("g ==> " + str(self.g))
      tmp_values.append("m ==> " + str(self.m))
      tmp_values.append("n ==> " + str(self.n))

      return "\n".join(tmp_values)

   def __repr__(self) -> str:
      return self.__str__()
