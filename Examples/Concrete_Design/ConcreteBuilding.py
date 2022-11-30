#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
baseName = os.path.basename(__file__)
dirName = os.path.dirname(__file__)
print('basename:    ', baseName)
print('dirname:     ', dirName)
sys.path.append(dirName + r'/../..')

#This script follows the basic design of conrete beams / slabs
#It is based on the following webinar: https://www.dlubal.com/de/support-und-schulungen/schulungen/videos/003441

#Import all modeules required to access RFEM

from RFEM.enums import *
from RFEM.initModel import Model, SetAddonStatus
from RFEM.LoadCasesAndCombinations.loadCasesAndCombinations import LoadCasesAndCombinations

from RFEM.BasicObjects.material import Material

from RFEM.BasicObjects.section import Section

from RFEM.BasicObjects.node import Node

from RFEM.BasicObjects.line import Line

from RFEM.BasicObjects.member import Member

from RFEM.TypesForNodes.nodalSupport import NodalSupport

from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings
from RFEM.LoadCasesAndCombinations.loadCase import LoadCase

from RFEM.Loads.memberLoad import MemberLoad

from RFEM.ConcreteDesign.ConcreteUltimateConfigurations import ConcreteUltimateConfiguration

from RFEM.TypesforConcreteDesign.ConcreteDurability import ConcreteDurability

from RFEM.LoadCasesAndCombinations.designSituation import DesignSituation
from RFEM.LoadCasesAndCombinations.loadCombination import LoadCombination

#Create a new Model

name = input('Please type the model name: ')
Model(True, name)

#deleting all available objects/materials/sections

Model.clientModel.service.delete_all()

#activate required add-ons

SetAddonStatus(Model.clientModel, AddOn.concrete_design_active, True)

#setting the requiered national annexes

LoadCasesAndCombinations({
                           "current_standard_for_combination_wizard": 6038,
                           "activate_combination_wizard_and_classification": True,
                           "activate_combination_wizard": True,
                           "result_combinations_active": True,
                           "result_combinations_parentheses_active": False,
                           "result_combinations_consider_sub_results": False,
                           "combination_name_according_to_action_category": True
                     },
                     model= Model)



#access the model through webservices

#Model.clientModel.service.begin_modification()



#creating requiered materials concrete + reinfcs
#orcement steel

Material(1, 'C30/37 | DIN EN 1992-1-1/NA/A1:2015-12')
Material(2, 'B500S(A) | DIN EN 1992-1-1/NA/A1:2015-12')

#create section made from concrete

Section(1, 'R_M1 0.3/0.45',1)

Section(2, 'R_M1 0.2/0.2',1)

#creating the model (nodes and lines)

Node(1, 0, 0, 0)
Node(2, 8, 0, 0)
Node(3, 8, 4, 0)
Node(4, 0, 4, 0)

Node(5, 0, 0, -4)
Node(6, 8, 0, -4)
Node(7, 8, 4, -4)
Node(8, 0, 4, -4)
Node(13, 4,4,-4)

Node(9, 0, 10, 0)
Node(10, 4, 10, 0)
Node(11, 0, 10, -4)
Node(12, 4, 10, -4)



#creating columns

Line(1, '1 5')
Line(2, '2 6')
Line(3, '3 7')
Line(4, '4 8')
Line(9, '9 11')
Line(10, '10 12')

#creating beams

Line(5, '5 6')
Line(6, '5 8')
Line(7, '6 7')
Line(8, '7 8')
Line(11, '8 11')
Line(12, '13 12')
Line(13, '11 12')

#assigning the created sections to the according lines
#this results in the creation of a member

#beams
Member(1, 5, 6, 0.0, 1, 1, 0, 0)
Member(2, 7, 8, 0.0, 1, 1, 0, 0)
Member(3, 11, 12, 0.0, 1, 1, 0, 0)

#columns
Member(4, 1, 5, 0.0, 2, 2, 0, 0)
Member(5, 2, 6, 0.0, 2, 2, 0, 0)
Member(6, 3, 7, 0.0, 2, 2, 0, 0)
Member(7, 4, 8, 0.0, 2, 2, 0, 0)
Member(8, 9, 11, 0.0, 2, 2, 0, 0)
Member(9, 10, 12, 0.0, 2, 2, 0, 0)

#create supports
NodalSupport(1, '1 2 3 4 9 10', NodalSupportType.FIXED)

#creating the loading on the structure
StaticAnalysisSettings.GeometricallyLinear(1, "Linear")

#own weight
LoadCase.StaticAnalysis(1, 'DEAD LOAD', True, 1, ActionCategoryType.ACTION_CATEGORY_PERMANENT_G, [True, 0.0, 0.0, 1.0])

#live load
LoadCase.StaticAnalysis(2, 'LIVE LOAD', True, 1, ActionCategoryType.ACTION_CATEGORY_IMPOSED_LOADS_CATEGORY_A_DOMESTIC_RESIDENTIAL_AREAS_QI_A, [False])

#adding loading to the system

MemberLoad(1, 1, '1 2 3', LoadDirectionType.LOAD_DIRECTION_LOCAL_Z, 6000)
MemberLoad(2, 2, '1 2 3', LoadDirectionType.LOAD_DIRECTION_LOCAL_Z, 10000)

#setting concrete design choices

ConcreteUltimateConfiguration(1,
                'ULS',
                'All',
                'All',
                'All',
                'All',
                '',
                '',
                None)

DesignSituation(1,
            DesignSituationType.DESIGN_SITUATION_TYPE_STR_PERMANENT_AND_TRANSIENT_6_10,
            True,
            None,
            '',
            None,
            model = Model)

LoadCombination(1,
                  AnalysisType.ANALYSIS_TYPE_STATIC,
                  1,
                  'ULS',
                  1,
                  False,
                  False,
                  False,
                  True,
                  [[1.35, 1, 0, False], [1.5, 2, 0, True]],
                  '',
                  None,
                  model = Model)

ConcreteDurability(1,
                "XC 1",
                "1 2 3 4 5 6 7 8 9",
                '',
                '',
                [True, False, False, False],
                None,
                [False, False, False],
                None,
                [DurabilityStructuralClassType.STANDARD, False, False, False, False],
                [False],
                [False],
                [DurabilityAllowanceDeviationType.STANDARD, False],
                '',
                None,
                model = Model)























