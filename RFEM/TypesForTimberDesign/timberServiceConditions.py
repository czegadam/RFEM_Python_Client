from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes, ConvertToDlString
from RFEM.enums import TimberServiceConditionsMoistureClass, TimberServiceConditionsTreatmentClass, \
    TimberServiceConditionsTemperatureClass

# For setting timber service conditions according to US  / CAN / GB standards
class TimberServiceConditions():
    def __init__(self,
                no: int = 1,
                name: str = '',
                members: str = '',
                member_sets: str = '',
                surfaces: str = '',
                surface_sets: str = '',
                moisture_service_condition = TimberServiceConditionsMoistureClass.TIMBER_MOISTURE_SERVICE_CONDITION_TYPE_DRY,
                treatment = TimberServiceConditionsTreatmentClass.TREATMENT_TYPE_NONE,
                temperature = TimberServiceConditionsTemperatureClass.TEMPERATURE_TYPE_EQUAL_TO_50,
                member_pressure_treated: (bool) = True,
                comment: str = '',
                params: dict = None):
        """
        Args:
            no (int): Timber Member Shear Panel Tag
            name (str): User Defined Member Shear Panel Name
            members (str): Assigned Members
            member_sets (str): Assigned Member Sets
            surfaces (str): Assigned Surfaces
            surface_sets (str): Assigned Surface Sets
            service_class (enum): Timber Service Conditions Moisture Class
            treatment (enum): Timber service conditions treatment class
            temperature (enum): Timber service conditions temperature class
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
        """

         # Client Model | Types For Timber Design Service Conditions
        clientObject = Model.clientModel.factory.create('ns0:timber_service_class')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member Service Class
        clientObject.no = no

        # Assigned Members
        clientObject.member = ConvertToDlString(members)

        # Assigned Member Sets
        clientObject.member_sets = ConvertToDlString(member_sets)

        # Assigned Surfaces
        clientObject.surfaces = ConvertToDlString(surfaces)

        # Assigned Surface Sets
        clientObject.surface_sets = ConvertToDlString(surface_sets)

        # Moisture Service Condition
        clientObject.moisture_service_condition = moisture_service_condition.name

        # Treatment Service Condition
        if treatment:
            clientObject.treatment = treatment.name

        # Temperature Service Condition
        if temperature:
            clientObject.temperature = temperature.name

        # Setting treatment of timber
        if member_pressure_treated:
            clientObject.member_pressure_treatment = member_pressure_treated

        # User Defined Name
        if name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Service Class to client model
        Model.clientModel.service.set_timber_service_conditions(clientObject)
