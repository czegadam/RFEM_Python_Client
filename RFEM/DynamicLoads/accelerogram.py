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

                        Library ID            Accelerogram
                        ----------           --------------
                            2		Ancona, Italy - station: Genio-Civile
                            3		Ancona, Italy - station: Genio-Civile
                            4		Ancona, Italy - station: Genio-Civile
                            5		Ancona, Italy - station: Genio-Civile
                            6		Ancona, Italy - station: Genio-Civile
                            7		Ancona, Italy - station: Genio-Civile
                            8		Ancona, Italy - station: Genio-Civile
                            9		Ancona, Italy - station: Genio-Civile
                            10		Ancona, Italy - station: Genio-Civile
                            12		Ancona, Italy - station: Vigil del Fuoco
                            13		Umbria, Italy - station: Valfabrica
                            14		Ancona, Italy - station: Genio-Civile
                            15		Ancona, Italy - station: Genio-Civile
                            16		Ancona, Italy - station: Genio-Civile
                            17		Ancona, Italy - station: Genio-Civile
                            18		Ancona, Italy - station: Genio-Civile
                            19		Ancona, Italy - station: Genio-Civile
                            20		Ancona, Italy - station: Genio-Civile
                            21		Ancona, Italy - station: Ancona-Palombina
                            22		Ancona, Italy - station: Ancona-Palombina
                            23		Ancona, Italy - station: Genio-Civile
                            24		Ancona, Italy - station: Genio-Civile
                            25		Ancona, Italy - station: Ancona-Palombina
                            26		Ancona, Italy - station: Genio-Civile
                            27		Ancona, Italy - station: Genio-Civile
                            28		Ancona, Italy - station: Ancona-Palombina
                            30		Ancona, Italy - station: Genio-Civile
                            31		Ancona, Italy - station: Ancona-Rocca
                            32		Ancona, Italy - station: Ancona-Palombina
                            33		Ancona, Italy - station: Genio-Civile
                            34		Ancona, Italy - station: Ancona-Rocca
                            35		Ancona, Italy - station: Ancona-Palombina
                            36		Racha, Georgia - station: Toros
                            37		Ancona, Italy - station: Genio-Civile
                            38		Ancona, Italy - station: Ancona-Palombina
                            39		Ancona, Italy - station: Torre d_Ago
                            40		Ancona, Italy - station: Ancona-Rocca
                            41		Ancona, Italy - station: Genio-Civile
                            42		Ionian, Greece - station: Lefkada-OTE Building
                            43		Ionian, Greece - station: Lefkada-OTE Building
                            44		Aftershock of Racha earthquake, Georgia - station: Stepanavan
                            45		Patras, Greece - station: Patra-OTE Building
                            46		Fruili, Italy - station: Asiago
                            47		Fruili, Italy - station: Barcis
                            48		Fruili, Italy - station: Castelfranco-Veneto
                            49		Fruili, Italy - station: Codroipo
                            50		Fruili, Italy - station: Conegliano-Veneto
                            51		Fruili, Italy - station: Cortina d_Ampezzo
                            52		Fruili, Italy - station: Feltre
                            53		Fruili, Italy - station: Malcesine
                            54		Fruili, Italy - station: Monselice
                            55		Fruili, Italy - station: Tolmezzo-Diga Ambiesta
                            56		Fruili, Italy - station: Tregnago
                            57		Fruili, Italy - station: Ljubljana-Imfin
                            58		Fruili, Italy - station: Ljubljana-Zrmk
                            59		Aftershock of Friuli earthquake, Italy - station: Tolmezzo-Diga Ambiesta
                            60		Aftershock of Friuli earthquake, Italy - station: Tolmezzo-Diga Ambiesta
                            62		Aftershock of Friuli earthquake, Italy - station: Forgaria-Cornio
                            63		Aftershock of Friuli earthquake, Italy - station: Maiano-Municipio
                            65		Aftershock of Friuli earthquake, Italy - station: Forgaria-Cornio
                            66		Aftershock of Friuli earthquake, Italy - station: Maiano-Municipio
                            67		Aftershock of Friuli earthquake, Italy - station: Forgaria-Cornio
                            68		Aftershock of Friuli earthquake, Italy - station: Maiano-Municipio
                            69		Aftershock of Friuli earthquake, Italy - station: Tarcento
                            70		Aftershock of Friuli earthquake, Italy - station: Forgaria-Cornio
                            71		Aftershock of Friuli earthquake, Italy - station: Tarcento
                            73		Gazli, Uzbekistan - station: Gazli
                            74		Aftershock of Friuli earthquake, Italy - station: Forgaria-Cornio
                            75		Aftershock of Friuli earthquake, Italy - station: San Rocco
                            76		Aftershock of Friuli earthquake, Italy - station: Forgaria-Cornio
                            77		Aftershock of Friuli earthquake, Italy - station: Tolmezzo-Diga Ambiesta
                            78		Aftershock of Friuli earthquake, Italy - station: Forgaria-Cornio
                            79		Aftershock of Friuli earthquake, Italy - station: Forgaria-Cornio
                            80		Aftershock of Friuli earthquake, Italy - station: Tolmezzo-Diga Ambiesta
                            81		Aftershock of Friuli earthquake, Italy - station: Forgaria-Cornio
                            82		Aftershock of Friuli earthquake, Italy - station: Maiano-Piano Terra
                            83		Aftershock of Friuli earthquake, Italy - station: Maiano-Piano Terra
                            84		Aftershock of Friuli earthquake, Italy - station: San Rocco
                            85		Aftershock of Friuli earthquake, Italy - station: Maiano-Piano Terra
                            86		Aftershock of Friuli earthquake, Italy - station: Maiano-Prato
                            87		Aftershock of Friuli earthquake, Italy - station: Tarcento
                            88		Denizli, Turkey - station: Denizli-Bayindirlik ve Iskan Mudurlugu
                            89		Aftershock of Friuli earthquake, Italy - station: Salsominore
                            90		Aftershock of Friuli earthquake, Italy - station: Forgaria-Cornio
                            91		Aftershock of Friuli earthquake, Italy - station: Buia
                            92		Aftershock of Friuli earthquake, Italy - station: Forgaria-Cornio
                            93		Aftershock of Friuli earthquake, Italy - station: Tolmezzo-Diga Ambiesta
                            94		Aftershock of Friuli earthquake, Italy - station: Maiano-Piano Terra
                            95		Aftershock of Friuli earthquake, Italy - station: Forgaria-Cornio
                            96		Aftershock of Friuli earthquake, Italy - station: Forgaria-Cornio
                            97		Aftershock of Friuli earthquake, Italy - station: Tolmezzo-Diga Ambiesta
                            98		Aftershock of Friuli earthquake, Italy - station: Maiano-Piano Terra
                            99		Aftershock of Friuli earthquake, Italy - station: Maiano-Prato
                            100		Aftershock of Friuli earthquake, Italy - station: San Rocco
                            101		Aftershock of Friuli earthquake, Italy - station: Forgaria-Cornio
                            102		Aftershock of Friuli earthquake, Italy - station: Tolmezzo-Diga Ambiesta
                            103		Aftershock of Friuli earthquake, Italy - station: Maiano-Prato
                            104		Aftershock of Friuli earthquake, Italy - station: Maiano-Piano Terra
                            105		Aftershock of Friuli earthquake, Italy - station: Tolmezzo-Diga Ambiesta
                            106		Aftershock of Friuli earthquake, Italy - station: Maiano-Piano Terra
                            107		Aftershock of Friuli earthquake, Italy - station: Maiano-Prato
                            108		Aftershock of Friuli earthquake, Italy - station: Tarcento
                            109		Aftershock of Friuli earthquake, Italy - station: Forgaria-Cornio
                            110		Aftershock of Friuli earthquake, Italy - station: Maiano-Prato
                            111		Aftershock of Friuli earthquake, Italy - station: Maiano-Piano Terra
                            112		Aftershock of Friuli earthquake, Italy - station: Kobarid-Osn.Skola
                            113		Aftershock of Friuli earthquake, Italy - station: Breginj-Fabrika IGLI
                            114		Aftershock of Friuli earthquake, Italy - station: Forgaria-Cornio
                            115		Aftershock of Friuli earthquake, Italy - station: San Rocco
                            116		Aftershock of Friuli earthquake, Italy - station: Buia
                            117		Aftershock of Friuli earthquake, Italy - station: Kobarid-Osn.Skola
                            120		Aftershock of Friuli earthquake, Italy - station: San Rocco
                            121		Aftershock of Friuli earthquake, Italy - station: Tregnago
                            122		Aftershock of Friuli earthquake, Italy - station: Buia
                            123		Aftershock of Friuli earthquake, Italy - station: Forgaria-Cornio
                            124		Aftershock of Friuli earthquake, Italy - station: Buia
                            125		Aftershock of Friuli earthquake, Italy - station: Forgaria-Cornio
                            126		Aftershock of Friuli earthquake, Italy - station: Breginj-Fabrika IGLI
                            127		Aftershock of Friuli earthquake, Italy - station: Kobarid-Osn.Skola
                            128		Aftershock of Friuli earthquake, Italy - station: Robic
                            129		Aftershock of Friuli earthquake, Italy - station: Codroipo
                            130		Aftershock of Friuli earthquake, Italy - station: Conegliano-Veneto
                            131		Aftershock of Friuli earthquake, Italy - station: San Rocco
                            132		Aftershock of Friuli earthquake, Italy - station: Tregnago
                            133		Aftershock of Friuli earthquake, Italy - station: Buia
                            134		Aftershock of Friuli earthquake, Italy - station: Forgaria-Cornio
                            135		Aftershock of Friuli earthquake, Italy - station: Breginj-Fabrika IGLI
                            136		Aftershock of Friuli earthquake, Italy - station: Forgaria-Cornio
                            137		Aftershock of Friuli earthquake, Italy - station: Buia
                            138		Aftershock of Friuli earthquake, Italy - station: Kobarid-Osn.Skola
                            139		Aftershock of Friuli earthquake, Italy - station: Breginj-Fabrika IGLI
                            140		Aftershock of Friuli earthquake, Italy - station: Robic
                            141		Aftershock of Friuli earthquake, Italy - station: Barcis
                            142		Aftershock of Friuli earthquake, Italy - station: Codroipo
                            143		Aftershock of Friuli earthquake, Italy - station: Conegliano-Veneto
                            144		Aftershock of Friuli earthquake, Italy - station: Cortina d_Ampezzo
                            145		Aftershock of Friuli earthquake, Italy - station: Feltre
                            146		Aftershock of Friuli earthquake, Italy - station: Forgaria-Cornio
                            147		Aftershock of Friuli earthquake, Italy - station: San Rocco
                            148		Aftershock of Friuli earthquake, Italy - station: Malcesine
                            149		Aftershock of Friuli earthquake, Italy - station: Tarcento
                            150		Aftershock of Friuli earthquake, Italy - station: Tregnago
                            151		Aftershock of Friuli earthquake, Italy - station: Buia
                            152		Aftershock of Friuli earthquake, Italy - station: Forgaria-Cornio
                            153		Caldiran, Turkey - station: Maku
                            154		Albstadt, Swabian Jura, Germany - station: Jungingen
                            155		Bucharest, Romania - station: Bucharest-Building Research Institute
                            156		Ionian, Greece - station: Argostoli-OTE Building
                            157		Castello, Italy - station: Citta di Castello
                            158		Aftershock of Racha earthquake, Georgia - station: Bavra
                            159		Friuli, Italy - station: Forgaria-Cornio
                            160		Friuli, Italy - station: San Rocco
                            161		Izmir, Turkey - station: Izmir-Bayindirlik ve Iskan Mudurlugu
                            162		Izmir, Turkey - station: Izmir-Bayindirlik ve Iskan Mudurlugu
                            163		Amfissa, Greece - station: Patra-OTE Building
                            164		Albstadt, Swabian Jura, Germany - station: Jungingen
                            165		Albstadt, Swabian Jura, Germany - station: Jungingen
                            166		Albstadt, Swabian Jura, Germany - station: Jungingen
                            167		Albstadt, Swabian Jura, Germany - station: Jungingen
                            168		Calabria, Italy - station: Pellaro
                            169		Calabria, Italy - station: Ferruzzano
                            170		Volvi, Greece - station: Thessaloniki-City Hotel
                            171		Racha, Georgia - station: Bavra
                            172		Basso Tirreno, Italy - station: Patti-Cabina Prima
                            173		Basso Tirreno, Italy - station: Naso
                            174		Basso Tirreno, Italy - station: Messina 1
                            175		Basso Tirreno, Italy - station: Milazzo
                            176		Achaia, Greece - station: Patra-OTE Building
                            177		Thessalonika, Greece - station: Thessaloniki-City Hotel
                            178		Albstadt, Swabian Jura, Germany - station: Jungingen
                            179		Aftershock of Kocaeli earthquake, Turkey - station: Adapazari-3
                            180		Aftershock of Kocaeli earthquake, Turkey - station: Hendek
                            181		Tabas, Iran - station: Boshroyeh
                            182		Tabas, Iran - station: Dayhook
                            183		Tabas, Iran - station: Ferdoos
                            184		Tabas, Iran - station: Kashmar
                            185		Tabas, Iran - station: Khezri
                            186		Tabas, Iran - station: Sedeh
                            187		Tabas, Iran - station: Tabas
                            188		Albstadt, Swabian Jura, Germany - station: Jungingen
                            189		Aftershock of Kocaeli earthquake, Turkey - station: Duzce-Meteoroloji Mudurlugu
                            190		Aftershock of Kocaeli earthquake, Turkey - station: Akyazi
                            191		Montenegro, Montenegro - station: Petrovac-Hotel Oliva
                            192		Montenegro, Montenegro - station: Ulcinj-Hotel Olimpic
                            193		Montenegro, Montenegro - station: Ulcinj-Hotel Albatros
                            194		Muradiye, Turkey - station: Muradiye-Meteoroloji Mudurlugu
                            195		Montenegro, Montenegro - station: Titograd-Seismoloska Stanica
                            196		Montenegro, Montenegro - station: Petrovac-Hotel Oliva
                            197		Montenegro, Montenegro - station: Ulcinj-Hotel Olimpic
                            198		Montenegro, Montenegro - station: Ulcinj-Hotel Albatros
                            199		Montenegro, Montenegro - station: Bar-Skupstina Opstine
                            200		Montenegro, Montenegro - station: Herceg Novi-O.S. D. Pavicic
                            201		Montenegro, Croatia - station: Dubrovnik-Pomorska Skola
                            202		Montenegro, Montenegro - station: Titograd-Geoloski Zavod
                            203		Montenegro, Bosnia and Herzegovina - station: Gacko-Zemlj. Zadruga
                            204		Montenegro, Macedonia - station: Debar-Skupstina Opstine
                            205		Aftershock of Montenegro earthquake, Montenegro - station: Ulcinj-Hotel Olimpic
                            206		Aftershock of Montenegro earthquake, Montenegro - station: Petrovac-Hotel Oliva
                            207		Aftershock of Montenegro earthquake, Montenegro - station: Bar-Skupstina Opstine
                            208		Aftershock of Montenegro earthquake, Montenegro - station: Ulcinj-Hotel Olimpic
                            209		Aftershock of Montenegro earthquake, Montenegro - station: Petrovac-Hotel Oliva
                            210		Aftershock of Montenegro earthquake, Montenegro - station: Ulcinj-Hotel Olimpic
                            211		Aftershock of Montenegro earthquake, Montenegro - station: Bar-Skupstina Opstine
                            212		Aftershock of Montenegro earthquake, Montenegro - station: Herceg Novi-O.S. D. Pavicic
                            213		Aftershock of Montenegro earthquake, Montenegro - station: Ulcinj-Hotel Olimpic
                            214		Aftershock of Montenegro earthquake, Montenegro - station: Ulcinj-Hotel Olimpic
                            215		Aftershock of Montenegro earthquake, Montenegro - station: Bar-Skupstina Opstine
                            216		Aftershock of Montenegro earthquake, Montenegro - station: Ulcinj-Hotel Albatros
                            217		Aftershock of Montenegro earthquake, Montenegro - station: Herceg Novi-O.S. D. Pavicic
                            218		Aftershock of Montenegro earthquake, Montenegro - station: Budva-PTT
                            219		Aftershock of Montenegro earthquake, Montenegro - station: Budva-PTT
                            220		Aftershock of Montenegro earthquake, Montenegro - station: Budva-PTT
                            221		Aftershock of Montenegro earthquake, Montenegro - station: Kotor-Zovod za Biologiju Mora
                            222		Aftershock of Montenegro earthquake, Montenegro - station: Ulcinj-Hotel Olimpic
                            223		Aftershock of Montenegro earthquake, Montenegro - station: Ulcinj-Hotel Albatros
                            224		Marche, Italy - station: Nocera Umbra
                            225		Marche, Italy - station: Nocera Umbra
                            226		Marche, Italy - station: Nocera Umbra
                            227		Aftershock of Montenegro earthquake, Montenegro - station: Ulcinj-Hotel Olimpic
                            228		Aftershock of Montenegro earthquake, Montenegro - station: Bar-Skupstina Opstine
                            229		Aftershock of Montenegro earthquake, Montenegro - station: Petrovac-Hotel Rivijera
                            230		Aftershock of Montenegro earthquake, Montenegro - station: Budva-PTT
                            231		Aftershock of Montenegro earthquake, Montenegro - station: Tivat-Aerodrom
                            232		Aftershock of Montenegro earthquake, Montenegro - station: Kotor Nas Rakit
                            233		Aftershock of Montenegro earthquake, Montenegro - station: Kotor-Zovod za Biologiju Mora
                            234		Aftershock of Montenegro earthquake, Montenegro - station: Herceg Novi-O.S. D. Pavicic
                            235		Aftershock of Kocaeli earthquake, Turkey - station: Golyaka
                            236		Buchak, Turkey - station: Bucak-Kandilli Gozlem Istasyonu
                            237		Aftershock of Montenegro earthquake, Montenegro - station: Ulcinj-Hotel Olimpic
                            238		Rigali, Italy - station: Nocera Umbra
                            239		Dursunbey, Turkey - station: Dursunbey-Kandilli Gozlem Istasyonu
                            240		Aftershock of Montenegro earthquake, Montenegro - station: Ulcinj-Hotel Olimpic
                            241		Friuli, Italy - station: Maiano-Municipio
                            242		Valnerina, Italy - station: Cascia
                            243		Valnerina, Italy - station: San Vittorino
                            244		Valnerina, Italy - station: Bevagna
                            245		Valnerina, Italy - station: Nocera Umbra
                            246		Valnerina, Italy - station: Arquata del Tronto
                            247		Valnerina, Italy - station: Spoleto
                            249		Umbria, Italy - station: Cascia-Cabina Petrucci
                            250		Umbria, Italy - station: Norcia
                            251		Umbria, Italy - station: Cascia-Cabina Petrucci
                            252		Umbria, Italy - station: Norcia
                            253		Umbria, Italy - station: Norcia
                            254		Umbria, Italy - station: Norcia
                            255		Umbria, Italy - station: Norcia
                            256		Vrancea, Romania - station: Cernavoda
                            257		Albstadt, Swabian Jura, Germany - station: Jungingen
                            258		Toscana, Italy - station: Vagli-Paese
                            259		Toscana, Italy - station: Barga
                            260		El Asnam, Algeria - station: El Safsaf
                            261		El Asnam, Algeria - station: Beni Rashid
                            262		El Asnam, Algeria - station: El Safsaf
                            263		El Asnam, Algeria - station: El Safsaf
                            264		El Asnam, Algeria - station: El Safsaf
                            265		El Asnam, Algeria - station: El Safsaf
                            266		El Asnam, Algeria - station: El Safsaf
                            267		El Asnam, Algeria - station: Beni Rashid
                            268		El Asnam, Algeria - station: El Safsaf
                            269		El Asnam, Algeria - station: Beni Rashid
                            270		El Asnam, Algeria - station: El Safsaf
                            271		El Asnam, Algeria - station: Beni Rashid
                            272		El Asnam, Algeria - station: El Safsaf
                            273		El Asnam, Algeria - station: Beni Rashid
                            274		El Asnam, Algeria - station: El Safsaf
                            275		El Asnam, Algeria - station: Beni Rashid
                            276		Vrancea, Romania - station: Istrita
                            277		El Asnam, Algeria - station: El Safsaf
                            278		El Asnam, Algeria - station: El Safsaf
                            279		El Asnam, Algeria - station: El Safsaf
                            280		El Asnam, Algeria - station: Beni Rashid
                            281		El Asnam, Algeria - station: Beni Rashid
                            282		Vrancea, Romania - station: Birlad
                            283		Vrancea, Romania - station: Birlad
                            284		Vrancea, Romania - station: Cernavoda
                            285		El Asnam, Algeria - station: Beni Rashid
                            286		Campano Lucano, Italy - station: Arienzo
                            287		Campano Lucano, Italy - station: Bagnoli-Irpino
                            288		Campano Lucano, Italy - station: Brienza
                            289		Campano Lucano, Italy - station: Mercato San Severino
                            290		Campano Lucano, Italy - station: Sturno
                            291		Campano Lucano, Italy - station: Calitri
                            292		Campano Lucano, Italy - station: Auletta
                            293		Campano Lucano, Italy - station: Rionero in Vulture
                            294		Campano Lucano, Italy - station: Bisaccia
                            295		Campano Lucano, Italy - station: Benevento
                            296		Campano Lucano, Italy - station: Torre del Greco
                            297		Campano Lucano, Italy - station: Tricarico
                            298		Campano Lucano, Italy - station: Garigliano-Centrale Nucleare 1
                            299		Campano Lucano, Italy - station: Bovino
                            300		Campano Lucano, Italy - station: San Severo
                            301		Campano Lucano, Italy - station: Vieste
                            302		Campano Lucano, Italy - station: Lauria
                            303		Campano Lucano, Italy - station: Roccamonfina
                            304		Campano Lucano, Italy - station: San Giorgio la Molara
                            305		Aftershock of Campano Lucano earthquake, Italy - station: Calitri-Cabina Pittoli
                            306		El Asnam, Algeria - station: Beni Rashid
                            307		Aftershock of Campano Lucano earthquake, Italy - station: Procisa Nuova
                            308		Aftershock of Campano Lucano earthquake, Italy - station: Selva Piana-Morra
                            309		Aftershock of Campano Lucano earthquake, Italy - station: Selva Piana-Morra
                            310		Aftershock of Campano Lucano earthquake, Italy - station: Procisa Nuova
                            311		Aftershock of Campano Lucano earthquake, Italy - station: Selva Piana-Morra
                            312		Aftershock of Campano Lucano earthquake, Italy - station: Oppido-Balzata
                            313		Aftershock of Campano Lucano earthquake, Italy - station: Procisa Nuova
                            314		Aftershock of Campano Lucano earthquake, Italy - station: Conza-Base
                            315		Aftershock of Campano Lucano earthquake, Italy - station: Calitri-Cabina Pittoli
                            317		Aftershock of Campano Lucano earthquake, Italy - station: Conza-Vetta
                            318		Aftershock of Campano Lucano earthquake, Italy - station: Cairano 1
                            319		Aftershock of Campano Lucano earthquake, Italy - station: Cairano 3
                            320		Aftershock of Campano Lucano earthquake, Italy - station: Cairano 4
                            321		Aftershock of Campano Lucano earthquake, Italy - station: Lioni-Macello
                            322		Aftershock of Campano Lucano earthquake, Italy - station: Procisa Nuova
                            323		Aftershock of Campano Lucano earthquake, Italy - station: Conza-Base
                            324		Aftershock of Campano Lucano earthquake, Italy - station: Cairano 2
                            325		Aftershock of Campano Lucano earthquake, Italy - station: Conza-Vetta
                            327		Aftershock of Campano Lucano earthquake, Italy - station: Cairano 4
                            328		Aftershock of Campano Lucano earthquake, Italy - station: Cairano 2
                            329		Aftershock of Campano Lucano earthquake, Italy - station: Cairano 3
                            330		Aftershock of Campano Lucano earthquake, Italy - station: Selva Piana-Morra
                            331		Aftershock of Campano Lucano earthquake, Italy - station: Torre del Greco
                            332		Aftershock of Campano Lucano earthquake, Italy - station: Arienzo
                            333		Alkion, Greece - station: Korinthos-OTE Building
                            334		Alkion, Greece - station: Xilokastro-OTE Building
                            335		Alkion, Greece - station: Korinthos-OTE Building
                            336		Preveza, Greece - station: Preveza-OTE Building
                            337		Preveza, Greece - station: Lefkada-OTE Building
                            338		Paliambela, Greece - station: Lefkada-OTE Building
                            339		Panagoula, Greece - station: Lefkada-OTE Building
                            340		Lefkas, Greece - station: Lefkada-OTE Building
                            341		Bay of Iskenderum, Turkey - station: Antakya-Hatay Bayindirlik Mudurlugu
                            342		Cazulas, Spain - station: Presa de Beznar 504
                            343		Urmiya, Iran - station: Orumieh 1
                            344		Ionian, Greece - station: Lefkada-Hospital
                            345		Ionian, Greece - station: Agrinio-Town Hall
                            346		Etolia, Greece - station: Lefkada-Hospital
                            347		Heraklio, Greece - station: Heraklio-Prefecture
                            348		Etolia, Greece - station: Lefkada-Hospital
                            349		Ionian, Greece - station: Lefkada-Hospital
                            350		Biga, Turkey - station: Edincik-Kandilli Gozlem Istasyonu
                            351		Biga, Turkey - station: Edremit-Meteoroloji Istasyonu
                            352		Biga, Turkey - station: Gonen-Meteoroloji Mudurlugu
                            353		Biga, Turkey - station: Balikesir-Bayindirlik ve Iskan Mudurlugu
                            354		Kars, Turkey - station: Horasan-Meteoroloji Mudurlugu
                            355		Heraklio, Greece - station: Heraklio-Prefecture
                            356		Balikesir, Turkey - station: Balikesir-Bayindirlik ve Iskan Mudurlugu
                            357		Aftershock of Racha earthquake, Georgia - station: Spitak-Karadzor
                            358		Umbria, Italy - station: Peglio
                            359		Umbria, Italy - station: Gubbio
                            360		Umbria, Italy - station: Citta di Castello-Regnano
                            361		Umbria, Italy - station: Nocera Umbra
                            362		Umbria, Italy - station: Umbertide
                            363		Umbria, Italy - station: Pietralunga
                            364		Lazio Abruzzo, Italy - station: Bussi
                            365		Lazio Abruzzo, Italy - station: Atina
                            366		Lazio Abruzzo, Italy - station: San Agapito
                            367		Lazio Abruzzo, Italy - station: Castelnuovo
                            368		Lazio Abruzzo, Italy - station: Ponte Corvo
                            369		Lazio Abruzzo, Italy - station: Roccamonfina
                            370		Lazio Abruzzo, Italy - station: Poggio-Picenze
                            371		Lazio Abruzzo, Italy - station: Barisciano
                            372		Lazio Abruzzo, Italy - station: Scafa
                            373		Lazio Abruzzo, Italy - station: Ortucchio
                            374		Lazio Abruzzo, Italy - station: Garigliano-Centrale Nucleare 1
                            375		Lazio Abruzzo, Italy - station: Garigliano-Centrale Nucleare 2
                            376		Racha, Georgia - station: Leninakan-SDR Station
                            377		Lazio Abruzzo, Italy - station: Taranta Peligna
                            378		Lazio Abruzzo, Italy - station: Cassino-Sant_ Elia
                            379		Aftershock of Lazio Abruzzo earthquake, Italy - station: Taranta Peligna
                            380		Aftershock of Lazio Abruzzo earthquake, Italy - station: Scafa
                            381		Aftershock of Lazio Abruzzo earthquake, Italy - station: San Agapito
                            382		Aftershock of Lazio Abruzzo earthquake, Italy - station: Atina
                            383		Aftershock of Lazio Abruzzo earthquake, Italy - station: Pescasseroli
                            384		Aftershock of Lazio Abruzzo earthquake, Italy - station: Villetta-Barrea
                            385		Aftershock of Lazio Abruzzo earthquake, Italy - station: Atina-Pretura Piano Terra
                            386		Aftershock of Lazio Abruzzo earthquake, Italy - station: Cassino-Sant_ Elia
                            387		Aftershock of Lazio Abruzzo earthquake, Italy - station: Pescasseroli
                            388		Aftershock of Lazio Abruzzo earthquake, Italy - station: Villetta-Barrea
                            389		Aftershock of Lazio Abruzzo earthquake, Italy - station: Pescasseroli
                            390		Aftershock of Lazio Abruzzo earthquake, Italy - station: Villetta-Barrea
                            391		Aftershock of Lazio Abruzzo earthquake, Italy - station: Atina-Pretura Esterno
                            392		Aftershock of Lazio Abruzzo earthquake, Italy - station: Atina-Pretura Piano Terra
                            393		Aftershock of Lazio Abruzzo earthquake, Italy - station: Scafa
                            394		Aftershock of Lazio Abruzzo earthquake, Italy - station: Pescasseroli
                            395		Aftershock of Lazio Abruzzo earthquake, Italy - station: Villetta-Barrea
                            396		Aftershock of Lazio Abruzzo earthquake, Italy - station: Atina-Pretura Piano Terra
                            397		Aftershock of Lazio Abruzzo earthquake, Italy - station: Pescasseroli
                            398		Aftershock of Lazio Abruzzo earthquake, Italy - station: Villetta-Barrea
                            399		Aftershock of Lazio Abruzzo earthquake, Italy - station: Atina-Pretura Esterno
                            400		Aftershock of Lazio Abruzzo earthquake, Italy - station: Pescasseroli
                            401		Aftershock of Lazio Abruzzo earthquake, Italy - station: Villetta-Barrea
                            402		Aftershock of Lazio Abruzzo earthquake, Italy - station: Atina-Pretura Piano Terra
                            403		Izmir, Turkey - station: Foca-Gumruk Mudurlugu
                            404		Aftershock of North Wales earthquake, United Kingdom - station: Trawsfynydd
                            405		Gulf of Corinth, Greece - station: Xilokastro-OTE Building
                            406		Elis, Greece - station: Amaliada-OTE Building
                            407		near coast of Preveza, Greece - station: Preveza-OTE Building
                            408		near coast of Preveza, Greece - station: Lefkada-Hospital
                            409		Mugla, Turkey - station: Koycegiz-Meteorological Station
                            410		Golbasi, Turkey - station: Golbasi-Devlet Hastanesi
                            411		Kusadasi, Turkey - station: Kusadasi-Meteoroloji Mudurlugu
                            412		Golbasi, Turkey - station: Golbasi-Devlet Hastanesi
                            413		Kalamata, Greece - station: Kalamata-Prefecture
                            414		Kalamata, Greece - station: Kalamata-OTE Building
                            415		Kalamata, Greece - station: Kalamata-Prefecture
                            416		Kalamata, Greece - station: Kalamata-Prefecture
                            417		Kalamata, Greece - station: Kalamata-Prefecture
                            418		Kalamata, Greece - station: Kalamata-Prefecture
                            419		Kalamata, Greece - station: Kalamata-Prefecture
                            420		Kalamata, Greece - station: Kalamata-OTE Building
                            421		Athens, Greece - station: Athens-Sepolia (Garage)
                            422		Kalamata, Greece - station: Kalamata-Prefecture
                            423		Tsipiana, Greece - station: Amaliada-OTE Building
                            424		Kounina, Greece - station: Aigio-OTE Building
                            425		Athens, Greece - station: Athens-Sepolia (Metro Station)
                            426		Dodecanese, Greece - station: Rodos-OTE Building
                            427		Ionian, Greece - station: Lefkada-OTE Building
                            428		Etolia, Greece - station: Valsamata-Seismograph Station
                            429		Etolia, Greece - station: Valsamata-Seismograph Station
                            430		Gulf of Corinth, Greece - station: Korinthos-OTE Building
                            431		Izmir, Turkey - station: Foca-Gumruk Mudurlugu
                            432		Ionian, Greece - station: Amaliada-OTE Building
                            433		Ionian, Greece - station: Amaliada-OTE Building
                            434		Ionian, Greece - station: Amaliada-OTE Building
                            435		Killini, Greece - station: Amaliada-OTE Building
                            436		Killini, Greece - station: Zakinthos-OTE Building
                            437		Athens, Greece - station: Athens-Syntagma (3rd lower level)
                            438		Killini, Greece - station: Vartolomio-I.Th. Residence
                            439		Spitak, Armenia - station: Gukasian
                            440		Aftershock of Spitak earthquake, Armenia - station: Gukasian
                            441		Ionian, Greece - station: Amaliada-OTE Building
                            442		Aftershock of Spitak earthquake, Armenia - station: Dzhrashen
                            443		Aftershock of Spitak earthquake, Armenia - station: Nalband
                            444		Aftershock of Spitak earthquake, Armenia - station: Stepanavan
                            445		Aftershock of Spitak earthquake, Armenia - station: Toros
                            446		Patras, Greece - station: Nafpaktos-OTE Building
                            447		Patras, Greece - station: Patra-OTE Building
                            448		Aftershock of Spitak earthquake, Armenia - station: Leninakan
                            449		Aftershock of Spitak earthquake, Armenia - station: Nalband
                            450		Aftershock of Spitak earthquake, Armenia - station: Stepanavan
                            451		Aftershock of Spitak earthquake, Armenia - station: Toros
                            452		Aftershock of Spitak earthquake, Armenia - station: Dzhrashen
                            453		Aftershock of Spitak earthquake, Armenia - station: Leninakan
                            454		Aftershock of Spitak earthquake, Armenia - station: Metz-Parni
                            455		Aftershock of Spitak earthquake, Armenia - station: Nalband
                            456		Aftershock of Spitak earthquake, Armenia - station: Stepanavan
                            457		Aftershock of Spitak earthquake, Armenia - station: Toros
                            458		Aftershock of Spitak earthquake, Armenia - station: Metz-Parni
                            459		Aftershock of Spitak earthquake, Armenia - station: Nalband
                            460		Aftershock of Spitak earthquake, Armenia - station: Stepanavan
                            461		Aftershock of Spitak earthquake, Armenia - station: Toros
                            462		Aftershock of Spitak earthquake, Armenia - station: Dzhrashen
                            463		Aftershock of Spitak earthquake, Armenia - station: Metz-Parni
                            464		Aftershock of Spitak earthquake, Armenia - station: Nalband
                            465		Aftershock of Spitak earthquake, Armenia - station: Toros
                            466		Patras, Greece - station: Patra-OTE Building
                            467		Athens, Greece - station: Athens-Papagos
                            468		near S coast of Crete, Greece - station: Rethimno-OTE Building
                            469		Aigion, Greece - station: Aigio-OTE Building
                            470		Athens, Greece - station: Athens-Sygrou-Fix
                            471		Vrancea, Romania - station: Vrancioaia
                            472		Vrancea, Romania - station: Bucharest-Building Research Institute
                            473		Vrancea, Romania - station: Vrancioaia
                            474		Purnari, Greece - station: Preveza-OTE Building
                            475		Manjil, Iran - station: Abhar
                            476		Manjil, Iran - station: Qazvin
                            477		Manjil, Iran - station: Tehran-Sarif University
                            478		Athens, Greece - station: Athens-Neo Psihiko
                            479		Manjil, Iran - station: Rudsar
                            480		Manjil, Iran - station: Tonekabun
                            481		Manjil, Iran - station: Gachsar
                            482		Duzce, Turkey - station: Mudurnu-Kaymakamlik Binasi
                            483		Spitak, Armenia - station: Spitak-Karadzor
                            484		Plati, Greece - station: Kalamata-Prefecture
                            485		Plati, Greece - station: Sparti-OTE Building
                            486		Spitak, Armenia - station: Spitak-Karadzor
                            487		Javakheti Highland, Armenia - station: Akhalkalaki
                            488		Javakheti Highland, Armenia - station: Bogdanovka
                            489		Javakheti Highland, Armenia - station: Bakuriani
                            490		Javakheti Highland, Armenia - station: Bavra
                            491		Javakheti Highland, Armenia - station: Vanadzor
                            492		Javakheti Highland, Armenia - station: Leninakan-SDR Station
                            493		Javakheti Highland, Armenia - station: Spitak-Karadzor
                            494		Javakheti Highland, Armenia - station: Stepanavan
                            495		Javakheti Highland, Armenia - station: Toros
                            496		Javakheti Highland, Armenia - station: Bavra
                            497		Javakheti Highland, Georgia - station: Stepanavan
                            498		Spitak, Armenia - station: Spitak-Karadzor
                            499		Racha, Georgia - station: Akhalkalaki
                            500		Racha, Georgia - station: Bogdanovka
                            501		Aftershock of Racha earthquake, Georgia - station: Ambrolauri
                            502		Aftershock of Racha earthquake, Georgia - station: Iri
                            503		Aftershock of Racha earthquake, Georgia - station: Oni-Base Camp
                            504		Aftershock of Racha earthquake, Georgia - station: Oni
                            505		Aftershock of Racha earthquake, Georgia - station: Ambrolauri
                            506		Aftershock of Racha earthquake, Georgia - station: Iri
                            507		Aftershock of Racha earthquake, Georgia - station: Oni-Base Camp
                            508		Aftershock of Racha earthquake, Georgia - station: Oni
                            509		Aftershock of Racha earthquake, Georgia - station: Sackhere
                            510		Aftershock of Racha earthquake, Georgia - station: Ambrolauri
                            511		Aftershock of Racha earthquake, Georgia - station: Zemo Bari
                            512		Aftershock of Racha earthquake, Georgia - station: Sackhere
                            513		Aftershock of Racha earthquake, Georgia - station: Ambrolauri
                            514		Aftershock of Racha earthquake, Georgia - station: Iri
                            515		Aftershock of Racha earthquake, Georgia - station: Oni-Base Camp
                            516		Aftershock of Racha earthquake, Georgia - station: Zemo Bari
                            517		Aftershock of Racha earthquake, Georgia - station: Iri
                            518		Aftershock of Racha earthquake, Georgia - station: Oni
                            519		Aftershock of Racha earthquake, Georgia - station: Zemo Bari
                            520		Aftershock of Racha earthquake, Georgia - station: Ambrolauri
                            521		Aftershock of Racha earthquake, Georgia - station: Iri
                            522		Aftershock of Racha earthquake, Georgia - station: Oni-Base Camp
                            523		Aftershock of Racha earthquake, Georgia - station: Oni
                            524		Aftershock of Racha earthquake, Georgia - station: Zemo Bari
                            525		Gulf of Messiniakos, Greece - station: Kalamata-Prefecture
                            526		Aftershock of Racha earthquake, Georgia - station: Oni-Base Camp
                            527		Aftershock of Racha earthquake, Georgia - station: Oni
                            528		Aftershock of Racha earthquake, Georgia - station: Zemo Bari
                            529		Aftershock of Racha earthquake, Georgia - station: Ambrolauri
                            530		Aftershock of Racha earthquake, Georgia - station: Iri
                            531		Aftershock of Racha earthquake, Georgia - station: Oni-Base Camp
                            532		Aftershock of Racha earthquake, Georgia - station: Oni
                            533		Aftershock of Racha earthquake, Georgia - station: Zemo Bari
                            534		near S coast of Crete, Greece - station: Rethimno-OTE Building
                            535		Erzincan, Turkey - station: Erzincan-Meteorologij Mudurlugu
                            536		Erzincan, Turkey - station: Tercan-Meteoroji Mudurlugu
                            537		Erzincan, Turkey - station: Refahiye-Kaymakamlik Binasi
                            538		Pulumur, Turkey - station: Erzincan-Meteorologij Mudurlugu
                            539		Aftershock of Grande Dixence quake, Switzerland - station: Grande Dixence-SDIF
                            540		Duzce, Turkey - station: Denizli-Bayindirlik ve Iskan Mudurlugu
                            541		Duzce, Turkey - station: Duzce-Meteoroloji Mudurlugu
                            542		Duzce, Turkey - station: Goynuk-Devlet Hastanesi
                            543		Duzce, Turkey - station: Iznik-Karayollari Sefligi Muracaati
                            544		Duzce, Turkey - station: Izmit-Meteoroloji Istasyonu
                            545		Mataranga, Greece - station: Amaliada-OTE Building
                            546		Mataranga, Greece - station: Patra-OTE Building
                            547		Izmir, Turkey - station: Cesme-Meteorological Station
                            548		Izmir, Turkey - station: Izmir-Bayindirlik ve Iskan Mudurlugu
                            549		Izmir, Turkey - station: Kusadasi-Meteoroloji Mudurlugu
                            550		Gulf of Corinth, Greece - station: Aigio-OTE Building
                            551		Gulf of Corinth, Greece - station: Mornos Dam-Damfoot
                            552		Gulf of Patras, Greece - station: Nafpaktos-OTE Building
                            553		Gulf of Corinth, Greece - station: Xilokastro-OTE Building
                            554		near coast of Filiatra, Greece - station: Kyparrisia-OTE Building
                            555		Kallithea, Greece - station: Patra-OTE Building
                            556		Pyrgos, Greece - station: Amaliada-OTE Building
                            557		Pyrgos, Greece - station: Amaliada-OTE Building
                            558		Pyrgos, Greece - station: Pirgos-Agriculture Bank
                            559		Pyrgos, Greece - station: Amaliada-OTE Building
                            560		Aftershock of Pyrgos earthquake, Greece - station: Amaliada-OTE Building
                            561		Aftershock of Pyrgos earthquake, Greece - station: Amaliada-OTE Building
                            562		Aftershock of Pyrgos earthquake, Greece - station: Amaliada-OTE Building
                            563		Aftershock of Pyrgos earthquake, Greece - station: Amaliada-OTE Building
                            564		Aftershock of Pyrgos earthquake, Greece - station: Amaliada-OTE Building
                            565		Se of Kalamata, Greece - station: Kalamata-Prefecture
                            566		Mouzakaiika, Greece - station: Lefkada-OTE Building
                            567		Mouzakaiika, Greece - station: Preveza-OTE Building
                            568		Aftershock of Pyrgos earthquake, Greece - station: Amaliada-OTE Building
                            569		Patras, Greece - station: Aigio-OTE Building
                            570		Patras, Greece - station: Amaliada-OTE Building
                            571		Patras, Greece - station: Messolongi-OTE Building
                            572		Patras, Greece - station: Nafpaktos-OTE Building
                            573		Patras, Greece - station: Patra-OTE Building
                            574		Aftershock of Patras earthquake, Greece - station: Patra-OTE Building
                            575		Aftershock of Patras earthquake, Greece - station: Patra-OTE Building
                            576		Duzce, Turkey - station: Usak-Meteorologji Mudurlugu
                            577		Gulf of Corinth, Greece - station: Aigio-OTE Building
                            580		Duzce, Turkey - station: Tosya-Meteoroloji Mudurlugu
                            581		Komilion, Greece - station: Lefkada-OTE Building
                            582		Komilion, Greece - station: Preveza-OTE Building
                            583		Ionian, Greece - station: Lefkada-OTE Building
                            584		off coast of Rethimno, Greece - station: Chania-OTE Building
                            585		off coast of Rethimno, Greece - station: Rethimno-OTE Building
                            586		Umbria, Italy - station: Colfiorito
                            587		Umbria, Italy - station: Nocera Umbra
                            588		Umbria, Italy - station: Colfiorito
                            589		Umbria, Italy - station: Nocera Umbra
                            590		Umbria, Italy - station: Colfiorito
                            591		Umbro-Marchigiano, Italy - station: Colfiorito
                            592		Umbro-Marchigiano, Italy - station: Colfiorito
                            593		Umbro-Marchigiano, Italy - station: Nocera Umbra
                            594		Umbro-Marchigiano, Italy - station: Nocera Umbra
                            595		Umbro-Marchigiano, Italy - station: Bevagna
                            596		Umbro-Marchigiano, Italy - station: Bevagna
                            597		Umbro-Marchigiano, Italy - station: Monte Fiegni
                            598		Umbro-Marchigiano, Italy - station: Monte Fiegni
                            599		Umbro-Marchigiano, Italy - station: Castelnuovo-Assisi
                            600		Umbro-Marchigiano, Italy - station: Castelnuovo-Assisi
                            601		Umbro-Marchigiano, Italy - station: Matelica
                            602		Umbro-Marchigiano, Italy - station: Matelica
                            603		Umbro-Marchigiano, Italy - station: Cascia
                            604		Umbro-Marchigiano, Italy - station: Cascia
                            605		Umbro-Marchigiano, Italy - station: Spoleto Monteluco
                            606		Umbro-Marchigiano, Italy - station: Forca Canapine
                            607		Umbro-Marchigiano, Italy - station: Forca Canapine
                            608		Umbro-Marchigiano, Italy - station: Gubbio
                            609		Umbro-Marchigiano, Italy - station: Leonessa
                            610		Umbro-Marchigiano, Italy - station: Leonessa
                            611		Umbro-Marchigiano, Italy - station: Gubbio-Piana
                            612		Umbro-Marchigiano, Italy - station: Gubbio-Piana
                            613		Umbro-Marchigiano, Italy - station: Rieti
                            614		Umbro-Marchigiano, Italy - station: Rieti
                            615		Umbro-Marchigiano, Italy - station: Pietralunga
                            616		Umbro-Marchigiano, Italy - station: Cagli
                            617		Umbro-Marchigiano, Italy - station: Peglio
                            618		Umbro-Marchigiano, Italy - station: Pennabilli
                            619		Umbro-Marchigiano, Italy - station: Senigallia
                            620		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Bevagna
                            621		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Gubbio
                            622		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Colfiorito
                            623		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Nocera Umbra
                            624		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Nocera Umbra-Salmata
                            625		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Castelnuovo-Assisi
                            626		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Monte Fiegni
                            627		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Norcia
                            628		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Forca Canapine
                            629		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Cascia
                            630		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Gubbio-Piana
                            631		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Rieti
                            632		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Leonessa
                            633		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Leonessa
                            634		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Gubbio-Piana
                            635		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Rieti
                            636		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Nocera Umbra
                            637		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Nocera Umbra-Salmata
                            638		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Cassignano
                            639		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Forca Canapine
                            640		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Norcia
                            641		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Spoleto Monteluco
                            642		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Cascia
                            643		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Matelica
                            644		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Castelnuovo-Assisi
                            645		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Bevagna
                            646		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Serravalle di Chienti
                            647		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Monte Fiegni
                            648		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Colfiorito
                            649		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Nocera Umbra-Biscontini
                            650		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Nocera Umbra-Biscontini
                            651		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Colfiorito-Casermette
                            652		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Colfiorito-Casermette
                            653		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Borgo-Cerreto Torre
                            654		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Borgo-Cerreto Torre
                            655		Umbro-Marchigiano, Italy - station: Borgo-Ottomila
                            656		Umbro-Marchigiano, Italy - station: Borgo-Ottomila
                            657		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Borgo-Ottomila
                            658		Sierentz, France - station: Beznau-Freifeld
                            659		Duzce, Turkey - station: Balikesir-Bayindirlik ve Iskan Mudurlugu
                            660		Duzce, Turkey - station: Bolu-Bayindirlik ve Iskan Mudurlugu
                            661		Duzce, Turkey - station: Bursa-Sivil Savunma Mudurluga
                            662		Duzce, Turkey - station: Canakkale-Meteoroloji Istasyonu
                            663		Duzce, Turkey - station: Istanbul-Bayindirlik ve Iskan Mudurlugu
                            664		Duzce, Turkey - station: Manisa-Bayindirlik Mudurlugu
                            665		Duzce, Turkey - station: Tekirdag-Bayindirlik Mudurlugu
                            666		Colle, Italy - station: Nocera Umbra
                            667		Wutoschingen, Germany - station: Basel-Tropenhaus
                            668		Wutoschingen, Germany - station: Beringen-Armbruststand
                            669		Wutoschingen, Germany - station: Bettingen-Gewerbehaus
                            670		Wutoschingen, Germany - station: Schweizerhalle-Ciba Geigy
                            671		Wutoschingen, Germany - station: Schaffhausen-Tanscherhalde
                            672		Pulumur, Turkey - station: Erzincan-Eksisu
                            673		Wutoschingen, Germany - station: Glottertal
                            674		Wutoschingen, Germany - station: Zurich-Degenried
                            675		Anzere, Switzerland - station: Grimisuat-Schulhaus
                            677		Aftershock of Schaan earthquake, Liechtenstein - station: Schaan-Hilti
                            678		Valpelline, Italy - station: Grande Dixence-SDIF
                            679		Grande Dixence, Switzerland - station: Grande Dixence-SDIF
                            680		Annecy, France - station: Genf-Marziano
                            681		Grande Dixence, Switzerland - station: Sion-Mayennets
                            682		Grande Dixence, Switzerland - station: Sion-Ophtalmologie
                            683		Valpelline, Italy - station: Mauvoisin-SM0F
                            684		Domodossola, Italy - station: Stalden-Merjen
                            685		Annecy, France - station: Yverdon-Jordils
                            686		Aftershock of Manjil earthquake, Iran - station: Barorud
                            687		Aftershock of Manjil earthquake, Iran - station: Barorud
                            688		Aftershock of Manjil earthquake, Iran - station: Barorud
                            689		Aftershock of Manjil earthquake, Iran - station: Gandja
                            690		Aftershock of Manjil earthquake, Iran - station: Gandja
                            691		Aftershock of Manjil earthquake, Iran - station: Ilja Tube
                            692		Aftershock of Manjil earthquake, Iran - station: Ilja Tube
                            693		Aftershock of Manjil earthquake, Iran - station: Ilja Tube
                            694		Aftershock of Manjil earthquake, Iran - station: Ilja Tube
                            695		Aftershock of Manjil earthquake, Iran - station: Ilja Tube
                            696		Aftershock of Manjil earthquake, Iran - station: Ilja Tube
                            697		Grande Dixence, Switzerland - station: Sion-Environment
                            698		Grande Dixence, Switzerland - station: Sion-Police Cantonale
                            699		Aftershock of Manjil earthquake, Iran - station: Rudbar
                            700		Aftershock of Manjil earthquake, Iran - station: Rudbar
                            701		Aftershock of Schaan earthquake, Liechtenstein - station: Buchs-Werdenberg
                            702		Aftershock of Manjil earthquake, Iran - station: Zietune
                            703		Aftershock of Manjil earthquake, Iran - station: Zietune
                            704		Cazulas, Spain - station: Santa Fe
                            705		foreshock of Friuli earthquake, Italy - station: Tolmezzo-Diga Ambiesta
                            706		foreshock of Friuli earthquake, Italy - station: Tolmezzo-Diga Ambiesta
                            707		foreshock of Friuli earthquake, Italy - station: Tarcento
                            708		Apt, France - station: Pierrevert-Maison Meunier
                            709		Aftershock of Schaan earthquake, Liechtenstein - station: Buchs-Malbun
                            710		Aix, France - station: Jouques-La Lantiere
                            711		Barcelonnette, France - station: Isola-Blockhaus
                            712		Cuneo, Italy - station: Isola-Blockhaus
                            713		Cuneo, Italy - station: Isola-Blockhaus
                            714		Barcelonnette, France - station: Serennes-Ecole
                            715		Briancon, France - station: Serennes-Ecole
                            716		Aftershock of Schaan earthquake, Liechtenstein - station: Buchs-Gewerbestrasse
                            717		Barcelonnette, France - station: Serennes-Ecole
                            718		Barcelonnette, France - station: Serennes-Ecole
                            719		Domodossola, Italy - station: Brig-Glis Dorf
                            720		Barcelonnette, France - station: Serennes-Ecole
                            721		Barcelonnette, France - station: Serennes-Ecole
                            722		Briancon, France - station: Serennes-Ecole
                            723		Cuneo, Italy - station: Serennes-Ecole
                            724		Grande Dixence, Switzerland - station: Salins-Turin
                            725		Barcelonnette, France - station: Serennes-Ecole
                            726		Barcelonnette, France - station: Serennes-Ecole
                            727		Athens, Greece - station: Athens 4 (Kipseli District)
                            728		Valpelline, Italy - station: Salins-Turin
                            729		Barcelonnette, France - station: Fouillouse-Blockhaus
                            730		Cuneo, Italy - station: Fouillouse-Blockhaus
                            731		Athens, Greece - station: Athens 2 (Chalandri District)
                            732		Barcelonnette, France - station: Fouillouse-Blockhaus
                            733		Kocaeli, Turkey - station: Yapi-Kredi Plaza Levent
                            734		Barcelonnette, France - station: Valensole-Catalany
                            735		Grenoble, France - station: Grenoble-CENG
                            736		San Remo, France - station: Volx-Maison Crest
                            737		Aix, France - station: Jouques-Centre Medico Social
                            738		Cuneo, Italy - station: Serennes-Ecole
                            739		Barcelonnette, France - station: Serennes-Ecole
                            740		San Remo, Italy - station: Pierrevert-Maison Meunier
                            741		Aix, France - station: St.Paul les Durance-Mairie
                            742		Barcelonnette, France - station: Serennes-Ecole
                            743		Barcelonnette, France - station: Serennes-Ecole
                            744		Barcelonnette, France - station: Serennes-Ecole
                            745		Barcelonnette, France - station: Serennes-Ecole
                            746		Cuneo, Italy - station: Serennes-Ecole
                            747		Athens, Greece - station: Athens 3 (Kallithea District)
                            748		Barcelonnette, France - station: Serennes-Ecole
                            749		Barcelonnette, France - station: Serennes-Ecole
                            750		Barcelonnette, France - station: Serennes-Ecole
                            751		Briancon, France - station: Serennes-Ecole
                            752		Barcelonnette, France - station: Serennes-Ecole
                            753		Turin, Italy - station: Serennes-Ecole
                            754		Kocaeli, Turkey - station: Heybeliada-Senatoryum
                            755		San Remo, Italy - station: Serennes-Ecole
                            756		Barcelonnette, France - station: Isola-Blockhaus
                            757		Annecy, France - station: Clansayes-Maison Cerquiglini
                            758		Umbro-Marchigiano, Italy - station: Norcia-Altavilla
                            759		Umbro-Marchigiano, Italy - station: Norcia-Zona Industriale
                            761		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Norcia-Zona Industriale
                            762		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Norcia-Altavilla
                            763		Umbro-Marchigiano, Italy - station: Borgo-Cerreto Torre
                            764		Umbro-Marchigiano, Italy - station: Borgo-Cerreto Torre
                            765		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Borgo-Cerreto Torre
                            766		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Borgo-Cerreto Torre
                            767		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Borgo-Campo Sportivo
                            768		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Foligno Santa Maria Infraportas-Base
                            769		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Foligno Santa Maria Infraportas-Base
                            770		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Nocera Umbra
                            771		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Nocera Umbra-Salmata
                            772		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Castelnuovo-Assisi
                            773		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Monte Fiegni
                            774		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Bevagna
                            775		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Gubbio
                            776		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Colfiorito
                            777		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Colfiorito
                            778		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Colfiorito
                            779		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Colfiorito
                            780		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Nocera Umbra
                            781		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Nocera Umbra
                            782		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Nocera Umbra-Salmata
                            783		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Gubbio-Piana
                            784		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Gubbio-Piana
                            785		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Rieti
                            786		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Rieti
                            787		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Gubbio-Piana
                            788		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Rieti
                            789		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Cascia
                            790		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Norcia
                            791		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Serravalle di Chienti
                            792		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Colfiorito
                            793		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Nocera Umbra
                            794		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Nocera Umbra
                            795		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Norcia
                            796		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Nocera Umbra-Salmata
                            797		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Nocera Umbra-Salmata
                            798		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Cassignano
                            799		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Cassignano
                            800		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Cassignano
                            801		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Forca Canapine
                            802		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Colfiorito
                            803		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Serravalle di Chienti
                            804		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Nocera Umbra-Salmata
                            805		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Cassignano
                            806		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Colfiorito
                            807		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Colfiorito
                            808		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Colfiorito
                            809		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Norcia
                            810		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Norcia
                            811		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Cascia
                            812		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Castelnuovo-Assisi
                            813		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Nocera Umbra-Biscontini
                            814		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Nocera Umbra-Biscontini
                            815		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Nocera Umbra-Biscontini
                            816		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Nocera Umbra-Biscontini
                            817		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Nocera Umbra-Biscontini
                            818		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Nocera Umbra-Biscontini
                            819		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Nocera Umbra-Biscontini
                            820		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Nocera Umbra-Biscontini
                            821		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Nocera Umbra-Biscontini
                            822		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Colfiorito-Casermette
                            823		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Colfiorito-Casermette
                            824		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Colfiorito-Casermette
                            825		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Colfiorito-Casermette
                            826		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Colfiorito-Casermette
                            827		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Colfiorito-Casermette
                            828		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Colfiorito-Casermette
                            829		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Colfiorito-Casermette
                            830		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Nocera Umbra
                            831		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Nocera Umbra
                            832		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Nocera Umbra
                            833		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Nocera Umbra
                            834		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Nocera Umbra-Biscontini
                            835		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Colfiorito-Casermette
                            836		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Colfiorito-Casermette
                            837		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Nocera Umbra
                            838		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Nocera Umbra
                            839		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Sellano
                            840		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Sellano
                            841		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Colfiorito
                            842		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Nocera Umbra-Biscontini
                            843		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Colfiorito-Casermette
                            844		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Sellano
                            845		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Nocera Umbra
                            846		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Sellano
                            847		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Sellano
                            848		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Nocera Umbra
                            849		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Nocera Umbra
                            850		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Nocera Umbra-Biscontini
                            851		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Nocera Umbra-Biscontini
                            852		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Nocera Umbra-Biscontini
                            853		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Nocera Umbra-Biscontini
                            854		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Gubbio-Piana
                            855		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Gubbio-Piana
                            856		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Nocera Umbra
                            857		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Nocera Umbra
                            858		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Sellano
                            859		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Sellano
                            860		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Norcia
                            861		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Serravalle di Chienti
                            862		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Cassignano
                            863		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Cassignano
                            864		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Bevagna
                            865		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Nocera Umbra-Salmata
                            866		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Colfiorito
                            867		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Matelica
                            868		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Peglio
                            869		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Castelnuovo-Assisi
                            870		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Gubbio
                            871		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Matelica
                            872		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Nocera Umbra-Salmata
                            873		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Cassignano
                            874		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Cassignano
                            875		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Bevagna
                            876		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Bevagna
                            877		Strait of Gibraltar, Spain - station: Adra (Almeria)
                            878		Strait of Gibraltar, Spain - station: Adra (Almeria)
                            879		Dinar, Turkey - station: Dinar-Meteoroloji Mudurlugu
                            880		Aftershock of Umbro-Marchigiana earthquake, Italy - station: Borgo-Cerreto Torre
                            881		Kocaeli, Turkey - station: Yesilkoy-Havaalani
                            882		Stroncone, Italy - station: Nocera Umbra
                            883		Kocaeli, Turkey - station: Botas-Gas Terminal
                            884		Norcia, Italy - station: Cascia-Cabina Petrucci
                            885		Norcia, Italy - station: Norcia
                            886		Giaveno, Italy - station: Pinerolo
                            887		W of Cosenza, Italy - station: Cosenza
                            888		Norcia, Italy - station: Norcia
                            889		Norcia, Italy - station: Norcia
                            890		off coast of Porto Sant_Elpidio, Italy - station: Scafa
                            891		Toscana, Italy - station: Pistoia
                            892		Norcia, Italy - station: Norcia
                            893		Roccanolfi, Italy - station: Norcia
                            894		Aftershock of Kocaeli earthquake, Turkey - station: Usak-Meteorologji Mudurlugu
                            895		Aftershock of Campano Lucano earthquake, Italy - station: Bagnoli-Irpino
                            896		Aftershock of Campano Lucano earthquake, Italy - station: Brienza
                            897		Aftershock of Campano Lucano earthquake, Italy - station: Sturno
                            898		Aftershock of Kocaeli earthquake, Turkey - station: Tekirdag-Bayindirlik Mudurlugu
                            899		Aftershock of Campano Lucano earthquake, Italy - station: Auletta
                            900		Campano Lucano, Italy - station: Garigliano-Centrale Nucleare 2
                            901		Aftershock of Campano Lucano earthquake, Italy - station: Brienza
                            902		Pizzo, Italy - station: Pizzo-Calabro
                            903		SW of Campobello di Mazara, Italy - station: Mazara del Vallo
                            904		street of Sicily, Italy - station: Mazara del Vallo
                            905		Aschio, Italy - station: Spoleto
                            906		Norcia, Italy - station: Spoleto
                            907		Aftershock of Kocaeli earthquake, Turkey - station: Sakarya-Bayindirlik ve Iskan Mudurlugu
                            908		near coast of Scalea, Italy - station: Lauria-Galdo
                            909		near coast of Scalea, Italy - station: Roggiano-Gravina
                            910		near coast of Marina di Monasterace, Italy - station: Ferruzzano
                            911		NW of Assisi, Italy - station: Nocera Umbra
                            912		N of Perugia, Italy - station: Nocera Umbra
                            913		NE of Perugia, Italy - station: Nocera Umbra
                            914		Collemincio, Italy - station: Nocera Umbra
                            915		Scritto, Italy - station: Nocera Umbra
                            916		Aftershock of Kocaeli earthquake, Turkey - station: Iznik-Karayollari Sefligi Muracaati
                            917		Aftershock of Kocaeli earthquake, Turkey - station: Izmit-Meteoroloji Istasyonu
                            918		E of Arienzo, Italy - station: Arienzo
                            919		Maddaloni, Italy - station: Arienzo
                            920		S of Parma, Italy - station: Fornovo
                            921		Arpiola, Italy - station: Tregnago
                            922		Aftershock of Lazio Abruzzo earthquake, Italy - station: Scafa
                            923		Aftershock of Lazio Abruzzo earthquake, Italy - station: Pescasseroli
                            924		Villetta Barrea, Italy - station: Villetta-Barrea
                            925		Garfagnana, Italy - station: Vagli-Paese
                            926		Garfagnana, Italy - station: Sestola
                            927		Garfagnana, Italy - station: Barga
                            928		Aftershock of Kocaeli earthquake, Turkey - station: Istanbul-Bayindirlik ve Iskan Mudurlugu
                            929		street of Messina, Italy - station: Villa San Giovanni
                            930		N of Reggio di Calabria, Italy - station: Villa San Giovanni
                            931		Aftershock of Kocaeli earthquake, Turkey - station: Gebze-Tubitak Marmara Arastirma Merkezi
                            932		Aftershock of Kocaeli earthquake, Turkey - station: Bornova-Eylul Universite Ziraat Fakultesi
                            933		Aftershock of Kocaeli earthquake, Turkey - station: Bursa-Sivil Savunma Mudurluga
                            934		Aftershock of Kocaeli earthquake, Turkey - station: Canakkale-Meteoroloji Istasyonu
                            935		Aftershock of Kocaeli earthquake, Turkey - station: Duzce-Meteoroloji Mudurlugu
                            936		NE of Reggio nell_Emilia, Italy - station: Novellara
                            937		NE of Reggio nell_Emilia, Italy - station: Sorbolo
                            938		Kocaeli, Turkey - station: Tekirdag-Bayindirlik Mudurlugu
                            939		Aftershock of Kocaeli earthquake, Turkey - station: Afyon-Bayindirlik ve Iskan Mudurlugu
                            940		Aftershock of Kocaeli earthquake, Turkey - station: Balikesir-Bayindirlik ve Iskan Mudurlugu
                            941		off coast of Acireale, Italy - station: Giarre
                            942		SE of Appricena, Italy - station: Sannicandro Garganico
                            943		Kocaeli, Turkey - station: Izmit-Meteoroloji Istasyonu
                            944		Potenza, Italy - station: Rionero in Vulture
                            945		Potenza, Italy - station: Rionero in Vulture
                            946		Potenza, Italy - station: Tricarico
                            947		Potenza, Italy - station: Brienza
                            948		Sicilia-Orientale, Italy - station: Catania-Piana
                            949		Sicilia-Orientale, Italy - station: Sortino
                            950		Sicilia-Orientale, Italy - station: Giarre
                            951		NE of San Giovanni in Fiore, Italy - station: San Giovanni in Fiore-PAL
                            952		S of Senigallia, Italy - station: Senigallia
                            953		Kocaeli, Turkey - station: Goynuk-Devlet Hastanesi
                            954		Basilicata, Italy - station: Rionero in Vulture
                            955		Kocaeli, Turkey - station: Iznik-Karayollari Sefligi Muracaati
                            956		Cuneo, Italy - station: Demonte
                            957		Collemincio, Italy - station: Nocera Umbra
                            958		Collemincio, Italy - station: Nocera Umbra
                            959		Demonte, Italy - station: Demonte
                            960		Sicilia-Orientale, Italy - station: Vizzini
                            961		Sicilia-Orientale, Italy - station: Noto
                            962		Sicilia-Orientale, Italy - station: Pachino
                            963		Sicilia-Orientale, Italy - station: Licata
                            964		Wiener Neustadt, Austria - station: Wiener Neustadt-Rathaus
                            965		Wiener Neustadt, Austria - station: Wiener Neustadt-Rathaus
                            966		Wiener Neustadt, Austria - station: Wiener Neustadt-Rathaus
                            967		Bludenz, Austria - station: Feldkirch-Gisingen
                            968		Schwadorf, Austria - station: Schwadorf
                            969		Ebreichsdorf, Austria - station: Wien-Palais Festetics
                            970		Ebreichsdorf, Austria - station: Wien-Hauptschule Schaumburgg
                            971		Ebreichsdorf, Austria - station: Wien-Schloss Neuwaldegg
                            972		Ebreichsdorf, Austria - station: Wiener Neustadt-Rathaus
                            973		Ebreichsdorf, Austria - station: Wiener Neustadt-Berufsschule Schneeberggasse
                            974		Campano Lucano, Italy - station: Gioia-Sannitica
                            975		Aftershock of Campano Lucano earthquake, Italy - station: Contrada Fiumicella-Teora
                            976		Aftershock of Campano Lucano earthquake, Italy - station: Contrada Fiumicella-Teora
                            977		Aftershock of Campano Lucano earthquake, Italy - station: Contrada Fiumicella-Teora
                            978		Aftershock of Campano Lucano earthquake, Italy - station: Contrada Fiumicella-Teora
                            979		Aftershock of Campano Lucano earthquake, Italy - station: Contrada Fiumicella-Teora
                            980		Aftershock of Campano Lucano earthquake, Italy - station: Contrada Fiumicella-Teora
                            981		Friuli, Italy - station: Tolmezzo-Diga Ambiesta
                            982		Friuli, Italy - station: Somplago-Uscita Galleria
                            983		Norcia, Italy - station: Cascia-Cabina Petrucci
                            984		Kocaeli, Turkey - station: Gebze-Tubitak Marmara Arastirma Merkezi
                            985		Mugello, Italy - station: Brasimone
                            986		Kocaeli, Turkey - station: Istanbul-Nukleer Santrali
                            987		Kocaeli, Turkey - station: Denizli-Bayindirlik ve Iskan Mudurlugu
                            988		Kocaeli, Turkey - station: Duzce-Meteoroloji Mudurlugu
                            989		Kocaeli, Turkey - station: Eregli-Kaymakamlik Binasi
                            990		Aftershock of Lazio Abruzzo earthquake, Italy - station: Atina-Pretura Terrazza
                            991		Aftershock of Lazio Abruzzo earthquake, Italy - station: Atina-Pretura Terrazza
                            992		Aftershock of Lazio Abruzzo earthquake, Italy - station: Atina-Pretura Terrazza
                            994		Aftershock of Lazio Abruzzo earthquake, Italy - station: Atina-Pretura Terrazza
                            995		Marano, Italy - station: Cosenza
                            996		Kocaeli, Turkey - station: Tokat-DSI Misafirhanesi
                            997		Grenoble, France - station: Annecy-DRASSM
                            998		Grenoble, France - station: Annecy-Prefecture
                            999		Grenoble, France - station: Aeroport Chambery-Aix
                            1000		Grenoble, France - station: Grenoble-Campus Universitaire
                            1001		Grenoble, France - station: Grenoble-Denis Hatzfeld
                            1002		Grenoble, France - station: Grenoble-St.Roch
                            1003		Grenoble, France - station: La Lechere
                            1004		Grenoble, France - station: Monetier les Bains
                            1005		Grenoble, France - station: Modane-Fort de St.Gobain
                            1006		Grenoble, France - station: Grenoble-Musee Dauphinois
                            1007		Grenoble, France - station: Grenoble-Pont de Claix
                            1008		Loma Prieta, United States - station: Capitola - Fire Station
                            1009		Loma Prieta, United States - station: Corralitos - Eureka Canyon Road
                            1011		Loma Prieta, United States - station: Hollister - South & Pine
                            1012		Loma Prieta, United States - station: San Jose - Santa Teresa Hills
                            1013		Loma Prieta, United States - station: San Francisco Airport
                            1014		Northridge, United States - station: Los Angeles - UCLA Grounds
                            1015		Northridge, United States - station: Los Angeles - Hollywood Storage Grounds
                            1016		Northridge, United States - station: Vasquez Rocks Park
                            1017		Northridge, United States - station: Malibu - Point Dume
                            1018		Northridge, United States - station: Los Angeles - Obregon Park
                            1020		Ancona, Italy - station: Ancona-Palombina
                            1021		Ancona, Italy - station: Ancona-Rocca
                            1022		Aftershock of Friuli earthquake, Italy - station: Tolmezzo-Diga Ambiesta
                            1023		Aftershock of Friuli earthquake, Italy - station: Forgaria-Cornio
                            1024		Aftershock of Friuli earthquake, Italy - station: Tolmezzo-Diga Ambiesta
                            1025		Aftershock of Friuli earthquake, Italy - station: Barcis
                            1026		Aftershock of Friuli earthquake, Italy - station: Conegliano-Veneto
                            1027		Valnerina, Italy - station: Mascioni
                            1028		Aftershock of Campano Lucano earthquake, Italy - station: Cairano 2
                            1029		Aftershock of Campano Lucano earthquake, Italy - station: Cairano 1
                            1030		Gulf of Corinth, Greece - station: Nafpaktos-OTE Building
                            1031		Gulf of Corinth, Greece - station: Patra-OTE Building
                            1032		Montenegro, Croatia - station: Veliki Ston-F-Ka Soli
                            1034		Gazli, Uzbekistan - station: Karakyr - JIPE
                            1035		Aftershock of Lazio Abruzzo earthquake, Italy - station: Atina-Pretura Terrazza
                            1036		Loma Prieta, United States - station: Gilroy - GCS Building
                            2060		Dillon, United States - station: Helena
                            2061		Dillon, United States - station: Butte
                            2062		Dillon, United States - station: W Yellowstone
                            2063		Dillon, United States - station: Helena
                            2064		Dillon, United States - station: Kalispell
                            2065		Dillon, United States - station: Dillon
                            2066		Dillon, United States - station: Lewiston
                            2067		Dillon, United States - station: Missoula
                            2068		Dillon, United States - station: Bozeman
                            2070		Denali, United States - station: R109
                            2071		Denali, United States - station: Alaska: TAPS Pump Station # 08
                            2072		Denali, United States - station: Fairbanks
                            2073		Denali, United States - station: Anchorage
                            2074		Denali, United States - station: Eagle River
                            2075		Denali, United States - station: Fairbanks
                            2076		Denali, United States - station: Anchorage
                            2077		Denali, United States - station: Anchorage
                            2078		Denali, United States - station: Alaska: TAPS Pump Station # 12
                            2079		Denali, United States - station: Anchorage
                            2080		Denali, United States - station: Valdez
                            2081		Denali, United States - station: Valdez
                            2082		Denali, United States - station: Anchorage
                            2083		Denali, United States - station: Alaska: TAPS Pump Station # 07
                            2084		Denali, United States - station: Alaska: TAPS Pump Station # 11
                            2085		Denali, United States - station: Carlo
                            2086		Denali, United States - station: Anchorage
                            2087		Denali, United States - station: Valdez
                            2088		Denali, United States - station: Alaska: TAPS Pump Station # 09
                            2089		Denali, United States - station: Anchorage
                            2090		Denali, United States - station: Anchorage
                            2091		Denali, United States - station: Anchorage
                            2092		Denali, United States - station: Alaska: TAPS Pump Station # 10
                            2093		Denali, United States - station: Fairbanks
                            2094		Denali, United States - station: Anchorage
                            2095		Denali, United States - station: Anchorage
                            2096		Denali, United States - station: Anchorage
                            2097		Denali, United States - station: Anchorage
                            2098		Denali, United States - station: Fairbanks
                            2099		 El Salvador, El Salvador - station: Santa Tecla
                            2100		 El Salvador, El Salvador - station: Acajutla Cepa
                            2101		 El Salvador, El Salvador - station: Ahuachapan
                            2102		 El Salvador, El Salvador - station: Seminario San Jose de la Montana
                            2103		 El Salvador, El Salvador - station: Sensuntepeque
                            2105		 El Salvador, El Salvador - station: Relaciones Exteriores
                            2106		 El Salvador, El Salvador - station: Cessa Metapan
                            2109		 El Salvador, El Salvador - station: Relaciones Exteriores
                            2110		 El Salvador, El Salvador - station: San Miguel
                            2111		 El Salvador, El Salvador - station: Observatorio
                            2113		 El Salvador, El Salvador - station: Cutuco
                            2115		 El Salvador, El Salvador - station: Presa 15 De Septiembre Dam
                            2117		 El Salvador, El Salvador - station: Santiago de Maria
                            2118		 El Salvador, El Salvador - station: Ciudadela Don Bosco
                            2119		 El Salvador, El Salvador - station: Santa Ana
                            2121		 El Salvador, El Salvador - station: Viveros de Dua
                            2124		Evansville, United States - station: St Louis
                            2125		 Iquique, Chile Earthquake, Chile - station: Limon Verde
                            2126		 Iquique, Chile Earthquake, Chile - station: Chusmiza
                            2127		 Kepulauan Mentawai Region, Indonesia - station: Sikuai Island
                            2128		 Kepulauan Mentawai Region, Indonesia - station: Sikuai Island
                            2129		Kiholo Bay, United States - station: Mauna Kea
                            2130		Kiholo Bay, United States - station: Waimea
                            2131		Kiholo Bay, United States - station: Volcano National Park
                            2132		Kiholo Bay, United States - station: Wailea
                            2133		Kiholo Bay, United States - station: Lanai City
                            2134		Kiholo Bay, United States - station: Mtn View
                            2135		Kiholo Bay, United States - station: Kailua-Kona
                            2136		Kiholo Bay, United States - station: Honolulu
                            2137		Kiholo Bay, United States - station: Honokaa
                            2138		Kiholo Bay, United States - station: Pahoa
                            2139		Kiholo Bay, United States - station: Kaunakakai
                            2140		Kiholo Bay, United States - station: Mauna Loa
                            2141		Kiholo Bay, United States - station: Hilo
                            2142		Kiholo Bay, United States - station: Pahala
                            2143		Kiholo Bay, United States - station: Hilo
                            2144		Kiholo Bay, United States - station: Laupahoehoe
                            2145		Kiholo Bay, United States - station: Hilo
                            2146		Kiholo Bay, United States - station: Waiohinu
                            2147		Kiholo Bay, United States - station: Anaehoomalu
                            2148		Kiholo Bay, United States - station: Honaunau
                            2149		Kiholo Bay, United States - station: Mauna Kea Hawaii Is
                            2150		Kiholo Bay, United States - station: Honolulu
                            2151		Kiholo Bay, United States - station: KeaLakekua
                            2152		Mahukona, United States - station: Pahoa
                            2153		Mahukona, United States - station: Hilo
                            2154		Mahukona, United States - station: Kohala
                            2155		Mahukona, United States - station: Hilo
                            2156		Mahukona, United States - station: Honaunau
                            2157		Mahukona, United States - station: Anaehoomalu
                            2158		Mahukona, United States - station: Kailua-Kona
                            2159		Mahukona, United States - station: Waimea
                            2160		Mahukona, United States - station: Mauna Kea
                            2161		Mahukona, United States - station: Mauna Loa
                            2162		Mahukona, United States - station: Mauna Kea Hawaii Is
                            2163		Mahukona, United States - station: Laupahoehoe
                            2164		Mahukona, United States - station: Hilo
                            2165		Mahukona, United States - station: Volcano National Park
                            2166		Mahukona, United States - station: Honomalino
                            2167		Mahukona, United States - station: Honokaa
                            2168		Mahukona, United States - station: KeaLakekua
                            2169		Mahukona, United States - station: Pahala
                            2170		Mineral, United States - station: Pearisburg
                            2171		Mineral, United States - station: Columbia
                            2172		Mineral, United States - station: Buffalo
                            2174		Mineral, United States - station: White River Jct.
                            2175		Mineral, United States - station: Summerville
                            2176		Mineral, United States - station: Charleston
                            2177		Mineral, United States - station: Albany
                            2178		Mineral, United States - station: Northampton
                            2179		Mineral, United States - station: VA:Charlottesvile
                            2180		Mineral, United States - station: Philadephia
                            2181		Mineral, United States - station: Manchester
                            2182		Mineral, United States - station: Boston
                            2183		Mineral, United States - station: Bedford
                            2184		Mineral, United States - station: VA:Corbin (Fredericksburg Obs)
                            2185		Oklahoma Earthquake, United States - station: St Louis
                            2186		Oklahoma Earthquake, United States - station: Lepanto
                            2187		Oklahoma Earthquake, United States - station: St Louis;Visitors Ctr
                            2188		Oklahoma Earthquake, United States - station: Poplar Bluff
                            2189		Oklahoma Earthquake, United States - station: Oklahoma City
                            2190		Oklahoma Earthquake, United States - station: Dexter
                            2191		 Puerto Rico, Puerto Rico - station: El Yunque
                            2192		 Puerto Rico, Puerto Rico - station: San Juan
                            2193		Puu Oo Crater, Hawaii Island, United States - station: Mauna Kea
                            2194		Puu Oo Crater, Hawaii Island, United States - station: KeaLakekua
                            2196		Puu Oo Crater, Hawaii Island, United States - station: Hilo
                            2197		Puu Oo Crater, Hawaii Island, United States - station: Mauna Loa
                            2198		Puu Oo Crater, Hawaii Island, United States - station: Hilo
                            2199		Puu Oo Crater, Hawaii Island, United States - station: Mauna Kea Hawaii Is
                            2200		Puu Oo Crater, Hawaii Island, United States - station: Kohala
                            2201		Puu Oo Crater, Hawaii Island, United States - station: Honokaa
                            2202		Puu Oo Crater, Hawaii Island, United States - station: Waimea
                            2203		Puu Oo Crater, Hawaii Island, United States - station: Volcano National Park
                            2204		Puu Oo Crater, Hawaii Island, United States - station: Pahala
                            2205		Puu Oo Crater, Hawaii Island, United States - station: Honaunau
                            2206		Puu Oo Crater, Hawaii Island, United States - station: Waiohinu
                            2207		Puu Oo Crater, Hawaii Island, United States - station: Hilo
                            2208		Puu Oo Crater, Hawaii Island, United States - station: Mtn View
                            2209		Puu Oo Crater, Hawaii Island, United States - station: Laupahoehoe
                            2210		Puu Oo Crater, Hawaii Island, United States - station: Pahoa
                            2211		 Virgin Islands, Puerto Rico - station: Arecibo
                            2212		 Virgin Islands, Puerto Rico - station: Loiza
                            2213		 Virgin Islands, Puerto Rico - station: San Juan
                            2214		 Virgin Islands, Puerto Rico - station: Bayamon
                            2215		 Virgin Islands, Puerto Rico - station: Ponce
                            2216		 Virgin Islands, Puerto Rico - station: Bayamon
                            2217		 Virgin Islands, Puerto Rico - station: Utuado
                            2218		 Virgin Islands, Puerto Rico - station: El Yunque
                            2219		 Virgin Islands, Puerto Rico - station: Ponce
                            2220		 Virgin Islands, Puerto Rico - station: Naguabo
                            2221		 Virgin Islands, Puerto Rico - station: Guayanilla
                            2222		 Virgin Islands, Puerto Rico - station: San Juan
                            2223		 WELLS, NV, Bulgaria - station: Pocatello
                            2224		Adak, Alaska, United States - station: Adak
                            2225		Amberley NewZealand, New Zealand - station: Waikari
                            2227		Amberley NewZealand, New Zealand - station: Seddon Fire Station
                            2228		Amberley NewZealand, New Zealand - station: Nelson Nelmac
                            2229		Amberley NewZealand, New Zealand - station: Lower Hutt IRL
                            2230		Amberley NewZealand, New Zealand - station: Wellington Emergency Management Office
                            2231		Amberley NewZealand, New Zealand - station: Havelock
                            2232		Amberley NewZealand, New Zealand - station: Takaka Scott's Farm
                            2233		Amberley NewZealand, New Zealand - station: Hawera High School
                            2234		Amberley NewZealand, New Zealand - station: Kaiapoi North School
                            2235		Amberley NewZealand, New Zealand - station: Wellington Pottery Association
                            2236		Amberley NewZealand, New Zealand - station: Inangahua Fire Station - Fire Station
                            2237		Amberley NewZealand, New Zealand - station: Te Horo House
                            2238		Amberley NewZealand, New Zealand - station: Westport Buller District Council
                            2239		Amberley NewZealand, New Zealand - station: Lower Hutt St Orans College - St Orans College
                            2240		Amberley NewZealand, New Zealand - station: Lower Hutt Emergency Management Office
                            2241		Amberley NewZealand, New Zealand - station: Cheviot Emergency Centre - Emergency Centre
                            2242		Amberley NewZealand, New Zealand - station: Lower Hutt Haywards Substation
                            2243		Amberley NewZealand, New Zealand - station: St Bernadette's School
                            2244		Amberley NewZealand, New Zealand - station: Point Howard
                            2245		Amberley NewZealand, New Zealand - station: Murchison Area School
                            2246		Amberley NewZealand, New Zealand - station: Wellington
                            2247		Amberley NewZealand, New Zealand - station: Palmerston North Boys High School - North Boys High School
                            2249		Amberley NewZealand, New Zealand - station: Porirua Free Ambulance Depot
                            2250		Amberley NewZealand, New Zealand - station: Amberley HDC
                            2251		Amberley NewZealand, New Zealand - station: Wellington Thorndon Fire Station
                            2252		Amberley NewZealand, New Zealand - station: Feilding Agricultural High School - Agricultural High School
                            2253		Amberley NewZealand, New Zealand - station: Kaikoura - South Bay
                            2254		Amberley NewZealand, New Zealand - station: Waiau Gorge
                            2255		Amberley NewZealand, New Zealand - station: Greta Valley
                            2256		Amberley NewZealand, New Zealand - station: Kaitoke Kiwi Ranch - Kiwi Ranch
                            2257		Amberley NewZealand, New Zealand - station: Lyttelton Port Oil Wharf
                            2258		Amberley NewZealand, New Zealand - station: Monrad Intermediate School
                            2259		Amberley NewZealand, New Zealand - station: Wellington Miramar School
                            2260		Amberley NewZealand, New Zealand - station: Wellington Karori Normal School - Karori Normal School
                            2261		Amberley NewZealand, New Zealand - station: Taita Central School
                            2262		Amberley NewZealand, New Zealand - station: Glyn Wye
                            2263		Amberley NewZealand, New Zealand - station: Petone Municipal Building
                            2264		Amberley NewZealand, New Zealand - station: Paraparaumu Primary School
                            2265		Amberley NewZealand, New Zealand - station: Porirua West
                            2266		Amberley NewZealand, New Zealand - station: Scargill
                            2267		Amberley NewZealand, New Zealand - station: Wainuiomata Hill
                            2268		Amberley NewZealand, New Zealand - station: Makara Bunker
                            2269		Amberley NewZealand, New Zealand - station: Kekerengu Valley Road
                            2270		Amberley NewZealand, New Zealand - station: Wellington International Airport
                            2271		Amberley NewZealand, New Zealand - station: Lower Hutt Unilever
                            2272		Amberley NewZealand, New Zealand - station: Upper Hutt College - College
                            2273		Amberley NewZealand, New Zealand - station: Hanmer Springs Emergency Centre - Emergency Centre
                            2274		Amberley NewZealand, New Zealand - station: Picton Queen Charlotte College - Queen Charlotte College
                            2275		Amberley NewZealand, New Zealand - station: Christchurch Papanui High School - Papanui High School
                            2276		Amberley NewZealand, New Zealand - station: Martinborough Wines Vineyard
                            2277		Amberley NewZealand, New Zealand - station: Porirua Library
                            2278		Amberley NewZealand, New Zealand - station: Somes Island
                            2279		Amberley NewZealand, New Zealand - station: Newlands
                            2280		Amberley NewZealand, New Zealand - station: Aotea Quay Pipitea
                            2281		Amberley NewZealand, New Zealand - station: Wainuiomata Bush Fire Force - Downhole Array (surface)
                            2282		Amberley NewZealand, New Zealand - station: Featherston Primary School
                            2283		Amberley NewZealand, New Zealand - station: Karamea School
                            2284		Amberley NewZealand, New Zealand - station: Springs Junction Fire Station - Fire Station
                            2285		Amberley NewZealand, New Zealand - station: Palmerston North Roslyn School
                            2286		Amberley NewZealand, New Zealand - station: Otaki School - Otaki School
                            2287		Amberley NewZealand, New Zealand - station: Culverden Airlie Farm
                            2288		Amberley NewZealand, New Zealand - station: Nelson Hospital
                            2289		Amberley NewZealand, New Zealand - station: Summerhill
                            2290		Amberley NewZealand, New Zealand - station: Wellington Te Papa Museum
                            2291		Amberley NewZealand, New Zealand - station: Ward Fire Station - Fire Station
                            2292		Amberley NewZealand, New Zealand - station: Wellington Frank Kitts Park - Frank Kitts Park
                            2293		Amberley NewZealand, New Zealand - station: Nelson Brightwater - Brightwater
                            2294		Amberley NewZealand, New Zealand - station: Blenheim Marlborough Girls College - Marlborough Girls College
                            2295		Amberley NewZealand, New Zealand - station: Foxton Beach School
                            2296		Amberley NewZealand, New Zealand - station: Reefton DOC Centre
                            2297		Amberley NewZealand, New Zealand - station: Christchurch Resthaven
                            2298		Amberley NewZealand, New Zealand - station: Wairau Valley Farm - Kowhai Cluain Farms
                            2299		Amberley NewZealand, New Zealand - station: Matariki Wadsworth Road
                            2300		Amberley NewZealand, New Zealand - station: Waikakaho Road
                            2301		Amberley NewZealand, New Zealand - station: Lower Hutt Normandale Rock Site - Normandale Rock Site
                            2302		Amberley NewZealand, New Zealand - station: Lower Hutt Normandale - Beethams
                            2303		Amberley NewZealand, New Zealand - station: Belmont
                            2304		Amberley NewZealand, New Zealand - station: Molesworth Station
                            2305		Amberley NewZealand, New Zealand - station: Lake Taylor Station
                            2306		Amberley NewZealand, New Zealand - station: Randwick School
                            2307		Amberley NewZealand, New Zealand - station: Wainuiomata Arakura School - Arakura School
                            2308		Amberley NewZealand, New Zealand - station: Petone Victoria Street
                            2309		Amberley NewZealand, New Zealand - station: Katoa Kindergarten
                            2310		Amberley NewZealand, New Zealand - station: Victoria University Law School
                            2311		Amberley NewZealand, New Zealand - station: Te Mara Farm Waiau
                            2312		Amberley NewZealand, New Zealand - station: Fairfield
                            2313		Amberley NewZealand, New Zealand - station: Nelson Council Building
                            2314		Amberley NewZealand, New Zealand - station: Living Springs Camp Governors Bay
                            2315		Amberley NewZealand, New Zealand - station: Seaview
                            2316		 Auckland Islands, New Zealand, New Zealand - station: Rarakau - (Southland District Council)
                            2317		 Auckland Islands, New Zealand, New Zealand - station: Wanaka National Park Headquarters
                            2318		 Auckland Islands, New Zealand, New Zealand - station: Invercargill City Council - City Council
                            2319		 Auckland Islands, New Zealand, New Zealand - station: Gore District Council - Council
                            2320		 Auckland Islands, New Zealand, New Zealand - station: Taieri Mouth Beach School - School
                            2321		 Auckland Islands, New Zealand, New Zealand - station: Te Anau Fire Station
                            2322		 Auckland Islands, New Zealand, New Zealand - station: Mossburn School
                            2323		 Auckland Islands, New Zealand, New Zealand - station: Dunedin St Kilda Fire Station
                            2324		 Auckland Islands, New Zealand, New Zealand - station: Dunedin Kings High School - Kings High School
                            2325		 Auckland Islands, New Zealand, New Zealand - station: Queenstown Police Station - Police Station
                            2326		 Fiordland, New Zealand - station: Dunedin
                            2327		 Fiordland, New Zealand - station: Benmore Dam
                            2328		 Fiordland, New Zealand - station: Wanaka
                            2329		 Fiordland, New Zealand - station: Castle Hill Station - Station
                            2330		 Fiordland, New Zealand - station: Harihari Fire Station - Fire Station
                            2331		 Fiordland, New Zealand - station: Christchurch Papanui High School - Papanui High School
                            2332		 Fiordland, New Zealand - station: Dunedin
                            2333		 Fiordland, New Zealand - station: Mossburn School
                            2334		 Fiordland, New Zealand - station: Waitaha Valley
                            2335		 Fiordland, New Zealand - station: Fox Glacier
                            2336		 Fiordland, New Zealand - station: Cheviot Emergency Centre - Emergency Centre
                            2337		 Fiordland, New Zealand - station: Inchbonnie Fitzsimmons Farm - Fitzsimmons Farm
                            2338		 Fiordland, New Zealand - station: Arnold River
                            2339		 Fiordland, New Zealand - station: Hawera
                            2340		 Fiordland, New Zealand - station: Nelson
                            2342		 Fiordland, New Zealand - station: Makarora Emergency Centre - Emergency Centre
                            2343		 Fiordland, New Zealand - station: Tekapo A Power Station - A Power Station (Meridian)
                            2344		 Fiordland, New Zealand - station: Springfield Fire Station - Fire Station
                            2345		 Fiordland, New Zealand - station: Christchurch Cashmere High School - Cashmere High School
                            2346		 Fiordland, New Zealand - station: Invercargill City Council - City Council
                            2347		 Fiordland, New Zealand - station: Wellington
                            2348		 Fiordland, New Zealand - station: Taumarunui High School - High School
                            2349		 Fiordland, New Zealand - station: Milford Sound
                            2350		 Fiordland, New Zealand - station: Christchurch
                            2351		 Fiordland, New Zealand - station: Ashburton
                            2352		 Fiordland, New Zealand - station: Greymouth
                            2353		 Fiordland, New Zealand - station: Kaikoura - South Bay
                            2354		 Fiordland, New Zealand - station: Timaru Roncalli College - Roncalli College
                            2355		 Fiordland, New Zealand - station: Balclutha
                            2356		 Fiordland, New Zealand - station: Gore
                            2357		 Fiordland, New Zealand - station: Motueka
                            2358		 Fiordland, New Zealand - station: Murchison
                            2359		 Fiordland, New Zealand - station: Darfield High School - High School
                            2360		 Fiordland, New Zealand - station: Dunedin
                            2361		 Fiordland, New Zealand - station: New Plymouth
                            2362		 Fiordland, New Zealand - station: Te Anau
                            2363		 Fiordland, New Zealand - station: Huiakama School
                            2364		 Fiordland, New Zealand - station: Karamea School
                            2365		 Fiordland, New Zealand - station: Dunedin Kings High School - Kings High School
                            2366		 Fiordland, New Zealand - station: Oamaru North
                            2367		 Fiordland, New Zealand - station: Mount Cook National Park Headquarters - National Park Headquarters
                            2368		 Fiordland, New Zealand - station: Hokitika
                            2369		 Fiordland, New Zealand - station: Balclutha
                            2370		 Fiordland, New Zealand - station: Christchurch
                            2371		 Fiordland, New Zealand - station: Aviemore Dam
                            2372		 Fiordland, New Zealand - station: Inangahua Fire Station - Fire Station
                            2373		 Fiordland, New Zealand - station: Christchurch
                            2375		 Fiordland, New Zealand - station: Queenstown Police Station - Police Station
                            2376		 Fiordland, New Zealand - station: Fairlie
                            2377		 Fiordland, New Zealand - station: Manapouri
                            2378		 Fiordland, New Zealand - station: Queenstown
                            2379		 Fiordland, New Zealand - station: Dunedin
                            2380		 Fiordland, New Zealand - station: Reefton
                            2381		 Fiordland, New Zealand - station: Kokatahi
                            2383		 Fiordland, New Zealand - station: Ashley School
                            2384		 Fiordland, New Zealand - station: Arthurs Pass
                            2385		 Fiordland, New Zealand - station: Haast
                            2386		Duzce, Turkey - station: Yesilkoy
                            2387		Duzce, Turkey - station: Yalova
                            2388		Duzce, Turkey - station: Levent
                            2389		Duzce, Turkey - station: Yalova
                            2391		Duzce, Turkey - station: Yalova
                            2393		Duzce, Turkey - station: Yalova
                            2394		Duzce, Turkey - station: Darica
                            2395		Duzce, Turkey - station: Yarimca
                            2397		Duzce, Turkey - station: Yalova
                            2398		Duzce, Turkey - station: Yalova
                            2399		Duzce, Turkey - station: Bursa
                            2400		Duzce, Turkey - station: Yalova
                            2401		Duzce, Turkey - station: Fatih
                            2402		Duzce, Turkey - station: K. Cekmece
                            2403		Duzce, Turkey - station: Eminonu
                            2404		Duzce, Turkey - station: Yalova
                            2405		Duzce, Turkey - station: Ambarli
                            2406		Duzce, Turkey - station: K. Mustalfa Pasa
                            2407		Duzce, Turkey - station: Heybeliada
                            2409		Duzce, Turkey - station: Yalova
                            2410		Duzce, Turkey - station: Darica
                            2412		Bhuj/Kachchh, India - station: Ahmedabad
                            2413		India-Burma Border, India - station: Umrongso
                            2414		India-Burma Border, India - station: Ummulong
                            2415		 India-Burma Border, India - station: Baithalongso
                            2416		 India-Burma Border, India - station: Saitsama
                            2417		India-Burma Border, India - station: Jhirighat
                            2418		India-Burma Border, India - station: Gunjung
                            2419		India-Burma Border, India - station: Koomber
                            2420		India-Burma Border, India - station: Umsning
                            2421		India-Burma Border, India - station: Kalain
                            2422		India-Burma Border, India - station: Panimur
                            2423		India-Burma Border, India - station: Katakhal
                            2424		India-Burma Border, India - station: Silchar
                            2425		India-Burma Border, India - station: Berlongfer
                            2426		 India-Burma Border, India - station: Baigao
                            2427		 India-Burma Border, India - station: Harengajao
                            2428		India-Burma Border, India - station: Hojai
                            2429		India-Burma Border, India - station: Mawsynram
                            2430		India-Burma Border, India - station: Hajadisa
                            2431		India-Burma Border, India - station: Nongstoin
                            2432		India-Burma Border, India - station: Dauki
                            2433		India-Burma Border, India - station: Khliehriat
                            2434		India-Burma Border, India - station: Shillong
                            2435		 India-Burma Border, India - station: Pynursla
                            2436		India-Burma Border, India - station: Nongkhlaw
                            2437		 India-Burma Border, India - station: Cherrapunji
                            2438		 India-Burma Border, India - station: Jellalpur
                            2439		India-Burma Border, India - station: Doloo
                            2440		India-Burma Border, India - station: Bamungao
                            2441		India-Burma Border, India - station: Loharghat
                            2442		India-Burma Border, India - station: Mawphlang
                            2443		India-Burma Border, India - station: Bokajan
                            2444		India-Burma Border, India - station: Mawkyrwat
                            2445		India-Burma Border, India - station: Diphu
                            2446		Miramichi, Canada - station: Holmes Lake
                            2447		Miramichi, Canada - station: Indian Brook II
                            2448		Miramichi, Canada - station: Mitchell Lake Rd
                            2449		Miramichi, Canada - station: Hickey Lakes
                            2450		Miramichi, Canada - station: Hickey Lakes
                            2451		New Hampshire, United States - station: Ball Mountain Dam
                            2452		New Hampshire, United States - station: North Springfield Dam
                            2453		New Hampshire, United States - station: North Hartland Dam
                            2454		New Hampshire, United States - station: Franklin Falls Dam
                            2455		New Hampshire, United States - station: White River Junction
                            2456		New Hampshire, United States - station: Union Village Dam
                            2457		 Saguenay, Canada - station: Island Falls
                            2458		 Saguenay, Canada - station: Dickey
                            2459		Scotts Mill, United States - station: Detroit Dam
                            2460		SE Alaska, United States - station: Icy Bay
                            2461		SE Alaska, United States - station: Yakutat. Alaska - FAA VOR Bldg Hangar
                            2462		SE Alaska, United States - station: Munday Creek
                            2463		Tabas, Iran - station: Ferdows
                            2464		Tabas, Iran - station: Khezri
                            2465		Tabas, Iran - station: Sedeh
                            2466		Tabas, Iran - station: Dayhook
                            2467		Tabas, Iran - station: Birjand
                            2468		Tabas, Iran - station: Boshrooyeh
                            2469		Tabas, Iran - station: Bajestan
                            2470		Tabas, Iran - station: Kashmar
                            2471		Tabas, Iran - station: Tabas
                            2472		 Uttarkashi, India - station: Kosani
                            2473		 Uttarkashi, India - station: Rudraprayag
                            2474		 Uttarkashi, India - station: Almora
                            2475		 Uttarkashi, India - station: Koteshwar
                            2476		 Uttarkashi, India - station: Bhatwari
                            2477		 Uttarkashi, India - station: Karnprayag
                            2478		 Uttarkashi, India - station: Tehri
                            2479		 Uttarkashi, India - station: Barkot
                            2480		 Uttarkashi, India - station: Srinagar
                            2481		 Uttarkashi, India - station: Uttarkashi
                            2482		 Uttarkashi, India - station: Koti
                            2483		 Uttarkashi, India - station: Purola
                            2484		 Uttarkashi, India - station: Ghansiali
                            2485		Valparaiso, Chile - station: Los Vilos
                            2486		Valparaiso, Chile - station: Valparaiso
                            2487		Valparaiso, Chile - station: San Isidro
                            2488		Valparaiso, Chile - station: Colbun
                            2489		Valparaiso, Chile - station: Chillan Institute
                            2490		Valparaiso, Chile - station: Santiago
                            2491		Valparaiso, Chile - station: Papudo
                            2492		Valparaiso, Chile - station: Melipilla
                            2493		Valparaiso, Chile - station: Iloca
                            2494		Valparaiso, Chile - station: Llayllay
                            2495		Valparaiso, Chile - station: Valparaiso el Almendral
                            2496		Valparaiso, Chile - station: Cauqenes
                            2497		Valparaiso, Chile - station: San Fernando
                            2498		Valparaiso, Chile - station: Pichilemu
                            2499		Valparaiso, Chile - station: Vina del Mar
                            2500		Valparaiso, Chile - station: Llolleo
                            2501		Valparaiso, Chile - station: Talca
                            2502		Valparaiso, Chile - station: Ventanas
                            2503		Valparaiso, Chile - station: San Felipe
                            2504		Valparaiso, Chile - station: Zapallar
                            2505		Valparaiso, Chile - station: Quintay
                            2506		Valparaiso, Chile - station: Illapel
                            2507		Valparaiso, Chile - station: Hualane
                            2508		Valparaiso, Chile - station: La Ligua
                            2509		Valparaiso, Chile - station: Constitucion
                            2510		Valparaiso, Chile - station: Rapel
                            2512		Valparaiso Aftershock, Chile - station: Constitucion
                            2513		Valparaiso Aftershock, Chile - station: Cauqenes
                            2514		Valparaiso Aftershock, Chile - station: Santiago
                            2515		Valparaiso Aftershock, Chile - station: Rapel
                            2516		Valparaiso Aftershock, Chile - station: Quintay
                            2517		Valparaiso Aftershock, Chile - station: San Fernando
                            2518		Valparaiso Aftershock, Chile - station: Iloca
                            2519		Valparaiso Aftershock, Chile - station: Ventanas
                            2520		Valparaiso Aftershock, Chile - station: Santiago
                            2536		 Enola, United States - station: Enola
                            2537		Enola, United States - station: Enola
                            2538		Enola, United States - station: Enola
                            2539		Enola, United States - station: Enola
                            2540		Enola, United States - station: Enola
                            2541		 Enola, United States - station: Enola
                            2542		 Enola, United States - station: Enola
                            2543		 Enola, United States - station: Enola
                            2544		 Enola, United States - station: Enola
                            2545		Enola, United States - station: Enola
                            2546		Enola, United States - station: Enola
                            2547		Gazli, Uzbekistan - station: Karakyr
                            2548		Limon, Costa Rica - station: San Jose
                            2549		Limon, Costa Rica - station: San Jose
                            2550		Limon, Costa Rica - station: Quepos
                            2551		Limon, Costa Rica - station: San Ramon
                            2552		Limon, Costa Rica - station: Golfito
                            2553		Limon, Costa Rica - station: Puriscal
                            2554		Limon, Costa Rica - station: Cachi
                            2555		Limon, Costa Rica - station: Guatuso
                            2556		Limon, Costa Rica - station: Cartago
                            2557		Limon, Costa Rica - station: San Jose
                            2558		Limon, Costa Rica - station: Alajuela
                            2559		Limon, Costa Rica - station: San Isidro
                            2560		Limon, Costa Rica - station: San Jose
                            2561		Limon, Costa Rica - station: San Jose
                            2562		 Nahanni, Canada - station: Nahanni
                            2563		Manjil, Iran - station: Abbar
                            2564		Manjil, Iran - station: Abhar
                            2565		Manjil, Iran - station: Gachesar
                            2566		Manjil, Iran - station: Tehran
                            2567		Manjil, Iran - station: Tehran
                            2568		Manjil, Iran - station: Qazvin
                            2569		Manjil, Iran - station: Tonekabun
                            2570		Manjil, Iran - station: Rudsar
                            2571		 Kozani, Greece - station: Florina
                            2572		 Kozani, Greece - station: Kastoria
                            2573		 Kozani, Greece - station: Larisa
                            2574		 Kozani, Greece - station: Kozani
                            2575		 Kozani, Greece - station: Edessa
                            2576		 Kozani, Greece - station: Veroia
                            2577		 Kozani, Greece - station: Kardista
                            2578		 Kozani, Greece - station: Grevena
                            2579		 Kozani, Greece - station: Chromio Anapsiktirio
                            2580		 Kozani, Greece - station: Grevena
                            2581		 Kozani, Greece - station: Grevena Posokemio
                            2582		 Kozani, Greece - station: Karpero
                            2583		 Northwest China, People's Republic of China - station: Xiker
                            2584		 Northwest China, People's Republic of China - station: Jiashi
                            2585		 Northwest China, People's Republic of China - station: Jiashi
                            2586		 Northwest China, People's Republic of China - station: Xiker
                            2587		 Northwest China, People's Republic of China - station: Xiker
                            2588		 Northwest China, People's Republic of China - station: Jiashi
                            2589		Taiwan, Taiwan - station: Lotung
                            2592		 Taiwan, Taiwan - station: Lotung
                            2594		 Taiwan, Taiwan - station: Lotung
                            2596		 Taiwan, Taiwan - station: Lotung
                            2599		 Taiwan, Taiwan - station: Lotung
                            2604		 Taiwan, Taiwan - station: Lotung
                            2615		 Taiwan, Taiwan - station: Lotung
                            2617		 Taiwan, Taiwan - station: Lotung
                            2618		 Taiwan, Taiwan - station: Lotung
                            2629		 Taiwan, Taiwan - station: Lotung
                            2630		 Taiwan, Taiwan - station: Lotung
                            2632		 Taiwan, Taiwan - station: Lotung
                            2633		 Taiwan, Taiwan - station: Lotung
                            2634		 Taiwan, Taiwan - station: Lotung
                            2637		 Taiwan, Taiwan - station: Lotung
                            2639		 Taiwan, Taiwan - station: Lotung
                            2640		 Taiwan, Taiwan - station: Lotung
                            2642		 Taiwan, Taiwan - station: Lotung
                            2644		 Taiwan, Taiwan - station: Lotung
                            2646		 Taiwan, Taiwan - station: Lotung
                            2647		 Taiwan, Taiwan - station: Lotung
                            2650		 Taiwan, Taiwan - station: Lotung
                            2651		 Taiwan, Taiwan - station: Lotung
                            2654		 Taiwan, Taiwan - station: Lotung
                            2660		Helena, United States - station: Helena
                            2661		Helena Aftershock, United States - station: Helena
                            2662		Kern County, United States - station: Taft
                            2663		Kern County, United States - station: Pasadena
                            2664		Kern County, United States - station: Los Angeles
                            2665		Kern County, United States - station: Los Angeles
                            2666		Kern County, United States - station: Santa Barbara. CA - Courthouse
                            2672		Landers, United States - station: Arcadia
                            2675		Landers, United States - station: West Covina
                            2679		Landers, United States - station: San Gabriel
                            2688		Landers, United States - station: Burbank
                            2690		Landers, United States - station: Panorama City
                            2692		Landers, United States - station: Anaheim
                            2698		Landers, United States - station: Santa Fe Springs
                            2703		Landers, United States - station: Covina
                            2704		Landers, United States - station: Hollywood
                            2706		Landers, United States - station: Bell Gardens
                            2708		Landers, United States - station: Arcadia
                            2710		Landers, United States - station: Carson
                            2712		Landers, United States - station: La Habra
                            2714		Landers, United States - station: Northridge
                            2715		Landers, United States - station: Sun Valley
                            2717		Landers, United States - station: Palos Verdes Estates
                            2718		Landers, United States - station: Brea
                            2723		Landers, United States - station: Sun Valley
                            2724		Landers, United States - station: Compton
                            2727		Landers, United States - station: Duarte
                            2729		Landers, United States - station: Lawndale
                            2730		Landers, United States - station: Hacienda Heights
                            2732		Landers, United States - station: Long Beach
                            2736		Landers, United States - station: Los Angeles
                            2737		Landers, United States - station: Los Angeles
                            2738		Landers, United States - station: Carson
                            2740		Landers, United States - station: Newhall
                            2741		Landers, United States - station: Santa Monica
                            2744		Landers, United States - station: Buena Park
                            2746		Landers, United States - station: Glendora
                            2747		Landers, United States - station: Sunland
                            2748		Landers, United States - station: El Monte
                            2749		Landers, United States - station: Manhattan Beach
                            2750		Landers, United States - station: Chatsworth
                            2752		Landers, United States - station: Los Angeles
                            2753		Landers, United States - station: Big Tujunga Station
                            2756		Landers, United States - station: Pasadena
                            2757		Landers, United States - station: Malibu
                            2759		Landers, United States - station: Baldwin Park
                            2760		Landers, United States - station: Glendale
                            2761		Landers, United States - station: Garden Grove
                            2770		Landers, United States - station: Fountain Valley
                            2773		Landers, United States - station: Downey
                            2774		Landers, United States - station: Los Angeles
                            2775		Landers, United States - station: La Crescenta
                            2776		Landers, United States - station: La Puente
                            2778		Landers, United States - station: Tustin
                            2779		Landers, United States - station: Lakewood
                            2786		Landers, United States - station: Huntington Beach
                            2792		 Landers, United States - station: Covina
                            2793		Landers, United States - station: Villa Park
                            2794		Puget Sound, United States - station: Olympia
                            2795		Puget Sound, United States - station: Seattle
                            2796		 Southern Sumatra, Indonesia - station: Sikuai Island
                            2797		Spitak, Armenia - station: Gukasyan
                            2798		Spitak Aftershock, Armenia - station: Gukasyan
                            2799		Western Washington, United States - station: Seattle Army Base
                            2800		Western Washington, United States - station: Olympia
                            2801		 Lesser Antilles, Puerto Rico - station: Ponce
                            2802		 Lesser Antilles, Puerto Rico - station: Arecibo
                            2803		 Lesser Antilles, Puerto Rico - station: Catano
                            2804		 Lesser Antilles, Puerto Rico - station: Mayaguez
                            2805		 Lesser Antilles, Puerto Rico - station: Humacao
                            2806		 Lesser Antilles, Puerto Rico - station: San Juan
                            2807		 Lesser Antilles, Puerto Rico - station: Carolina
                            2808		 Lesser Antilles, Puerto Rico - station: Cayey
                            2809		 Lesser Antilles, Puerto Rico - station: Canovanas
                            2810		Denali, United States - station: Anchorage
                            2811		Izmit-Kocaeli, Turkey - station: Bursa
                            2813		Izmit-Kocaeli, Turkey - station: Ambarli
                            2814		Izmit-Kocaeli, Turkey - station: Darica
                            2815		Izmit-Kocaeli, Turkey - station: Fatih
                            2817		Izmit-Kocaeli, Turkey - station: Yesilkoy
                            2819		Izmit-Kocaeli, Turkey - station: M. Ereglisi
                            2820		Izmit-Kocaeli, Turkey - station: Heybeliada
                            2821		Izmit-Kocaeli, Turkey - station: K. Cekmece
                            2822		Peru Coast, Peru - station: Arequipa
                            2823		Peru Coast, Peru - station: Arequipa
                            2824		Peru Coast, Peru - station: Lima
                            2825		Nisqually, United States - station: Olympia
                            2833		Nisqually, United States - station: Gig Harbor
                            2839		Nisqually, United States - station: Wynoochee Dam
                            2840		Nisqually, United States - station: Anacortes
                            2842		Nisqually, United States - station: Olympia
                            2850		Nisqually, United States - station: Tacoma
                            2852		Nisqually, United States - station: Seattle
                            2855		Nisqually, United States - station: Quinalt Lake
                            2858		Nisqually, United States - station: Seattle
                            2865		Nisqually, United States - station: Bremerton
                            2869		Nisqually, United States - station: Seattle
                            2871		Nisqually, United States - station: Forks
                            2873		Nisqually, United States - station: Mossyrock Dam
                            2875		Nisqually, United States - station: Port Gamble
                            2876		Nisqually, United States - station: Port Angeles
                            2878		Nisqually, United States - station: Chief Joseph Dam
                            2881		Nisqually, United States - station: Seattle
                            2882		Nisqually, United States - station: Howard Hanson Dam
                            2888		Nisqually, United States - station: Everett
                            2893		Nisqually, United States - station: Shelton
                            2896		Nisqually, United States - station: Seattle
                            2899		Nisqually, United States - station: Tolt River Dam
                            2901		Nisqually, United States - station: Olympia
                            2902		Nisqually, United States - station: Stanwood
                            2904		Nisqually, United States - station: Aberdeen
                            2910		Nisqually, United States - station: Port Townsend
                            2914		Nisqually, United States - station: Seattle
                            2920		British Columbia, Canada - station: Juneau, Auke Bay Fire Sta
                            2921		British Columbia, Canada - station: Juneau, Airport Fire Station
                            2922		British Columbia, Canada - station: Juneau, Downtown Fire Sta
                            2923		Nahanni, Canada - station: Nahanni
                            2924		Guadalupe Victoria, Baja, California, United States - station: Bonds Corner
                            2925		Guadalupe Victoria, Baja, California, United States - station: Calexico
                            2926		Guadalupe Victoria, Baja, California, United States - station: Holtville
                            2927		Guadalupe Victoria, Baja, California, United States - station: El Centro, Meadows Union School
                            2928		Guadalupe Victoria, Baja, California, United States - station: El Centro, Centro Community Hospital
                            2930		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name - AKT002
                            2931		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            2932		Tohoku 2011/03/11 05:46:24, Japan - station: Miyata
                            2933		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            2934		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            2935		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            2936		Tohoku 2011/03/11 05:46:24, Japan - station: Ohmagari,
                            2937		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            2938		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            2939		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            2940		Tohoku 2011/03/11 05:46:24, Japan - station: Nishiki-N,
                            2941		Tohoku 2011/03/11 05:46:24, Japan - station: Nishiki-N,
                            2942		Tohoku 2011/03/11 05:46:24, Japan - station: Nishiki-S,
                            2943		Tohoku 2011/03/11 05:46:24, Japan - station: Nishiki-S,
                            2944		Tohoku 2011/03/11 05:46:24, Japan - station: Higashinaruse,
                            2945		Tohoku 2011/03/11 05:46:24, Japan - station: Higashinaruse,
                            2946		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            2947		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            2948		Tohoku 2011/03/11 05:46:24, Japan - station: Ani,
                            2949		Tohoku 2011/03/11 05:46:24, Japan - station: Ani,
                            2950		Tohoku 2011/03/11 05:46:24, Japan - station: Kazuno,
                            2951		Tohoku 2011/03/11 05:46:24, Japan - station: Kazuno,
                            2952		Tohoku 2011/03/11 05:46:24, Japan - station: Nishisenboku,
                            2953		Tohoku 2011/03/11 05:46:24, Japan - station: Nishisenboku,
                            2954		Tohoku 2011/03/11 05:46:24, Japan - station: Nakasen,
                            2955		Tohoku 2011/03/11 05:46:24, Japan - station: Nakasen,
                            2956		Tohoku 2011/03/11 05:46:24, Japan - station: Oomori,
                            2957		Tohoku 2011/03/11 05:46:24, Japan - station: Oomori,
                            2958		Tohoku 2011/03/11 05:46:24, Japan - station: Yuzawa,
                            2959		Tohoku 2011/03/11 05:46:24, Japan - station: Yuzawa,
                            2960		Tohoku 2011/03/11 05:46:24, Japan - station: Mutsu,
                            2961		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            2962		Tohoku 2011/03/11 05:46:24, Japan - station: Minamidohri,
                            2963		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            2964		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            2965		Tohoku 2011/03/11 05:46:24, Japan - station: Noheji,
                            2966		Tohoku 2011/03/11 05:46:24, Japan - station: Misawa,
                            2967		Tohoku 2011/03/11 05:46:24, Japan - station: Hachinohe,
                            2968		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            2969		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            2970		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            2971		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            2972		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            2973		Tohoku 2011/03/11 05:46:24, Japan - station: Noheji,
                            2974		Tohoku 2011/03/11 05:46:24, Japan - station: Noheji,
                            2975		Tohoku 2011/03/11 05:46:24, Japan - station: Rokkasyo,
                            2976		Tohoku 2011/03/11 05:46:24, Japan - station: Rokkasyo,
                            2977		Tohoku 2011/03/11 05:46:24, Japan - station: Towadako-W,
                            2978		Tohoku 2011/03/11 05:46:24, Japan - station: Towadako-W,
                            2979		Tohoku 2011/03/11 05:46:24, Japan - station: Towadako-E,
                            2980		Tohoku 2011/03/11 05:46:24, Japan - station: Towadako-E,
                            2981		Tohoku 2011/03/11 05:46:24, Japan - station: Hachinohe,
                            2982		Tohoku 2011/03/11 05:46:24, Japan - station: Hachinohe,
                            2983		Tohoku 2011/03/11 05:46:24, Japan - station: Shingou,
                            2984		Tohoku 2011/03/11 05:46:24, Japan - station: Shingou,
                            2985		Tohoku 2011/03/11 05:46:24, Japan - station: Nagawa,
                            2986		Tohoku 2011/03/11 05:46:24, Japan - station: Nagawa,
                            2987		Tohoku 2011/03/11 05:46:24, Japan - station: Tatsuko,
                            2988		Tohoku 2011/03/11 05:46:24, Japan - station: Tatsuko,
                            2989		Tohoku 2011/03/11 05:46:24, Japan - station: Noda,
                            2990		Tohoku 2011/03/11 05:46:24, Japan - station: Matsudo,
                            2991		Tohoku 2011/03/11 05:46:24, Japan - station: Shiroi,
                            2992		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            2993		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            2994		Tohoku 2011/03/11 05:46:24, Japan - station: Narita,
                            2995		Tohoku 2011/03/11 05:46:24, Japan - station: Sakura,
                            2996		Tohoku 2011/03/11 05:46:24, Japan - station: Urayasu,
                            2997		Tohoku 2011/03/11 05:46:24, Japan - station: Chiba,
                            2998		Tohoku 2011/03/11 05:46:24, Japan - station: Yohkaichiba,
                            2999		Tohoku 2011/03/11 05:46:24, Japan - station: Hasunuma,
                            3000		Tohoku 2011/03/11 05:46:24, Japan - station: Tohgane,
                            3001		Tohoku 2011/03/11 05:46:24, Japan - station: Mobara,
                            3002		Tohoku 2011/03/11 05:46:24, Japan - station: Anezaki,
                            3003		Tohoku 2011/03/11 05:46:24, Japan - station: Kisaradu,
                            3004		Tohoku 2011/03/11 05:46:24, Japan - station: Misaki,
                            3005		Tohoku 2011/03/11 05:46:24, Japan - station: Ichiba,
                            3006		Tohoku 2011/03/11 05:46:24, Japan - station: Kyonan,
                            3007		Tohoku 2011/03/11 05:46:24, Japan - station: Kamogawa,
                            3008		Tohoku 2011/03/11 05:46:24, Japan - station: Futtsu,
                            3009		Tohoku 2011/03/11 05:46:24, Japan - station: Inage,
                            3010		Tohoku 2011/03/11 05:46:24, Japan - station: Chounan,
                            3011		Tohoku 2011/03/11 05:46:24, Japan - station: Ichikawa-Kita,
                            3012		Tohoku 2011/03/11 05:46:24, Japan - station: Gyoutoku,
                            3013		Tohoku 2011/03/11 05:46:24, Japan - station: Shimohsa,
                            3014		Tohoku 2011/03/11 05:46:24, Japan - station: Shimohsa,
                            3015		Tohoku 2011/03/11 05:46:24, Japan - station: Chiba,
                            3016		Tohoku 2011/03/11 05:46:24, Japan - station: Chiba,
                            3017		Tohoku 2011/03/11 05:46:24, Japan - station: Futtsu,
                            3018		Tohoku 2011/03/11 05:46:24, Japan - station: Futtsu,
                            3019		Tohoku 2011/03/11 05:46:24, Japan - station: Narita,
                            3020		Tohoku 2011/03/11 05:46:24, Japan - station: Narita,
                            3021		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3022		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3023		Tohoku 2011/03/11 05:46:24, Japan - station: Kamogawa,
                            3024		Tohoku 2011/03/11 05:46:24, Japan - station: Kamogawa,
                            3025		Tohoku 2011/03/11 05:46:24, Japan - station: Sohma,
                            3026		Tohoku 2011/03/11 05:46:24, Japan - station: Yanagawa,
                            3027		Tohoku 2011/03/11 05:46:24, Japan - station: Fukushima,
                            3028		Tohoku 2011/03/11 05:46:24, Japan - station: Iitate,
                            3029		Tohoku 2011/03/11 05:46:24, Japan - station: Haramachi,
                            3030		Tohoku 2011/03/11 05:46:24, Japan - station: Katsurao,
                            3031		Tohoku 2011/03/11 05:46:24, Japan - station: Funehiki,
                            3032		Tohoku 2011/03/11 05:46:24, Japan - station: Ono,
                            3033		Tohoku 2011/03/11 05:46:24, Japan - station: Hirono,
                            3034		Tohoku 2011/03/11 05:46:24, Japan - station: Iwaki,
                            3035		Tohoku 2011/03/11 05:46:24, Japan - station: Nakoso,
                            3036		Tohoku 2011/03/11 05:46:24, Japan - station: Furudono,
                            3037		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3038		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3039		Tohoku 2011/03/11 05:46:24, Japan - station: Shirakawa,
                            3040		Tohoku 2011/03/11 05:46:24, Japan - station: Sukagawa,
                            3041		Tohoku 2011/03/11 05:46:24, Japan - station: Kohriyama,
                            3042		Tohoku 2011/03/11 05:46:24, Japan - station: Nihommatsu,
                            3043		Tohoku 2011/03/11 05:46:24, Japan - station: Inawashiro,
                            3044		Tohoku 2011/03/11 05:46:24, Japan - station: Kitakata,
                            3045		Tohoku 2011/03/11 05:46:24, Japan - station: Nishiaidu,
                            3046		Tohoku 2011/03/11 05:46:24, Japan - station: Aiduwakamatsu,
                            3047		Tohoku 2011/03/11 05:46:24, Japan - station: Nakano,
                            3048		Tohoku 2011/03/11 05:46:24, Japan - station: Shimogoh,
                            3049		Tohoku 2011/03/11 05:46:24, Japan - station: Nangoh,
                            3050		Tohoku 2011/03/11 05:46:24, Japan - station: Takinohara,
                            3051		Tohoku 2011/03/11 05:46:24, Japan - station: Hinoemata,
                            3052		Tohoku 2011/03/11 05:46:24, Japan - station: Kawauchi,
                            3053		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3054		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3055		Tohoku 2011/03/11 05:46:24, Japan - station: Takasato,
                            3056		Tohoku 2011/03/11 05:46:24, Japan - station: Takasato,
                            3057		Tohoku 2011/03/11 05:46:24, Japan - station: Aizutakada,
                            3058		Tohoku 2011/03/11 05:46:24, Japan - station: Aizutakada,
                            3059		Tohoku 2011/03/11 05:46:24, Japan - station: Shimogou,
                            3060		Tohoku 2011/03/11 05:46:24, Japan - station: Shimogou,
                            3061		Tohoku 2011/03/11 05:46:24, Japan - station: Ina,
                            3062		Tohoku 2011/03/11 05:46:24, Japan - station: Ina,
                            3063		Tohoku 2011/03/11 05:46:24, Japan - station: Naganuma,
                            3064		Tohoku 2011/03/11 05:46:24, Japan - station: Naganuma,
                            3065		Tohoku 2011/03/11 05:46:24, Japan - station: Kooriyama,
                            3066		Tohoku 2011/03/11 05:46:24, Japan - station: Kooriyama,
                            3067		Tohoku 2011/03/11 05:46:24, Japan - station: Nishigou,
                            3068		Tohoku 2011/03/11 05:46:24, Japan - station: Nishigou,
                            3069		Tohoku 2011/03/11 05:46:24, Japan - station: Yabuki,
                            3070		Tohoku 2011/03/11 05:46:24, Japan - station: Yabuki,
                            3071		Tohoku 2011/03/11 05:46:24, Japan - station: Hirata,
                            3072		Tohoku 2011/03/11 05:46:24, Japan - station: Hirata,
                            3073		Tohoku 2011/03/11 05:46:24, Japan - station: Iwaki-E,
                            3074		Tohoku 2011/03/11 05:46:24, Japan - station: Iwaki-E,
                            3075		Tohoku 2011/03/11 05:46:24, Japan - station: Fukushima,
                            3076		Tohoku 2011/03/11 05:46:24, Japan - station: Fukushima,
                            3077		Tohoku 2011/03/11 05:46:24, Japan - station: Kawamata,
                            3078		Tohoku 2011/03/11 05:46:24, Japan - station: Kawamata,
                            3079		Tohoku 2011/03/11 05:46:24, Japan - station: Miharu,
                            3080		Tohoku 2011/03/11 05:46:24, Japan - station: Miharu,
                            3081		Tohoku 2011/03/11 05:46:24, Japan - station: Miyakoji,
                            3082		Tohoku 2011/03/11 05:46:24, Japan - station: Miyakoji,
                            3083		Tohoku 2011/03/11 05:46:24, Japan - station: Tadami,
                            3084		Tohoku 2011/03/11 05:46:24, Japan - station: Tadami,
                            3085		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3086		Tohoku 2011/03/11 05:46:24, Japan - station: Kamitakara,
                            3087		Tohoku 2011/03/11 05:46:24, Japan - station: Kamitakara,
                            3088		Tohoku 2011/03/11 05:46:24, Japan - station: Katashina,
                            3089		Tohoku 2011/03/11 05:46:24, Japan - station: Minakami,
                            3090		Tohoku 2011/03/11 05:46:24, Japan - station: Numata,
                            3091		Tohoku 2011/03/11 05:46:24, Japan - station: Kusatsu,
                            3092		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3093		Tohoku 2011/03/11 05:46:24, Japan - station: Shibukawa,
                            3094		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3095		Tohoku 2011/03/11 05:46:24, Japan - station: Kiryuh,
                            3096		Tohoku 2011/03/11 05:46:24, Japan - station: Tatebayashi,
                            3097		Tohoku 2011/03/11 05:46:24, Japan - station: Ohta,
                            3098		Tohoku 2011/03/11 05:46:24, Japan - station: Isesaki,
                            3099		Tohoku 2011/03/11 05:46:24, Japan - station: Takasaki,
                            3100		Tohoku 2011/03/11 05:46:24, Japan - station: Mamba,
                            3101		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3102		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3103		Tohoku 2011/03/11 05:46:24, Japan - station: Tone,
                            3104		Tohoku 2011/03/11 05:46:24, Japan - station: Tone,
                            3105		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3106		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3107		Tohoku 2011/03/11 05:46:24, Japan - station: Tomioka,
                            3108		Tohoku 2011/03/11 05:46:24, Japan - station: Tomioka,
                            3109		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3110		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3111		Tohoku 2011/03/11 05:46:24, Japan - station: Tadami,
                            3112		Tohoku 2011/03/11 05:46:24, Japan - station: Tadami,
                            3113		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3114		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3115		Tohoku 2011/03/11 05:46:24, Japan - station: Todohokke,
                            3116		Tohoku 2011/03/11 05:46:24, Japan - station: Daigo,
                            3117		Tohoku 2011/03/11 05:46:24, Japan - station: Takahagi,
                            3118		Tohoku 2011/03/11 05:46:24, Japan - station: Hitachi,
                            3119		Tohoku 2011/03/11 05:46:24, Japan - station: Ohmiya,
                            3120		Tohoku 2011/03/11 05:46:24, Japan - station: Kasama,
                            3121		Tohoku 2011/03/11 05:46:24, Japan - station: Mito,
                            3122		Tohoku 2011/03/11 05:46:24, Japan - station: Nakaminato,
                            3123		Tohoku 2011/03/11 05:46:24, Japan - station: Shimodate,
                            3124		Tohoku 2011/03/11 05:46:24, Japan - station: Koga,
                            3125		Tohoku 2011/03/11 05:46:24, Japan - station: Shimotsuma,
                            3126		Tohoku 2011/03/11 05:46:24, Japan - station: Tsukuba,
                            3127		Tohoku 2011/03/11 05:46:24, Japan - station: Ishioka,
                            3128		Tohoku 2011/03/11 05:46:24, Japan - station: Hokota,
                            3129		Tohoku 2011/03/11 05:46:24, Japan - station: Tsuchiura,
                            3130		Tohoku 2011/03/11 05:46:24, Japan - station: Iwai,
                            3131		Tohoku 2011/03/11 05:46:24, Japan - station: Toride,
                            3132		Tohoku 2011/03/11 05:46:24, Japan - station: Edosaki,
                            3133		Tohoku 2011/03/11 05:46:24, Japan - station: Kashima,
                            3134		Tohoku 2011/03/11 05:46:24, Japan - station: Edosaki,
                            3135		Tohoku 2011/03/11 05:46:24, Japan - station: Edosaki,
                            3136		Tohoku 2011/03/11 05:46:24, Japan - station: Ishige,
                            3137		Tohoku 2011/03/11 05:46:24, Japan - station: Ishige,
                            3138		Tohoku 2011/03/11 05:46:24, Japan - station: Iwase,
                            3139		Tohoku 2011/03/11 05:46:24, Japan - station: Iwase,
                            3140		Tohoku 2011/03/11 05:46:24, Japan - station: Daigo,
                            3141		Tohoku 2011/03/11 05:46:24, Japan - station: Daigo,
                            3142		Tohoku 2011/03/11 05:46:24, Japan - station: Takahagi,
                            3143		Tohoku 2011/03/11 05:46:24, Japan - station: Takahagi,
                            3144		Tohoku 2011/03/11 05:46:24, Japan - station: Jyuuoh,
                            3145		Tohoku 2011/03/11 05:46:24, Japan - station: Jyuuoh,
                            3146		Tohoku 2011/03/11 05:46:24, Japan - station: Gozenyama,
                            3147		Tohoku 2011/03/11 05:46:24, Japan - station: Gozenyama,
                            3148		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3149		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3150		Tohoku 2011/03/11 05:46:24, Japan - station: Kasumigaura,
                            3151		Tohoku 2011/03/11 05:46:24, Japan - station: Kasumigaura,
                            3152		Tohoku 2011/03/11 05:46:24, Japan - station: Hitachinaka,
                            3153		Tohoku 2011/03/11 05:46:24, Japan - station: Hitachinaka,
                            3154		Tohoku 2011/03/11 05:46:24, Japan - station: Hitachinaka,
                            3155		Tohoku 2011/03/11 05:46:24, Japan - station: Hitachinaka,
                            3156		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3157		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3158		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3159		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3160		Tohoku 2011/03/11 05:46:24, Japan - station: Taneichi,
                            3161		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3162		Tohoku 2011/03/11 05:46:24, Japan - station: Fudai,
                            3163		Tohoku 2011/03/11 05:46:24, Japan - station: Miyako,
                            3164		Tohoku 2011/03/11 05:46:24, Japan - station: Kamaishi,
                            3165		Tohoku 2011/03/11 05:46:24, Japan - station: Daitoh,
                            3166		Tohoku 2011/03/11 05:46:24, Japan - station: Ichinoseki,
                            3167		Tohoku 2011/03/11 05:46:24, Japan - station: Mizusawa,
                            3168		Tohoku 2011/03/11 05:46:24, Japan - station: Kitakami,
                            3169		Tohoku 2011/03/11 05:46:24, Japan - station: Tohno,
                            3170		Tohoku 2011/03/11 05:46:24, Japan - station: Ishidoriya,
                            3171		Tohoku 2011/03/11 05:46:24, Japan - station: Kawajiri,
                            3172		Tohoku 2011/03/11 05:46:24, Japan - station: Kawai,
                            3173		Tohoku 2011/03/11 05:46:24, Japan - station: Momma,
                            3174		Tohoku 2011/03/11 05:46:24, Japan - station: Morioka,
                            3175		Tohoku 2011/03/11 05:46:24, Japan - station: Iwaizumi,
                            3176		Tohoku 2011/03/11 05:46:24, Japan - station: Yabukawa,
                            3177		Tohoku 2011/03/11 05:46:24, Japan - station: Nishine,
                            3178		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3179		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3180		Tohoku 2011/03/11 05:46:24, Japan - station: Ninohe,
                            3181		Tohoku 2011/03/11 05:46:24, Japan - station: Ohshida,
                            3182		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3183		Tohoku 2011/03/11 05:46:24, Japan - station: Ninohe-E,
                            3184		Tohoku 2011/03/11 05:46:24, Japan - station: Ninohe-E,
                            3185		Tohoku 2011/03/11 05:46:24, Japan - station: Tamayama,
                            3186		Tohoku 2011/03/11 05:46:24, Japan - station: Tamayama,
                            3187		Tohoku 2011/03/11 05:46:24, Japan - station: Iwaizumi,
                            3188		Tohoku 2011/03/11 05:46:24, Japan - station: Iwaizumi,
                            3189		Tohoku 2011/03/11 05:46:24, Japan - station: Sumita,
                            3190		Tohoku 2011/03/11 05:46:24, Japan - station: Sumita,
                            3191		Tohoku 2011/03/11 05:46:24, Japan - station: Fujisawa,
                            3192		Tohoku 2011/03/11 05:46:24, Japan - station: Fujisawa,
                            3193		Tohoku 2011/03/11 05:46:24, Japan - station: Ninohe-W,
                            3194		Tohoku 2011/03/11 05:46:24, Japan - station: Ninohe-W,
                            3195		Tohoku 2011/03/11 05:46:24, Japan - station: Karumai,
                            3196		Tohoku 2011/03/11 05:46:24, Japan - station: Karumai,
                            3197		Tohoku 2011/03/11 05:46:24, Japan - station: Kuji-N,
                            3198		Tohoku 2011/03/11 05:46:24, Japan - station: Kuji-N,
                            3199		Tohoku 2011/03/11 05:46:24, Japan - station: Kuji-S,
                            3200		Tohoku 2011/03/11 05:46:24, Japan - station: Kuji-S,
                            3201		Tohoku 2011/03/11 05:46:24, Japan - station: Ashiro,
                            3202		Tohoku 2011/03/11 05:46:24, Japan - station: Ashiro,
                            3203		Tohoku 2011/03/11 05:46:24, Japan - station: Ichinohe,
                            3204		Tohoku 2011/03/11 05:46:24, Japan - station: Ichinohe,
                            3205		Tohoku 2011/03/11 05:46:24, Japan - station: Kunohe,
                            3206		Tohoku 2011/03/11 05:46:24, Japan - station: Kunohe,
                            3207		Tohoku 2011/03/11 05:46:24, Japan - station: Kuzumaki,
                            3208		Tohoku 2011/03/11 05:46:24, Japan - station: Kuzumaki,
                            3209		Tohoku 2011/03/11 05:46:24, Japan - station: Tarou,
                            3210		Tohoku 2011/03/11 05:46:24, Japan - station: Tarou,
                            3211		Tohoku 2011/03/11 05:46:24, Japan - station: Yahaba,
                            3212		Tohoku 2011/03/11 05:46:24, Japan - station: Yahaba,
                            3213		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3214		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3215		Tohoku 2011/03/11 05:46:24, Japan - station: Kawai-N,
                            3216		Tohoku 2011/03/11 05:46:24, Japan - station: Kawai-N,
                            3217		Tohoku 2011/03/11 05:46:24, Japan - station: Hanamaki-S,
                            3218		Tohoku 2011/03/11 05:46:24, Japan - station: Hanamaki-S,
                            3219		Tohoku 2011/03/11 05:46:24, Japan - station: Yamada,
                            3220		Tohoku 2011/03/11 05:46:24, Japan - station: Yamada,
                            3221		Tohoku 2011/03/11 05:46:24, Japan - station: Touwa,
                            3222		Tohoku 2011/03/11 05:46:24, Japan - station: Touwa,
                            3223		Tohoku 2011/03/11 05:46:24, Japan - station: Kamaishi,
                            3224		Tohoku 2011/03/11 05:46:24, Japan - station: Kamaishi,
                            3225		Tohoku 2011/03/11 05:46:24, Japan - station: Kanegasaki,
                            3226		Tohoku 2011/03/11 05:46:24, Japan - station: Kanegasaki,
                            3227		Tohoku 2011/03/11 05:46:24, Japan - station: Ichinoseki-E,
                            3228		Tohoku 2011/03/11 05:46:24, Japan - station: Ichinoseki-E,
                            3229		Tohoku 2011/03/11 05:46:24, Japan - station: Rikuzentakata,
                            3230		Tohoku 2011/03/11 05:46:24, Japan - station: Rikuzentakata,
                            3231		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3232		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3233		Tohoku 2011/03/11 05:46:24, Japan - station: Kawasaki,
                            3234		Tohoku 2011/03/11 05:46:24, Japan - station: Yokohama,
                            3235		Tohoku 2011/03/11 05:46:24, Japan - station: Misaki,
                            3236		Tohoku 2011/03/11 05:46:24, Japan - station: Futamatagawa,
                            3237		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3238		Tohoku 2011/03/11 05:46:24, Japan - station: Sagamihara,
                            3239		Tohoku 2011/03/11 05:46:24, Japan - station: Atsugi,
                            3240		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3241		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3242		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3243		Tohoku 2011/03/11 05:46:24, Japan - station: Odawara,
                            3244		Tohoku 2011/03/11 05:46:24, Japan - station: Yamakita,
                            3245		Tohoku 2011/03/11 05:46:24, Japan - station: Hiratsuka-st1,
                            3246		Tohoku 2011/03/11 05:46:24, Japan - station: Hiratsuka-st2,
                            3247		Tohoku 2011/03/11 05:46:24, Japan - station: Hiratsuka-st3,
                            3248		Tohoku 2011/03/11 05:46:24, Japan - station: Hiratsuka-st4,
                            3249		Tohoku 2011/03/11 05:46:24, Japan - station: Hiratsuka-st5,
                            3250		Tohoku 2011/03/11 05:46:24, Japan - station: Hiratsuka-st6,
                            3251		Tohoku 2011/03/11 05:46:24, Japan - station: Yokohama,
                            3252		Tohoku 2011/03/11 05:46:24, Japan - station: Yokohama,
                            3253		Tohoku 2011/03/11 05:46:24, Japan - station: Atsugi,
                            3254		Tohoku 2011/03/11 05:46:24, Japan - station: Atsugi,
                            3255		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3256		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3257		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3258		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3259		Tohoku 2011/03/11 05:46:24, Japan - station: Kesennuma,
                            3260		Tohoku 2011/03/11 05:46:24, Japan - station: Utatsu,
                            3261		Tohoku 2011/03/11 05:46:24, Japan - station: Tohwa,
                            3262		Tohoku 2011/03/11 05:46:24, Japan - station: Tsukidate,
                            3263		Tohoku 2011/03/11 05:46:24, Japan - station: Naruko,
                            3264		Tohoku 2011/03/11 05:46:24, Japan - station: Furukawa,
                            3265		Tohoku 2011/03/11 05:46:24, Japan - station: Toyosato,
                            3266		Tohoku 2011/03/11 05:46:24, Japan - station: Kitakami,
                            3267		Tohoku 2011/03/11 05:46:24, Japan - station: Taiwa,
                            3268		Tohoku 2011/03/11 05:46:24, Japan - station: Ishinomaki,
                            3269		Tohoku 2011/03/11 05:46:24, Japan - station: Oshika,
                            3270		Tohoku 2011/03/11 05:46:24, Japan - station: Shiogama,
                            3271		Tohoku 2011/03/11 05:46:24, Japan - station: Sendai,
                            3272		Tohoku 2011/03/11 05:46:24, Japan - station: Sakunami,
                            3273		Tohoku 2011/03/11 05:46:24, Japan - station: Iwanuma,
                            3274		Tohoku 2011/03/11 05:46:24, Japan - station: Shiroishi,
                            3275		Tohoku 2011/03/11 05:46:24, Japan - station: Kakuda,
                            3276		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3277		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3278		Tohoku 2011/03/11 05:46:24, Japan - station: Karakuwa,
                            3279		Tohoku 2011/03/11 05:46:24, Japan - station: Karakuwa,
                            3280		Tohoku 2011/03/11 05:46:24, Japan - station: Touwa,
                            3281		Tohoku 2011/03/11 05:46:24, Japan - station: Touwa,
                            3282		Tohoku 2011/03/11 05:46:24, Japan - station: Onoda,
                            3283		Tohoku 2011/03/11 05:46:24, Japan - station: Onoda,
                            3284		Tohoku 2011/03/11 05:46:24, Japan - station: Tajiri,
                            3285		Tohoku 2011/03/11 05:46:24, Japan - station: Tajiri,
                            3286		Tohoku 2011/03/11 05:46:24, Japan - station: Iwanuma,
                            3287		Tohoku 2011/03/11 05:46:24, Japan - station: Iwanuma,
                            3288		Tohoku 2011/03/11 05:46:24, Japan - station: Shiroishi,
                            3289		Tohoku 2011/03/11 05:46:24, Japan - station: Shiroishi,
                            3290		Tohoku 2011/03/11 05:46:24, Japan - station: Yamamoto,
                            3291		Tohoku 2011/03/11 05:46:24, Japan - station: Yamamoto,
                            3292		Tohoku 2011/03/11 05:46:24, Japan - station: Shizugawa,
                            3293		Tohoku 2011/03/11 05:46:24, Japan - station: Shizugawa,
                            3294		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3295		Tohoku 2011/03/11 05:46:24, Japan - station: Suwa,
                            3296		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3297		Tohoku 2011/03/11 05:46:24, Japan - station: Fujimi,
                            3298		Tohoku 2011/03/11 05:46:24, Japan - station: Fujimi,
                            3299		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3300		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3301		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3302		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3303		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3304		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3305		Tohoku 2011/03/11 05:46:24, Japan - station: Kanose,
                            3306		Tohoku 2011/03/11 05:46:24, Japan - station: Tsukawa,
                            3307		Tohoku 2011/03/11 05:46:24, Japan - station: Tsukawa,
                            3308		Tohoku 2011/03/11 05:46:24, Japan - station: Kamikawa,
                            3309		Tohoku 2011/03/11 05:46:24, Japan - station: Kamikawa,
                            3310		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3311		Tohoku 2011/03/11 05:46:24, Japan - station: Kumagaya,
                            3312		Tohoku 2011/03/11 05:46:24, Japan - station: Kuki,
                            3313		Tohoku 2011/03/11 05:46:24, Japan - station: Nagatoro,
                            3314		Tohoku 2011/03/11 05:46:24, Japan - station: Ogawa,
                            3315		Tohoku 2011/03/11 05:46:24, Japan - station: Chichibu,
                            3316		Tohoku 2011/03/11 05:46:24, Japan - station: Higashimatsuyama,
                            3317		Tohoku 2011/03/11 05:46:24, Japan - station: Kasukabe,
                            3318		Tohoku 2011/03/11 05:46:24, Japan - station: Kawagoe,
                            3319		Tohoku 2011/03/11 05:46:24, Japan - station: Ohmiya,
                            3320		Tohoku 2011/03/11 05:46:24, Japan - station: Kawaguchi,
                            3321		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3322		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3323		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3324		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3325		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3326		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3327		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3328		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3329		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3330		Tohoku 2011/03/11 05:46:24, Japan - station: Kamiizumi,
                            3331		Tohoku 2011/03/11 05:46:24, Japan - station: Kamiizumi,
                            3332		Tohoku 2011/03/11 05:46:24, Japan - station: Kawamoto,
                            3333		Tohoku 2011/03/11 05:46:24, Japan - station: Kawamoto,
                            3334		Tohoku 2011/03/11 05:46:24, Japan - station: Naguri,
                            3335		Tohoku 2011/03/11 05:46:24, Japan - station: Naguri,
                            3336		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3337		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3338		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3339		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3340		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3341		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3342		Tohoku 2011/03/11 05:46:24, Japan - station: Hannoh,
                            3343		Tohoku 2011/03/11 05:46:24, Japan - station: Hannoh,
                            3344		Tohoku 2011/03/11 05:46:24, Japan - station: Itoh,
                            3345		Tohoku 2011/03/11 05:46:24, Japan - station: Higashiizu,
                            3346		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3347		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3348		Tohoku 2011/03/11 05:46:24, Japan - station: Shimizu,
                            3349		Tohoku 2011/03/11 05:46:24, Japan - station: Shuzenji,
                            3350		Tohoku 2011/03/11 05:46:24, Japan - station: Shuzenji,
                            3351		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3352		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3353		Tohoku 2011/03/11 05:46:24, Japan - station: Fujiwara,
                            3354		Tohoku 2011/03/11 05:46:24, Japan - station: Yumoto,
                            3355		Tohoku 2011/03/11 05:46:24, Japan - station: Yaita,
                            3356		Tohoku 2011/03/11 05:46:24, Japan - station: Ogawa,
                            3357		Tohoku 2011/03/11 05:46:24, Japan - station: Utsunomiya,
                            3358		Tohoku 2011/03/11 05:46:24, Japan - station: Kanuma,
                            3359		Tohoku 2011/03/11 05:46:24, Japan - station: Imaichi,
                            3360		Tohoku 2011/03/11 05:46:24, Japan - station: Ashio,
                            3361		Tohoku 2011/03/11 05:46:24, Japan - station: Kuzuu,
                            3362		Tohoku 2011/03/11 05:46:24, Japan - station: Oyama,
                            3363		Tohoku 2011/03/11 05:46:24, Japan - station: Mooka,
                            3364		Tohoku 2011/03/11 05:46:24, Japan - station: Motegi,
                            3365		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3366		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3367		Tohoku 2011/03/11 05:46:24, Japan - station: Kuriyama-W,
                            3368		Tohoku 2011/03/11 05:46:24, Japan - station: Kuriyama-W,
                            3369		Tohoku 2011/03/11 05:46:24, Japan - station: Yaita,
                            3370		Tohoku 2011/03/11 05:46:24, Japan - station: Yaita,
                            3371		Tohoku 2011/03/11 05:46:24, Japan - station: Ootawara,
                            3372		Tohoku 2011/03/11 05:46:24, Japan - station: Ootawara,
                            3373		Tohoku 2011/03/11 05:46:24, Japan - station: Imaichi,
                            3374		Tohoku 2011/03/11 05:46:24, Japan - station: Imaichi,
                            3375		Tohoku 2011/03/11 05:46:24, Japan - station: Ujiie,
                            3376		Tohoku 2011/03/11 05:46:24, Japan - station: Ujiie,
                            3377		Tohoku 2011/03/11 05:46:24, Japan - station: Batou,
                            3378		Tohoku 2011/03/11 05:46:24, Japan - station: Batou,
                            3379		Tohoku 2011/03/11 05:46:24, Japan - station: Awano,
                            3380		Tohoku 2011/03/11 05:46:24, Japan - station: Awano,
                            3381		Tohoku 2011/03/11 05:46:24, Japan - station: Utsunomiya,
                            3384		Tohoku 2011/03/11 05:46:24, Japan - station: Haga,
                            3385		Tohoku 2011/03/11 05:46:24, Japan - station: Hikawa,
                            3386		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3387		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3388		Tohoku 2011/03/11 05:46:24, Japan - station: Hachiohji,
                            3389		Tohoku 2011/03/11 05:46:24, Japan - station: Machida,
                            3390		Tohoku 2011/03/11 05:46:24, Japan - station: Koganei,
                            3391		Tohoku 2011/03/11 05:46:24, Japan - station: Shinjuku,
                            3392		Tohoku 2011/03/11 05:46:24, Japan - station: Okada,
                            3393		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3394		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3395		Tohoku 2011/03/11 05:46:24, Japan - station: Kameido,
                            3396		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3397		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3398		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3399		Tohoku 2011/03/11 05:46:24, Japan - station: Hachieda,
                            3400		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3401		Tohoku 2011/03/11 05:46:24, Japan - station: Sarue,
                            3402		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3403		Tohoku 2011/03/11 05:46:24, Japan - station: Yahiro,
                            3404		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3405		Tohoku 2011/03/11 05:46:24, Japan - station: Shinozaki,
                            3406		Tohoku 2011/03/11 05:46:24, Japan - station: Ukita,
                            3407		Tohoku 2011/03/11 05:46:24, Japan - station: Mizue,
                            3408		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3409		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3410		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3411		Tohoku 2011/03/11 05:46:24, Japan - station: Hachiohji,
                            3412		Tohoku 2011/03/11 05:46:24, Japan - station: Hachiohji,
                            3413		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3414		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3415		Tohoku 2011/03/11 05:46:24, Japan - station: Tabayama,
                            3416		Tohoku 2011/03/11 05:46:24, Japan - station: Ohtsuki,
                            3417		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3418		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3419		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3420		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3421		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3422		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3423		Tohoku 2011/03/11 05:46:24, Japan - station: Shinjoh,
                            3424		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3425		Tohoku 2011/03/11 05:46:24, Japan - station: Obanazawa,
                            3426		Tohoku 2011/03/11 05:46:24, Japan - station: Higashine,
                            3427		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3428		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3429		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3430		Tohoku 2011/03/11 05:46:24, Japan - station: Kaminoyama,
                            3431		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3432		Tohoku 2011/03/11 05:46:24, Japan - station: Oguni,
                            3433		Tohoku 2011/03/11 05:46:24, Japan - station: Shimoyachi,
                            3434		Tohoku 2011/03/11 05:46:24, Japan - station: Yonezawa,
                            3435		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3436		Tohoku 2011/03/11 05:46:24, Japan - station: Tendou,
                            3437		Tohoku 2011/03/11 05:46:24, Japan - station: Tendou,
                            3438		Tohoku 2011/03/11 05:46:24, Japan - station: Yamagata,
                            3439		Tohoku 2011/03/11 05:46:24, Japan - station: Yamagata,
                            3440		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3441		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3442		Tohoku 2011/03/11 05:46:24, Japan - station: Kaminoyama,
                            3443		Tohoku 2011/03/11 05:46:24, Japan - station: Kaminoyama,
                            3444		Tohoku 2011/03/11 05:46:24, Japan - station: Takahata,
                            3445		Tohoku 2011/03/11 05:46:24, Japan - station: Takahata,
                            3446		Tohoku 2011/03/11 05:46:24, Japan - station: Yonezawa,
                            3447		Tohoku 2011/03/11 05:46:24, Japan - station: Yonezawa,
                            3448		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3449		Tohoku 2011/03/11 05:46:24, Japan - station: Empty name
                            3450		Tohoku 2011/03/11 05:46:24, Japan - station: Nishikawa-W,
                            3451		Tohoku 2011/03/11 05:46:24, Japan - station: Nishikawa-W,
                            3452		Tohoku 2011/03/11 05:46:24, Japan - station: Nishikawa-E,
                            3453		Tohoku 2011/03/11 05:46:24, Japan - station: Nishikawa-E,
                            3454		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Shirataki,
                            3456		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Syari-N,
                            3457		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Syari-N,
                            3458		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Rubeshibe,
                            3459		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Rubeshibe,
                            3460		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Oketo-E,
                            3461		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Oketo-E,
                            3462		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Minamidohri,
                            3463		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Noheji,
                            3464		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Noheji,
                            3465		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Biratori-E,
                            3466		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Biratori-E,
                            3467		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Monbetsu-W,
                            3468		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Monbetsu-W,
                            3469		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Shizunai,
                            3470		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Shizunai,
                            3471		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Minamifurano,
                            3472		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Rubeshibe,
                            3473		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Oketo,
                            3474		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Utoro,
                            3475		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Fujimi,
                            3476		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Aidomari,
                            3477		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Shibetsu,
                            3478		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Nakashibetsu,
                            3479		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Kaminishishumbetsu,
                            3480		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Betsukai,
                            3481		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Honbetsukai,
                            3482		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Atsutoko,
                            3483		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Ochiishi,
                            3484		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Nemuro,
                            3485		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Nosappu,
                            3486		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Hamanaka,
                            3487		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Akkeshi,
                            3488		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Kushiro,
                            3489		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Tohro,
                            3490		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Shibeccha,
                            3491		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Teshikaga,
                            3492		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Kawayu,
                            3493		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Akankohan,
                            3494		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Tsurui,
                            3495		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Akan,
                            3496		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Shiranuka,
                            3497		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Chokubetsu,
                            3498		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Futamata,
                            3499		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Rikubetsu,
                            3500		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Ashoro,
                            3501		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Hombetsu,
                            3502		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Urahoro,
                            3503		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Ikeda,
                            3504		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Nukabira,
                            3505		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Shihoro,
                            3506		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Obihiro,
                            3507		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Nakasatsunai,
                            3508		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Taiki,
                            3509		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Shintoku,
                            3510		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Hiroo,
                            3511		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Horokeshi,
                            3512		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Biratori,
                            3513		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Mombetsu,
                            3514		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Shizunai,
                            3515		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Noya,
                            3516		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Mitsuishi,
                            3517		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Urakawa,
                            3518		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Samani,
                            3519		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Erimomisaki,
                            3520		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Meguro,
                            3521		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Hobetsu,
                            3522		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Mukawa,
                            3523		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Oiwake,
                            3524		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Hayakita,
                            3525		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Muroran,
                            3526		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Ohtaki,
                            3527		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Minamikayabe,
                            3528		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Todohokke,
                            3529		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Toi,
                            3530		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Ebetsu,
                            3531		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Chitose,
                            3532		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Shikotsukohan,
                            3533		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Oiwake
                            3534		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Oiwake
                            3535		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Atsuma
                            3536		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Atsuma
                            3537		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Muroran,
                            3538		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Muroran,
                            3539		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Ootaki,
                            3540		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Ootaki,
                            3541		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Shimukappu,
                            3542		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Shimukappu,
                            3543		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Nakafurano,
                            3544		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Nakafurano,
                            3545		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Akan-N,
                            3546		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Akan-N,
                            3547		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Akan-S,
                            3548		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Akan-S,
                            3549		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Shibecha-N,
                            3550		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Shibecha-N,
                            3551		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Shibecha-S,
                            3552		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Shibecha-S,
                            3553		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Tsurui-W,
                            3554		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Tsurui-W,
                            3555		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Tsurui-E,
                            3556		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Tsurui-E,
                            3557		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Tsurui-S,
                            3558		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Tsurui-S,
                            3559		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Hamanaka,
                            3560		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Hamanaka,
                            3561		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Shibetsu-S,
                            3562		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Shibetsu-S,
                            3563		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Bekkai-E,
                            3565		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Bekkai-W,
                            3566		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Bekkai-W,
                            3567		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Kuriyama,
                            3568		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Kuriyama,
                            3569		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Rikubetsu,
                            3570		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Rikubetsu,
                            3571		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Asyoro-E,
                            3572		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Asyoro-E,
                            3573		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Asyoro-W,
                            3574		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Asyoro-W,
                            3575		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Shintoku-S,
                            3576		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Shintoku-S,
                            3577		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Honbetsu,
                            3578		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Honbetsu,
                            3579		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Memuro,
                            3580		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Memuro,
                            3581		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Toyokoro,
                            3582		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Toyokoro,
                            3583		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Taiki,
                            3584		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Taiki,
                            3585		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Shintoku-N,
                            3586		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Shintoku-N,
                            3587		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Shimizu,
                            3588		Tokachi-oki 2003/09/25 19:50:07, Japan - station: Shimizu,
                            3589		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Noda,
                            3590		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Matsudo,
                            3591		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Shiroi,
                            3592		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Empty name
                            3593		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Empty name
                            3594		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Narita,
                            3595		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Sakura,
                            3596		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Urayasu,
                            3597		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Chiba,
                            3598		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Yohkaichiba,
                            3599		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Hasunuma,
                            3600		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Tohgane,
                            3601		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Mobara,
                            3602		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Anezaki,
                            3603		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Kisaradu,
                            3604		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Misaki,
                            3605		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Ichiba,
                            3606		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Futtsu,
                            3607		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Chounan,
                            3608		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Ichikawa-Kita,
                            3609		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Gyoutoku,
                            3610		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Shimohsa,
                            3611		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Shimohsa,
                            3612		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Chiba,
                            3613		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Chiba,
                            3614		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Narita,
                            3615		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Narita,
                            3616		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Empty name
                            3617		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Empty name
                            3618		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Kamogawa,
                            3619		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Kamogawa,
                            3620		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Sohma,
                            3621		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Iitate,
                            3622		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Haramachi,
                            3623		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Funehiki,
                            3624		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Ono,
                            3625		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Iwaki,
                            3626		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Nakoso,
                            3627		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Furudono,
                            3628		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Empty name
                            3629		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Empty name
                            3630		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Kohriyama,
                            3631		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Nihommatsu,
                            3632		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Aiduwakamatsu,
                            3633		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Hinoemata,
                            3634		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Naganuma,
                            3635		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Naganuma,
                            3636		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Nishigou,
                            3637		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Nishigou,
                            3638		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Yabuki,
                            3639		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Yabuki,
                            3640		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Hirata,
                            3641		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Hirata,
                            3642		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Iwaki-E,
                            3643		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Iwaki-E,
                            3644		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Kawamata,
                            3645		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Kawamata,
                            3646		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Miharu,
                            3647		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Miharu,
                            3648		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Miyakoji,
                            3649		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Miyakoji,
                            3650		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Katashina,
                            3651		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Numata,
                            3652		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Kiryuh,
                            3653		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Tatebayashi,
                            3654		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Ohta,
                            3655		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Isesaki,
                            3656		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Empty name
                            3657		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Empty name
                            3658		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Daigo,
                            3659		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Takahagi,
                            3660		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Hitachi,
                            3661		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Ohmiya,
                            3662		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Kasama,
                            3663		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Mito,
                            3664		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Nakaminato,
                            3665		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Shimodate,
                            3666		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Koga,
                            3667		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Shimotsuma,
                            3668		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Tsukuba,
                            3669		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Ishioka,
                            3670		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Hokota,
                            3671		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Tsuchiura,
                            3672		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Iwai,
                            3673		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Toride,
                            3674		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Edosaki,
                            3675		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Kashima,
                            3676		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Edosaki,
                            3677		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Edosaki,
                            3678		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Ishige,
                            3679		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Ishige,
                            3680		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Iwase,
                            3681		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Iwase,
                            3682		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Daigo,
                            3683		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Daigo,
                            3684		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Takahagi,
                            3685		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Takahagi,
                            3686		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Jyuuoh,
                            3687		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Jyuuoh,
                            3688		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Gozenyama,
                            3689		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Gozenyama,
                            3690		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Empty name
                            3691		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Empty name
                            3692		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Kasumigaura,
                            3693		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Kasumigaura,
                            3694		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Hitachinaka,
                            3695		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Hitachinaka,
                            3696		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Hitachinaka,
                            3697		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Hitachinaka,
                            3698		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Empty name
                            3699		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Empty name
                            3700		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Empty name
                            3701		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Empty name
                            3702		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Kamaishi,
                            3703		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Daitoh,
                            3704		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Tohno,
                            3705		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Kamaishi,
                            3706		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Kamaishi,
                            3707		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Kawasaki,
                            3708		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Yokohama,
                            3709		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Hiratsuka-st6,
                            3710		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Yokohama,
                            3711		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Yokohama,
                            3712		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Kesennuma,
                            3713		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Iwanuma,
                            3714		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Yamamoto,
                            3715		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Yamamoto,
                            3716		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Kuki,
                            3717		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Nagatoro,
                            3718		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Kasukabe,
                            3719		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Kawaguchi,
                            3720		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Kawamoto,
                            3721		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Kawamoto,
                            3722		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Hannoh,
                            3723		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Hannoh,
                            3724		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Empty name
                            3725		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Fujiwara,
                            3726		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Yaita,
                            3727		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Ogawa,
                            3728		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Kanuma,
                            3729		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Imaichi,
                            3730		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Ashio,
                            3731		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Oyama,
                            3732		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Mooka,
                            3733		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Motegi,
                            3734		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Empty name
                            3735		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Empty name
                            3736		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Kuriyama-W,
                            3737		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Kuriyama-W,
                            3738		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Ootawara,
                            3739		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Ootawara,
                            3740		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Imaichi,
                            3741		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Imaichi,
                            3742		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Ujiie,
                            3743		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Ujiie,
                            3744		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Batou,
                            3745		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Batou,
                            3746		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Awano,
                            3747		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Awano,
                            3748		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Utsunomiya,
                            3749		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Utsunomiya,
                            3750		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Haga,
                            3751		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Haga,
                            3752		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Shinjuku,
                            3753		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Empty name
                            3754		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Kameido,
                            3755		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Empty name
                            3756		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Empty name
                            3757		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Empty name
                            3758		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Hachieda,
                            3759		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Empty name
                            3760		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Sarue,
                            3761		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Empty name
                            3762		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Yahiro,
                            3763		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Empty name
                            3764		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Shinozaki,
                            3765		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Ukita,
                            3766		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Mizue,
                            3767		Near the East Coast of Honshu 2011/03/11 06:15:40, Japan - station: Empty name
                            3768		Kozani, Greece - station: Chromio Anapsiktirio
                            3769		Kozani, Greece - station: Grevena
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
