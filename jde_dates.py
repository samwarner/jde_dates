from datetime import datetime, date

class JdeDates:
    """ 
    Creates an object which accepts either a JDE Julian date (CYYDDD) or 
    a standard ISO date (YYYY-MM-DD), and then converts it to the other
    format, storing both as attributes.
    """
    def __init__(self, value_in):
        self.value_in = value_in
        self.iso_date = None
        self.julian_date = None
        self._convert()
        
    def _convert(self):
        # Test if date object and apply the approprate conversion
        if isinstance(self.value_in, date):
            self.iso_date = self.value_in
            self.julian_date = int(self.value_in.strftime(
                '%Y%j')) - 1900000
        else:
            self.julian_date = self.value_in
            self.iso_date = datetime.date(datetime.strptime(
                str(int(self.value_in) + 1900000), '%Y%j'))



def convert_to_julian(iso_date):
    return int(iso_date.strftime('%Y%j')) - 1900000


def convert_to_iso(julian_date):
    return datetime.date(datetime.strptime(
        str(int(julian_date) + 1900000), '%Y%j'))