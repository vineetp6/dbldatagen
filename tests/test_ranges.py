from pyspark.sql.types import StructType, StructField, IntegerType, StringType, FloatType, TimestampType
import databrickslabs_testdatagenerator as dg
from pyspark.sql import SparkSession
import unittest
from pyspark.sql import functions as F
import logging

spark = dg.SparkSingleton.getLocalInstance("basic tests")


class TestRanges(unittest.TestCase):
    testDataSpec = None
    dfTestData = None
    row_count = 100000
    column_count = 50

    def setUp(self):
        print("setting up")
        FORMAT = '%(asctime)-15s %(message)s'
        logging.basicConfig(format=FORMAT)

    @classmethod
    def setUpClass(cls):
        pass

    def test_numeric_range1(self):
        r1 = dg.NRange(1, 20, 1)

        print(r1.getDiscreteRange())

    def test_numeric_range2(self):
        r1 = dg.NRange(1.5, 2.5, 0.35)

        print(r1.getDiscreteRange())

        self.assertEqual(r1.getScale(), 2)

    def test_numeric_range3(self):
        r1 = dg.NRange(1.5, 2.5, 0.5)

        print(r1.getDiscreteRange())

    def test_numeric_range4(self):
        r1 = dg.NRange(0, 4, 0.5)

        print(r1.getDiscreteRange())


# run the tests
# if __name__ == '__main__':
#  print("Trying to run tests")
#  unittest.main(argv=['first-arg-is-ignored'],verbosity=2,exit=False)

# def runTests(suites):
#    suite = unittest.TestSuite()
#    result = unittest.TestResult()
#    for testSuite in suites:
#        suite.addTest(unittest.makeSuite(testSuite))
#    runner = unittest.TextTestRunner()
#    print(runner.run(suite))


# runTests([TestBasicOperation])

if __name__ == '__main__':
    unittest.main()