#DEPENDENCIES

#Allow Path Access to the Prelude's Directory

import sys
if not(".." in sys.path):
   sys.path.append("..")

#Utilities Dependencies
from Py_Preludes import *

#Typing Dependencies
from typing import List

#Machine Refinement Dependencies
from TrafficLightSystemMch_mch import *

#Machine Internal Context Dependencies
from TrafficLightSystemCtx_ctx import *


#Translation of Machine: TrafficLightSystemRef
#This machine refines the following machine: TrafficLightSystemMch_class
#This machine sees the following context: TrafficLightSystemCtx_class


class TrafficLightSystemRef_class(TrafficLightSystemMch_class):

   def __init__( self , TrafficLightSystemCtx_userIn : TrafficLightSystemCtx_class = TrafficLightSystemCtx_class() ) -> None:

      #Assign Parameter to Context Extended Dependency Object
      self.__TrafficLightSystemCtx : TrafficLightSystemCtx_class = TrafficLightSystemCtx_userIn
      if not(self.__TrafficLightSystemCtx.Initialized_ContextGetMethod()):
         self.__TrafficLightSystemCtx.checkedInit()

      #Variables
      self.cars_colours : PySet[COLOURS_CS]
      self.cars_go : bool
      self.peds_colour : COLOURS_CS
      self.peds_go : bool
      #EndVariables

      #INITIALISATION of variables
      self.cars_go = False
      self.peds_go = False
      self.peds_colour = self.TrafficLightSystemCtx_get().red
      self.cars_colours = PySet({self.TrafficLightSystemCtx_get().red})

      #Check ALL Invariants if enabled.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("Invariants violated after INITIALISATION.")

   #Internal Context Dependency Object Get Method

   def TrafficLightSystemCtx_get(self) -> TrafficLightSystemCtx_class:
      return self.__TrafficLightSystemCtx

   #Variables Get/Set Methods

   @property
   def cars_colours(self) -> PySet[COLOURS_CS]:
      return self.__cars_colours

   @cars_colours.setter
   def cars_colours(self, cars_colours_userIn : PySet[COLOURS_CS]) -> None:
      self.__cars_colours : PySet[COLOURS_CS] = cars_colours_userIn

   @property
   def cars_go(self) -> bool:
      return self.__cars_go

   @cars_go.setter
   def cars_go(self, cars_go_userIn : bool) -> None:
      self.__cars_go : bool = cars_go_userIn

   @property
   def peds_colour(self) -> COLOURS_CS:
      return self.__peds_colour

   @peds_colour.setter
   def peds_colour(self, peds_colour_userIn : COLOURS_CS) -> None:
      self.__peds_colour : COLOURS_CS = peds_colour_userIn

   @property
   def peds_go(self) -> bool:
      return self.__peds_go

   @peds_go.setter
   def peds_go(self, peds_go_userIn : bool) -> None:
      self.__peds_go : bool = peds_go_userIn

   #End Variables Get Methods

   #Invariants Check Methods

   def gluing_invariantCheck(self) -> bool:
      return PyPrelude.LogicEquivalence(self.peds_go == True, self.peds_colour == self.TrafficLightSystemCtx_get().green)

   def gluing_cars_invariantCheck(self) -> bool:
      return PyPrelude.LogicEquivalence(self.cars_go == True, self.cars_colours.PyContains(self.TrafficLightSystemCtx_get().green))

   def inv0_invariantCheck(self) -> bool:
      return P.BOOL().PyContains(self.cars_go)

   def inv1_invariantCheck(self) -> bool:
      return P.BOOL().PyContains(self.peds_go)

   def inv10_invariantCheck(self) -> bool:
      return PySet({self.TrafficLightSystemCtx_get().red, self.TrafficLightSystemCtx_get().green}).PyContains(self.peds_colour)

   def inv11_invariantCheck(self) -> bool:
      return self.cars_colours.PyIsSubset(self.TrafficLightSystemCtx_get().COLOURS)

   def inv2_invariantCheck(self) -> bool:
      return not((self.cars_go == True and self.peds_go == True))

   #Check ALL Invariants

   def checkAllInvariants(self) -> bool:
      checkedAns_local : bool = True
      allInvariants_local : List[str] = [ "gluing" , "gluing_cars" , "inv0" , "inv1" , "inv10" , "inv11" , "inv2" ]

      for Invariant_local in allInvariants_local:
         InvariantMethod_local = getattr(self,Invariant_local + "_invariantCheck")
         checkedAns_local = checkedAns_local and InvariantMethod_local()

      return checkedAns_local

   #End Check ALL Invariants Method

   #Events

   #set_peds_go - Event

   def set_peds_go_eventGuards(self) -> bool:
      guard_ans : bool = True

      #Set Parameters as an Attribute.

      #Check Event PreConditions.
      if P.DESIGN_BY_CONTRACT_ENABLED():
         try:
            if True and (self.cars_go == False) and (self.cars_colours.PyNotContains(self.TrafficLightSystemCtx_get().green)):
               guard_ans = True
            else:
               guard_ans = False
         except:
            guard_ans = False
      else:
         guard_ans = True

      return guard_ans

   def set_peds_go_eventActions(self) -> None:

      attempt_Count : int = 0
      while not(self.set_peds_go_eventGuards()):
         if attempt_Count == P.LOWMAXGENATTEMPTS():
            raise GuardsViolated("Guards of the Event could not be fulfilled.")
         attempt_Count += 1

      #Set Parameters as an Attribute.

      #Event Actions

      self.peds_go, self.peds_colour = True, self.TrafficLightSystemCtx_get().green

      #Check Invariants after the actions are executed.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("PostConditions of the Event could not be fulfilled.")


   #End Event

   #set_peds_stop - Event

   def set_peds_stop_eventGuards(self) -> bool:
      guard_ans : bool = True

      #Set Parameters as an Attribute.

      #Check Event PreConditions.
      if P.DESIGN_BY_CONTRACT_ENABLED():
         try:
            if True:
               guard_ans = True
            else:
               guard_ans = False
         except:
            guard_ans = False
      else:
         guard_ans = True

      return guard_ans

   def set_peds_stop_eventActions(self) -> None:

      if not(self.set_peds_stop_eventGuards()):
         raise GuardsViolated("Guards of the Event could not be fulfilled.")

      #Set Parameters as an Attribute.

      #Event Actions

      self.peds_go, self.peds_colour = False, self.TrafficLightSystemCtx_get().red

      #Check Invariants after the actions are executed.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("PostConditions of the Event could not be fulfilled.")


   #End Event

   #set_cars - Event

   def set_cars_eventGuards(self, new_value_userIn : bool, new_value_colours_userIn : PySet[COLOURS_CS]) -> bool:
      guard_ans : bool = True

      #Set Parameters as an Attribute.
      self.new_value : bool = new_value_userIn
      self.new_value_colours : PySet[COLOURS_CS] = new_value_colours_userIn

      #Check Event PreConditions.
      if P.DESIGN_BY_CONTRACT_ENABLED():
         try:
            if True and (P.BOOL().PyContains(self.new_value)) and (PyPrelude.LogicImplication(self.new_value == True, self.peds_go == False)) and (self.new_value_colours.PyIsSubset(self.TrafficLightSystemCtx_get().COLOURS)) and (PyPrelude.LogicImplication(self.new_value_colours.PyContains(self.TrafficLightSystemCtx_get().green), self.peds_colour == self.TrafficLightSystemCtx_get().red)) and (PyPrelude.LogicImplication(self.cars_colours == PySet({self.TrafficLightSystemCtx_get().yellow}), self.new_value_colours == PySet({self.TrafficLightSystemCtx_get().red}))) and (PyPrelude.LogicImplication(self.cars_colours == PySet({self.TrafficLightSystemCtx_get().red}), self.new_value_colours == PySet({self.TrafficLightSystemCtx_get().red, self.TrafficLightSystemCtx_get().yellow}))) and (PyPrelude.LogicImplication(self.cars_colours == PySet({self.TrafficLightSystemCtx_get().red, self.TrafficLightSystemCtx_get().yellow}), self.new_value_colours == PySet({self.TrafficLightSystemCtx_get().green}))) and (PyPrelude.LogicImplication(self.cars_colours == PySet({self.TrafficLightSystemCtx_get().green}), self.new_value_colours == PySet({self.TrafficLightSystemCtx_get().yellow}))):
               guard_ans = True
            else:
               guard_ans = False
         except:
            guard_ans = False
      else:
         guard_ans = True

      del(self.new_value)
      del(self.new_value_colours)
      return guard_ans

   def set_cars_eventActions(self, new_value_userIn : bool = P.NoParam(), new_value_colours_userIn : PySet[COLOURS_CS] = P.NoParam()) -> None:

      if new_value_userIn is None:
         new_value_userIn = P.PyRandValGen("bool")
      if new_value_colours_userIn is None:
         new_value_colours_userIn = P.PyRandValGen("PySet[COLOURS_CS]")

      attempt_Count : int = 0
      while not(self.set_cars_eventGuards(new_value_userIn, new_value_colours_userIn)):
         new_value_userIn = P.PyRandValGen("bool")
         new_value_colours_userIn = P.PyRandValGen("PySet[COLOURS_CS]")
         if attempt_Count == P.LOWMAXGENATTEMPTS():
            raise GuardsViolated("Guards of the Event could not be fulfilled.")
         attempt_Count += 1

      #Set Parameters as an Attribute.
      self.new_value = new_value_userIn
      self.new_value_colours = new_value_colours_userIn

      #Event Actions

      self.cars_go, self.cars_colours = self.new_value, self.new_value_colours

      #Check Invariants after the actions are executed.
      if P.DESIGN_BY_CONTRACT_ENABLED() and not(self.checkAllInvariants()):
         raise Exception("PostConditions of the Event could not be fulfilled.")

      del(self.new_value)
      del(self.new_value_colours)

   #End Event

   #User/Debugging Functions

   def __str__(self) -> str:
      tmp_values : List[str] = list()

      #Print Internal Context Constants
      tmp_values.append(self.__TrafficLightSystemCtx.__str__())

      #Print Variables
      tmp_values.append("###")
      tmp_values.append("Variables")

      tmp_values.append("cars_colours ==> " + str(self.cars_colours))
      tmp_values.append("cars_go ==> " + str(self.cars_go))
      tmp_values.append("peds_colour ==> " + str(self.peds_colour))
      tmp_values.append("peds_go ==> " + str(self.peds_go))

      return "\n".join(tmp_values)

   def __repr__(self) -> str:
      return self.__str__()

   def PyGuardsState(self) -> None:
      #This method will show which events (with no parameters) can be executed.
      tmp_values : List[str] = list()
      list_events_noparams : List[str] = ["set_peds_go", "set_peds_stop"]
      list_events_params : List[Tuple[str,List[str]]] = [("set_cars",["bool", "PySet[COLOURS_CS]"])]
      tmp_values.append("State of the Guards of every event!")
      for event_name in list_events_noparams:
         guards_to_check = getattr(self,event_name + "_eventGuards")
         tmp_values.append(event_name + " ==> " + str(guards_to_check()))
      for event_name,params_type in list_events_params:
         if len(params_type)>1:
            tmp_values.append(event_name + " ==> Undetermined")
            continue
         guards_to_check = getattr(self,event_name + "_eventGuards")
         guards_state = False
         for possible_any in P.ObtainSetFromType(params_type[0]):
            try:
               guards_state = guards_to_check(possible_any)
            except:
               continue
            if guards_state:
               tmp_values.append(event_name + " ==> " + str(guards_state) + ", e.g. with param = " + str(possible_any))
               break
         if not guards_state:
            tmp_values.append(event_name + " ==> " + str(guards_state))
      print("\n".join(tmp_values))

   def PyAutoExecute(self) -> None:
      #This method will try to find an event to execute.
      list_events_strs : List[str] = ["set_peds_go", "set_peds_stop", "set_cars"]
      amount_of_events : int = len(list_events_strs)
      attempt_count : int = 0
      while(attempt_count < P.MaxAutoExecuteAttempts()):
         event_iter : int = randint(0,amount_of_events-1)
         event_name : str = list_events_strs[event_iter]
         try:
            event_to_attempt = getattr(self,event_name + "_eventActions")
            event_to_attempt()
            print(event_name + " succesfully executed!!!")
            print(self)
            return
         except GuardsViolated:
            attempt_count += 1
      print("No event could be AutoExecuted")
