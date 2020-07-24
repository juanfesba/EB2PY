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

@unique
class CITIES_CS(Enum):

   # CUSTOM USER CODE BEGIN: Increase or decrease the amount of finite elements as you wish!

   CITIES0 = auto()
   CITIES1 = auto()
   CITIES2 = auto()
   CITIES3 = auto()
   CITIES4 = auto()
   CITIES5 = auto()
   CITIES6 = auto()

   # CUSTOM USER CODE END

#Include this new Type in the Prelude.
P.AddCarrierSet("CITIES_CS",CITIES_CS)


#Translation of Context: DjkstraCtx


class DjkstraCtx_class():

   def __init__(self) -> None:

      #Context Utils
      self.__Initialized_Context = False
      self.__Attributes_SetFlag : bool = True

      #CarrierSets
      self.CITIES : PySet[CITIES_CS] = P.PyCarrierSetGet("CITIES_CS")
      #EndCarrierSets
      self.__Attributes_SetFlag = False

      #Constants
      self.BERLIN : CITIES_CS
      self.BOGOTA : CITIES_CS
      self.CALI : CITIES_CS
      self.LA : CITIES_CS
      self.MADRID : CITIES_CS
      self.SANFRANCISCO : CITIES_CS
      self.TOKYO : CITIES_CS
      self.graph : PyRel[CITIES_CS,Tuple[CITIES_CS,int]]
      self.sort_func : PyRel[PyRel[int,Tuple[CITIES_CS,int]],PyRel[int,Tuple[CITIES_CS,int]]]
      self.source : CITIES_CS
      #EndConstants


   #Initialized_Context Flag Attribute Get Method
   def Initialized_ContextGetMethod(self) -> bool:
      return self.__Initialized_Context

   #CarrierSets Get/Set Methods

   @property
   def CITIES(self) -> PySet[CITIES_CS]:
      return self.__CITIES

   @CITIES.setter
   def CITIES(self, CITIES_userIn : PySet[CITIES_CS]) -> None:
      if self.__Attributes_SetFlag == False: raise Exception("Changing the state of this Context is disabled.")
      self.__CITIES : PySet[CITIES_CS] = CITIES_userIn

   #End CarrierSets Get/Set Methods

   #Constants Get/Set Methods

   @property
   def BERLIN(self) -> CITIES_CS:
      return self.__BERLIN

   @BERLIN.setter
   def BERLIN(self, BERLIN_userIn : CITIES_CS) -> None:
      if self.__Attributes_SetFlag == False: raise Exception("Changing the state of this Context is disabled.")
      self.__BERLIN : CITIES_CS = BERLIN_userIn

   @property
   def BOGOTA(self) -> CITIES_CS:
      return self.__BOGOTA

   @BOGOTA.setter
   def BOGOTA(self, BOGOTA_userIn : CITIES_CS) -> None:
      if self.__Attributes_SetFlag == False: raise Exception("Changing the state of this Context is disabled.")
      self.__BOGOTA : CITIES_CS = BOGOTA_userIn

   @property
   def CALI(self) -> CITIES_CS:
      return self.__CALI

   @CALI.setter
   def CALI(self, CALI_userIn : CITIES_CS) -> None:
      if self.__Attributes_SetFlag == False: raise Exception("Changing the state of this Context is disabled.")
      self.__CALI : CITIES_CS = CALI_userIn

   @property
   def LA(self) -> CITIES_CS:
      return self.__LA

   @LA.setter
   def LA(self, LA_userIn : CITIES_CS) -> None:
      if self.__Attributes_SetFlag == False: raise Exception("Changing the state of this Context is disabled.")
      self.__LA : CITIES_CS = LA_userIn

   @property
   def MADRID(self) -> CITIES_CS:
      return self.__MADRID

   @MADRID.setter
   def MADRID(self, MADRID_userIn : CITIES_CS) -> None:
      if self.__Attributes_SetFlag == False: raise Exception("Changing the state of this Context is disabled.")
      self.__MADRID : CITIES_CS = MADRID_userIn

   @property
   def SANFRANCISCO(self) -> CITIES_CS:
      return self.__SANFRANCISCO

   @SANFRANCISCO.setter
   def SANFRANCISCO(self, SANFRANCISCO_userIn : CITIES_CS) -> None:
      if self.__Attributes_SetFlag == False: raise Exception("Changing the state of this Context is disabled.")
      self.__SANFRANCISCO : CITIES_CS = SANFRANCISCO_userIn

   @property
   def TOKYO(self) -> CITIES_CS:
      return self.__TOKYO

   @TOKYO.setter
   def TOKYO(self, TOKYO_userIn : CITIES_CS) -> None:
      if self.__Attributes_SetFlag == False: raise Exception("Changing the state of this Context is disabled.")
      self.__TOKYO : CITIES_CS = TOKYO_userIn

   @property
   def graph(self) -> PyRel[CITIES_CS,Tuple[CITIES_CS,int]]:
      return self.__graph

   @graph.setter
   def graph(self, graph_userIn : PyRel[CITIES_CS,Tuple[CITIES_CS,int]]) -> None:
      if self.__Attributes_SetFlag == False: raise Exception("Changing the state of this Context is disabled.")
      self.__graph : PyRel[CITIES_CS,Tuple[CITIES_CS,int]] = graph_userIn

   @property
   def sort_func(self) -> PyRel[PyRel[int,Tuple[CITIES_CS,int]],PyRel[int,Tuple[CITIES_CS,int]]]:
      return self.__sort_func

   @sort_func.setter
   def sort_func(self, sort_func_userIn : PyRel[PyRel[int,Tuple[CITIES_CS,int]],PyRel[int,Tuple[CITIES_CS,int]]]) -> None:
      if self.__Attributes_SetFlag == False: raise Exception("Changing the state of this Context is disabled.")
      self.__sort_func : PyRel[PyRel[int,Tuple[CITIES_CS,int]],PyRel[int,Tuple[CITIES_CS,int]]] = sort_func_userIn

   @property
   def source(self) -> CITIES_CS:
      return self.__source

   @source.setter
   def source(self, source_userIn : CITIES_CS) -> None:
      if self.__Attributes_SetFlag == False: raise Exception("Changing the state of this Context is disabled.")
      self.__source : CITIES_CS = source_userIn

   #End Constants Get Methods

   #Axiom Check Methods

   def ax0_axiomCheck(self) -> bool:
      return self.CITIES.PyPartition([PySet({self.CALI}), PySet({self.BOGOTA}), PySet({self.LA}), PySet({self.SANFRANCISCO}), PySet({self.MADRID}), PySet({self.BERLIN}), PySet({self.TOKYO})])

   def ax1_axiomCheck(self) -> bool:
      return self.source == self.CALI

   def ax2_axiomCheck(self) -> bool:
      return PyFamilies(PyFamilyTypes.Relations, self.CITIES, self.CITIES.PyCartesianProduct(P.NAT())).PyContains(self.graph)

   def ax3_axiomCheck(self) -> bool:
      return PyFamilies(PyFamilyTypes.PartialFunctions, PyFamilies(PyFamilyTypes.PartialFunctions, P.NAT(), self.CITIES.PyCartesianProduct(P.NAT())), PyFamilies(PyFamilyTypes.PartialFunctions, P.NAT(), self.CITIES.PyCartesianProduct(P.NAT()))).PyContains(self.sort_func)

   #End Axiom Check Methods

   #Check ALL Axioms

   def checkAllAxioms(self) -> bool:
      checkedAns_local : bool = True
      allAxioms_local : List[str] = [ "ax0" , "ax1" , "ax2" , "ax3" ]

      for Axiom_local in allAxioms_local:
         AxiomMethod_local = getattr(self,Axiom_local + "_axiomCheck")
         checkedAns_local = checkedAns_local and AxiomMethod_local()

      return checkedAns_local

   #End Check ALL Axioms

   #Checked Initialization Method
   def checkedInit(self, BERLIN_userIn : CITIES_CS = P.NoParam(), BOGOTA_userIn : CITIES_CS = P.NoParam(), CALI_userIn : CITIES_CS = P.NoParam(), LA_userIn : CITIES_CS = P.NoParam(), MADRID_userIn : CITIES_CS = P.NoParam(), SANFRANCISCO_userIn : CITIES_CS = P.NoParam(), TOKYO_userIn : CITIES_CS = P.NoParam(), graph_userIn : PyRel[CITIES_CS,Tuple[CITIES_CS,int]] = P.NoParam(), sort_func_userIn : PyRel[PyRel[int,Tuple[CITIES_CS,int]],PyRel[int,Tuple[CITIES_CS,int]]] = P.NoParam(), source_userIn : CITIES_CS = P.NoParam() ) -> None:

      if BERLIN_userIn is None:
         BERLIN_userIn = P.PyRandValGen("CITIES_CS")
      if BOGOTA_userIn is None:
         BOGOTA_userIn = P.PyRandValGen("CITIES_CS")
      if CALI_userIn is None:
         CALI_userIn = P.PyRandValGen("CITIES_CS")
      if LA_userIn is None:
         LA_userIn = P.PyRandValGen("CITIES_CS")
      if MADRID_userIn is None:
         MADRID_userIn = P.PyRandValGen("CITIES_CS")
      if SANFRANCISCO_userIn is None:
         SANFRANCISCO_userIn = P.PyRandValGen("CITIES_CS")
      if TOKYO_userIn is None:
         TOKYO_userIn = P.PyRandValGen("CITIES_CS")
      if graph_userIn is None:
         graph_userIn = P.PyRandValGen("PyRel[CITIES_CS,Tuple[CITIES_CS,int]]")
      if sort_func_userIn is None:
         sort_func_userIn = P.PyRandValGen("PyRel[PyRel[int,Tuple[CITIES_CS,int]],PyRel[int,Tuple[CITIES_CS,int]]]")
      if source_userIn is None:
         source_userIn = P.PyRandValGen("CITIES_CS")

      if self.__Initialized_Context: raise Exception("Context already initialized!")
      self.__Initialized_Context = True

      #Enable Attributes Set Method
      self.__Attributes_SetFlag = True

      self.BERLIN = BERLIN_userIn
      self.BOGOTA = BOGOTA_userIn
      self.CALI = CALI_userIn
      self.LA = LA_userIn
      self.MADRID = MADRID_userIn
      self.SANFRANCISCO = SANFRANCISCO_userIn
      self.TOKYO = TOKYO_userIn
      self.graph = graph_userIn
      self.sort_func = sort_func_userIn
      self.source = source_userIn

      if P.DESIGN_BY_CONTRACT_ENABLED():
         attempt_Count : int = 0
         while not(self.checkAllAxioms()):
            self.BERLIN = P.PyRandValGen("CITIES_CS")
            self.BOGOTA = P.PyRandValGen("CITIES_CS")
            self.CALI = P.PyRandValGen("CITIES_CS")
            self.LA = P.PyRandValGen("CITIES_CS")
            self.MADRID = P.PyRandValGen("CITIES_CS")
            self.SANFRANCISCO = P.PyRandValGen("CITIES_CS")
            self.TOKYO = P.PyRandValGen("CITIES_CS")
            self.graph = P.PyRandValGen("PyRel[CITIES_CS,Tuple[CITIES_CS,int]]")
            self.sort_func = P.PyRandValGen("PyRel[PyRel[int,Tuple[CITIES_CS,int]],PyRel[int,Tuple[CITIES_CS,int]]]")
            self.source = P.PyRandValGen("CITIES_CS")
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
      tmp_values.append("DjkstraCtx Constants")

      tmp_values.append("BERLIN ==> " + str(self.BERLIN))
      tmp_values.append("BOGOTA ==> " + str(self.BOGOTA))
      tmp_values.append("CALI ==> " + str(self.CALI))
      tmp_values.append("LA ==> " + str(self.LA))
      tmp_values.append("MADRID ==> " + str(self.MADRID))
      tmp_values.append("SANFRANCISCO ==> " + str(self.SANFRANCISCO))
      tmp_values.append("TOKYO ==> " + str(self.TOKYO))
      tmp_values.append("graph ==> " + str(self.graph))
      tmp_values.append("sort_func ==> " + str(self.sort_func))
      tmp_values.append("source ==> " + str(self.source))

      return "\n".join(tmp_values)

   def __repr__(self) -> str:
      return self.__str__()
