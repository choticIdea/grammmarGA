import random as r
import Translator;
import xlrd;
import copy;

class Individu():
    """docstring for Individu"""

    def __init__(self, kromosom, bitsPerCode):
        # kromosom isinya array of integer antara 0 atau 1
        self.kromosom = kromosom;
        self.fitness();
        self.prodCode = [];
        idx = 0;
        num = 0;
        for c in kromosom:
            idx += 1;
            if (idx > 0 and idx % bitsPerCode == 0):
                self.prodCode.append(num);
                num = 0;
            num += 2 ^ (idx % bitsperCode) * c;

    def fitness(self):
        # fungsi translasi dipanggil sebelash sini
        return None;

    def translasi(self):
        # fungsi untuk mentranslasi deretan biner dari 0,1
        # menjadi suatu persamaan
        ret = Translator.bintodec(self.kromosom);
        return ret;


bitsperCode = 9;
cromosomCode = 10;
generation = 100;
epoch = 0;


def random_indv(panjang):
    # menghasilkan individu dengan kromosom acak dari 0 samapi 1
    # panjang kromosom  = panjang
    calon_kromosom = []
    for i in range(panjang):
        calon_kromosom.append(r.randint(0, 1))
    return Individu(calon_kromosom, bitsperCode)


def random_populasi(jum_indiv, panjang):
    # membangkitkan populasi dari fungsi random individu
    calon_populasi = []
    for i in range(jum_indiv):
        calon_populasi.append(random_indv(panjang))
    return calon_populasi


def cross_over(indv1, indv2):
    # melakukan operasi pindah silang, dengan satu titik potong acak
    titik_potong = r.randint(0, len(indv2.kromosom))
    anak1 = indv1.kromosom[:titik_potong] + indv2.kromosom[titik_potong:]
    anak2 = indv2.kromosom[:titik_potong] + indv1.kromosom[titik_potong:]
    return Individu(anak1), Individu(anak2)


def mutasi(individu, permutation_rate):
    # melakukan mutasi dengan membalik nilai bit pada kromosom individu
    mutan = []
    for gen in individu.kromosom:
        p = r.uniform(0, 1)
        if p <= permutation_rate:
            if gen == 0:
                mutan.append(1)
            else:
                mutan.append(0)
        else:
            mutan.append(gen)
    return Individu(mutan)


def convert(translateCode):
    if (translateCode == Translator.prev):
        return prev;
    elif (translateCode == Translator.close):
        return close;
    elif (translateCode == Translator.low):
        return low;
    elif (translateCode == Translator.high):
        return high;


def compute(f, rowData):
    ret = 0;
    stack = [];
    while len(f) != 0:
        if (Translator.isOperator(f[len(f) - 1]) == False):
            idx = convert(f.pop())
            stack.append(rowData[idx])

        else:

            opr = f.pop();
            if (opr == Translator.plus):
                res = stack.pop() + stack.pop();
            elif (opr == Translator.minus):
                res = stack.pop() - stack.pop();
            elif (opr == Translator.times):
                res = stack.pop() * stack.pop();
            elif (opr == Translator.division):
                res = stack.pop() / stack.pop();
            print(res);
            stack.append(res);
    return stack.pop() - rowData[avg]


# loading data;
book = xlrd.open_workbook("DataHistorisANTAM.xlsx");
sheet = book.sheet_by_index(0);
data = []
drow = []
for row in range(1, sheet.nrows):
    drow = [];
    for col in range(sheet.ncols):
        drow.append(sheet.cell_value(row, col));
    data.append(drow);

# constants defining
# coloumn index in data
prev = 0
open = 1
high = 2
low = 3
close = 4
avg = 10;
#

pops = random_populasi(1, bitsperCode * cromosomCode);
formula = Translator.placebo();

totalSE = 0;
t = 0;
for row in data:
    f = copy.copy(formula);
    t = compute(f, row);
    t = t * t;
    totalSE += t;
mse = totalSE / len(data);
print(mse);


# replacing pops with better one
