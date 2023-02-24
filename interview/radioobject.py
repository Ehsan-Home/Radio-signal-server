import json


class RadioObject():
    def __init__(self, type, dispersion, right_ascension, declination):
        if self.verifyType(type):
            self.type = type
        else:
            raise Exception("The type is not valid")

        try:
            assert 0 < dispersion <= 13000
            self.dispersion = dispersion
        except:
            raise Exception("dispersion is not in range")

        try:
            assert 0 <= right_ascension <= 360
            self.right_ascension = right_ascension
        except:
            raise Exception("right_ascension is not in range")

        try:
            assert -90 <= declination <= 90
            self.declination = declination
        except:
            raise Exception("declination is not in range")

    def verifyType(self, type):
        validTypes = ['rrat', 'frb', 'neutron_star', 'white_dwarf', 'magnetar']
        if type in validTypes:
            return True
        else:
            return False

    def payload(self):
        # {"type":"rrat",...}
        return json.dumps({'type': self.type, 'dispersion': self.dispersion, 'right_ascension': self.right_ascension, 'declination': self.declination})


# obj = RadioObject('rrat', -30, 40, 20)
# print(obj.payload())
