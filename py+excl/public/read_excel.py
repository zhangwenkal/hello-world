import xlrd,os
from xlrd import open_workbook

proDir=os.path.join(os.path.dirname(__file__),os.path.pardir)
proDir=os.path.abspath(proDir)

class readExcel(object):
    def __init__(self, xls_name,sheet_name):
        xlspath=os.path.join(proDir,'TestFile','case',xls_name)
        file=open_workbook(xlspath)
        self.sheet=file.sheet_by_name(sheet_name)


    @property
    def getRows(self):
        # 获取行数
        row = self.sheet.nrows
        return row

    @property
    def getCol(self):
        # 获取列数
        col = self.sheet.ncols
        return col

    # 以下是分别获取每一列的数值
    @property
    def getNo(self):
        TestNo = []
        for i in range(1, self.getRows):
            TestNo.append(self.sheet.cell_value(i, 0))
        return TestNo

    @property
    def getMethod(self):
        TestMethod = []
        for i in range(1, self.getRows):
            TestMethod.append(self.sheet.cell_value(i, 1))
        return TestMethod

    @property
    def getData(self):
        TestData = []
        for i in range(1, self.getRows):
            TestData.append(self.sheet.cell_value(i, 2))
        return TestData

    @property
    def getUrl(self):
        TestUrl = []
        for i in range(1, self.getRows):
            TestUrl.append(self.sheet.cell_value(i, 3))
        return TestUrl

    @property
    def getResult(self):
        TestResult = []
        for i in range(1, self.getRows):
            TestResult.append(self.sheet.cell_value(i, 4))
        return TestResult

    @property
    def getCode(self):
        TestCode = []
        for i in range(1, self.getRows):
            TestCode.append(self.sheet.cell_value(i, 5))
        return TestCode