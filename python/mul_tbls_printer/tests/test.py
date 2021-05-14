import unittest

from ..mul_tbls_printer import MulTblsPrinter
from .consts import *

class Test(unittest.TestCase):
    def assert_mul_tbls_printer(self, tbl_no, limit, exp_output):
        mulTblsPrinterObj = MulTblsPrinter(limit)
        self.assertEqual(mulTblsPrinterObj.gen_mul_tbls(tbl_no), exp_output)

    def test_case1(self):
        self.assert_mul_tbls_printer(5, 10, TC1_EXP_OUTPUT)

    def test_case2(self):
        self.assert_mul_tbls_printer(7, 15, TC2_EXP_OUTPUT)

    def test_case3(self):
        self.assert_mul_tbls_printer(13, 20, TC3_EXP_OUTPUT)

if __name__=='__main__':
   unittest.main()