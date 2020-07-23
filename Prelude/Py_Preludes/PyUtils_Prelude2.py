#imports Enum
from enum import Enum,auto,unique

#imports Typing
from typing import Set,TypeVar,Generic,Any,Callable,cast,Iterator,Tuple,Any,Dict,Type,List,Optional

#imports Utils
from copy import deepcopy

#imports Random
from random import randint,choice

#Supporting Imports
from math import log2

#Supporting Variables

T = TypeVar('T')
D = TypeVar('D')
R = TypeVar('R')

class PyBaseFunc():

   @staticmethod
   def Unspecified_FuncBool0() -> bool:
      #print('Test_PreludeBaseFunc.Unspecified_FuncBool0')
      raise Exception('No special Bool Function 0 args was set for this object')

   @staticmethod
   def Unspecified_FuncInt0() -> int:
      #print('Test_PreludeBaseFunc.Unspecified_FuncInt0')
      raise Exception('No special Int Function 0 args was set for this object')

   @staticmethod
   def Unspecified_FuncBool1(element : Any) -> bool:
      #print('Test_PreludeBaseFunc.Unspecified_FuncBool1')
      raise Exception('No special Bool Function 1 arg was set for this object')

   @staticmethod
   def Unspecified_FuncInt1(element : Any) -> int:
      #print('Test_PreludeBaseFunc.Unspecified_FuncInt1')
      raise Exception('No special Int Function 1 arg was set for this object')

   @staticmethod
   def Unspecified_FuncPySet0() -> 'PySet':
      #print('Test_PreludeBaseFunc.Unspecified_FuncPySet0')
      raise Exception('No special PySet Function 0 arg was set for this object')

   @staticmethod
   def Unspecified_FuncPySet1(element : Any) -> 'PySet':
      #print('Test_PreludeBaseFunc.Unspecified_FuncPySet1')
      raise Exception('No special PySet Function 1 arg was set for this object')

   @staticmethod
   def ReturnFalse0() -> bool:
      #print('Test_PreludeBaseFunc.ReturnFalse0')
      return False

   @staticmethod
   def ReturnFalse1(element : Any) -> bool:
      #print('Test_PreludeBaseFunc.ReturnFalse1')
      return False

   @staticmethod
   def ReturnTrue0() -> bool:
      #print('Test_PreludeBaseFunc.ReturnTrue0')
      return True

   @staticmethod
   def ReturnTrue1(element : Any) -> bool:
      #print('Test_PreludeBaseFunc.ReturnTrue1')
      return True

   @staticmethod
   def NAT_ContainsFunc(element : int) -> bool:
      #print('Test_PreludeBaseFunc.NAT_ContainsFunc')
      if isinstance(element,int) and element >=0:
         return True
      return False
   
   @staticmethod
   def NAT1_ContainsFunc(element : int) -> bool:
      #print('Test_PreludeBaseFunc.NAT1_ContainsFunc')
      if isinstance(element,int) and element >0:
         return True
      return False

   @staticmethod
   def INT_ContainsFunc(element : int) -> bool:
      #print('Test_PreludeBaseFunc.INT_ContainsFunc')
      if isinstance(element,int):
         return True
      return False

   @staticmethod
   def PNAT_ContainsFunc(int_set : 'PySet[int]') -> bool:
      #print('Test_PreludeBaseFunc.PNAT_ContainsFunc')
      for element in int_set:
         if not PyBaseFunc.NAT_ContainsFunc(element):
            return False
      return True
   
   @staticmethod
   def PNAT1_ContainsFunc(int_set : 'PySet[int]') -> bool:
      #print('Test_PreludeBaseFunc.PNAT1_ContainsFunc')
      for element in int_set:
         if not PyBaseFunc.NAT1_ContainsFunc(element):
            return False
      return True

   @staticmethod
   def PINT_ContainsFunc(int_set : 'PySet[int]') -> bool:
      #print('Test_PreludeBaseFunc.PINT_ContainsFunc')
      for element in int_set:
         if not PyBaseFunc.INT_ContainsFunc(element):
            return False
      return True

   @staticmethod
   def P1NAT_ContainsFunc(int_set : 'PySet[int]') -> bool:
      #print('Test_PreludeBaseFunc.P1NAT_ContainsFunc')
      for element in int_set:
         if not PyBaseFunc.NAT_ContainsFunc(element):
            return False
      if len(int_set)>0:
         return True
      return False
   
   @staticmethod
   def P1NAT1_ContainsFunc(int_set : 'PySet[int]') -> bool:
      #print('Test_PreludeBaseFunc.P1NAT1_ContainsFunc')
      for element in int_set:
         if not PyBaseFunc.NAT1_ContainsFunc(element):
            return False
      if len(int_set)>0:
         return True
      return False

   @staticmethod
   def P1INT_ContainsFunc(int_set : 'PySet[int]') -> bool:
      #print('Test_PreludeBaseFunc.P1INT_ContainsFunc')
      for element in int_set:
         if not PyBaseFunc.INT_ContainsFunc(element):
            return False
      if len(int_set)>0:
         return True
      return False

   @staticmethod
   def PNATXNAT_ContainsFunc(natxnat_set : 'PyRel[int,int]') -> bool:
      #print('Test_PreludeBaseFunc.PNATXNAT_ContainsFunc')
      for left_ele,right_ele in natxnat_set:
         if not PyBaseFunc.NAT_ContainsFunc(left_ele) or not PyBaseFunc.NAT_ContainsFunc(right_ele):
            return False
      return True
   
   @staticmethod
   def PINTXINT_ContainsFunc(intxint_set : 'PyRel[int,int]') -> bool:
      #print('Test_PreludeBaseFunc.PINTXINT_ContainsFunc')
      for left_ele,right_ele in intxint_set:
         if not PyBaseFunc.INT_ContainsFunc(left_ele) or not PyBaseFunc.INT_ContainsFunc(right_ele):
            return False
      return True

   @staticmethod
   def PINTXNAT_ContainsFunc(intxnat_set : 'PyRel[int,int]') -> bool:
      #print('Test_PreludeBaseFunc.PINTXNAT_ContainsFunc')
      for left_ele,right_ele in intxnat_set:
         if not PyBaseFunc.INT_ContainsFunc(left_ele) or not PyBaseFunc.NAT_ContainsFunc(right_ele):
            return False
      return True

   @staticmethod
   def P1NATXNAT_ContainsFunc(natxnat_set : 'PyRel[int,int]') -> bool:
      #print('Test_PreludeBaseFunc.P1NATXNAT_ContainsFunc')
      for left_ele,right_ele in natxnat_set:
         if not PyBaseFunc.NAT_ContainsFunc(left_ele) or not PyBaseFunc.NAT_ContainsFunc(right_ele):
            return False
      if len(natxnat_set)>0:
         return True
      return False
   
   @staticmethod
   def P1INTXINT_ContainsFunc(intxint_set : 'PyRel[int,int]') -> bool:
      #print('Test_PreludeBaseFunc.P1INTXINT_ContainsFunc')
      for left_ele,right_ele in intxint_set:
         if not PyBaseFunc.INT_ContainsFunc(left_ele) or not PyBaseFunc.INT_ContainsFunc(right_ele):
            return False
      if len(intxint_set)>0:
         return True
      return False

   @staticmethod
   def P1INTXNAT_ContainsFunc(intxnat_set : 'PyRel[int,int]') -> bool:
      #print('Test_PreludeBaseFunc.P1INTXNAT_ContainsFunc')
      for left_ele,right_ele in intxnat_set:
         if not PyBaseFunc.INT_ContainsFunc(left_ele) or not PyBaseFunc.NAT_ContainsFunc(right_ele):
            return False
      if len(intxnat_set)>0:
         return True
      return False

   ###Debug Method
   @staticmethod
   def test(element:int) -> bool:
      #print('Test_PreludesBaseFunc.test')
      if element < -80 and element > -100:
         return True
      return False

   @staticmethod
   def ReturnEmptySet0() -> 'PySet':
      #print('Test_PreludeBaseFunc.ReturnEmptySet0')
      return PySet()
   
   @staticmethod
   def ReturnEmptySet1(set_elems : 'PySet') -> 'PySet':
      #print('Test_PreludeBaseFunc.ReturnEmptySet0')
      return PySet()

   @staticmethod
   def ReturnPyNAT_0() -> 'PyNAT':
      return PyNAT()

   @staticmethod
   def ReturnPyINT_0() -> 'PyINT':
      return PyINT()

   @staticmethod
   def ReturnPyNAT_1(int_set : 'PySet[int]') -> 'PyNAT':
      return PyNAT()

   @staticmethod
   def ReturnPyINT_1(int_set : 'PySet[int]') -> 'PyINT':
      return PyINT()

   @staticmethod
   def ReturnPyNAT_NAT(nat_set : 'PySet[int]') -> 'PySet[int]':
      for nat_ele in nat_set:
         if PyBaseFunc.NAT_ContainsFunc(nat_ele):
            return PyNAT()
      return PySet()

   @staticmethod
   def ReturnPyNAT_INT(nat_set : 'PySet[int]') -> 'PySet[int]':
      for nat_ele in nat_set:
         if PyBaseFunc.NAT_ContainsFunc(nat_ele):
            return PyINT()
      return PySet()

   @staticmethod
   def ID_Rel_Func(any_set : 'PySet') -> 'PySet':
      return any_set

   ###Debug Method
   @staticmethod
   def test2(dom_elements : 'PySet[int]') -> 'PySet[int]':
      #print('Test_PreludesBaseFunc.test2')
      ans_set : Set[int] = set()
      for dom_ele in dom_elements:
         if dom_ele == 1:
            ans_set.update({10,100})
         elif dom_ele == 2:
            ans_set.update({20,200})
         elif dom_ele == 3:
            ans_set.update({3,4,7})
      return PySet(ans_set)


@unique
class PyFamilyTypes(Enum):

   UndeterminedFamilyType = auto()
   Relations = auto()
   TotalRelations = auto()
   SurjectiveRelations = auto()
   TotalSurjectiveRelations = auto()
   PartialFunctions = auto()
   TotalFunctions = auto()
   PartialInjections = auto()
   TotalInjections = auto()
   PartialSurjections = auto()
   TotalSurjections = auto()
   Bijections = auto()


class GuardsViolated(Exception):
   pass


class PyBaseIter():

   def __iter__(self) -> Iterator:
      return self
   
   def __next__(self):
      raise Exception('No special __next__ Function was specified for this object')

class PyNAT_Iter(PyBaseIter):

   def __iter__(self) -> Iterator:
      self.boundary : int = P.FINITE_SPECIAL_SETS_LIMIT()
      self.iterator : int = -1
      return self
   
   def __next__(self) -> int:
      if P.USE_FINITE_SPECIAL_SETS():
         self.iterator += 1
         if self.iterator > self.boundary:
            raise StopIteration
         return self.iterator
         
      raise Exception('You cannot traverse an infinite set. Set the Prelude Parameter USE_FINITE_SPECIAL_SETS to True.')

class PyNAT1_Iter(PyBaseIter):

   def __iter__(self) -> Iterator:
      self.boundary : int = P.FINITE_SPECIAL_SETS_LIMIT()
      self.iterator : int = 0
      return self
   
   def __next__(self) -> int:
      if P.USE_FINITE_SPECIAL_SETS():
         self.iterator += 1
         if self.iterator > self.boundary:
            raise StopIteration
         return self.iterator
         
      raise Exception('You cannot traverse an infinite set. Set the Prelude Parameter USE_FINITE_SPECIAL_SETS to True.')

class PyINT_Iter(PyBaseIter):

   def __iter__(self) -> Iterator:
      self.boundary : int = P.FINITE_SPECIAL_SETS_LIMIT()
      self.iterator : int = - self.boundary - 1
      return self
   
   def __next__(self) -> int:
      if P.USE_FINITE_SPECIAL_SETS():
         self.iterator += 1
         if self.iterator > self.boundary:
            raise StopIteration
         return self.iterator
      raise Exception('You cannot traverse an infinite set. Set the Prelude Parameter USE_FINITE_SPECIAL_SETS to True.')

class PySet(Generic[T]):

   def __init__(self, initialElements : Set[T] = set()) -> None:
      #print('Test_PySet.__init__')
      self.__FiniteInclusion : Set[T] = initialElements

   def FiniteInclusion(self) -> Set[T]:
      return self.__FiniteInclusion.copy()

   def __str__(self) -> str:
      return 'PySet(' + self.__FiniteInclusion.__str__() + ')'

   def __repr__(self) -> str:
      return 'PySet(' + self.__FiniteInclusion.__repr__() + ')'

   def __len__(self) -> int:
      return len(self.__FiniteInclusion)

   def __iter__(self) -> Iterator: #Necessary to be able to override __contains__
      return self.__FiniteInclusion.__iter__()

   def __eq__(self,other) -> bool:
      if isinstance(other,PyCondSet) or isinstance(other,PyCondRel):
         raise Exception('Operation not supported for implicit Sets')
      if isinstance(other,PySet) or isinstance(other,PyRel):
         return self.__FiniteInclusion.__eq__(other.FiniteInclusion())
      raise Exception('Operation only supported for PySet')

   def __hash__(self):
      return hash(frozenset(self.__FiniteInclusion))

   def __contains__(self,element : object) -> bool: #Liskov Principle
      raise Exception('Due to the Liskov Principle, TypeCheck will not work, use PyContains instead.')

   def PyContains(self,element : T) -> bool:
      #O(1)
      #print('Test_PySet.PyContains')
      return self.__FiniteInclusion.__contains__(element)

   def PyNotContains(self,element : T) -> bool:
      #O(1)
      #print('Test_PySet.PyNotContains')
      return not self.PyContains(element)

   def PyUnion(self, other : 'PySet[T]') -> 'PySet[T]':
      #O(m+n) between PySets.
      #print('Test_PySet.PyUnion')

      if isinstance(other, PyCondSet_TreeExt):
         return other.PyUnion(self)
      elif isinstance(other, PyCondSet_Ext):
         new_finite_inclusion : Set = other.FiniteInclusion().union(self.__FiniteInclusion)
         return PyCondSet_Ext(other.FuncContains(), new_finite_inclusion, other.FiniteExclusion().difference(new_finite_inclusion))
      elif isinstance(other, PyCondSet):
         return PyCondSet_Ext(other.FuncContains(), self.FiniteInclusion())
      return PySet(self.__FiniteInclusion.union(other.FiniteInclusion()))

   def PyIntersection(self, other : 'PySet[T]') -> 'PySet[T]':
      #O(m) between PySets.
      #print('Test_PySet.PyIntersection')
      
      if isinstance(other, PyCondSet):
         intersection_set : Set = set()
         for element in self:
            if other.PyContains(element):
               intersection_set.add(element)
         return PySet(intersection_set)
      return PySet(self.__FiniteInclusion.intersection(other.FiniteInclusion()))

   def PyDifference(self, other : 'PySet[T]') -> 'PySet[T]':
      #O(m) between PySets.
      #print('Test_PySet.PyDifference')

      if isinstance(other, PyCondSet):
         difference_set : Set = self.FiniteInclusion()
         for element in self:
            if other.PyContains(element):
               difference_set.discard(element)
         return PySet(difference_set)
      return PySet(self.__FiniteInclusion.difference(other.FiniteInclusion()))

   def PyCartesianProduct(self, other : 'PySet') -> 'PyRel[T,Any]':
      #O(m*n) between PySets.
      #print('Test_PySet.PyCartesianProduct')
      if isinstance(other, PyCondSet_Ext):
         raise Exception('Operation only supported between iterable PySets')
      cartesian_product : Set[Tuple[T,Any]] = set()
      for self_ele in self:
         for other_ele in other:
            cartesian_product.add((self_ele, other_ele))
      return PyRel(cartesian_product)

   def PyIsSubset(self, other : 'PySet[T]') -> bool:
      #O(n)
      #print('Test_PySet.PyIsSubset')
      for element in self:
         if not(other.PyContains(element)):
            return False
      return True

   def PyNotSubset(self, other : 'PySet[T]') -> bool:
      #O(n)
      #print('Test_PySet.PyNotSubset')
      return not self.PyIsSubset(other)

   def PyIsProperSubset(self, other : 'PySet[T]') -> bool:
      #O(n)
      #print('Test_PySet.PyIsProperSubset')
      if len(self)==len(other):
         return False
      return self.PyIsSubset(other)

   def PyNotProperSubset(self, other : 'PySet[T]') -> bool:
      #O(n)
      #print('Test_PySet.PyNotProperSubset')
      return not self.PyIsProperSubset(other)

   def PyFinite(self) -> bool:
      #O(1)
      #print('Test_PySet.PyFinite')
      return True

   def PyPartition(self, partition_sets : 'List[PySet[T]]') -> bool:
      #print('Test_PySet.PyPartition')
      checking_set : PySet[T] = PySet()
      for partition_set in partition_sets:
         if isinstance(partition_set, PyCondSet):
            raise Exception('Operation only supported between PySets')
         if len(checking_set.PyIntersection(partition_set)) > 0:
            return False
         checking_set = checking_set.PyUnion(partition_set)
      if checking_set.__eq__(self):
         return True
      return False

   def PyPowerSet(self) -> 'PySet[PySet[T]]':
      #print('Test_PySet.PyPowerSet')
      elements_list : List[T] = list(self.FiniteInclusion())
      power_set : Set[PySet[T]] = set()
      for set_picker in range(2**len(self)):
         current_set : Set[T] = set()
         for i in range(len(self)):
            if set_picker & 1<<i != 0:
               current_set.add(elements_list[i])
         power_set.add(PySet(current_set))
      return PySet(power_set)

   def PyPowerSet1(self) -> 'PySet[PySet[T]]':
      #print('Test_PySet.PyPowerSet1')
      elements_list : List[T] = list(self.FiniteInclusion())
      power_set : Set[PySet[T]] = set()
      for set_picker in range(1,2**len(self)):
         current_set : Set[T] = set()
         for i in range(len(self)):
            if set_picker & 1<<i != 0:
               current_set.add(elements_list[i])
         power_set.add(PySet(current_set))
      return PySet(power_set)

   def PyChoice(self) -> T:
      #print('Test_PySet.PyChoice')
      return choice(list(self.__FiniteInclusion))

   def PyDomain(self) -> 'PySet[D]':
      #print('Test_PySet.PyDomain')
      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)
      return tmp_pyrel.PyDomain()

   def PyRange(self) -> 'PySet[R]':
      #print('Test_PySet.PyRange')
      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)
      return tmp_pyrel.PyRange()

   def PyComposition(self, other : 'PyRel[R,T]') -> 'PyRel[D,T]':
      #print('Test_PySet.PyComposition')
      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)
      return tmp_pyrel.PyComposition(other)

   def PyBackwardComposition(self, other : 'PyRel[T,D]') -> 'PyRel[T,R]':
      #print('Test_PySet.PyBackwardComposition')
      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)
      return tmp_pyrel.PyBackwardComposition(other)

   def PyDomainRestriction(self, other : 'PySet[D]') -> 'PyRel[D,R]':
      #print('Test_PySet.PyDomainRestriction')
      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)
      return tmp_pyrel.PyDomainRestriction(other)

   def PyRangeRestriction(self, other : 'PySet[R]') -> 'PyRel[D,R]':
      #print('Test_PySet.PyRangeRestriction')
      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)
      return tmp_pyrel.PyRangeRestriction(other)

   def PyDomainSubstraction(self, other : 'PySet[D]') -> 'PyRel[D,R]':
      #print('Test_PySet.PyDomainSubstraction')
      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)
      return tmp_pyrel.PyDomainSubstraction(other)

   def PyRangeSubstraction(self, other : 'PySet[R]') -> 'PyRel[D,R]':
      #print('Test_PySet.PyRangeSubstraction')
      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)
      return tmp_pyrel.PyRangeSubstraction(other)

   def __invert__(self) -> 'PyRel[R,D]': #Inverse Relation method
      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)
      return tmp_pyrel.__invert__()

   def __getitem__(self, keys : 'PySet[D]') -> 'PySet[R]': #Relational Image method
      #O(range)
      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)
      return tmp_pyrel.__getitem__(keys)

   def PyOverriding(self, other : 'PyRel[D,R]') -> 'PyRel[D,R]':
      #print('Test_PySet.PyOverriding')
      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)
      return tmp_pyrel.PyOverriding(other)

   def PyDirectProduct(self, other : 'PyRel[D,T]') -> 'PyRel[D,Tuple[R,T]]':
      #print('Test_PySet.PyDirectProduct')
      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)
      return tmp_pyrel.PyDirectProduct(other)

   def PyIsTotal(self, domain_set : 'PySet[D]') -> bool:
      #print('Test_PySet.PyIsTotal')
      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)
      return tmp_pyrel.PyIsTotal(domain_set)

   def PyIsSurjection(self, range_set : 'PySet[R]') -> bool:
      #print('Test_PySet.PyIsSurjection')
      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)
      return tmp_pyrel.PyIsSurjection(range_set)

   def PyIsRelation(self, domain_set : 'PySet[D]', range_set : 'PySet[R]') -> bool:
      #print('Test_PySet.PyIsRelation')
      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)
      return tmp_pyrel.PyIsRelation(domain_set,range_set)

   def PyIsTotalRelation(self, domain_set : 'PySet[D]', range_set : 'PySet[R]') -> bool:
      #print('Test_PySet.PyIsTotalRelation')
      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)
      return tmp_pyrel.PyIsTotalRelation(domain_set,range_set)

   def PyIsSurjectiveRelation(self, domain_set : 'PySet[D]', range_set : 'PySet[R]') -> bool:
      #print('Test_PySet.PyIsSurjectiveRelation')
      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)
      return tmp_pyrel.PyIsSurjectiveRelation(domain_set,range_set)

   def PyIsTotalSurjectiveRelation(self, domain_set : 'PySet[D]', range_set : 'PySet[R]') -> bool:
      #print('Test_PySet.PyIsTotalSurjectiveRelation')
      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)
      return tmp_pyrel.PyIsTotalSurjectiveRelation(domain_set,range_set)

   def PyIsWellDefined(self) -> bool:
      #print('Test_PySet.PyIsWellDefined')
      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)
      return tmp_pyrel.PyIsWellDefined()

   def PyIsFunction(self, domain_set : 'PySet[D]', range_set : 'PySet[R]') -> bool:
      #print('Test_PySet.PyIsFunction')
      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)
      return tmp_pyrel.PyIsFunction(domain_set,range_set)

   def PyIsPartialFunction(self, domain_set : 'PySet[D]', range_set : 'PySet[R]') -> bool:
      #print('Test_PySet.PyIsPartialFunction')
      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)
      return tmp_pyrel.PyIsPartialFunction(domain_set,range_set)

   def PyIsTotalFunction(self, domain_set : 'PySet[D]', range_set : 'PySet[R]') -> bool:
      #print('Test_PySet.PyIsTotalFunction')
      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)
      return tmp_pyrel.PyIsTotalFunction(domain_set,range_set)

   def PyIsInjection(self) -> bool:
      #print('Test_PySet.PyIsInjection')
      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)
      return tmp_pyrel.PyIsInjection()

   def PyIsPartialInjection(self, domain_set : 'PySet[D]', range_set : 'PySet[R]') -> bool:
      #print('Test_PySet.PyIsPartialInjection')
      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)
      return tmp_pyrel.PyIsPartialInjection(domain_set,range_set)

   def PyIsTotalInjection(self, domain_set : 'PySet[D]', range_set : 'PySet[R]') -> bool:
      #print('Test_PySet.PyIsTotalInjection')
      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)
      return tmp_pyrel.PyIsTotalInjection(domain_set,range_set)

   def PyIsPartialSurjection(self, domain_set : 'PySet[D]', range_set : 'PySet[R]') -> bool:
      #print('Test_PySet.PyIsPartialSurjection')
      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)
      return tmp_pyrel.PyIsPartialSurjection(domain_set,range_set)

   def PyIsTotalSurjection(self, domain_set : 'PySet[D]', range_set : 'PySet[R]') -> bool:
      #print('Test_PySet.PyIsTotalSurjection')
      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)
      return tmp_pyrel.PyIsTotalSurjection(domain_set,range_set)

   def PyIsBijection(self, domain_set : 'PySet[D]', range_set : 'PySet[R]') -> bool:
      #print('Test_PySet.PyIsBijection')
      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)
      return tmp_pyrel.PyIsBijection(domain_set,range_set)

   def __call__(self, domain_element : D) -> R: #Apply method
      tmp_pyrel : PyRel = MypyPySetCastPyRel(self)
      return tmp_pyrel.__call__(domain_element)


class PyCondSet(PySet[T]):

   def __init__(self, funcContains : Callable[[T],bool] = PyBaseFunc.Unspecified_FuncBool1,
                iterator_class : PyBaseIter = PyBaseIter(),
                length_func : Callable[[],int] = PyBaseFunc.Unspecified_FuncInt0,
                finite_func : Callable[[],bool] = PyBaseFunc.Unspecified_FuncBool0) -> None:
      #print('Test_PyCondSet.__init__')
      self.__FuncContains : Callable[[T],bool] = funcContains
      self.__IteratorClass : PyBaseIter = iterator_class
      self.__LengthFunc : Callable[[],int] = length_func
      self.__FiniteFunc : Callable[[],bool] = finite_func

   def FuncContains(self) -> Callable[[T],bool]:
      return self.__FuncContains

   def IteratorClass(self) -> PyBaseIter:
      return self.__IteratorClass

   def LengthFunc(self) -> Callable[[],int]:
      return self.__LengthFunc

   def FiniteFunc(self) -> Callable[[],bool]:
      return self.__FiniteFunc

   def __str__(self) -> str:
      return 'PyCondSet(' + self.__FuncContains.__str__() + ')'

   def __repr__(self) -> str:
      return 'PyCondSet(' + self.__FuncContains.__str__() + ')'

   def __len__(self) -> int:
      return self.__LengthFunc()

   def __iter__(self) -> Iterator: #Necessary to be able to override __contains__
      return self.__IteratorClass.__iter__()

   def __eq__(self,other) -> bool:
      if isinstance(other, PyCondSet_TreeExt):
         raise Exception('Can not determine the result')
      elif isinstance(other, PyCondSet_Ext):
         if other.FuncContains() == self.__FuncContains and len(other.FiniteInclusion()) == 0 and len(other.FiniteExclusion()) == 0:
            return True
      elif isinstance(other, PyCondSet):
         if other.FuncContains() == self.__FuncContains:
            return True
      raise Exception('Can not determine the result')

   def __hash__(self):
      return hash(self.__FuncContains)

   # >> def __contains__(self,element : object) -> bool: #Inherited

   def PyContains(self,element : T) -> bool:
      #O(self.__FuncContains)
      #print('Test_PyCondSet.PyContains')
      return self.__FuncContains(element)

   # >> def PyNotContains(self,element : T) -> bool: #Inherited

   def PyUnion(self, other : 'PySet[T]') -> 'PySet[T]':
      #print('Test_PyCondSet.PyUnion')

      if isinstance(other, PyCondSet_TreeExt):
         return other.PyUnion(self)
      elif isinstance(other, PyCondSet_Ext):
         return PyCondSet_TreeExt(funcContains = self.FuncContains()).PyUnion(other)
      elif isinstance(other, PyCondSet):
         return PyCondSet_TreeExt(funcContains = self.FuncContains()).PyUnion(other)
      return other.PyUnion(self)

   def PyIntersection(self, other : 'PySet[T]') -> 'PySet[T]':
      #print('Test_PyCondSet.PyIntersection')
      
      if isinstance(other, PyCondSet_TreeExt):
         return other.PyIntersection(self)
      elif isinstance(other, PyCondSet_Ext):
         return PyCondSet_TreeExt(funcContains = self.FuncContains()).PyIntersection(other)
      elif isinstance(other, PyCondSet):
         return PyCondSet_TreeExt(funcContains = self.FuncContains()).PyIntersection(other)
      return other.PyIntersection(self)

   def PyDifference(self, other : 'PySet[T]') -> 'PySet[T]':
      #print('Test_PyCondSet.PyDifference')

      if isinstance(other, PyCondSet_TreeExt):
         return other.PyDifference(self)
      elif isinstance(other, PyCondSet_Ext):
         return PyCondSet_TreeExt(funcContains = self.FuncContains()).PyDifference(other)
      elif isinstance(other, PyCondSet):
         return PyCondSet_TreeExt(funcContains = self.FuncContains()).PyDifference(other)
      return PyCondSet_TreeExt(funcContains = self.FuncContains(),finiteExclusion = other.FiniteInclusion())

   # >> def PyCartesianProduct(self, other : 'PySet') -> 'PyRel[T,Any]': #Inherited + __iter__

   # >> def PyIsSubset(self, other : 'PySet[T]') -> bool: #Inherited + __iter__

   # >> def PyNotSubset(self, other : 'PySet[T]') -> bool: #Inherited + __iter__

   # >> def PyIsProperSubset(self, other : 'PySet[T]') -> bool: #Inherited + __iter__ + __len__

   # >> def PyNotProperSubset(self, other : 'PySet[T]') -> bool: #Inherited + __iter__ + __len__

   def PyFinite(self) -> bool:
      return self.__FiniteFunc()

   def PyPartition(self, partition_sets : 'List[PySet[T]]') -> bool:
      raise Exception('Operation not supported for Implicit Sets')

   def PyPowerSet(self) -> PySet[PySet[T]]: #Unsupported
      raise Exception('Operation not supported for Implicit Sets')

   def PyPowerSet1(self) -> PySet[PySet[T]]: #Unsupported
      raise Exception('Operation not supported for Implicit Sets')

   def PyChoice(self) -> T: #Unsupported
      #print('Test_PyCondSet.PyChoice')
      raise Exception('Operation not supported for Implicit Sets')


class PyNAT(PyCondSet[int]):

   def __init__(self) -> None:
      #print('Test_PyNAT.__init__')
      self._PyCondSet__FuncContains : Callable[[int],bool] = PyBaseFunc.NAT_ContainsFunc
      self._PyCondSet__IteratorClass : PyBaseIter = PyNAT_Iter()

   def __str__(self) -> str:
      return 'PyNAT()'

   def __repr__(self) -> str:
      return 'PyNAT()'

   def __len__(self) -> int: #Unsupported
      raise Exception('This set has no finite cardinality.')

   # >> def __iter__(self) -> Iterator: #Inherited

   # >> def __eq__(self,other) -> bool: #Inherited

   # >> def __hash__(self): #Inherited

   # >> def __contains__(self,element : object) -> bool: #Inherited

   # >> def PyContains(self,element : int) -> bool: #Inherited

   # >> def PyNotContains(self,element : int) -> bool: #Inherited

   def PyUnion(self, other : PySet[int]) -> PySet[int]:
      #print('Test_PyNAT.PyUnion')
      if isinstance(other, PyNAT):
         return PyNAT()
      if isinstance(other, PyNAT1):
         return PyNAT()
      if isinstance(other, PyINT):
         return PyINT()
      return super().PyUnion(other)

   def PyIntersection(self, other : PySet[int]) -> PySet[int]:
      #print('Test_PyNAT.PyIntersection')
      if isinstance(other, PyNAT):
         return PyNAT()
      if isinstance(other, PyNAT1):
         return PyNAT1()
      if isinstance(other, PyINT):
         return PyNAT()
      return super().PyIntersection(other)

   def PyDifference(self, other : PySet[int]) -> PySet[int]:
      #print('Test_PyNAT.PyDifference')
      if isinstance(other, PyNAT):
         return PySet()
      if isinstance(other, PyNAT1):
         return PySet({0})
      if isinstance(other, PyINT):
         return PySet()
      return super().PyDifference(other)

   def PyCartesianProduct(self, other : PySet[int]) -> 'PyRel[int,int]':
      #print('Test_PyNAT.PyCartesianProduct')
      if isinstance(other, PyNAT):
         return PyNATXNAT()
      return super().PyCartesianProduct(other)

   def PyIsSubset(self, other : PySet[int]) -> bool:
      #print('Test_PyNAT.PyIsSubset')
      if isinstance(other, PyNAT):
         return True
      if isinstance(other, PyNAT1):
         return False
      if isinstance(other, PyINT):
         return True
      if other.PyFinite():
         return False
      return super().PyIsSubset(other)

   # >> def PyNotSubset(self, other : 'PySet[int]') -> bool: #Inherited

   def PyIsProperSubset(self, other : PySet[int]) -> bool:
      #print('Test_PyNAT.PyIsProperSubset')
      if isinstance(other, PyNAT):
         return False
      if isinstance(other, PyNAT1):
         return False
      if isinstance(other, PyINT):
         return True
      if other.PyFinite():
         return False
      raise Exception('Can not determine the result')

   # >> def PyNotProperSubset(self, other : 'PySet[int]') -> bool: #Inherited

   def PyFinite(self) -> bool:
      return False

   # >> def PyPartition(self, partition_sets : 'List[PySet[int]]') -> bool: #Inherited #Unsupported

   def PyPowerSet(self) -> PySet[PySet[int]]:
      return PyCondSet(PyBaseFunc.PNAT_ContainsFunc, finite_func = PyBaseFunc.ReturnFalse0)

   def PyPowerSet1(self) -> PySet[PySet[int]]:
      return PyCondSet(PyBaseFunc.P1NAT_ContainsFunc, finite_func = PyBaseFunc.ReturnFalse0)

   def PyChoice(self) -> int:
      #print('Test_PyNAT.PyChoice')
      return randint(0,P.RAND_INT_RANGE()[1])


class PyNAT1(PyCondSet[int]):

   def __init__(self) -> None:
      #print('Test_PyNAT1.__init__')
      self._PyCondSet__FuncContains : Callable[[int],bool] = PyBaseFunc.NAT1_ContainsFunc
      self._PyCondSet__IteratorClass : PyBaseIter = PyNAT1_Iter()

   def __str__(self) -> str:
      return 'PyNAT1()'

   def __repr__(self) -> str:
      return 'PyNAT1()'

   def __len__(self) -> int: #Unsupported
      raise Exception('This set has no finite cardinality.')

   # >> def __iter__(self) -> Iterator: #Inherited

   # >> def __eq__(self,other) -> bool: #Inherited

   # >> def __hash__(self): #Inherited

   # >> def __contains__(self,element : object) -> bool: #Inherited

   # >> def PyContains(self,element : int) -> bool: #Inherited

   # >> def PyNotContains(self,element : int) -> bool: #Inherited

   def PyUnion(self, other : PySet[int]) -> PySet[int]:
      #print('Test_PyNAT1.PyUnion')
      if isinstance(other, PyNAT):
         return PyNAT()
      if isinstance(other, PyNAT1):
         return PyNAT1()
      if isinstance(other, PyINT):
         return PyINT()
      return super().PyUnion(other)

   def PyIntersection(self, other : PySet[int]) -> PySet[int]:
      #print('Test_PyNAT1.PyIntersection')
      if isinstance(other, PyNAT):
         return PyNAT1()
      if isinstance(other, PyNAT1):
         return PyNAT1()
      if isinstance(other, PyINT):
         return PyNAT1()
      return super().PyIntersection(other)

   def PyDifference(self, other : PySet[int]) -> PySet[int]:
      #print('Test_PyNAT1.PyDifference')
      if isinstance(other, PyNAT):
         return PySet()
      if isinstance(other, PyNAT1):
         return PySet()
      if isinstance(other, PyINT):
         return PySet()
      return super().PyDifference(other)

   # >> PyCartesianProduct(self, other : 'PySet') -> 'PyRel[T,Any]': #Inherited

   def PyIsSubset(self, other : PySet[int]) -> bool:
      #print('Test_PyNAT1.PyIsSubset')
      if isinstance(other, PyNAT):
         return True
      if isinstance(other, PyNAT1):
         return True
      if isinstance(other, PyINT):
         return True
      if other.PyFinite():
         return False
      return super().PyIsSubset(other)

   # >> def PyNotSubset(self, other : 'PySet[int]') -> bool: #Inherited

   def PyIsProperSubset(self, other : PySet[int]) -> bool:
      #print('Test_PyNAT1.PyIsProperSubset')
      if isinstance(other, PyNAT):
         return True
      if isinstance(other, PyNAT1):
         return False
      if isinstance(other, PyINT):
         return True
      if other.PyFinite():
         return False
      raise Exception('Can not determine the result')

   # >> def PyNotProperSubset(self, other : 'PySet[int]') -> bool: #Inherited

   def PyFinite(self) -> bool:
      return False

   # >> def PyPartition(self, partition_sets : 'List[PySet[int]]') -> bool: #Inherited #Unsupported

   def PyPowerSet(self) -> PySet[PySet[int]]:
      return PyCondSet(PyBaseFunc.PNAT1_ContainsFunc, finite_func = PyBaseFunc.ReturnFalse0)

   def PyPowerSet1(self) -> PySet[PySet[int]]:
      return PyCondSet(PyBaseFunc.P1NAT1_ContainsFunc, finite_func = PyBaseFunc.ReturnFalse0)

   def PyChoice(self) -> int:
      #print('Test_PyNAT1.PyChoice')
      return randint(1,P.RAND_INT_RANGE()[1])


class PyINT(PyCondSet[int]):

   def __init__(self) -> None:
      #print('Test_PyINT.__init__')
      self._PyCondSet__FuncContains : Callable[[int],bool] = PyBaseFunc.INT_ContainsFunc
      self._PyCondSet__IteratorClass : PyBaseIter = PyINT_Iter()

   def __str__(self) -> str:
      return 'PyINT()'

   def __repr__(self) -> str:
      return 'PyINT()'

   def __len__(self) -> int: #Unsupported
      raise Exception('This set has no finite cardinality.')

   # >> def __iter__(self) -> Iterator: #Inherited

   # >> def __eq__(self,other) -> bool: #Inherited

   # >> def __hash__(self): #Inherited

   # >> def __contains__(self,element : object) -> bool: #Inherited

   # >> def PyContains(self,element : int) -> bool: #Inherited

   # >> def PyNotContains(self,element : int) -> bool: #Inherited

   def PyUnion(self, other : PySet[int]) -> PySet[int]:
      #print('Test_PyINT.PyUnion')
      if isinstance(other, PyNAT):
         return PyINT()
      if isinstance(other, PyNAT1):
         return PyINT()
      if isinstance(other, PyINT):
         return PyINT()
      return super().PyUnion(other)

   def PyIntersection(self, other : PySet[int]) -> PySet[int]:
      #print('Test_PyINT.PyIntersection')
      if isinstance(other, PyNAT):
         return PyNAT()
      if isinstance(other, PyNAT1):
         return PyNAT1()
      if isinstance(other, PyINT):
         return PyINT()
      return super().PyIntersection(other)

   def PyDifference(self, other : PySet[int]) -> PySet[int]:
      #print('Test_PyINT.PyDifference')
      if isinstance(other, PyINT):
         return PySet()
      return super().PyDifference(other)

   def PyCartesianProduct(self, other : PySet[int]) -> 'PyRel[int,int]':
      #print('Test_PyINT.PyCartesianProduct')
      if isinstance(other, PyINT):
         return PyINTXINT()
      if isinstance(other, PyNAT):
         return PyINTXNAT()
      return super().PyCartesianProduct(other)

   def PyIsSubset(self, other : PySet[int]) -> bool:
      #print('Test_PyINT.PyIsSubset')
      if isinstance(other, PyNAT):
         return False
      if isinstance(other, PyNAT1):
         return False
      if isinstance(other, PyINT):
         return True
      if other.PyFinite():
         return False
      return super().PyIsSubset(other)

   # >> def PyNotSubset(self, other : 'PySet[T]') -> bool: #Inherited

   def PyIsProperSubset(self, other : PySet[int]) -> bool:
      #print('Test_PyINT.PyIsProperSubset')
      if isinstance(other, PyNAT):
         return False
      if isinstance(other, PyNAT1):
         return False
      if isinstance(other, PyINT):
         return False
      if other.PyFinite():
         return False
      raise Exception('Can not determine the result')

   # >> def PyNotProperSubset(self, other : 'PySet[int]') -> bool: #Inherited

   def PyFinite(self) -> bool:
      return False

   # >> def PyPartition(self, partition_sets : 'List[PySet[int]]') -> bool: #Inherited #Unsupported

   def PyPowerSet(self) -> PySet[PySet[int]]:
      return PyCondSet(PyBaseFunc.PINT_ContainsFunc, finite_func = PyBaseFunc.ReturnFalse0)

   def PyPowerSet1(self) -> PySet[PySet[int]]:
      return PyCondSet(PyBaseFunc.P1INT_ContainsFunc, finite_func = PyBaseFunc.ReturnFalse0)

   def PyChoice(self) -> int:
      #print('Test_PyINT.PyChoice')
      return randint(P.RAND_INT_RANGE()[0],P.RAND_INT_RANGE()[1])


class PyCondSet_Ext(PyCondSet[T]):

   def __init__(self, funcContains : Callable[[T],bool] = PyBaseFunc.Unspecified_FuncBool1,
                finiteInclusion : Set[T] = set(),
                finiteExclusion : Set[T] = set()) -> None:
      #print('Test_PyCondSet_Ext.__init__')
      self._PyCondSet__FuncContains : Callable[[T],bool] #Necessary for mypy to recognize the attribute.
      super().__init__(funcContains)
      self.__FiniteInclusion : Set[T] = finiteInclusion
      self.__FiniteExclusion : Set[T] = finiteExclusion

   def FiniteInclusion(self) -> Set[T]:
      return self.__FiniteInclusion.copy()

   def FiniteExclusion(self) -> Set[T]:
      return self.__FiniteExclusion.copy()

   def __str__(self) -> str:
      return 'PyCondSet_Ext(' + self._PyCondSet__FuncContains.__str__() + ' \nFiniteInclusion(' + self.__FiniteInclusion.__str__() + ')\nFiniteExclusion(' + self.__FiniteExclusion.__str__() +'}))'

   def __repr__(self) -> str:
      return 'PyCondSet_Ext(' + self._PyCondSet__FuncContains.__str__() + ' \nFiniteInclusion(' + self.__FiniteInclusion.__str__() + ')\nFiniteExclusion(' + self.__FiniteExclusion.__str__() +'}))'

   def __len__(self) -> int: #Unsupported
      raise Exception('Unsupported Operation for PyCondSet_Ext')

   def __iter__(self) -> Iterator: #Unsupported
      raise Exception('Unsupported Operation for PyCondSet_Ext')

   def __eq__(self,other) -> bool:
      if isinstance(other, PyCondSet_TreeExt):
         raise Exception('Can not determine the result')
      elif isinstance(other, PyCondSet_Ext):
         if other.FuncContains() == self._PyCondSet__FuncContains and other.FiniteInclusion() == self.__FiniteInclusion and other.FiniteExclusion() == self.__FiniteExclusion:
            return True
      elif isinstance(other, PyCondSet):
         if other.FuncContains() == self._PyCondSet__FuncContains and len(self.__FiniteInclusion) == 0 and len(self.__FiniteExclusion) == 0:
            return True
      raise Exception('Can not determine the result')

   def __hash__(self): #Unsupported
      raise Exception('Unsupported Operation for PyCondSet_Ext')

   # >> def __contains__(self,element : object) -> bool: #Inherited #Unsupported

   def PyContains(self,element : T) -> bool:
      #print('Test_PyCondSet_Ext.PyContains')
      #O(self.__FuncContains) + O(n)
      if element in self.__FiniteInclusion:
         return True
      if element in self.__FiniteExclusion:
         return False
      return self._PyCondSet__FuncContains(element)

   # >> def PyNotContains(self,element : T) -> bool: #Inherited

   def PyUnion(self, other : 'PySet[T]') -> 'PySet[T]':
      #print('Test_PyCondSet_Ext.PyUnion')

      if isinstance(other, PyCondSet_TreeExt):
         return other.PyUnion(self)
      elif isinstance(other, PyCondSet_Ext):
         return PyCondSet_TreeExt(funcContains = self.FuncContains(),finiteInclusion = self.FiniteInclusion(),finiteExclusion = self.FiniteExclusion()).PyUnion(other)
      elif isinstance(other, PyCondSet):
         return other.PyUnion(self)
      return other.PyUnion(self)

   def PyIntersection(self, other : 'PySet[T]') -> 'PySet[T]':
      #print('Test_PyCondSet_Ext.PyIntersection')
      
      if isinstance(other, PyCondSet_TreeExt):
         return other.PyIntersection(self)
      elif isinstance(other, PyCondSet_Ext):
         return PyCondSet_TreeExt(funcContains = self.FuncContains(),finiteInclusion = self.FiniteInclusion(),finiteExclusion = self.FiniteExclusion()).PyIntersection(other)
      elif isinstance(other, PyCondSet):
         return other.PyIntersection(self)
      return other.PyIntersection(self)

   def PyDifference(self, other : 'PySet[T]') -> 'PySet[T]':
      #print('Test_PyCondSet_Ext.PyDifference')

      if isinstance(other, PyCondSet_TreeExt):
         return other.PyDifference(self)
      elif isinstance(other, PyCondSet_Ext):
         return PyCondSet_TreeExt(funcContains = self.FuncContains(),finiteInclusion = self.FiniteInclusion(),finiteExclusion = self.FiniteExclusion()).PyDifference(other)
      elif isinstance(other, PyCondSet):
         return other.PyDifference(self)
      return PyCondSet_TreeExt(self.FuncContains(),self.FiniteInclusion().difference(other.FiniteInclusion()),self.FiniteExclusion().union(other.FiniteInclusion()))

   def PyCartesianProduct(self, other : 'PySet') -> 'PyRel[T,Any]': #Unsupported
      raise Exception('Unsupported Operation for PyCondSet_Ext')

   def PyIsSubset(self, other : 'PySet[T]') -> bool: #Unsupported
      raise Exception('Unsupported Operation for PyCondSet_Ext')

   def PyNotSubset(self, other : 'PySet[T]') -> bool: #Unsupported
      raise Exception('Unsupported Operation for PyCondSet_Ext')

   def PyIsProperSubset(self, other : 'PySet[T]') -> bool: #Unsupported
      raise Exception('Unsupported Operation for PyCondSet_Ext')

   def PyNotProperSubset(self, other : 'PySet[T]') -> bool: #Unsupported
      raise Exception('Unsupported Operation for PyCondSet_Ext')

   def PyFinite(self) -> bool: #Unsupported
      raise Exception('Unsupported Operation for PyCondSet_Ext')

   # >> def PyPartition(self, partition_sets : 'List[PySet[T]]') -> bool: #Inherited #Unsupported

   # >> def PyPowerSet(self) -> 'PySet[PySet[T]]': #Inherited #Unsupported

   # >> def PyPowerSet1(self) -> 'PySet[PySet[T]]': #Inherited #Unsupported

   # >> def PyChoice(self) -> T: #Inherited #Unsupported


class PyTreeNode_Default(Generic[T]):

   def __init__(self, funcContains : Callable[[T],bool] = PyBaseFunc.Unspecified_FuncBool1,
                finiteInclusion : Set[T] = set(),
                finiteExclusion : Set[T] = set()) -> None:
      #print('Test_PyTreeNode_Default.__init__')
      self.__NodePyCondSetExt : PyCondSet_Ext[T] = PyCondSet_Ext(funcContains,finiteInclusion,finiteExclusion)

   def __str__(self) -> str:
      return 'NodeDefault(' + self.__NodePyCondSetExt.__str__() + ')'

   def __repr__(self) -> str:
      return 'NodeDefault(' + self.__NodePyCondSetExt.__str__() + ')'

   def PyContains(self,element : T) -> bool:
      #O(self.__NodePyCondSetExt.PyContains)
      #print('Test_PyTreeNode_Default.PyContains')
      return self.__NodePyCondSetExt.PyContains(element)


class PyTreeNode_Union(PyTreeNode_Default[T]):

   def __init__(self, pyTreeNode_Left : PyTreeNode_Default[T],pyTreeNode_Right : PyTreeNode_Default) -> None:
      #print('Test_PyTreeNode_Union.__init__')
      self.__PyTreeNode_Left : PyTreeNode_Default[T] = pyTreeNode_Left
      self.__PyTreeNode_Right : PyTreeNode_Default[T] = pyTreeNode_Right

   def __str__(self) -> str:
      return 'NodeUnion(' + self.__PyTreeNode_Left.__str__() + '\nUnion\n' + self.__PyTreeNode_Right.__str__() + ')'

   def __repr__(self) -> str:
      return 'NodeUnion(' + self.__PyTreeNode_Left.__str__() + '\nUnion\n' + self.__PyTreeNode_Right.__str__() + ')'

   def PyContains(self,element : T) -> bool:
      #O(self.__PyTreeNode_Left.PyContains + self.__PyTreeNode_Right.PyContains)
      #print('Test_PyTreeNode_Union.PyContains')
      return self.__PyTreeNode_Left.PyContains(element) or self.__PyTreeNode_Right.PyContains(element)


class PyTreeNode_Intersection(PyTreeNode_Default[T]):

   def __init__(self, pyTreeNode_Left : PyTreeNode_Default[T], pyTreeNode_Right : PyTreeNode_Default) -> None:
      #print('Test_PyTreeNode_Intersection.__init__')
      self.__PyTreeNode_Left : PyTreeNode_Default[T] = pyTreeNode_Left
      self.__PyTreeNode_Right : PyTreeNode_Default[T] = pyTreeNode_Right

   def __str__(self) -> str:
      return 'NodeIntersection(' + self.__PyTreeNode_Left.__str__() + '\nIntersection\n' + self.__PyTreeNode_Right.__str__() + ')'

   def __repr__(self) -> str:
      return 'NodeIntersection(' + self.__PyTreeNode_Left.__str__() + '\nIntersection\n' + self.__PyTreeNode_Right.__str__() + ')'

   def PyContains(self,element : T) -> bool:
      #O(self.__PyTreeNode_Left.PyContains + self.__PyTreeNode_Right.PyContains)
      #print('Test_PyTreeNode_Intersection.PyContains')
      return self.__PyTreeNode_Left.PyContains(element) and self.__PyTreeNode_Right.PyContains(element)


class PyTreeNode_Difference(PyTreeNode_Default[T]):

   def __init__(self, pyTreeNode_Left : PyTreeNode_Default[T], pyTreeNode_Right : PyTreeNode_Default) -> None:
      #print('Test_PyTreeNode_Difference.__init__')
      self.__PyTreeNode_Left : PyTreeNode_Default[T] = pyTreeNode_Left
      self.__PyTreeNode_Right : PyTreeNode_Default[T] = pyTreeNode_Right

   def __str__(self) -> str:
      return 'NodeDifference(' + self.__PyTreeNode_Left.__str__() + '\nDifference\n' + self.__PyTreeNode_Right.__str__() + ')'

   def __repr__(self) -> str:
      return 'NodeDifference(' + self.__PyTreeNode_Left.__str__() + '\nDifference\n' + self.__PyTreeNode_Right.__str__() + ')'

   def PyContains(self,element : T) -> bool:
      #O(self.__PyTreeNode_Left.PyContains + self.__PyTreeNode_Right.PyContains)
      #print('Test_PyTreeNode_Difference.PyContains')
      return self.__PyTreeNode_Left.PyContains(element) and not self.__PyTreeNode_Right.PyContains(element)


class PyCondSet_TreeExt(PyCondSet_Ext[T]):

   def __init__(self, funcContains : Callable[[T],bool] = PyBaseFunc.Unspecified_FuncBool1,
                finiteInclusion : Set[T] = set(),
                finiteExclusion : Set[T] = set()) -> None:
      #print('Test_PyCondSet_TreeExt.__init__')
      self.__TreeRoot : PyTreeNode_Default = PyTreeNode_Default(funcContains,finiteInclusion,finiteExclusion)

   def TreeRoot(self) -> PyTreeNode_Default:
      return deepcopy(self.__TreeRoot)

   def __str__(self) -> str:
      return 'PyCondSet_TreeExt(' + self.__TreeRoot.__str__() + ')'

   def __repr__(self) -> str:
      return 'PyCondSet_TreeExt(' + self.__TreeRoot.__str__() + ')'

   def __len__(self) -> int: #Unsupported
      raise Exception('Unsupported Operation for PyCondSet_TreeExt')

   def __iter__(self) -> Iterator: #Unsupported
      raise Exception('Unsupported Operation for PyCondSet_TreeExt')

   def __eq__(self,other) -> bool:
      if isinstance(other, PyCondSet_TreeExt):
         return self.__TreeRoot == other.TreeRoot()
      raise Exception('Can not determine the result')

   def __hash__(self): #Unsupported
      raise Exception('Unsupported Operation for PyCondSet_TreeExt')

   # >> def __contains__(self,element : object) -> bool: #Inherited #Unsupported

   def PyContains(self,element : T) -> bool:
      #O(self.__TreeRoot.PyContains)
      #print('Test_PyCondSet_TreeExt.PyContains')
      return self.__TreeRoot.PyContains(element)

   # >> def PyNotContains(self,element : T) -> bool: #Inherited

   def PyUnion(self, setRight : PySet[T]) -> PySet[T]:
      #O()
      #print('Test_PyCondSet_TreeExt.PyUnion')

      ans : PyCondSet_TreeExt[T]
      nodeLeft : PyTreeNode_Default[T] = deepcopy(self.__TreeRoot)
      nodeRight : PyTreeNode_Default[T]

      if isinstance(setRight,PyCondSet_TreeExt):
         nodeRight = deepcopy(setRight.__TreeRoot)

      elif isinstance(setRight,PyCondSet_Ext):
         nodeRight = PyTreeNode_Default(setRight.FuncContains(),setRight.FiniteInclusion(),setRight.FiniteExclusion())

      elif isinstance(setRight,PyCondSet):
         nodeRight = PyTreeNode_Default(setRight.FuncContains())

      else:
         nodeRight = PyTreeNode_Default(finiteInclusion = setRight.FiniteInclusion())

      newNode : PyTreeNode_Union[T] = PyTreeNode_Union(nodeLeft,nodeRight)

      ans = PyCondSet_TreeExt()
      ans.setTreeRoot(newNode)

      return ans

   def PyIntersection(self, setRight : PySet[T]) -> PySet[T]:
      #O()
      #print('Test_PyCondSet_TreeExt.PyIntersection')

      ans : PyCondSet_TreeExt[T]
      nodeLeft : PyTreeNode_Default[T]
      nodeRight : PyTreeNode_Default[T]

      if isinstance(setRight,PyCondSet_TreeExt):
         
         nodeLeft = deepcopy(self.__TreeRoot)
         nodeRight = deepcopy(setRight.__TreeRoot)

      elif isinstance(setRight,PyCondSet_Ext):

         nodeLeft = deepcopy(self.__TreeRoot)
         nodeRight = PyTreeNode_Default(setRight.FuncContains(),setRight.FiniteInclusion(),setRight.FiniteExclusion())

      elif isinstance(setRight,PyCondSet):

         nodeLeft = deepcopy(self.__TreeRoot)
         nodeRight = PyTreeNode_Default(setRight.FuncContains())

      else:

         nodeLeft = deepcopy(self.__TreeRoot)
         nodeRight = PyTreeNode_Default(finiteInclusion = setRight.FiniteInclusion())

      newNode : PyTreeNode_Intersection[T] = PyTreeNode_Intersection(nodeLeft,nodeRight)

      ans = PyCondSet_TreeExt()
      ans.setTreeRoot(newNode)

      return ans

   def PyDifference(self, setRight : PySet[T]) -> PySet[T]:
      #O()
      #print('Test_PyCondSet_TreeExt.PyDifference')

      ans : PyCondSet_TreeExt[T]
      nodeLeft : PyTreeNode_Default[T]
      nodeRight : PyTreeNode_Default[T]

      if isinstance(setRight,PyCondSet_TreeExt):
         
         nodeLeft = deepcopy(self.__TreeRoot)
         nodeRight = deepcopy(setRight.__TreeRoot)

      elif isinstance(setRight,PyCondSet_Ext):

         nodeLeft = deepcopy(self.__TreeRoot)
         nodeRight = PyTreeNode_Default(setRight.FuncContains(),setRight.FiniteInclusion(),setRight.FiniteExclusion())

      elif isinstance(setRight,PyCondSet):

         nodeLeft = deepcopy(self.__TreeRoot)
         nodeRight = PyTreeNode_Default(setRight.FuncContains())

      else:

         nodeLeft = deepcopy(self.__TreeRoot)
         nodeRight = PyTreeNode_Default(finiteInclusion = setRight.FiniteInclusion())

      newNode : PyTreeNode_Difference[T] = PyTreeNode_Difference(nodeLeft,nodeRight)

      ans = PyCondSet_TreeExt()
      ans.setTreeRoot(newNode)

      return ans

   def PyCartesianProduct(self, other : 'PySet') -> 'PyRel[T,Any]': #Unsupported
      raise Exception('Unsupported Operation for PyCondSet_TreeExt')

   def PyIsSubset(self, other : 'PySet[T]') -> bool: #Unsupported
      raise Exception('Unsupported Operation for PyCondSet_TreeExt')

   def PyNotSubset(self, other : 'PySet[T]') -> bool: #Unsupported
      raise Exception('Unsupported Operation for PyCondSet_TreeExt')

   def PyIsProperSubset(self, other : 'PySet[T]') -> bool: #Unsupported
      raise Exception('Unsupported Operation for PyCondSet_TreeExt')

   def PyNotProperSubset(self, other : 'PySet[T]') -> bool: #Unsupported
      raise Exception('Unsupported Operation for PyCondSet_TreeExt')

   def PyFinite(self) -> bool: #Unsupported
      raise Exception('Unsupported Operation for PyCondSet_TreeExt')

   # >> def PyPartition(self, partition_sets : 'List[PySet[T]]') -> bool: #Inherited #Unsupported

   # >> def PyPowerSet(self) -> 'PySet[PySet[T]]': #Inherited #Unsupported

   # >> def PyPowerSet1(self) -> 'PySet[PySet[T]]': #Inherited #Unsupported

   # >> def PyChoice(self) -> T: #Inherited #Unsupported

   def setTreeRoot(self, newRoot : PyTreeNode_Default[T]) -> None:
      #O(1)
      #print('Test_PyCondSet_TreeExt.setTreeRoot')
      self.__TreeRoot = newRoot


class PyRel(Generic[D,R]):

   def __init__(self, initialElements : Set[Tuple[D,R]] = set())->None:
      #print('Test_PyRel.__init__')
      self.__FiniteInclusion : Set[Tuple[D,R]] = initialElements

   def FiniteInclusion(self) -> Set[Tuple[D,R]]:
      return self.__FiniteInclusion.copy()

   def __str__(self) -> str:
      return 'PyRel(' + self.__FiniteInclusion.__str__() + ')'

   def __repr__(self) -> str:
      return 'PyRel(' + self.__FiniteInclusion.__repr__() + ')'

   def __len__(self) -> int:
      return len(self.__FiniteInclusion)

   def __iter__(self) -> Iterator:
      return self.__FiniteInclusion.__iter__()

   def __eq__(self,other) -> bool:
      if isinstance(other,PyCondRel) or isinstance(other,PyCondSet):
         raise Exception('Operation not supported for implicit Rels')
      if isinstance(other,PyRel) or isinstance(other,PySet):
         return self.__FiniteInclusion.__eq__(other.FiniteInclusion())
      raise Exception('PySets should not operate with PyRels in this Operation')

   def __hash__(self):
      return hash(frozenset(self.__FiniteInclusion))

   def __contains__(self,element : object) -> bool: #Liskov Principle
      raise Exception('Due to the Liskov Principle, TypeCheck will not work, use PyContains instead.')

   def PyContains(self,element : Tuple[D,R]) -> bool:
      #O(1)
      #print('Test_PyRel.PyContains')
      return self.__FiniteInclusion.__contains__(element)

   def PyNotContains(self,element : Tuple[D,R]) -> bool:
      #O(1)
      #print('Test_PyRel.PyContains')
      return not self.PyContains(element)

   def PyUnion(self, other : 'PyRel[D,R]') -> 'PyRel[D,R]':
      #O(m+n) between PyRels.
      #print('Test_PyRel.PyUnion')
      
      if isinstance(other, PyCondRel):
         raise Exception('Operation not supported for implicit PyRels')
      return PyRel(self.__FiniteInclusion.union(other.FiniteInclusion()))

   def PyIntersection(self, other : 'PyRel[D,R]') -> 'PyRel[D,R]':
      #O(n) when other is PyCondRel
      #O(m+n) between PyRels.
      #print('Test_PyRel.PyIntersection')
      
      if isinstance(other, PyCondRel):
         intersection_set : Set[Tuple[D,R]] = set()
         for element in self:
            if other.PyContains(element):
               intersection_set.add(element)
         return PyRel(intersection_set)
      return PyRel(self.__FiniteInclusion.intersection(other.FiniteInclusion()))

   def PyDifference(self, other : 'PyRel[D,R]') -> 'PyRel[D,R]':
      #O(n) between PyRels.
      #print('Test_PyRel.PyDifference')

      if isinstance(other, PyCondRel):
         difference_set : Set[Tuple[D,R]] = self.FiniteInclusion()
         for element in self:
            if other.PyContains(element):
               difference_set.discard(element)
         return PyRel(difference_set)
      return PyRel(self.__FiniteInclusion.difference(other.FiniteInclusion()))

   def PyCartesianProduct(self, other : PySet) -> 'PyRel[Tuple[D,R],Any]':
      #O(m*n) between PySets.
      #print('Test_PyRel.PyCartesianProduct')
      if isinstance(other, PyCondSet):
         raise Exception('Operation only supported between iterable PySets')
      cartesian_product : Set[Tuple[Tuple[D,R],Any]] = set()
      for self_ele in self:
         for other_ele in other:
            cartesian_product.add((self_ele, other_ele))
      return PyRel(cartesian_product)

   def PyIsSubset(self, other : 'PyRel[D,R]') -> bool:
      #O(n)
      #print('Test_PyRel.PyIsSubset')
      for element in self:
         if not(other.PyContains(element)):
            return False
      return True

   def PyNotSubset(self, other : 'PyRel[D,R]') -> bool:
      #O(n)
      #print('Test_PyRel.PyNotSubset')
      return not self.PyIsSubset(other)

   def PyIsProperSubset(self, other : 'PyRel[D,R]') -> bool:
      #O(n)
      #print('Test_PyRel.PyIsProperSubset')
      if len(self)==len(other):
         return False
      return self.PyIsSubset(other)

   def PyNotProperSubset(self, other : 'PyRel[D,R]') -> bool:
      #O(n)
      #print('Test_PyRel.PyNotProperSubset')
      return not self.PyIsProperSubset(other)

   def PyFinite(self) -> bool:
      #O(1)
      #print('Test_PyRel.PyFinite')
      return True

   def PyPartition(self, partition_rels : 'List[PyRel[D,R]]') -> bool:
      #print('Test_PyRel.PyPartition')
      checking_rel : PyRel[D,R] = PyRel()
      for partition_rel in partition_rels:
         if isinstance(partition_rel, PyCondRel):
            raise Exception('Operation only supported between PyRels')
         if len(checking_rel.PyIntersection(partition_rel)) > 0:
            return False
         checking_rel = checking_rel.PyUnion(partition_rel)
      if checking_rel.__eq__(self):
         return True
      return False

   def PyPowerSet(self) -> 'PySet[PyRel[D,R]]':
      #print('Test_PyRel.PyPowerSet')
      elements_list : List[Tuple[D,R]] = list(self.FiniteInclusion())
      power_set : Set[PyRel[D,R]] = set()
      for rel_picker in range(2**len(self)):
         current_rel : Set[Tuple[D,R]] = set()
         for i in range(len(self)):
            if rel_picker & 1<<i != 0:
               current_rel.add(elements_list[i])
         power_set.add(PyRel(current_rel))
      return PySet(power_set)

   def PyPowerSet1(self) -> 'PySet[PyRel[D,R]]':
      #print('Test_PyRel.PyPowerSet1')
      elements_list : List[Tuple[D,R]] = list(self.FiniteInclusion())
      power_set : Set[PyRel[D,R]] = set()
      for rel_picker in range(1,2**len(self)):
         current_rel : Set[Tuple[D,R]] = set()
         for i in range(len(self)):
            if rel_picker & 1<<i != 0:
               current_rel.add(elements_list[i])
         power_set.add(PyRel(current_rel))
      return PySet(power_set)

   def PyChoice(self) -> Tuple[D,R]:
      #print('Test_PySet.PyChoice')
      return choice(list(self.__FiniteInclusion))

   def PyDomain(self) -> PySet[D]:
      #print('Test_PyRel.PyDomain')
      domain_set : Set[D] = set()
      for dom_ele,_ran_ele in self:
         domain_set.add(dom_ele)
      return PySet(domain_set)

   def PyRange(self) -> PySet[R]:
      #print('Test_PyRel.PyRange')
      range_set : Set[R] = set()
      for _dom_ele,ran_ele in self:
         range_set.add(ran_ele)
      return PySet(range_set)

   def PyComposition(self, other : 'PyRel[R,T]') -> 'PyRel[D,T]':
      #print('Test_PyRel.PyComposition')
      new_relation : Set[Tuple[D,T]] = set()
      for left_ele,right_ele in self:
         relational_image : PySet[T] = other[PySet({right_ele})]
         for range_element in relational_image:
            new_relation.add((left_ele,range_element))
      return PyRel(new_relation)

   def PyBackwardComposition(self, other : 'PyRel[T,D]') -> 'PyRel[T,R]':
      #print('Test_PyRel.PyBackwardComposition')
      return other.PyComposition(self)

   def PyDomainRestriction(self, other : PySet[D]) -> 'PyRel[D,R]':
      #print('Test_PyRel.PyDomainRestriction')
      domain_restriction : Set[Tuple[D,R]] = set()
      for tuple_element in self:
         if other.PyContains(tuple_element[0]):
            domain_restriction.add(tuple_element)
      return PyRel(domain_restriction)

   def PyRangeRestriction(self, other : PySet[R]) -> 'PyRel[D,R]':
      #print('Test_PyRel.PyRangeRestriction')
      range_restriction : Set[Tuple[D,R]] = set()
      for tuple_element in self:
         if other.PyContains(tuple_element[1]):
            range_restriction.add(tuple_element)
      return PyRel(range_restriction)

   def PyDomainSubstraction(self, other : PySet[D]) -> 'PyRel[D,R]':
      #print('Test_PyRel.PyDomainSubstraction')
      domain_substraction : Set[Tuple[D,R]] = set()
      for tuple_element in self:
         if other.PyNotContains(tuple_element[0]):
            domain_substraction.add(tuple_element)
      return PyRel(domain_substraction)

   def PyRangeSubstraction(self, other : PySet[R]) -> 'PyRel[D,R]':
      #print('Test_PyRel.PyRangeSubstraction')
      range_substraction : Set[Tuple[D,R]] = set()
      for tuple_element in self:
         if other.PyNotContains(tuple_element[1]):
            range_substraction.add(tuple_element)
      return PyRel(range_substraction)

   def __invert__(self) -> 'PyRel[R,D]': #Inverse Relation method
      inverse_relation : Set[Tuple[R,D]] = set()
      for dom_ele,ran_ele in self:
         inverse_relation.add((ran_ele,dom_ele))
      return PyRel(inverse_relation)

   def __getitem__(self, keys : PySet[D]) -> PySet[R]: #Relational Image method
      #O(range)
      relational_image : Set[R] = set()
      for left_ele,right_ele in self:
         if keys.PyContains(left_ele):
            relational_image.add(right_ele)
      return PySet(relational_image)

   def PyOverriding(self, other : 'PyRel[D,R]') -> 'PyRel[D,R]':
      #print('Test_PyRel.PyOverriding')
      return other.PyUnion(self.PyDomainSubstraction(other.PyDomain()))

   def PyDirectProduct(self, other : 'PyRel[D,T]') -> 'PyRel[D,Tuple[R,T]]':
      #print('Test_PyRel.PyDirectProduct')
      direct_product : Set[Tuple[D,Tuple[R,T]]] = set()
      for domain_element in self.PyDomain():
         self_image : PySet[R] = self[PySet({domain_element})]
         other_image : PySet[T] = other[PySet({domain_element})]
         cartesian_product = self_image.PyCartesianProduct(other_image)
         for cart_prod_tuple in cartesian_product:
            direct_product.add((domain_element,cart_prod_tuple))
      return PyRel(direct_product)

   def PyIsTotal(self, domain_set : PySet[D]) -> bool:
      #print('Test_PyRel.PyIsTotal')
      return self.PyDomain() == domain_set

   def PyIsSurjection(self, range_set : PySet[R]) -> bool:
      #print('Test_PyRel.PyIsSurjection')
      return self.PyRange() == range_set

   def PyIsRelation(self, domain_set : PySet[D], range_set : PySet[R]) -> bool:
      #print('Test_PyRel.PyIsRelation')
      return self.PyDomain().PyIsSubset(domain_set) and self.PyRange().PyIsSubset(range_set)

   def PyIsTotalRelation(self, domain_set : PySet[D], range_set : PySet[R]) -> bool:
      #print('Test_PyRel.PyIsTotalRelation')
      return self.PyIsRelation(domain_set,range_set) and self.PyIsTotal(domain_set)

   def PyIsSurjectiveRelation(self, domain_set : PySet[D], range_set : PySet[R]) -> bool:
      #print('Test_PyRel.PyIsSurjectiveRelation')
      return self.PyIsRelation(domain_set,range_set) and self.PyIsSurjection(range_set)

   def PyIsTotalSurjectiveRelation(self, domain_set : PySet[D], range_set : PySet[R]) -> bool:
      #print('Test_PyRel.PyIsTotalSurjectiveRelation')
      return self.PyIsTotalRelation(domain_set,range_set) and self.PyIsSurjection(range_set)

   def PyIsWellDefined(self) -> bool:
      #print('Test_PyRel.PyIsWellDefined')
      domain_elements : PySet[D] = self.PyDomain()
      for dom_ele in domain_elements:
         image_elements : PySet[R] = self[PySet({dom_ele})]
         if len(image_elements)!=1:
            return False
      return True

   def PyIsFunction(self, domain_set : PySet[D], range_set : PySet[R]) -> bool:
      #print('Test_PyRel.PyIsFunction')
      return self.PyIsWellDefined() and self.PyIsRelation(domain_set, range_set)

   def PyIsPartialFunction(self, domain_set : PySet[D], range_set : PySet[R]) -> bool:
      #print('Test_PyRel.PyIsPartialFunction')
      return self.PyIsFunction(domain_set, range_set)

   def PyIsTotalFunction(self, domain_set : PySet[D], range_set : PySet[R]) -> bool:
      #print('Test_PyRel.PyIsTotalFunction')
      return self.PyIsFunction(domain_set, range_set) and self.PyIsTotal(domain_set)

   def PyIsInjection(self) -> bool:
      #print('Test_PyRel.PyIsInjection')
      inverse_rel = ~self
      return inverse_rel.PyIsWellDefined()

   def PyIsPartialInjection(self, domain_set : PySet[D], range_set : PySet[R]) -> bool:
      #print('Test_PyRel.PyIsPartialInjection')
      return self.PyIsInjection() and self.PyIsPartialFunction(domain_set, range_set)

   def PyIsTotalInjection(self, domain_set : PySet[D], range_set : PySet[R]) -> bool:
      #print('Test_PyRel.PyIsTotalInjection')
      return self.PyIsInjection() and self.PyIsTotalFunction(domain_set, range_set)

   def PyIsPartialSurjection(self, domain_set : PySet[D], range_set : PySet[R]) -> bool:
      #print('Test_PyRel.PyIsPartialSurjection')
      return self.PyIsPartialFunction(domain_set, range_set) and self.PyIsSurjection(range_set)

   def PyIsTotalSurjection(self, domain_set : PySet[D], range_set : PySet[R]) -> bool:
      #print('Test_PyRel.PyIsTotalSurjection')
      return self.PyIsTotalFunction(domain_set, range_set) and self.PyIsSurjection(range_set)

   def PyIsBijection(self, domain_set : PySet[D], range_set : PySet[R]) -> bool:
      #print('Test_PyRel.PyIsBijection')
      return self.PyIsInjection() and self.PyIsTotalSurjection(domain_set,range_set)

   def __call__(self, domain_element : D) -> R: #Apply method
      for dom_elem, ran_elem in self:
         if dom_elem == domain_element:
            return ran_elem
      raise Exception('This element had no image!')


class PyCondRel(PyRel[D,R]):
   
   def __init__(self, relation_func : Callable[[PySet[D]],PySet[R]] = PyBaseFunc.Unspecified_FuncPySet1,
                domain_set : PySet[D] = PyCondSet(),
                range_set : PySet[R] = PyCondSet(),
                inverse_func : Callable[[PySet[R]],PySet[D]] = PyBaseFunc.Unspecified_FuncPySet1) -> None:
      #print('Test_PyCondRel.__init__')
      self.__RelationFunc : Callable[[PySet[D]],PySet[R]] = relation_func
      self.__DomainSet : PySet[D] = domain_set
      self.__RangeSet : PySet[R] = range_set
      self.__InverseFunc : Callable[[PySet[R]],PySet[D]] = inverse_func

   def RelationFunc(self) -> Callable[[PySet[D]],PySet[R]]:
      return self.__RelationFunc

   def DomainSet(self) -> PySet[D]:
      return self.__DomainSet

   def RangeSet(self) -> PySet[R]:
      return self.__RangeSet

   def InverseFunc(self) -> Callable[[PySet[R]],PySet[D]]:
      return self.__InverseFunc

   def __str__(self) -> str:
      return 'PyCondRel(' + self.__RelationFunc.__str__() + ' \nDomainSet(' + self.__DomainSet.__str__() + ')\nRangeSet(' + self.__RangeSet.__str__() +  ')\nInverseFunc(' + self.__InverseFunc.__str__() +'))'

   def __repr__(self) -> str:
      return 'PyCondRel(' + self.__RelationFunc.__str__() + ' \nDomainSet(' + self.__DomainSet.__str__() + ')\nRangeSet(' + self.__RangeSet.__str__() +  ')\nInverseFunc(' + self.__InverseFunc.__str__() +'))'

   def __len__(self) -> int: # + domain + relfunc
      rel_length = 0
      for dom_ele in self.PyDomain():
         image_elems : PySet[R] = self[PySet({dom_ele})]
         rel_length += len(image_elems)
      return rel_length

   def __iter__(self) -> Iterator: # + domain + relfunc
      all_tuples : Set[Tuple[D,R]] = set()
      for dom_ele in self.PyDomain():
         image_elems : PySet[R] = self[PySet({dom_ele})]
         for image_elem in image_elems:
            all_tuples.add((dom_ele,image_elem))
      return all_tuples.__iter__()

   def __eq__(self,other) -> bool: # + all
      if isinstance(other, PyCondRel):
         if other.RelationFunc() == self.__RelationFunc and other.DomainSet() == self.__DomainSet and other.RangeSet() == self.__RangeSet:
            return True
      raise Exception('Can not determine the result')

   def __hash__(self):
      return hash(self.__RelationFunc)

   # >> def __contains__(self,element : object) -> bool: #Inherited

   def PyContains(self,tuple_element : Tuple[D,R]) -> bool:
      #O(self.__RelationFunc + len(domain_set))
      #print('Test_PyCondRel.PyContains')
      preimage_element : D = tuple_element[0]
      image_element : R = tuple_element[1]
      image_elements : PySet[R] = self[PySet({preimage_element})]
      return image_elements.PyContains(image_element)

   # >> def PyNotContains(self,element : Tuple[D,R]) -> bool: #Inherited

   def PyUnion(self, other : PyRel[D,R]) -> PyRel[D,R]: #Unsupported
      raise Exception('Operation only supported between PyRels.')

   def PyIntersection(self, other : PyRel[D,R]) -> PyRel[D,R]: #Unsupported
      if isinstance(other,PyCondRel):
         raise Exception('Operation not supported between implicit PyRels!')
      return other.PyIntersection(self)

   def PyDifference(self, other : PyRel[D,R]) -> PyRel[D,R]: #Unsupported
      raise Exception('Operation only supported between PyRels.')

   # >> def PyCartesianProduct(self, other : PySet) -> PyRel[Tuple[D,R],Any]: #Inherited + __iter__

   # >> def PyIsSubset(self, other : PyRel[D,R]) -> bool: #Inherited + __iter__

   # >> def PyNotSubset(self, other : PyRel[D,R]) -> bool: #Inherited + __iter__

   # >> def PyIsProperSubset(self, other : PyRel[D,R]) -> bool: #Inherited + __iter__ + __len__

   # >> def PyNotProperSubset(self, other : PyRel[D,R]) -> bool: #Inherited + __iter__ + __len__

   def PyFinite(self) -> bool:
      return self.PyDomain().PyFinite() and self.PyRange().PyFinite()

   def PyPartition(self, partition_rels : List[PyRel[D,R]]) -> bool: #Unsupported
      raise Exception('Operation not supported for Implicit Rels')

   def PyPowerSet(self) -> PySet[PyRel[D,R]]: #Unsupported
      raise Exception('Operation not supported for Implicit Rels')

   def PyPowerSet1(self) -> PySet[PyRel[D,R]]: #Unsupported
      raise Exception('Operation not supported for Implicit Rels')

   def PyChoice(self) -> Tuple[D,R]: #Unsupported
      #print('Test_PyCondRel.PyChoice')
      raise Exception('Operation not supported for Implicit Sets')

   def PyDomain(self) -> PySet[D]:
      #O(1)
      #print('Test_PyCondRel.PyDomain')
      return self.__DomainSet

   def PyRange(self) -> PySet[R]:
      #O(1)
      #print('Test_PyCondRel.PyRange')
      return self.__RangeSet

   # >> def PyComposition(self, other : 'PyRel[R,T]') -> 'PyRel[D,T]': #Inherited

   # >> def PyBackwardComposition(self, other : 'PyRel[T,D]') -> 'PyRel[T,R]' #Inherited

   # >> def PyDomainRestriction(self, other : PySet[D]) -> 'PyRel[D,R]': #Inherited

   # >> def PyRangeRestriction(self, other : PySet[R]) -> 'PyRel[D,R]': #Inherited

   # >> def PyDomainSubstraction(self, other : PySet[D]) -> 'PyRel[D,R]': #Inherited

   # >> def PyRangeSubstraction(self, other : PySet[R]) -> 'PyRel[D,R]': #Inherited

   def __invert__(self) -> 'PyCondRel[R,D]': #Inverse Relation method
      return PyCondRel(self.__InverseFunc,self.__RangeSet,self.__DomainSet,self.__RelationFunc)

   def __getitem__(self, keys : PySet[D]) -> PySet[R]: #Relational Image method
      #O(self.__RelationFunc)
      return self.__RelationFunc(keys)

   # >> def PyOverriding(self, other : 'PyRel[D,R]') -> 'PyRel[D,R]': #Inherited

   # >> def PyDirectProduct(self, other : 'PyRel[D,T]') -> 'PyRel[D,Tuple[R,T]]': #Inherited

   # >> def PyIsTotal(self, domain_set : PySet[D]) -> bool: #Inherited

   # >> def PyIsSurjection(self, range_set : PySet[R]) -> bool: #Inherited

   # >> def PyIsRelation(self, domain_set : PySet[D], range_set : PySet[R]) -> bool: #Inherited

   # >> def PyIsTotalRelation(self, domain_set : PySet[D], range_set : PySet[R]) -> bool: #Inherited

   # >> def PyIsSurjectiveRelation(self, domain_set : PySet[D], range_set : PySet[R]) -> bool: #Inherited

   # >> def PyIsTotalSurjectiveRelation(self, domain_set : PySet[D], range_set : PySet[R]) -> bool: #Inherited

   # >> def PyIsWellDefined(self) -> bool: #Inherited

   # >> def PyIsFunction(self, domain_set : PySet[D], range_set : PySet[R]) -> bool: #Inherited

   # >> def PyIsPartialFunction(self, domain_set : PySet[D], range_set : PySet[R]) -> bool: #Inherited

   # >> def PyIsTotalFunction(self, domain_set : PySet[D], range_set : PySet[R]) -> bool: #Inherited

   # >> def PyIsInjection(self) -> bool: #Inherited

   # >> def PyIsPartialInjection(self, domain_set : PySet[D], range_set : PySet[R]) -> bool: #Inherited

   # >> def PyIsTotalInjection(self, domain_set : PySet[D], range_set : PySet[R]) -> bool: #Inherited

   # >> def PyIsPartialSurjection(self, domain_set : PySet[D], range_set : PySet[R]) -> bool: #Inherited

   # >> def PyIsTotalSurjection(self, domain_set : PySet[D], range_set : PySet[R]) -> bool: #Inherited

   # >> def PyIsBijection(self, domain_set : PySet[D], range_set : PySet[R]) -> bool: #Inherited

   def __call__(self, domain_element : D) -> R: #Apply method
      element_images : PySet[R] = self[PySet({domain_element})]
      if len(element_images)==0:
         raise Exception('This element has no images related to it')
      return list(element_images)[0]


class PyNATXNAT(PyCondRel[int,int]):

   def __init__(self) -> None:
      #print('Test_NATXNAT.__init__')
      self._PyCondRel__RelationFunc : Callable[[PySet[int]],PySet[int]] = PyBaseFunc.ReturnPyNAT_NAT
      self._PyCondRel__DomainSet : PySet[int] = PyNAT()
      self._PyCondRel__RangeSet : PySet[int] = PyNAT()
      self._PyCondRel__InverseFunc : Callable[[PySet[int]],PySet[int]] = PyBaseFunc.ReturnPyNAT_NAT

   def __str__(self) -> str:
      return 'PyNATXNAT()'
   
   def __repr__(self) -> str:
      return 'PyNATXNAT()'

   def __len__(self) -> int: #Unsupported
      raise Exception('This set has no finite cardinality.')

   # >> def __iter__(self) -> Iterator: #Inherited

   # >> def __eq__(self,other) -> bool: #Inherited

   # >> def __hash__(self): #Inherited

   # >> def __contains__(self,element : object) -> bool: #Inherited

   def PyContains(self,tuple_element : Tuple[int,int]) -> bool:
      #O(1)
      #print('Test_PyNATXNAT.PyContains')
      if tuple_element[0] >= 0 and tuple_element[1] >=0:
         return True
      return False

   # >> def PyNotContains(self,element : Tuple[int,int]) -> bool: #Inherited

   def PyUnion(self, other : PyRel[int,int]) -> PyRel[int,int]:
      #print('Test_PyNATXNAT.PyUnion')
      if isinstance(other, PyNATXNAT):
         return PyNATXNAT()
      if isinstance(other, PyINTXINT):
         return PyINTXINT()
      if isinstance(other, PyINTXNAT):
         return PyINTXNAT()
      raise Exception('Can not determine the result')

   def PyIntersection(self, other : PyRel[int,int]) -> PyRel[int,int]:
      #print('Test_PyNATXNAT.PyIntersection')
      if isinstance(other, PyNATXNAT):
         return PyNATXNAT()
      if isinstance(other, PyINTXINT):
         return PyNATXNAT()
      if isinstance(other, PyINTXNAT):
         return PyNATXNAT()
      return super().PyIntersection(other)

   def PyDifference(self, other : PyRel[int,int]) -> PyRel[int,int]:
      #print('Test_PyNATXNAT.PyDifference')
      if isinstance(other, PyNATXNAT):
         return PyRel()
      if isinstance(other, PyINTXINT):
         return PyRel()
      if isinstance(other, PyINTXNAT):
         return PyRel()
      raise Exception('Can not determine the result')

   # >> def PyCartesianProduct(self, other : PySet) -> PyRel[Tuple[int,int],Any]: #Inherited

   def PyIsSubset(self, other : PyRel[int,int]) -> bool:
      #print('Test_PyNATXNAT.PyIsSubset')
      if isinstance(other, PyNATXNAT):
         return True
      if isinstance(other, PyINTXINT):
         return True
      if isinstance(other, PyINTXNAT):
         return True
      if other.PyFinite():
         return False
      return super().PyIsSubset(other)

   # >> def PyNotSubset(self, other : PyRel[int,int]) -> bool: #Inherited

   def PyIsProperSubset(self, other : PyRel[int,int]) -> bool:
      #print('Test_PyNATXNAT.PyIsProperSubset')
      if isinstance(other, PyNATXNAT):
         return False
      if isinstance(other, PyINTXINT):
         return True
      if isinstance(other, PyINTXNAT):
         return True
      if other.PyFinite():
         return False
      raise Exception('Can not determine the result')

   # >> def PyNotProperSubset(self, other : PyRel[int,int]) -> bool: #Inherited

   def PyFinite(self) -> bool:
      return False

   # >> def PyPartition(self, partition_sets : List[PyRel[int,int]]) -> bool: #Inherited #Unsupported

   def PyPowerSet(self) -> PySet[PyRel[int,int]]:
      return PyCondSet(PyBaseFunc.PNATXNAT_ContainsFunc, finite_func = PyBaseFunc.ReturnFalse0)

   def PyPowerSet1(self) -> PySet[PyRel[int,int]]:
      return PyCondSet(PyBaseFunc.P1NATXNAT_ContainsFunc, finite_func = PyBaseFunc.ReturnFalse0)

   def PyChoice(self) -> Tuple[int,int]:
      #print('Test_PyNATXNAT.PyChoice')
      return (randint(0,P.RAND_INT_RANGE()[1]),randint(0,P.RAND_INT_RANGE()[1]))

   # >> def PyDomain(self) -> PySet[int]: #Inherited

   # >> def PyRange(self) -> PySet[int]: #Inherited

   # >> def PyComposition(self, other : 'PyRel[int,int]') -> 'PyRel[int,int]': #Inherited

   # >> def PyBackwardComposition(self, other : 'PyRel[int,int]') -> 'PyRel[int,int]' #Inherited

   # >> def PyDomainRestriction(self, other : PySet[int]) -> 'PyRel[int,int]': #Inherited

   # >> def PyRangeRestriction(self, other : PySet[int]) -> 'PyRel[int,int]': #Inherited

   # >> def PyDomainSubstraction(self, other : PySet[int]) -> 'PyRel[int,int]': #Inherited

   # >> def PyRangeSubstraction(self, other : PySet[int]) -> 'PyRel[int,int]': #Inherited

   # >> def __invert__(self) -> 'PyCondRel[int,int]': #Inherited

   # >> def __getitem__(self, keys : PySet[int]) -> PySet[R]: #Inherited

   # >> def PyOverriding(self, other : 'PyRel[int,int]') -> 'PyRel[int,int]': #Inherited

   # >> def PyDirectProduct(self, other : 'PyRel[int,int]') -> 'PyRel[int,Tuple[int,int]]': #Inherited

   # >> def PyIsTotal(self, domain_set : PySet[int]) -> bool: #Inherited

   # >> def PyIsSurjection(self, range_set : PySet[int]) -> bool: #Inherited

   # >> def PyIsRelation(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited

   # >> def PyIsTotalRelation(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited

   # >> def PyIsSurjectiveRelation(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited

   # >> def PyIsTotalSurjectiveRelation(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited

   def PyIsWellDefined(self) -> bool:
      return False

   # >> def PyIsFunction(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited

   # >> def PyIsPartialFunction(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited

   # >> def PyIsTotalFunction(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited

   def PyIsInjection(self) -> bool:
      return False

   # >> def PyIsPartialInjection(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited

   # >> def PyIsTotalInjection(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited

   # >> def PyIsPartialSurjection(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited

   # >> def PyIsTotalSurjection(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited

   # >> def PyIsBijection(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited

   # >> def __call__(self, domain_element : int) -> R: #Inherited


class PyINTXINT(PyCondRel[int,int]):

   def __init__(self) -> None:
      #print('Test_INTXINT.__init__')
      self._PyCondRel__RelationFunc : Callable[[PySet[int]],PySet[int]] = PyBaseFunc.ReturnPyINT_1
      self._PyCondRel__DomainSet : PySet[int] = PyINT()
      self._PyCondRel__RangeSet : PySet[int] = PyINT()
      self._PyCondRel__InverseFunc : Callable[[PySet[int]],PySet[int]] = PyBaseFunc.ReturnPyINT_1

   def __str__(self) -> str:
      return 'PyINTXINT()'

   def __repr__(self) -> str:
      return 'PyINTXINT()'

   def __len__(self) -> int: #Unsupported
      raise Exception('This set has no finite cardinality.')

   # >> def __iter__(self) -> Iterator: #Inherited

   # >> def __eq__(self,other) -> bool: #Inherited

   # >> def __hash__(self): #Inherited

   # >> def __contains__(self,element : object) -> bool: #Inherited

   def PyContains(self,tuple_element : Tuple[int,int]) -> bool:
      #O(1)
      #print('Test_PyINTXINT.PyContains')
      if isinstance(tuple_element[0],int) and isinstance(tuple_element[1],int):
         return True
      return False

   # >> def PyNotContains(self,element : Tuple[int,int]) -> bool: #Inherited

   def PyUnion(self, other : PyRel[int,int]) -> PyRel[int,int]:
      #print('Test_PyINTXINT.PyUnion')
      if isinstance(other, PyNATXNAT):
         return PyINTXINT()
      if isinstance(other, PyINTXINT):
         return PyINTXINT()
      if isinstance(other, PyINTXNAT):
         return PyINTXINT()
      raise Exception('Can not determine the result')

   def PyIntersection(self, other : PyRel[int,int]) -> PyRel[int,int]:
      #print('Test_PyINTXINT.PyIntersection')
      if isinstance(other, PyNATXNAT):
         return PyNATXNAT()
      if isinstance(other, PyINTXINT):
         return PyINTXINT()
      if isinstance(other, PyINTXNAT):
         return PyINTXNAT()
      return super().PyIntersection(other)

   def PyDifference(self, other : PyRel[int,int]) -> PyRel[int,int]:
      #print('Test_PyINTXINT.PyDifference')
      if isinstance(other, PyINTXINT):
         return PyRel()
      raise Exception('Can not determine the result')

   # >> def PyCartesianProduct(self, other : PySet) -> PyRel[Tuple[int,int],Any]: #Inherited

   def PyIsSubset(self, other : PyRel[int,int]) -> bool:
      #print('Test_PyINTXINT.PyIsSubset')
      if isinstance(other, PyNATXNAT):
         return False
      if isinstance(other, PyINTXINT):
         return True
      if isinstance(other, PyINTXNAT):
         return False
      if other.PyFinite():
         return False
      return super().PyIsSubset(other)

   # >> def PyNotSubset(self, other : PyRel[int,int]) -> bool: #Inherited

   def PyIsProperSubset(self, other : PyRel[int,int]) -> bool:
      #print('Test_PyINTXINT.PyIsProperSubset')
      if isinstance(other, PyNATXNAT):
         return False
      if isinstance(other, PyINTXINT):
         return False
      if isinstance(other, PyINTXNAT):
         return False
      if other.PyFinite():
         return False
      raise Exception('Can not determine the result')

   # >> def PyNotProperSubset(self, other : PyRel[int,int]) -> bool: #Inherited

   def PyFinite(self) -> bool:
      return False

   # >> def PyPartition(self, partition_sets : List[PyRel[int,int]]) -> bool: #Inherited #Unsupported

   def PyPowerSet(self) -> PySet[PyRel[int,int]]:
      return PyCondSet(PyBaseFunc.PINTXINT_ContainsFunc, finite_func = PyBaseFunc.ReturnFalse0)

   def PyPowerSet1(self) -> PySet[PyRel[int,int]]:
      return PyCondSet(PyBaseFunc.P1INTXINT_ContainsFunc, finite_func = PyBaseFunc.ReturnFalse0)

   def PyChoice(self) -> Tuple[int,int]:
      #print('Test_PyINTXINT.PyChoice')
      return (randint(P.RAND_INT_RANGE()[0],P.RAND_INT_RANGE()[1]),randint(P.RAND_INT_RANGE()[0],P.RAND_INT_RANGE()[1]))

   # >> def PyDomain(self) -> PySet[int]: #Inherited

   # >> def PyRange(self) -> PySet[int]: #Inherited

   # >> def PyComposition(self, other : 'PyRel[int,int]') -> 'PyRel[int,int]': #Inherited

   # >> def PyBackwardComposition(self, other : 'PyRel[int,int]') -> 'PyRel[int,int]' #Inherited

   # >> def PyDomainRestriction(self, other : PySet[int]) -> 'PyRel[int,int]': #Inherited

   # >> def PyRangeRestriction(self, other : PySet[int]) -> 'PyRel[int,int]': #Inherited

   # >> def PyDomainSubstraction(self, other : PySet[int]) -> 'PyRel[int,int]': #Inherited

   # >> def PyRangeSubstraction(self, other : PySet[int]) -> 'PyRel[int,int]': #Inherited

   # >> def __invert__(self) -> 'PyCondRel[int,int]': #Inherited

   # >> def __getitem__(self, keys : PySet[int]) -> PySet[R]: #Inherited

   # >> def PyOverriding(self, other : 'PyRel[int,int]') -> 'PyRel[int,int]': #Inherited

   # >> def PyDirectProduct(self, other : 'PyRel[int,int]') -> 'PyRel[int,Tuple[int,int]]': #Inherited

   # >> def PyIsTotal(self, domain_set : PySet[int]) -> bool: #Inherited

   # >> def PyIsSurjection(self, range_set : PySet[int]) -> bool: #Inherited

   # >> def PyIsRelation(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited

   # >> def PyIsTotalRelation(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited

   # >> def PyIsSurjectiveRelation(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited

   # >> def PyIsTotalSurjectiveRelation(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited

   def PyIsWellDefined(self) -> bool:
      return False

   # >> def PyIsFunction(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited

   # >> def PyIsPartialFunction(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited

   # >> def PyIsTotalFunction(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited

   def PyIsInjection(self) -> bool:
      return False

   # >> def PyIsPartialInjection(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited

   # >> def PyIsTotalInjection(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited

   # >> def PyIsPartialSurjection(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited

   # >> def PyIsTotalSurjection(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited

   # >> def PyIsBijection(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited

   # >> def __call__(self, domain_element : int) -> R: #Inherited


class PyINTXNAT(PyCondRel[int,int]):

   def __init__(self) -> None:
      #print('Test_INTXNAT.__init__')
      self._PyCondRel__RelationFunc : Callable[[PySet[int]],PySet[int]] = PyBaseFunc.ReturnPyNAT_1
      self._PyCondRel__DomainSet : PySet[int] = PyINT()
      self._PyCondRel__RangeSet : PySet[int] = PyNAT()
      self._PyCondRel__InverseFunc : Callable[[PySet[int]],PySet[int]] = PyBaseFunc.ReturnPyNAT_INT

   def __str__(self) -> str:
      return 'PyINTXNAT()'

   def __repr__(self) -> str:
      return 'PyINTXNAT()'

   def __len__(self) -> int: #Unsupported
      raise Exception('This set has no finite cardinality.')

   # >> def __iter__(self) -> Iterator: #Inherited

   # >> def __eq__(self,other) -> bool: #Inherited

   # >> def __hash__(self): #Inherited

   # >> def __contains__(self,element : object) -> bool: #Inherited

   def PyContains(self,tuple_element : Tuple[int,int]) -> bool:
      #O(1)
      #print('Test_PyINTXNAT.PyContains')
      if isinstance(tuple_element[0],int) and tuple_element[1] >=0:
         return True
      return False

   # >> def PyNotContains(self,element : Tuple[int,int]) -> bool: #Inherited

   def PyUnion(self, other : PyRel[int,int]) -> PyRel[int,int]:
      #print('Test_PyINTXNAT.PyUnion')
      if isinstance(other, PyNATXNAT):
         return PyINTXNAT()
      if isinstance(other, PyINTXINT):
         return PyINTXINT()
      if isinstance(other, PyINTXNAT):
         return PyINTXNAT()
      raise Exception('Can not determine the result')

   def PyIntersection(self, other : PyRel[int,int]) -> PyRel[int,int]:
      #print('Test_PyINTXNAT.PyIntersection')
      if isinstance(other, PyNATXNAT):
         return PyNATXNAT()
      if isinstance(other, PyINTXINT):
         return PyINTXNAT()
      if isinstance(other, PyINTXNAT):
         return PyINTXNAT()
      return super().PyIntersection(other)

   def PyDifference(self, other : PyRel[int,int]) -> PyRel[int,int]:
      #print('Test_PyINTXNAT.PyDifference')
      if isinstance(other, PyINTXINT):
         return PyRel()
      if isinstance(other, PyINTXNAT):
         return PyRel()
      raise Exception('Can not determine the result')

   def PyCartesianProduct(self, other : PySet) -> PyRel[Tuple[int,int],Any]: #Unsupported
      raise Exception('Operation not supported')

   def PyIsSubset(self, other : PyRel[int,int]) -> bool:
      #print('Test_PyINTXNAT.PyIsSubset')
      if isinstance(other, PyNATXNAT):
         return False
      if isinstance(other, PyINTXINT):
         return True
      if isinstance(other, PyINTXNAT):
         return True
      if other.PyFinite():
         return False
      return super().PyIsSubset(other)

   # >> def PyNotSubset(self, other : PyRel[int,int]) -> bool: #Inherited

   def PyIsProperSubset(self, other : PyRel[int,int]) -> bool:
      #print('Test_PyINTXNAT.PyIsProperSubset')
      if isinstance(other, PyNATXNAT):
         return False
      if isinstance(other, PyINTXINT):
         return True
      if isinstance(other, PyINTXNAT):
         return False
      if other.PyFinite():
         return False
      raise Exception('Can not determine the result')

   # >> def PyNotProperSubset(self, other : PyRel[int,int]) -> bool: #Inherited

   def PyFinite(self) -> bool:
      return False

   # >> def PyPartition(self, partition_sets : List[PyRel[int,int]]) -> bool: #Inherited #Unsupported

   def PyPowerSet(self) -> PySet[PyRel[int,int]]:
      return PyCondSet(PyBaseFunc.PINTXNAT_ContainsFunc, finite_func = PyBaseFunc.ReturnFalse0)

   def PyPowerSet1(self) -> PySet[PyRel[int,int]]:
      return PyCondSet(PyBaseFunc.P1INTXNAT_ContainsFunc, finite_func = PyBaseFunc.ReturnFalse0)

   def PyChoice(self) -> Tuple[int,int]:
      #print('Test_PyINTXNAT.PyChoice')
      return (randint(P.RAND_INT_RANGE()[0],P.RAND_INT_RANGE()[1]),randint(0,P.RAND_INT_RANGE()[1]))

   # >> def PyDomain(self) -> PySet[int]: #Inherited

   # >> def PyRange(self) -> PySet[int]: #Inherited

   # >> def PyComposition(self, other : 'PyRel[int,int]') -> 'PyRel[int,int]': #Inherited

   # >> def PyBackwardComposition(self, other : 'PyRel[int,int]') -> 'PyRel[int,int]' #Inherited

   # >> def PyDomainRestriction(self, other : PySet[int]) -> 'PyRel[int,int]': #Inherited

   # >> def PyRangeRestriction(self, other : PySet[int]) -> 'PyRel[int,int]': #Inherited

   # >> def PyDomainSubstraction(self, other : PySet[int]) -> 'PyRel[int,int]': #Inherited

   # >> def PyRangeSubstraction(self, other : PySet[int]) -> 'PyRel[int,int]': #Inherited

   # >> def __invert__(self) -> 'PyCondRel[int,int]': #Inherited

   # >> def __getitem__(self, keys : PySet[int]) -> PySet[R]: #Inherited

   # >> def PyOverriding(self, other : 'PyRel[int,int]') -> 'PyRel[int,int]': #Inherited

   # >> def PyDirectProduct(self, other : 'PyRel[int,int]') -> 'PyRel[int,Tuple[int,int]]': #Inherited

   # >> def PyIsTotal(self, domain_set : PySet[int]) -> bool: #Inherited

   # >> def PyIsSurjection(self, range_set : PySet[int]) -> bool: #Inherited

   # >> def PyIsRelation(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited

   # >> def PyIsTotalRelation(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited

   # >> def PyIsSurjectiveRelation(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited

   # >> def PyIsTotalSurjectiveRelation(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited

   def PyIsWellDefined(self) -> bool:
      return False

   # >> def PyIsFunction(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited

   # >> def PyIsPartialFunction(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited

   # >> def PyIsTotalFunction(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited

   def PyIsInjection(self) -> bool:
      return False

   # >> def PyIsPartialInjection(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited

   # >> def PyIsTotalInjection(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited

   # >> def PyIsPartialSurjection(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited

   # >> def PyIsTotalSurjection(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited

   # >> def PyIsBijection(self, domain_set : PySet[int], range_set : PySet[int]) -> bool: #Inherited

   # >> def __call__(self, domain_element : int) -> R: #Inherited


class PyID(PyCondRel):

   def __init__(self) -> None:
      #print('Test_ID.__init__')
      self._PyCondRel__RelationFunc : Callable[[PySet],PySet] = PyBaseFunc.ID_Rel_Func
      self._PyCondRel__DomainSet : PySet = PyCondSet()
      self._PyCondRel__RangeSet : PySet = PyCondSet()
      self._PyCondRel__InverseFunc : Callable[[PySet],PySet] = PyBaseFunc.ID_Rel_Func

   def __str__(self) -> str:
      return 'PyID()'
   
   def __repr__(self) -> str:
      return 'PyID()'

   def __len__(self) -> int: #Unsupported
      raise Exception('Unsupported Operation for PyID.')

   def __iter__(self) -> Iterator: #Unsupported
      raise Exception('Unsupported Operation for PyID.')

   def __eq__(self,other) -> bool: #Unsupported
      raise Exception('Unsupported Operation for PyID.')

   def __hash__(self): #Unsupported
      raise Exception('Unsupported Operation for PyID.')

   # >> def __contains__(self,element : object) -> bool: #Inherited

   def PyContains(self,tuple_element : Tuple) -> bool:
      #O(1)
      #print('Test_PyID.PyContains')
      if tuple_element[0] == tuple_element[1]:
         return True
      return False

   # >> def PyNotContains(self,element : Tuple) -> bool: #Inherited

   def PyUnion(self, other : PyRel) -> PyRel: #Unsupported
      raise Exception('Can not determine the result')

   def PyIntersection(self, other : PyRel) -> PyRel:
      return super().PyIntersection(other)

   def PyDifference(self, other : PyRel) -> PyRel: #Unsupported
      raise Exception('Can not determine the result')

   def PyCartesianProduct(self, other : PySet) -> PyRel[Tuple[Any,Any],Any]: #Unsupported
      raise Exception('Can not determine the result')

   def PyIsSubset(self, other : PyRel) -> bool: #Unsupported
      raise Exception('Can not determine the result')

   # >> def PyNotSubset(self, other : PyRel) -> bool: #Inherited #Unsupported

   def PyIsProperSubset(self, other : PyRel) -> bool: #Unsupported
      raise Exception('Can not determine the result')

   # >> def PyNotProperSubset(self, other : PyRel) -> bool: #Inherited #Unsupported

   def PyFinite(self) -> bool:
      return False

   # >> def PyPartition(self, partition_sets : List[PyRel]) -> bool: #Inherited #Unsupported

   def PyPowerSet(self) -> PySet[PyRel]: #Unsupported
      raise Exception('Can not determine the result')

   def PyPowerSet1(self) -> PySet[PyRel]: #Unsupported
      raise Exception('Can not determine the result')

   # >> def PyChoice(self) -> Tuple: #Inherited #Unsupported

   def PyDomain(self) -> PySet[D]: #Unsupported
      raise Exception('Unsupported Operation for PyID.')

   def PyRange(self) -> PySet[R]: #Unsupported
      raise Exception('Unsupported Operation for PyID.')

   def PyComposition(self, other : PyRel) -> PyRel: #Unsupported
      raise Exception('Unsupported Operation for PyID.')

   def PyBackwardComposition(self, other : PyRel) -> PyRel: #Unsupported
      raise Exception('Unsupported Operation for PyID.')

   def PyDomainRestriction(self, other : PySet) -> PyRel:
      restricted_id : Set[Tuple[Any,Any]] = set()
      for element in other:
         restricted_id.add((element,element))
      return PyRel(restricted_id)

   def PyRangeRestriction(self, other : PySet) -> PyRel:
      restricted_id : Set[Tuple[Any,Any]] = set()
      for element in other:
         restricted_id.add((element,element))
      return PyRel(restricted_id)

   def PyDomainSubstraction(self, other : PySet) -> PyRel: #Unsupported
      raise Exception('Unsupported Operation for PyID.')

   def PyRangeSubstraction(self, other : PySet) -> PyRel: #Unsupported
      raise Exception('Unsupported Operation for PyID.')

   def __invert__(self) -> 'PyID': #Inverse Relation method
      return PyID()

   # >> def __getitem__(self, keys : PySet) -> PySet: #Inherited

   def PyOverriding(self, other : PyRel) -> PyRel: #Unsupported
      raise Exception('Unsupported Operation for PyID.')

   # >> def PyDirectProduct(self, other : PyRel) -> PyRel[Any,Tuple[Any,Any]]: #Inherited #Unsupported

   # >> def PyIsTotal(self, domain_set : PySet) -> bool: #Inherited #Unsupported

   # >> def PyIsSurjection(self, range_set : PySet) -> bool: #Inherited #Unsupported

   # >> def PyIsRelation(self, domain_set : PySet, range_set : PySet) -> bool: #Inherited #Unsupported

   # >> def PyIsTotalRelation(self, domain_set : PySet, range_set : PySet) -> bool: #Inherited #Unsupported

   # >> def PyIsSurjectiveRelation(self, domain_set : PySet, range_set : PySet) -> bool: #Inherited #Unsupported

   # >> def PyIsTotalSurjectiveRelation(self, domain_set : PySet, range_set : PySet) -> bool: #Inherited #Unsupported

   def PyIsWellDefined(self) -> bool:
      return False

   # >> def PyIsFunction(self, domain_set : PySet, range_set : PySet) -> bool: #Inherited #Unsupported

   # >> def PyIsPartialFunction(self, domain_set : PySet, range_set : PySet) -> bool: #Inherited #Unsupported

   # >> def PyIsTotalFunction(self, domain_set : PySet, range_set : PySet) -> bool: #Inherited #Unsupported

   def PyIsInjection(self) -> bool:
      return True

   # >> def PyIsPartialInjection(self, domain_set : PySet, range_set : PySet) -> bool: #Inherited #Unsupported

   # >> def PyIsTotalInjection(self, domain_set : PySet, range_set : PySet) -> bool: #Inherited #Unsupported

   # >> def PyIsPartialSurjection(self, domain_set : PySet, range_set : PySet) -> bool: #Inherited #Unsupported

   # >> def PyIsTotalSurjection(self, domain_set : PySet, range_set : PySet) -> bool: #Inherited #Unsupported

   # >> def PyIsBijection(self, domain_set : PySet, range_set : PySet) -> bool: #Inherited #Unsupported

   # >> def __call__(self, domain_element : Any) -> Any: #Apply method #Inherited


class PyFamilies(Generic[D,R]):

   def __init__(self, familyType : PyFamilyTypes = PyFamilyTypes.UndeterminedFamilyType,
                domain_set : PySet[D] = PySet(),
                range_set : PySet[R] = PySet()) -> None:
      #print('Test_PyFamilies.__init__')
      self.__FamilyType : PyFamilyTypes = familyType
      self.__DomainSet : PySet[D] = domain_set
      self.__RangeSet : PySet[R] = range_set

   def FamilyType(self) -> PyFamilyTypes:
      return self.__FamilyType

   def DomainSet(self) -> PySet[D]:
      return self.__DomainSet

   def RangeSet(self) -> PySet[R]:
      return self.__RangeSet

   def __str__(self) -> str:
      return 'PyFamilies(' + self.__FamilyType.__str__() + ' \nDomainSet(' + self.__DomainSet.__str__() +  ')\nRangeSet(' + self.__RangeSet.__str__() + '))'

   def __repr__(self) -> str:
      return 'PyFamilies(' + self.__FamilyType.__str__() + ' \nDomainSet(' + self.__DomainSet.__str__() +  ')\nRangeSet(' + self.__RangeSet.__str__() + '))'

   def PyContains(self,relation : PyRel[D,R]) -> bool:
      #print('Test_PyFamilies.PyContains')
      if self.__FamilyType == PyFamilyTypes.Relations:
         return relation.PyIsRelation(self.__DomainSet,self.__RangeSet)
      if self.__FamilyType == PyFamilyTypes.TotalRelations:
         return relation.PyIsTotalRelation(self.__DomainSet,self.__RangeSet)
      if self.__FamilyType == PyFamilyTypes.SurjectiveRelations:
         return relation.PyIsSurjectiveRelation(self.__DomainSet,self.__RangeSet)
      if self.__FamilyType == PyFamilyTypes.TotalSurjectiveRelations:
         return relation.PyIsTotalSurjectiveRelation(self.__DomainSet,self.__RangeSet)
      if self.__FamilyType == PyFamilyTypes.PartialFunctions:
         return relation.PyIsPartialFunction(self.__DomainSet,self.__RangeSet)
      if self.__FamilyType == PyFamilyTypes.TotalFunctions:
         return relation.PyIsTotalFunction(self.__DomainSet,self.__RangeSet)
      if self.__FamilyType == PyFamilyTypes.PartialInjections:
         return relation.PyIsPartialInjection(self.__DomainSet,self.__RangeSet)
      if self.__FamilyType == PyFamilyTypes.TotalInjections:
         return relation.PyIsTotalInjection(self.__DomainSet,self.__RangeSet)
      if self.__FamilyType == PyFamilyTypes.PartialSurjections:
         return relation.PyIsPartialSurjection(self.__DomainSet,self.__RangeSet)
      if self.__FamilyType == PyFamilyTypes.TotalSurjections:
         return relation.PyIsTotalSurjection(self.__DomainSet,self.__RangeSet)
      if self.__FamilyType == PyFamilyTypes.Bijections:
         return relation.PyIsBijection(self.__DomainSet,self.__RangeSet)
      raise Exception('Family Type unrecognized.')

   def PyNotContains(self,relation : PyRel[D,R]) -> bool:
      #print('Test_PyFamilies.PyNotContains')
      return not self.PyContains(relation)

   def PyChoice(self) -> PyRel[D,R]:
      #print('Test_PyFamilies.PyChoice')
      tfunc_tuples : Set[Tuple[D,R]] = set()
      if self.__FamilyType == PyFamilyTypes.TotalFunctions:
         for dom_ele in self.__DomainSet:
            tfunc_tuples.add((dom_ele,self.__RangeSet.PyChoice()))
         return PyRel(tfunc_tuples)
      if self.__FamilyType == PyFamilyTypes.TotalInjections:
         if isinstance(self.__RangeSet,PyCondSet_Ext):
            raise Exception('Operation not supported for PyCondSet_Ext in TotalInjections.')
         if isinstance(self.__RangeSet,PyCondSet):
            visited_range_set : Set[R] = set()
            for dom_ele in self.__DomainSet:
               if self.__RangeSet.PyFinite() and len(visited_range_set) == len(self.__RangeSet):
                  raise Exception('It was not possible to create a TotalInjective Relation')
               img_ele = self.__RangeSet.PyChoice()
               while(img_ele in visited_range_set):
                     img_ele = self.__RangeSet.PyChoice()
               tfunc_tuples.add((dom_ele,img_ele))
               visited_range_set.add(img_ele)
            return PyRel(tfunc_tuples)
         if isinstance(self.__RangeSet,PySet):
            non_visited_range_set : Set[R] = self.__RangeSet.FiniteInclusion()
            for dom_ele in self.__DomainSet:
               if len(non_visited_range_set) == 0:
                  raise Exception('It was not possible to create a TotalInjective Relation')
               img_ele = choice(list(non_visited_range_set))
               tfunc_tuples.add((dom_ele,img_ele))
               non_visited_range_set.discard(img_ele)
            return PyRel(tfunc_tuples)
      raise Exception('Operation only supported for TotalFunctions or TotalInjections.')


class PyPrelude():

   def __init__(self) -> None:

      ###Special Pararmeters###

      # Amount of times that the Prelude will try to generate valid values
      #    for the parameters of an event.
      self.__lowMaxRandomGenAttempts : int = 5
      
      # Amount of times that the Prelude will try to generate valid values
      #    for the constants of a context.
      self.__highMaxRandomGenAttempts : int = 10

      # Flag to activate or deactivate all the contracts.
      self.__DESIGN_BY_CONTRACT_ENABLED : bool = True
      
      # Amount of times that the Prelude will try to choose an enabled event
      #    from a machine and execute it.
      self.__MaxAutoExecuteAttempts : int = 10
      
      # When True, the Prelude will traverse infinite Sets (like the natural numbers set) by traversing a finite set that represents that infinite set.
      #    This parameter NEEDS to be True so that the Prelude can execute predicates that require the traversing of infinite sets (for example, when there is a
      #    quantified predicate where the bound variable is type 'int'.
      self.__USE_FINITE_SPECIAL_SETS : bool = False

      # Value that defines the size of the finite sets that represent infinite setes when USE_FINITE_SPECIAL_SETS is True. For example, if this parameter = 10,
      #    then the integers will go from -10 to 10, the natural number will go from 0 to 10, and the natural numbers without the 0 will go from 1 to 10.
      self.__FINITE_SPECIAL_SETS_LIMIT : int = 10

      # PyRandValGen will generate random integer values within this range.
      self.__RAND_INT_RANGE : Tuple[int,int] = (-100,100)

      # PyRandValGen will generate random sets (PySet) of at most this amount of elements.
      self.__RAND_SET_SIZE : int = 5

      # PyRandValGen will generate random relations (PyRel) of at most this amount of elements.
      self.__RAND_REL_SIZE : int = 5

      ###PyRandValGen CarrierSets###
      self.__CarrierSetClasses : Dict[str,Type[Enum]] = dict()
      self.__CarrierSets : Dict[str,PySet[Enum]] = dict()
      self.__CarrierSetsIters : Dict[str,int] = dict()

   #This method exists to avoid Optional[ ] Typings.
   def NoParam(self) -> Any:
      return None
      
   def BOOL(self) -> PySet[bool]:
      return PySet({True,False})

   def NAT(self) -> PyNAT:
      return PyNAT()

   def NAT1(self) -> PyNAT1:
      return PyNAT1()

   def INT(self) -> PyINT:
      return PyINT()

   def PNAT(self) -> PyCondSet[PySet[int]]:
      return PyCondSet(PyBaseFunc.PNAT_ContainsFunc, finite_func = PyBaseFunc.ReturnFalse0)

   def PNAT1(self) -> PyCondSet[PySet[int]]:
      return PyCondSet(PyBaseFunc.PNAT1_ContainsFunc, finite_func = PyBaseFunc.ReturnFalse0)

   def PINT(self) -> PyCondSet[PySet[int]]:
      return PyCondSet(PyBaseFunc.PINT_ContainsFunc, finite_func = PyBaseFunc.ReturnFalse0)

   def P1NAT(self) -> PyCondSet[PySet[int]]:
      return PyCondSet(PyBaseFunc.P1NAT_ContainsFunc, finite_func = PyBaseFunc.ReturnFalse0)

   def P1NAT1(self) -> PyCondSet[PySet[int]]:
      return PyCondSet(PyBaseFunc.P1NAT1_ContainsFunc, finite_func = PyBaseFunc.ReturnFalse0)

   def P1INT(self) -> PyCondSet[PySet[int]]:
      return PyCondSet(PyBaseFunc.P1INT_ContainsFunc, finite_func = PyBaseFunc.ReturnFalse0)

   def NATXNAT(self) -> PyNATXNAT:
      return PyNATXNAT()

   def INTXINT(self) -> PyINTXINT:
      return PyINTXINT()

   def INTXNAT(self) -> PyINTXNAT:
      return PyINTXNAT()

   def ID(self) -> PyID:
      return PyID()

   def LOWMAXGENATTEMPTS(self) -> int:
      return self.__lowMaxRandomGenAttempts

   def HIGHMAXGENATTEMPTS(self) -> int:
      return self.__highMaxRandomGenAttempts

   def MaxAutoExecuteAttempts(self) -> int:
      return self.__MaxAutoExecuteAttempts

   def DESIGN_BY_CONTRACT_ENABLED(self) -> bool:
      return self.__DESIGN_BY_CONTRACT_ENABLED

   def USE_FINITE_SPECIAL_SETS(self) -> bool:
      return self.__USE_FINITE_SPECIAL_SETS

   def RAND_INT_RANGE(self) -> Tuple[int,int]:
      return self.__RAND_INT_RANGE

   def RAND_SET_SIZE(self) -> int:
      return self.__RAND_SET_SIZE

   def RAND_REL_SIZE(self) -> int:
      return self.__RAND_REL_SIZE

   def FINITE_SPECIAL_SETS_LIMIT(self) -> int:
      return self.__FINITE_SPECIAL_SETS_LIMIT

   def setLowMaxGenAttempts(self, newLowMaxAttempts: int) -> None:
      assert(newLowMaxAttempts>=0)
      self.__lowMaxRandomGenAttempts = newLowMaxAttempts

   def setHighMaxGenAttempts(self, newHighMaxAttempts: int) -> None:
      assert(newHighMaxAttempts>=0)
      self.__highMaxRandomGenAttempts = newHighMaxAttempts

   def setDESIGN_BY_CONTRACT_ENABLED(self, newDESIGN_BY_CONTRACT : bool) -> None:
      self.__DESIGN_BY_CONTRACT_ENABLED = newDESIGN_BY_CONTRACT

   def setUSE_FINITE_SPECIAL_SETS(self, newUSE_FINITE_SPECIAL_SETS : bool) -> None:
      self.__USE_FINITE_SPECIAL_SETS = newUSE_FINITE_SPECIAL_SETS

   def setRAND_INT_RANGE(self, newRAND_INT_RANGE: Tuple[int,int]) -> None:
      assert(newRAND_INT_RANGE[0]<=newRAND_INT_RANGE[1])
      self.__RAND_INT_RANGE = newRAND_INT_RANGE

   def setRAND_SET_SIZE(self, newRAND_SET_SIZE: int) -> None:
      assert(newRAND_SET_SIZE > 0)
      self.__RAND_SET_SIZE = newRAND_SET_SIZE

   def setRAND_REL_SIZE(self, newRAND_REL_SIZE: int) -> None:
      assert(newRAND_REL_SIZE > 0)
      self.__RAND_REL_SIZE = newRAND_REL_SIZE

   def setFINITE_SPECIAL_SETS_LIMIT(self, newFINITE_SPECIAL_SETS_LIMIT: int) -> None:
      assert(newFINITE_SPECIAL_SETS_LIMIT > 0)
      self.__FINITE_SPECIAL_SETS_LIMIT = newFINITE_SPECIAL_SETS_LIMIT

   #PY RANDOM VALUE GENERATOR #Weak Typechecking

   def PyRandIntGen(self) -> int:
      return randint(P.RAND_INT_RANGE()[0],P.RAND_INT_RANGE()[1])

   def PyRandBoolGen(self) -> bool:
      return choice((True,False))

   def PyRandPySetGen(self, pyType : str) -> PySet:
      tmp : Set = set()
      for e in range(P.RAND_SET_SIZE()):
         tmp.add(self.PyRandValGen(pyType[6:-1]))
      return PySet(tmp)

   def PyRandEnumGen(self, pyType : str) -> Enum:
      EnumType : Type[Enum] = self.__CarrierSetClasses[pyType]
      self.__CarrierSetsIters[pyType] += 1
      if self.__CarrierSetsIters[pyType] > len(EnumType):
         self.__CarrierSetsIters[pyType] = 1
      return EnumType(self.__CarrierSetsIters[pyType])

   def PyRandTupleGen(self, pyType : str) -> Tuple:

      parenthesis_count : int = 0
      i_index : int = 6
      for char in pyType[6:]:
         if char == ',' and parenthesis_count == 0:
            break
         if char == '[':
            parenthesis_count += 1
         if char == ']':
            parenthesis_count -= 1
         i_index += 1
         
      return ( self.PyRandValGen(pyType[6:i_index]), self.PyRandValGen(pyType[i_index+1:-1]) )

   def PyRandPyRelGen(self, pyType : str) -> PyRel:
      return PyRel( self.PyRandValGen( 'PySet[Tuple[' + pyType[6:] + ']').FiniteInclusion() )

   def PyRandValGen(self, pyType : str ) -> Any:
      if pyType == 'bool':
         return self.PyRandBoolGen()
      elif pyType == 'int':
         return self.PyRandIntGen()
      elif pyType[:5] == 'PySet':
         return self.PyRandPySetGen(pyType)
      elif pyType in self.__CarrierSets:
         return self.PyRandEnumGen(pyType)
      elif pyType[:5] == 'Tuple':
         return self.PyRandTupleGen(pyType)
      elif pyType[:5] == 'PyRel':
         return self.PyRandPyRelGen(pyType)
      else:
         raise Exception('Error PyPrelude.PyRandValGen')

   def PyCarrierSetGet(self, carrierSetName : str ) -> PySet[Any]:
      return self.__CarrierSets[carrierSetName]

   def AddCarrierSet(self, carrierSetName : str, carrierSetClassType : Type[Enum]) -> None:
      self.__CarrierSetClasses[carrierSetName] = carrierSetClassType

      tmp : Set[Enum] = set()
      for element in carrierSetClassType:
         tmp.add(element)  
      self.__CarrierSets[carrierSetName] = PySet(tmp)
      self.__CarrierSetsIters[carrierSetName] = 0

   def getCarrierSets(self) -> Dict[str,PySet[Enum]]:
      return self.__CarrierSets

   def getCarrierSetClasses(self) -> Dict[str,Type[Enum]]:
      return self.__CarrierSetClasses

   def getCarrierSetsIters(self) -> Dict[str,int]:
      return self.__CarrierSetsIters

   @staticmethod
   def LogicImplication(left : bool,right : bool) -> bool:
      if left == True and right == False:
         return False
      return True

   @staticmethod
   def LogicEquivalence(left : bool,right : bool) -> bool:
      if (left == True and right == True) or (left == False and right == False):
         return True
      return False

   @staticmethod
   def Minimum(int_set : PySet[int]) -> int:
      if isinstance(int_set, PyCondSet):
         raise Exception('Minimum operation is not supported for implicit sets.')
      return min(int_set.FiniteInclusion())

   @staticmethod
   def Maximum(int_set : PySet[int]) -> int:
      if isinstance(int_set, PyCondSet):
         raise Exception('Maximum operation is not supported for implicit sets.')
      return max(int_set.FiniteInclusion())

   def ObtainSetFromTuple(self, pyType : str) -> PyRel:

      parenthesis_count : int = 0
      i_index : int = 6
      for char in pyType[6:]:
         if char == ',' and parenthesis_count == 0:
            break
         if char == '[':
            parenthesis_count += 1
         if char == ']':
            parenthesis_count -= 1
         i_index += 1
         
      return self.ObtainSetFromType(pyType[6:i_index]).PyCartesianProduct(self.ObtainSetFromType(pyType[i_index+1:-1]))

   def ObtainSetFromSet(self, pyType : str) -> PySet[PySet]:
      return self.ObtainSetFromType(pyType[6:-1]).PyPowerSet()

   def ObtainSetFromType(self, pyType : str) -> Any:
      
      if pyType == 'bool':
         return PySet({True,False})
      elif pyType == 'int':
         return PyINT()
      elif pyType[:5] == 'PySet':
         return self.ObtainSetFromSet(pyType)
      elif pyType in self.__CarrierSets:
         return self.__CarrierSets[pyType]
      elif pyType[:5] == 'Tuple':
         return self.ObtainSetFromTuple(pyType)
      elif pyType[:5] == 'PyRel':
         return self.ObtainSetFromTuple(pyType).PyPowerSet()
      else:
         raise Exception('Error PyPrelude.ObtainSetFromType')

   def BecomesSuchThat(self,
                       predicate : Callable[[List[Any]],bool],
                       BoundIdentType : str) -> Any:
      set_to_iter = self.ObtainSetFromType(BoundIdentType)
      possible_values : Set = set()

      for possible_value in set_to_iter:
         try:
            if predicate(possible_value):
               possible_values.add(possible_value)
         except:
            pass

      if len(possible_values) == 0:
         raise Exception('No value managed to accomplish the given predicate!')
      return PySet(possible_values).PyChoice()

      
   def QuantifiedForAll(self, predicate : Callable[[List[Any]],bool] , BoundIdentDeclsAndTypes : List[Tuple[int,str]]) -> bool:

      boundIdentifiersAmount : int = len(BoundIdentDeclsAndTypes)

      #Create Array Of Sets
      boundIdentifiersSets : List[Any] = [ None for e in range(boundIdentifiersAmount) ]

      #Obtain Sets from Types
      for BoundIdentDeclAndType in BoundIdentDeclsAndTypes:
         boundIdentifiersSets[BoundIdentDeclAndType[0]] = self.ObtainSetFromType( BoundIdentDeclAndType[1] )

      #Create Array of Iters
      boundIdentifiersIters : List[Iterator] = [ iter(boundIdentifiersSets[i]) for i in range(boundIdentifiersAmount) ]

      #Create and Initialize Array of lambda Parameters
      boundIdentifiersValues : List[Any] = [ None for e in range(boundIdentifiersAmount) ]
      for i in range(boundIdentifiersAmount):
         try:
            boundIdentifiersValues[i] = next(boundIdentifiersIters[i])
         except StopIteration:
            return True #chrome-extension://oemmndcbldboiebfnladdacbdfmadadm/http://cse.unl.edu/~cbourke/CSCE235/notes/PredicatesQuantifiers-HandoutNoNotes.pdf

      #Try al possibilities
      indexIterator : int = boundIdentifiersAmount-1
      while(indexIterator>=0):
         
         try:
            if predicate(boundIdentifiersValues) == False:
               return False
         except:
            pass
         
         try:
            boundIdentifiersValues[indexIterator] = next(boundIdentifiersIters[indexIterator])
         except StopIteration:
            boundIdentifiersIters[indexIterator] = iter(boundIdentifiersSets[indexIterator])
            boundIdentifiersValues[indexIterator] = next(boundIdentifiersIters[indexIterator])
            indexIterator-=1
            flag : bool = True
            while(flag and indexIterator>=0):
               try:
                  boundIdentifiersValues[indexIterator] = next(boundIdentifiersIters[indexIterator])
                  indexIterator = boundIdentifiersAmount-1
                  flag = False
               except StopIteration:
                  boundIdentifiersIters[indexIterator] = iter(boundIdentifiersSets[indexIterator])
                  boundIdentifiersValues[indexIterator] = next(boundIdentifiersIters[indexIterator])
                  indexIterator-=1
      
      return True

   def QuantifiedExists(self, predicate : Callable[[List[Any]],bool] , BoundIdentDeclsAndTypes : List[Tuple[int,str]]) -> bool:

      boundIdentifiersAmount : int = len(BoundIdentDeclsAndTypes)

      #Create Array Of Sets
      boundIdentifiersSets : List[Any] = [ None for e in range(boundIdentifiersAmount) ]

      #Obtain Sets from Types
      for BoundIdentDeclAndType in BoundIdentDeclsAndTypes:
         boundIdentifiersSets[BoundIdentDeclAndType[0]] = self.ObtainSetFromType( BoundIdentDeclAndType[1] )

      #Create Array of Iters
      boundIdentifiersIters : List[Iterator] = [ iter(boundIdentifiersSets[i]) for i in range(boundIdentifiersAmount) ]

      #Create and Initialize Array of lambda Parameters
      boundIdentifiersValues : List[Any] = [ None for e in range(boundIdentifiersAmount) ]
      for i in range(boundIdentifiersAmount):
         try:
            boundIdentifiersValues[i] = next(boundIdentifiersIters[i])
         except StopIteration:
            return False #chrome-extension://oemmndcbldboiebfnladdacbdfmadadm/http://cse.unl.edu/~cbourke/CSCE235/notes/PredicatesQuantifiers-HandoutNoNotes.pdf

      #Try al possibilities
      indexIterator : int = boundIdentifiersAmount-1
      while(indexIterator>=0):

         try:
            if predicate(boundIdentifiersValues) == True:
               return True
         except:
            pass
         
         try:
            boundIdentifiersValues[indexIterator] = next(boundIdentifiersIters[indexIterator])
         except StopIteration:
            boundIdentifiersIters[indexIterator] = iter(boundIdentifiersSets[indexIterator])
            boundIdentifiersValues[indexIterator] = next(boundIdentifiersIters[indexIterator])
            indexIterator-=1
            flag : bool = True
            while(flag and indexIterator>=0):
               try:
                  boundIdentifiersValues[indexIterator] = next(boundIdentifiersIters[indexIterator])
                  indexIterator = boundIdentifiersAmount-1
                  flag = False
               except StopIteration:
                  boundIdentifiersIters[indexIterator] = iter(boundIdentifiersSets[indexIterator])
                  boundIdentifiersValues[indexIterator] = next(boundIdentifiersIters[indexIterator])
                  indexIterator-=1
      
      return False

   def DebugArray(self, pyrel_as_arr : PyRel[int,Any]) -> List[Any]:
      if isinstance(pyrel_as_arr,PyCondRel):
         raise Exception('Operation not supported for implicit Rels.')
      converted_array : List[Any] = list(pyrel_as_arr.FiniteInclusion())
      converted_array.sort(key= lambda tuple_in_arr:tuple_in_arr[0])
      return [element[1] for element in converted_array]


P : PyPrelude = PyPrelude()

# Methods to deal with Mypy inconsistencies.

def MypyPySetCastPyRel(pyset_to_cast : PySet) -> PyRel:
   return PyRel(pyset_to_cast.FiniteInclusion())

def MypyPyCondSet(lambda_func : Callable) -> PyCondSet:
   return PyCondSet(lambda_func)

'''
#PENDING
   #Discuss OR Check
      #Create Special Class for PyNat, PyNat1, etc.
      #SubSet with finite element is possible.
      #Operations return duplicates
      #Operate with &


##### TEST FOR SIMPLE PYSET
t10 : PySet[int] = PySet({3,4})
t11 : PySet[int] = PySet({4,3})
t12 : PySet[int] = PySet({7})
print(t12.PyContains(7))
print(t12.PyNotContains(7))

##### TEST FOR SPECIAL PYSET
t13 : PySet[int] = PySet({3,4})
t14 : PySet[int] = PySet({0,3,4})
t15 : PySet[int] = PySet({-1,3,4})
print(P.PNAT().PyContains(t13))
print(P.PNAT().PyContains(t14))
print(P.PNAT().PyContains(t15))
print(P.PNAT1().PyContains(t13))
print(P.PNAT1().PyContains(t14))
print(P.PNAT1().PyContains(t15))
print(P.PINT().PyContains(t13))
print(P.PINT().PyContains(t14))
print(P.PINT().PyContains(t15))

##### TEST FOR PYSET OF PYSETS
t20 : PySet[PySet[int]] = PySet({PySet({3,4}),PySet({4,3}),PySet(),PySet({7})})
t21 : PySet[PySet[int]]= PySet({PyCondSet(),PyCondSet(PyBaseFunc.NAT_ContainsFunc)})

##### TEST FOR PYUNION AND PYINTERSECTION AND PYDIFFERENCE
t30 : PySet[int] = PySet({3,4,10})
t31 : PySet[int] = t30.PyUnion(t12)
t34 : PySet[int] = PySet({3,4,20})
print(t30.PyIntersection(t34))
print(t30.PyDifference(t34))

##### TEST FOR PYCARTESIANPRODUCT
t23 : PyRel[int,int] = t30.PyCartesianProduct(t34)
print(t23)

##### TEST FOR PYISSUBSET
t32 : PySet[int] = PySet({-3, 4, 10})
t33 : PySet[int] = PySet({-3, 4, 5})
print(t32.PyIsSubset(PyNAT()))
print(t32.PyIsSubset(PyINT()))
print(t32.PyIsSubset(t33))
print(t32.PyNotSubset(t33))

##### TEST FOR PYPARTITION
t35 : PySet[int] = PySet({1, 2, 3, 4, 5})
t36 : PySet[int] = PySet({1, 2})
t37 : PySet[int] = PySet({3})
t38 : PySet[int] = PySet({4, 5})
t39 : PySet[int] = PySet({4, 5, 7})
print(t35.PyPartition([t36,t37]))
print(t35.PyPartition([t36,t37,t38]))
print(t35.PyPartition([t36,t37,t39]))

##### TEST FOR PYPOWERSET +1
t22 : PySet[int] = PySet({1,2,3})
print(t22.PyPowerSet())
print(len(t22.PyPowerSet()))
print(t22.PyPowerSet1())
print(len(t22.PyPowerSet1()))

##### TEST PYCONDSET and PyNAT
t40 : PySet[int] = PyCondSet(PyBaseFunc.NAT_ContainsFunc)
t40.PyContains(4)
t41 : PySet[int] = PyNAT()
print(t41.PyContains(7))
print(t41.PyUnion(t32))

t42 : PySet[int] = PyINT()
print(t41.PyUnion(t42))
t43 : PySet[int] = PyNAT1()
print(t41.PyUnion(t42))
# Test PyUnion and PyIntersection and PyDifference on PyCondSet (PySet)
print(t11.PyUnion(t41))
print(t32.PyIntersection(t41))
print(t32.PyDifference(t41))
P.setUSE_FINITE_SPECIAL_SETS(True)
print(t22.PyCartesianProduct(P.NAT()))
print(P.NAT().PyCartesianProduct(t22))
P.setUSE_FINITE_SPECIAL_SETS(False)

##### TEST PYCONDSET_EXT
t50 : PySet[int] = PyCondSet_Ext(PyBaseFunc.NAT_ContainsFunc,{-3,-7},{90})
print(t50.PyContains(10))
print(t50.PyContains(-7))
print(t50.PyContains(90))
# Test PyUnion and PyIntersection and PyDifference on PyCondSet_Ext (PySet)
print(t11.PyUnion(t50))
print(t32.PyIntersection(t50))
print(t32.PyDifference(t50))

##### TEST PYCONDSET_TREEEXT
t60 : PySet[int] = PyCondSet_TreeExt(PyBaseFunc.NAT_ContainsFunc,{-5,-7,-95},{90})
t61 : PySet[int] = PyCondSet_TreeExt(PyBaseFunc.test,{50},{22})
t62 = t60.PyUnion(t61)
print(t62.PyContains(90))
t63 = t60.PyIntersection(t61)
print(t63.PyContains(90))
print(t63.PyContains(-5))
print(t63.PyContains(-95))
t64 = t60.PyDifference(t61)
print(t64.PyContains(90))
print(t64.PyContains(-5))
print(t64.PyContains(-95))
# Test PyUnion and PyIntersection and PyDifference on PyCondSet_TreeExt (PySet)
print(t11.PyUnion(t60))
print(t32.PyIntersection(t60))
print(t32.PyDifference(t60))
# Test PyUnion and PyIntersection and PyDifference on PyCondSet_TreeExt (PyCondSet)
print(t40.PyUnion(t60))
print(t42.PyIntersection(t60))
print(t40.PyDifference(t60))

##### TEST PYRANDVALGEN
t70 : PySet[PySet[int]] = P.PyRandValGen('PySet[PySet[int]]')
t71 : Tuple[int,Tuple[Tuple[int,int],int]] = P.PyRandValGen('Tuple[int,Tuple[Tuple[int,int],int]]')
print(t71)

##### TEST PYREL: PYCONTAINS
t81 : PyRel[int,int] = PyRel({(3,4),(4,7)})
t82 : PyRel[int,int] = PyRel({(4,3),(4,7)})
t83 : PyCondRel[int,int] = PyCondRel(PyBaseFunc.test2,PySet({1,2,3}),PySet({3,4,7,10,20,100,200}))
t84 : PySet[int] = PySet({-3, 4, 10})
t85 : PyCondRel[int,int] = P.NATXNAT()

print(t81.PyContains((4,3)))
print(t81.PyNotContains((4,3)))
print(t83.PyContains((1,100)))
print(t83.PyContains((2,100)))
print(t83.PyNotContains((3,3)))

##### TEST PYREL: PYUNION AND PYINTERSECTION AND PYDIFFERENCE AND CARTESIANPRODUCT
print(t81.PyUnion(t82))
print(t81.PyIntersection(t82))
print(t81.PyIntersection(t83))
print(t81.PyIntersection(PyINTXINT()))
print(PyINTXINT().PyIntersection(t81))
print(t81.PyIntersection(PyID()))
print(PyID().PyIntersection(t81.PyUnion(PyRel({(7,7)}))))
print(t81.PyDifference(t83))
print(t81.PyCartesianProduct(t84))
#P.setUSE_FINITE_SPECIAL_SETS(True)
#print(t85.PyCartesianProduct(t81))
#P.setUSE_FINITE_SPECIAL_SETS(False)

##### TEST PYREL: PYISSUBSET AND PYNOTSUBSET AND PYISPROPERSUBSET AND PYNOTPROPERSUBSET AND PYFINITE AND PYPARTITION AND PYPOWERSET AND PYFINITE
t90 : PyRel[int,int] = PyRel({(3,4),(4,7)})
t91 : PyRel[int,int] = PyRel({(3,4),(4,7),(7,9),(4,9),(2,1),(2,2),(2,2)})
t92 : PyRel[int,int] = PyRel({(7,9)})
t93 : PyRel[int,int] = PyRel({(2,2),(7,10),(3,5),(8,2)})
t94 : PyCondRel[int,int] = PyCondRel(PyBaseFunc.test2,PySet({1,2,3}),PySet({3,4,7,10,20,100,200}))
t95 : PyRel[int,int] = PyRel({(2,2),(7,10),(3,5),(8,7)})
print(t90.PyIsSubset(t91))
print(t82.PyIsSubset(t91))
print(t90.PyNotSubset(t91))
print(t82.PyNotSubset(t91))
print(t81.PyIsProperSubset(t90))
print(t90.PyIsProperSubset(t91))
print(t81.PyNotProperSubset(t90))
print(t90.PyFinite())
print(t91.PyFinite())
print(t91.PyPartition([t90,t92]))
print(t91.PyPartition([t90,t93]))
print(t91.PyPartition([t91,PyRel()]))
print(t92.PyPowerSet())
print(len(t91.PyPowerSet()))
print(t91.PyPowerSet1())
print(len(t91.PyPowerSet1()))
print(t94.PyFinite()) #####################################################TESTS HERE
print(t94.PyDomain())

##### TEST PYREL: PYDOMAIN AND PYRANGE AND PYCOMPOSITION AND PYDOMAIN|RANGE RESTRICTION|SUBSTRACTION AND INVERSE AND RELIMAGE AND PYOVERRIDING AND PYDIRECTPRODUCT
#        AND PY ISRELATION | ISTOTALRELATION | ISSURJECTIVERELATION | ISTOTALSURJECTIVERELATION | ISWELLDEFINED | ALL INJECTSURJECTBIJECTION FUNCTIONS
print(t82.PyDomain())
print(t82.PyRange())
print(t91.PyComposition(t93))
print(t91.PyBackwardComposition(t95))
print(t93.PyDomainRestriction(PySet({7,2,37})))
print(t93.PyRangeRestriction(PySet({7,9,2,10})))
print(t93.PyDomainSubstraction(PySet({7,2,37})))
print(t93.PyRangeSubstraction(PySet({7,9,2,10})))
print(~t93)
print(t93[PySet({2,7})])
print(t91.PyOverriding(t93))
print(t91.PyDirectProduct(t93))
print(t90.PyIsRelation(PySet({3,4,5}),PySet({3,4,5})))
print(t90.PyIsRelation(PySet({3,4,5}),PySet({4,7})))
print(t90.PyIsTotalRelation(PySet({3,4,5}),PySet({7,3,4,5})))
print(t90.PyIsTotalRelation(PySet({3,4}),PySet({7,3,4,5})))
print(t90.PyIsSurjectiveRelation(PySet({3,4,5}),PySet({3,4,7})))
print(t90.PyIsSurjectiveRelation(PySet({3,4,5}),PySet({4,7})))
print(t90.PyIsTotalSurjectiveRelation(PySet({3,4,5}),PySet({3,4,7})))
print(t90.PyIsTotalSurjectiveRelation(PySet({3,4}),PySet({4,7})))
print(t94.PyIsTotalRelation(PySet({1,2,3}),PySet({3,4,7,10,20,100,200})))
print(t94.PyIsTotalFunction(PySet({1,2,3}),PySet({3,4,7,10,20,100,200})))

print(t90.PyIsWellDefined())
print(t91.PyIsWellDefined())
print(t90.PyIsTotal(PySet({3,4})))
print(t90.PyIsTotal(PySet({3,4,5})))
print(t90.PyIsTotalFunction(PySet({3,4}),PySet({4,7,9})))
print(t90.PyIsTotalFunction(PySet({3,4,5}),PySet({4,7,9})))
print(t90.PyIsInjection())
print(t93.PyIsInjection())
print(t90.PyIsSurjection(PySet({4,7})))
print(t90.PyIsSurjection(PySet({7,4,9})))
print(t93.PyIsBijection(PySet({2,7,3,8}),PySet({2,5,10})))
print(t93.PyIsTotalSurjection(PySet({2,7,3,8}),PySet({2,5,10})))
print(t95.PyIsBijection(PySet({2,7,3,8}),PySet({2,5,10,7})))
print(t93[PySet({2,7})])
print(t90(3))
print(t95(7))
print(t91(4))

##### TEST PYNATXNAT AND SIMILARS
print(P.ID().PyDomainRestriction(PySet({3,4,5})))
print(PyRel({(0,-3),(3,7)}).PyIsSubset(P.INTXINT()))

##### FAMILYOF
family_of_relations0 : PyFamilies = PyFamilies(PyFamilyTypes.Relations,PySet({3,4,5}),PySet({3,4,5}))
print(family_of_relations0.PyContains(t90))
family_of_relations1 : PyFamilies = PyFamilies(PyFamilyTypes.Relations,PySet({3,4,5}),PySet({4,7}))
print(family_of_relations1.PyContains(t90))
family_of_relations2 : PyFamilies = PyFamilies(PyFamilyTypes.TotalSurjectiveRelations,PySet({3,4,5}),PySet({3,4,7}))
print(family_of_relations2.PyContains(t90))
family_of_relations3 : PyFamilies = PyFamilies(PyFamilyTypes.TotalSurjectiveRelations,PySet({3,4}),PySet({4,7}))
print(family_of_relations3.PyContains(t90))

### PYCHOICE AND OBTAINSETFROMTYPE
print(PySet({10,20,37,40,50}).PyChoice())
print(P.NAT1().PyChoice())
print(t91.PyChoice())
print(P.NATXNAT().PyChoice())
print(P.ObtainSetFromType('Tuple[bool,bool]'))
print(PyFamilies(PyFamilyTypes.TotalFunctions,PySet({1,2,3,4,5}),PySet({'a','b','c','d'})).PyChoice())
print(PyFamilies(PyFamilyTypes.TotalInjections,PySet({1,2,3,4,5}),PySet({'a','b','c','d','e','f','g'})).PyChoice())

### OTHER TESTS
t100 = MypyPyCondSet(lambda boundIdentifiers : True if ((( boundIdentifiers[0] ) > 5) and (( boundIdentifiers[1] ) < 10)) else False)
print(t100.PyContains((7,7)))
t101 = MypyPyCondSet(lambda boundIdentifiers : True if (P.NAT().PyContains(boundIdentifiers)) else False)
'''
