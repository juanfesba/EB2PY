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

#Context Extension Dependencies
from SimpleTwoWayCtx_ctx import *


#CarrierSet Types Declarations


#Translation of Context: SimpleTwoWayCtxExt
#This context extends the following context: SimpleTwoWayCtx_class


class SimpleTwoWayCtxExt_class():

   def __init__(self) -> None:

      #Context Utils
      self.__Initialized_Context = False
      self.__Attributes_SetFlag : bool = True

      #Context Extended Dependency Object
      self.__SimpleTwoWayCtx : SimpleTwoWayCtx_class

      #CarrierSets
      #EndCarrierSets
      self.__Attributes_SetFlag = False

      #Constants
      self.OTHERDIR : PyRel[DIRECTION_CS,DIRECTION_CS]
      #EndConstants


   #Context Extended Dependency Object Get Method

   def SimpleTwoWayCtx_get(self) -> SimpleTwoWayCtx_class:
      return self.__SimpleTwoWayCtx

   #Initialized_Context Flag Attribute Get Method
   def Initialized_ContextGetMethod(self) -> bool:
      return self.__Initialized_Context

   #CarrierSets Get/Set Methods

   #End CarrierSets Get/Set Methods

   #Constants Get/Set Methods

   @property
   def OTHERDIR(self) -> PyRel[DIRECTION_CS,DIRECTION_CS]:
      return self.__OTHERDIR

   @OTHERDIR.setter
   def OTHERDIR(self, OTHERDIR_userIn : PyRel[DIRECTION_CS,DIRECTION_CS]) -> None:
      if self.__Attributes_SetFlag == False: raise Exception("Changing the state of this Context is disabled.")
      self.__OTHERDIR : PyRel[DIRECTION_CS,DIRECTION_CS] = OTHERDIR_userIn

   #End Constants Get Methods

   #Axiom Check Methods

   def ax2_axiomCheck(self) -> bool:
      return PyFamilies(PyFamilyTypes.TotalFunctions, self.SimpleTwoWayCtx_get().DIRECTION, self.SimpleTwoWayCtx_get().DIRECTION).PyContains(self.OTHERDIR)

   def ax3_axiomCheck(self) -> bool:
      return self.OTHERDIR(self.SimpleTwoWayCtx_get().NorthSouth) == self.SimpleTwoWayCtx_get().EastWest

   def ax4_axiomCheck(self) -> bool:
      return self.OTHERDIR(self.SimpleTwoWayCtx_get().EastWest) == self.SimpleTwoWayCtx_get().NorthSouth

   def ax5_axiomCheck(self) -> bool:
      return P.QuantifiedForAll( (lambda boundIdentifiers : PyPrelude.LogicImplication(self.SimpleTwoWayCtx_get().DIRECTION.PyContains(boundIdentifiers[0]), self.OTHERDIR(self.OTHERDIR(boundIdentifiers[0])) == boundIdentifiers[0])) , [ (0,"DIRECTION_CS") ] ) 

   def ax6_axiomCheck(self) -> bool:
      return self.OTHERDIR.PyComposition(self.OTHERDIR).PyIsSubset(P.ID())

   #End Axiom Check Methods

   #Check ALL Axioms

   def checkAllAxioms(self) -> bool:
      checkedAns_local : bool = True
      allAxioms_local : List[str] = [ "ax2" , "ax3" , "ax4" , "ax5" , "ax6" ]

      for Axiom_local in allAxioms_local:
         AxiomMethod_local = getattr(self,Axiom_local + "_axiomCheck")
         checkedAns_local = checkedAns_local and AxiomMethod_local()

      return checkedAns_local

   #End Check ALL Axioms

   #Checked Initialization Method
   def checkedInit(self , SimpleTwoWayCtx_userIn : SimpleTwoWayCtx_class = SimpleTwoWayCtx_class(), OTHERDIR_userIn : PyRel[DIRECTION_CS,DIRECTION_CS] = P.NoParam() ) -> None:

      if OTHERDIR_userIn is None:
         OTHERDIR_userIn = P.PyRandValGen("PyRel[DIRECTION_CS,DIRECTION_CS]")

      if self.__Initialized_Context: raise Exception("Context already initialized!")
      self.__Initialized_Context = True

      #Enable Attributes Set Method
      self.__Attributes_SetFlag = True

      #Assign Parameter to Context Extended Dependency Object
      self.__SimpleTwoWayCtx = SimpleTwoWayCtx_userIn
      if not(self.__SimpleTwoWayCtx.Initialized_ContextGetMethod()):
         self.__SimpleTwoWayCtx.checkedInit()

      self.OTHERDIR = OTHERDIR_userIn

      if P.DESIGN_BY_CONTRACT_ENABLED():
         attempt_Count : int = 0
         while not(self.checkAllAxioms()):
            self.OTHERDIR = P.PyRandValGen("PyRel[DIRECTION_CS,DIRECTION_CS]")
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
      tmp_values.append("SimpleTwoWayCtxExt Constants")

      tmp_values.append("OTHERDIR ==> " + str(self.OTHERDIR))

      #Print Extended Context Constants
      tmp_values.append(self.__SimpleTwoWayCtx.__str__())

      return "\n".join(tmp_values)

   def __repr__(self) -> str:
      return self.__str__()
