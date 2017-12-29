# jde_dates
Simple conversion module to help working with Julian dates (CYYDDD) in JD Edwards.

## Basic Usage
### JdeDates class object
Following are examples of creating class objects, with the constructor invoking the conversion method automatically.
Once successfully instantiated, the JdeDates object holds the input and both date formats as attributes.

```python
from datetime import datetime, date
from jde_dates import JdeDates

#  Inputs can be valid date(), int(), or str() objects
converted1 = JdeDates(date(2017, 12, 31))
converted2 = JdeDates(115222)
converted3 = JdeDates('112322')

print("Input: {}".format(converted1.value_in))  # Input: 2017-12-31
print("ISO Date: {}".format(converted1.iso_date))  # ISO Date: 2017-12-31
print("Julian Date: {}\n".format(converted1.julian_date))  # Julian Date: 117365

print("Input: {}".format(converted2.value_in))  # Input: 115222
print("ISO Date: {}".format(converted2.iso_date))  # ISO Date: 2015-08-10
print("Julian Date: {}\n".format(converted2.julian_date))  # Julian Date: 115222

print("Input: {}".format(converted3.value_in))  # Input: 112322
print("ISO Date: {}".format(converted3.iso_date))  # ISO Date: 2012-11-17
print("Julian Date: {}\n".format(converted3.julian_date)) # Julian Date: 112322
```

## License
This project is licensed under the MIT License - see the LICENSE.md file for details
