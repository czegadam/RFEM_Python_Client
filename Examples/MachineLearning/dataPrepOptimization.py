import os
import sys
baseName = os.path.basename(__file__)
dirName = os.path.dirname(__file__)
print('basename:    ', baseName)
print('dirname:     ', dirName)
sys.path.append(dirName + r'/../..')

from RFEM.enums import AddOn, DesignSituationType, LoadDirectionType, ModelType, NodalSupportType, OptimizeOnType, Optimizer, StaticAnalysisType, SteelBoundaryConditionsSupportType, SteelBoundaryConditionsEccentricityTypeZ, AnalysisType
from RFEM.initModel import Model, Calculate_all, SetModelType, SetAddonStatus
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.section import Section
from RFEM.BasicObjects.member import Member
from RFEM.TypesForNodes.nodalSupport import NodalSupport
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings
from RFEM.LoadCasesAndCombinations.loadCase import LoadCase
from RFEM.LoadCasesAndCombinations.designSituation import DesignSituation
from RFEM.Loads.memberLoad import MemberLoad
from RFEM.Results.resultTables import GetMaxValue, ResultTables
from RFEM.Calculate import optimizationSettings
from RFEM.Calculate.meshSettings import GetModelInfo

from RFEM.SteelDesign.steelUltimateConfigurations import SteelDesignUltimateConfigurations
from RFEM.LoadCasesAndCombinations.designSituation import DesignSituation
from RFEM.LoadCasesAndCombinations.loadCombination import LoadCombination
from RFEM.LoadCasesAndCombinations.loadCasesAndCombinations import LoadCasesAndCombinations


import pandas as pd
import random as rd

sectionList = ['IPE 80', 'IPE 100', 'IPE 120', 'IPE 140', 'IPE 160', 'IPE 180',
               'IPE 200', 'IPE 220', 'IPE 240', 'IPE 270', 'IPE 300', 'IPE 330',
               'IPE 360', 'IPE 400', 'IPE 450', 'IPE 500', 'IPE 500', 'IPE 600',
               'IPE 750x137', 'IPE 750x147', 'IPE 750x173', 'IPE 750x196']


length = rd.randint(1,20)
force = rd.randint(1,20)
print(length, force)



finalData = pd.DataFrame(columns=['Length (m)', 'Force (kN/m)', 'Section'])
lengthFinalList = []
forceFinalList = []
SectionFinalList = []


Model(True, 'dataPrep.rf6')
SetModelType(ModelType.E_MODEL_TYPE_2D_XZ_PLANE_STRESS)
SetAddonStatus(Model.clientModel, AddOn.steel_design_active, True)
SetAddonStatus(Model.clientModel, AddOn.cost_estimation_active, True)


#SetAddonStatus(Model, AddOn.steel_design_active, True)


Model.clientModel.service.begin_modification()
Model.clientModel.service.delete_all()

Model.clientModel.service.set_addon_statuses()

Node(1, 0, 0, 0)
Node(2, length, 0, 0)

Material(1, "S235")

NodalSupport(1, '1', NodalSupportType.HINGED)
NodalSupport(2, '2', NodalSupportType.ROLLER_IN_X)

StaticAnalysisSettings(1, 'Linear', StaticAnalysisType.GEOMETRICALLY_LINEAR)

LoadCase(1, 'DEAD', [True, 0, 0, 1])

MemberLoad(1, 1, '1', LoadDirectionType.LOAD_DIRECTION_LOCAL_Z, force*1000)

Section(1, 'IPE 80', 1)

Member(1, 1, 2, 0, 1, 1)


LoadCasesAndCombinations({
                    "current_standard_for_combination_wizard": 6207,
                    "activate_combination_wizard_and_classification": True,
                    "activate_combination_wizard": True,
                    "result_combinations_active": True,
                    "result_combinations_parentheses_active": False,
                    "result_combinations_consider_sub_results": False,
                    "combination_name_according_to_action_category": True
                 },
                 model= Model)

DesignSituation(1,
                DesignSituationType.DESIGN_SITUATION_TYPE_EQU_PERMANENT_AND_TRANSIENT,
                True,
                None,
                '',
                None,
                model = Model)

LoadCombination(1,
                AnalysisType.ANALYSIS_TYPE_STATIC,
                1,
                [False],
                1,
                False,
                False,
                False,
                True,
                [[1.5, 1, 0, False]],
                '',
                None,
                model = Model)


SteelDesignUltimateConfigurations(1, [False], 'All', 'All', '', None, model = Model)


optimizationSettings.OptimizationSettings(True, 28, OptimizeOnType.E_OPTIMIZE_ON_TYPE_MIN_WHOLE_WEIGHT, Optimizer.E_OPTIMIZER_TYPE_ALL_MUTATIONS, 0.2, model = Model)

Calculate_all()

Model.clientModel.service.finish_modification()

SectionFinalList.append(Model.clientModel.service.get_section(1).name)
lengthFinalList.append(length)
forceFinalList.append(force)











