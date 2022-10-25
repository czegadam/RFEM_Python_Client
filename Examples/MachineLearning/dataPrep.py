import os
import sys
baseName = os.path.basename(__file__)
dirName = os.path.dirname(__file__)
print('basename:    ', baseName)
print('dirname:     ', dirName)
sys.path.append(dirName + r'/../..')

from RFEM.enums import LoadDirectionType, ModelType, NodalSupportType, StaticAnalysisType
from RFEM.initModel import Model, Calculate_all, SetModelType
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.section import Section
from RFEM.BasicObjects.member import Member
from RFEM.TypesForNodes.nodalSupport import NodalSupport
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings
from RFEM.LoadCasesAndCombinations.loadCase import LoadCase
from RFEM.Loads.memberLoad import MemberLoad
from RFEM.Results.resultTables import GetMaxValue, ResultTables

import pandas as pd

sectionList = ['IPE 80', 'IPE 100', 'IPE 120', 'IPE 140', 'IPE 160', 'IPE 180',
               'IPE 200', 'IPE 220', 'IPE 240', 'IPE 270', 'IPE 300', 'IPE 330',
               'IPE 360', 'IPE 400', 'IPE 450', 'IPE 500', 'IPE 500', 'IPE 600',
               'IPE 750x137', 'IPE 750x147', 'IPE 750x173', 'IPE 750x196']


lengthList = list(range(1, 17, 1))
forceList = list(range(1, 21, 1))

finalData = pd.DataFrame(columns=['Length (m)', 'Force (kN/m)', 'Section'])
lengthFinalList = []
forceFinalList = []
SectionFinalList = []

tryList = [5,6]

Model(True, 'dataPrep.rf6')
SetModelType(ModelType.E_MODEL_TYPE_2D_XZ_PLANE_STRESS)

for l in lengthList:

    dispLimit = l/3000

    for f in forceList:

        memberDisp = 10
        i = 0

        while memberDisp>dispLimit:

            Model.clientModel.service.begin_modification()
            Model.clientModel.service.delete_all()

            Node(1, 0, 0, 0)
            Node(2, l, 0, 0)

            Material(1, "S235")

            NodalSupport(1, '1', NodalSupportType.HINGED)
            NodalSupport(2, '2', NodalSupportType.ROLLER_IN_X)

            StaticAnalysisSettings(1, 'Linear', StaticAnalysisType.GEOMETRICALLY_LINEAR)

            LoadCase(1, 'DEAD', [True, 0, 0, 1])

            MemberLoad(1, 1, '1', LoadDirectionType.LOAD_DIRECTION_LOCAL_Z, f*1000)

            Section(1, sectionList[i], 1)

            Member(1, 1, 2, 0, 1, 1)

            Calculate_all()

            Model.clientModel.service.finish_modification()

            memberDisp = GetMaxValue(ResultTables.MembersLocalDeformations(), 'displacement_z')

            print("Iteration for length {} and for force {} the section is {}".format(l, f, sectionList[i]))

            if memberDisp<dispLimit:
                SectionFinalList.append(sectionList[i])

            i += 1

            lengthFinalList.append(l)
            forceFinalList.append(f)












