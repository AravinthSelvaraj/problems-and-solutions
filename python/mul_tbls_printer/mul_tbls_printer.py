class MulTblsPrinter:
    def __init__(self, limit):
        self.limit = limit

    def gen_mul_tbls(self, tbl_no):
        tables_str = ''
        for no in range (1, self.limit + 1):
            res = no * tbl_no
            no_str = '{: <3}'.format(no)
            line_str = no_str + 'x  ' + str(tbl_no) + '  =  ' + str(res)
            tables_str = tables_str + line_str
            if no < self.limit:
                tables_str = tables_str + '\n'
        return tables_str

if __name__=='__main__':
    mul_tbls_printer_obj = MulTblsPrinter(20)
    tbl_no = int(input('Enter tables number:'))
    print(mul_tbls_printer_obj.gen_mul_tbls(tbl_no))