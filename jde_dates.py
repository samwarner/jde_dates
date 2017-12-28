from datetime import datetime, date

class JdeDates():
    """ 
    Creates an object which accepts either a julian date or 
    a standard date, and then converts it to the other format.
    """
    def __init__(self, value_in):
        self.value_in = value_in
        self.iso_date = None
        self.julian_date = None
        self.convert()
        
    def convert(self):
        # test if date object and apply the approprate conversion
        if isinstance(self.value_in, date):
            self.iso_date = self.value_in
            self.julian_date = int(self.value_in.strftime(
                '%Y%j')) - 1900000
        else:
            self.julian_date = self.value_in
            self.iso_date = datetime.date(datetime.strptime(
                str(int(self.value_in) + 1900000), '%Y%j'))


