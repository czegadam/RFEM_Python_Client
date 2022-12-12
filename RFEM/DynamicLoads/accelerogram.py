from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes
from RFEM.enums import AccelerogramDefinitionType

class Accelerogram():

    def __init__(self,
                 no: int = 1,
                 name: str = '',
                 constant_period_step: float = None,
                 sort_table: bool = True,
                 user_defined_accelerogram: list = None,
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Args:
            no (int): Accelerogram Tag
            name (str): User Defined Name
            constant_period_step (float): Enables Constant Period Step
            sort_table (bool): Sort Table Option
            user_defined_accelerogram (list): User Defined Accelerogram

                user_defined_accelerogram = [[time, acceleration_x, acceleration_y, acceleration_z], [time, acceleration_x, acceleration_y, acceleration_z], ...]

            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # client model | accelerogram
        clientObject = model.clientModel.factory.create('ns0:accelerogram')

        # clear object atributes | sets all the atributes to none
        clearAttributes(clientObject)

        # accelerogram no.
        clientObject.no = no

        # accelerogram definition type
        clientObject.definition_type = AccelerogramDefinitionType.USER_DEFINED.name

        # user defined name
        if name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # constant period step option
        if constant_period_step:
            clientObject.user_defined_accelerogram_step_enabled = True
            clientObject.user_defined_accelerogram_time_step = constant_period_step

        # sort table option
        clientObject.user_defined_accelerogram_sorted = sort_table

        # user defined accelerogram
        clientObject.user_defined_accelerogram = model.clientModel.factory.create('ns0:accelerogram.user_defined_accelerogram')

        for i,j in enumerate(user_defined_accelerogram):
            acg = model.clientModel.factory.create('ns0:accelerogram_user_defined_accelerogram_row')
            acg.no = i+1
            acg.row.time = user_defined_accelerogram[i][0]
            acg.row.acceleration_x = user_defined_accelerogram[i][1]
            acg.row.acceleration_y = user_defined_accelerogram[i][2]
            acg.row.acceleration_z = user_defined_accelerogram[i][3]

            clientObject.user_defined_accelerogram.accelerogram_user_defined_accelerogram.append(acg)

        # comment
        clientObject.comment = comment

        # adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add global parameter to client model
        model.clientModel.service.set_accelerogram(clientObject)

    @staticmethod
    def FromLibrary(no: int = 1,
                    library_id: int = None,
                    comment: str = '',
                    params: dict = None,
                    model = Model):
        """
        Args:
            no (int): Accelerogram Tag
            library_id (int): Library ID of Accelerogram
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # client model | accelerogram
        clientObject = model.clientModel.factory.create('ns0:accelerogram')

        # clear object atributes | sets all the atributes to none
        clearAttributes(clientObject)

        # accelerogram no.
        clientObject.no = no

        # response spectrum definition type
        clientObject.definition_type = AccelerogramDefinitionType.FROM_LIBRARY.name

        # library id
        clientObject.library_id = library_id

        # comment
        clientObject.comment = comment

        # adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add global parameter to client model
        model.clientModel.service.set_accelerogram(clientObject)
