#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
baseName = os.path.basename(__file__)
dirName = os.path.dirname(__file__)
print('basename:    ', baseName)
print('dirname:     ', dirName)
sys.path.append(dirName + r'/../..')

from RFEM.enums import NodalSupportType, LoadDirectionType
from RFEM.initModel import Model, Calculate_all
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.section import Section
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.member import Member
from RFEM.TypesForNodes.nodalSupport import NodalSupport
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings
from RFEM.LoadCasesAndCombinations.loadCase import LoadCase
from RFEM.Loads.nodalLoad import NodalLoad
from RFEM.Calculate.meshSettings import GetModelInfo

# Set to True if new model is created, False if modifying an existing model



if __name__ == '__main__':
    isNewModel = True
    modelName = 'TestModel'

    horizontalSpacing = "2+(4s2)*4+2"
    verticalSpacing = "3+3*4+5"

    verSpacing = [2,4,2,4,2,4,2,4,2]
    horSpacing = [3,4,4,4,5]

    # Calculating Node coordinates
    horNodes = [0]
    for n in horSpacing:
        xn = horNodes[-1]+n
        horNodes.append(xn)

    verNodes = [0]
    for m in verSpacing:
        xm = verNodes[-1]+m
        verNodes.append(xm)

    iTot = len(horNodes)
    memberNo = 1
    for j, nodeX in enumerate(verNodes):
        #add code
        for i, nodeZ in enumerate(horNodes)
            #add code
            nodeNo = 1+i+iTot*j
            Node(nodeNo, nodeX, 0.0, nodeZ)
            if nodeNo>1 and memberNo<13:
                Member(memberNo, nodeNo-1, nodeNo, 0.0, 1, 1)
                memberNo +=1

    Model(isNewModel, modelName) # get model
    Model.clientModel.service.begin_modification()

    
    Material(1, 'S235')

    Section(1, 'IPE 200')




Model.clientModel.service.finish_modification()