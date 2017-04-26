import xlrd;
def getData(start,end):
    ret = [];
    for i in range(start,end):
        ret.append(data[i]);
        print(data[i])
    return ret;

book = xlrd.open_workbook("dataFix.xlsx");
sheet = book.sheet_by_index(0);
data = []
for row in range(1, sheet.nrows):
        data.append(sheet.cell_value(row, 10));
last = 5;
first = 0;
res = [];
predict = 0;
while last < len(data) and predict < 8:
    dats  = getData(first,last);

    last += 1;
    first += 1;
    if(last == len(data)):
        data.append(dats[4]);
        res.append(dats[4]);
        predict += 1;
print(res);
print(len(res))