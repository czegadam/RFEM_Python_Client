import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.enums import AddOn, NodalSupportType, LoadDirectionType
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
from RFEM.initModel import SetAddonStatus
from RFEM.ConcreteDesign.ConcreteUltimateConfigurations import ConcreteUltimateConfiguration

if Model.clientModel is None:
    Model()

def test_concrete_design_uls():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')
    Material(2, 'C30/37')

    Section(1, 'IPE 200', 2)

    Node(1, 0.0, 0.0, 0.0)
    Node(2, 10, 0.0, 0.0)

    Member(1, 1, 2, 0.0, 1, 1,)

    NodalSupport(1, '1', NodalSupportType.FIXED)

    LoadCase(1, 'Self-Weight', [True, 0.0, 0.0, 1.0])

    NodalLoad(1, 1, '2', LoadDirectionType.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W, 1*1000)
    Model.clientModel.service.finish_modification()

    ConcreteUltimateConfiguration(1, 'ULS', '1', 'All', '', '', '1 2')

    uls = Model.clientModel.service.get_concrete_design_sls_configuration(1)

    assert uls.name == 'ULS'
    assert uls.assigned_to_members == 1