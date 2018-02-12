import unittest
from donation_analytics import getValues
class TestUM(unittest.TestCase):

	    def test_getValues(self):
		    	    line = "C00384516|N|M2|P|201702039042410894|15|IND|SABOURIN, JAMES|LOOKOUT MOUNTAIN|GA|028956146|UNUM|SVP, CORPORATE COMMUNICATIONS|01312018|384||PR2283904845050|1147350||P/R DEDUCTION ($192.00 BI-WEEKLY)|4020820171370029339"	
		            self.assertEqual(getValues(line),["C00384516","SABOURIN, JAMES","02895","2018",384 ] )
