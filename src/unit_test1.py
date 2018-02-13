import unittest
from donation_analytics import percentile,getValues
class TestUM(unittest.TestCase):

	    def test_getValues1(self):
		    	    line = "C00384516|N|M2|P|201702039042410894|15|IND|SABOURIN, JAMES|LOOKOUT MOUNTAIN|GA|028956146|UNUM|SVP, CORPORATE COMMUNICATIONS|01312018|384||PR2283904845050|1147350||P/R DEDUCTION ($192.00 BI-WEEKLY)|4020820171370029339"	
		            self.assertEqual(getValues(line),["C00384516","SABOURIN, JAMES","02895","2018",384 ] )

	    def test_getValues2(self):
		    line = ""
		    self.assertEqual(getValues(line),None)
		    
	    def test_getValues3(self):
		    	    line = "C00384516|N|M2|P|201702039042410894|15|IND|SABOURIN, JAMES|LOOKOUT MOUNTAIN|GA|026|UNUM|SVP, CORPORATE COMMUNICATIONS|01312018|384||PR2283904845050|1147350||P/R DEDUCTION ($192.00 BI-WEEKLY)|4020820171370029339"	
		            self.assertEqual(getValues(line),None )

	    def test_getValues4(self):
		    	    line = "C00384516|N|M2|P|201702039042410894|15|IND|SABOURIN, JAMES|LOOKOUT MOUNTAIN|GA|028956146|UNUM|SVP, CORPORATE COMMUNICATIONS|01/31/2018|384||PR2283904845050|1147350||P/R DEDUCTION ($192.00 BI-WEEKLY)|4020820171370029339"	
		            self.assertEqual(getValues(line),None )

	    def test_getValues5(self):
		    	    line = "C00384516|N|M2|P|201702039042410894|15|IND|SABOURIN, JAMES|LOOKOUT MOUNTAIN|GA|028956146|UNUM|SVP, CORPORATE COMMUNICATIONS|01312018|-384||PR2283904845050|1147350||P/R DEDUCTION ($192.00 BI-WEEKLY)|4020820171370029339"	
		            self.assertEqual(getValues(line),None )

	    def test_percentile1(self):
		    	heap = [15, 20, 35, 40, 50]
			n = len(heap)
			self.assertEqual(percentile(heap,30,n),20 )
			self.assertEqual(percentile(heap,40,n),20 )
			self.assertEqual(percentile(heap,5,n),15 )

	    def test_percentile2(self):
		    	heap = [3, 6, 7, 8, 8, 10, 13, 15, 16, 20]
			n = len(heap)
			self.assertEqual(percentile(heap,25,n),7)
			self.assertEqual(percentile(heap,50,n),8)
			self.assertEqual(percentile(heap,75,n),15)
			self.assertEqual(percentile(heap,100,n),20)

	    def test_percentile3(self):
		    	heap = [3, 6, 7, 8, 8, 9, 10, 13, 15, 16, 20]
			n = len(heap)
			self.assertEqual(percentile(heap,25,n),7)
			self.assertEqual(percentile(heap,50,n),9 )
			self.assertEqual(percentile(heap,75,n),15)
			self.assertEqual(percentile(heap,100,n),20)

	    #def testCaseValues(self):
				
