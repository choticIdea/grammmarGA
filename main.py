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
    a = Individu(anak1,bitsperCode);
    b = Individu(anak2,bitsperCode)
    child = [];
    child.append(a);
    child.append(b);
    rnd = r.randint(1,100);
    if(rnd > mutationRate):
       child.append(mutasi(a,mutationRate));
       child.append(mutasi(b,mutationRate));
    return child

def getData(start,end):
    ret = [];
    for i in range(start,end):
        ret.append(data[i][avg]);
    return ret;
def mutasi(individu, permutation_rate):
    # melakukan mutasi dengan membalik nilai bit pada kromosom individu
    mutan = []
    for gen in individu.kromosom:
        p = r.uniform(0, 1) * 100;
        if p > permutation_rate:
            if gen == 0:
                mutan.append(1)
            else:
                mutan.append(0)
        else:
            mutan.append(gen)
    return Individu(mutan,bitsperCode)


def convert(translateCode):
    if (translateCode == Translator.first):
        return prev;
    elif (translateCode == Translator.fifth):
        return close;
    elif (translateCode == Translator.fourth):
        return low;
    elif (translateCode == Translator.third):
        return high;
    elif (translateCode == Translator.second):
        return open;
def createZeros(size):
    z = [];
    for i in range(0,size):
        z.append(0);
    return z;


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
                x1 = stack.pop();
                x2 = stack.pop();
                if(x2 != 0):
                    res = x1 / x2;
                else :
                    return x1;# -1 is infinite symbol, hence the Error is automatically set big;

            stack.append(res);

    return stack.pop();


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
mutationRate = 40;#ranging from 1-100 , this number is chance to mutate in percentage
#
epoch = 0;
maxEpoch = 150;
startingPops =40;
pops = random_populasi(startingPops, bitsperCode * cromosomCode);

#formula = Translator.translate(pops[0].prodCode);
totalSE = 0;
while epoch < maxEpoch:
    #generate new pops/child
    clone = copy.copy(pops);

    while(len(clone) != 0):
        children = cross_over(clone.pop(),clone.pop());
        pops = pops+children;

    msePops = [];
    #evaluate
    for individu in pops:
        formula = [];

        formula = Translator.translate(individu.prodCode);

        f = copy.copy(formula)
        print(f);
        v = Translator.verify(f);


        if(v == False):
            msePops.append(100000);
            continue;


        else:
            last = 5;
            first = 0;
            while (last < len(data) - 1):
                row = getData(first, last);



                if (v == False):
                    break;
                f = copy.copy(formula)

                t = compute(f, row);
                t = abs(t-data[last][avg]);
                t = t * t;
                totalSE += t;
                first += 1;
                last += 1
            mse = totalSE / len(data);
        msePops.append(mse);
        mse = 0;
        totalSE = 0;



    #sorting
    bestMSE = -1;
    idx = 0;
    t = [];
    for i in range(len(pops)):
        for k in range(i, len(pops)):
            if (bestMSE == -1 or bestMSE > msePops[k]):
                bestMSE = msePops[k];
                idx = k;

        t = pops[i];
        pops[i] = pops[idx];
        pops[idx] = t;
        t = msePops[i];
        msePops[i] = msePops[idx];
        msePops[idx] = t;

        idx = -1;
        bestMSE = -1;
    print(msePops)
    #culling weak individuals
    pops = pops[:startingPops];
    msePops = msePops[:startingPops];
    print(msePops)
    epoch+= 1;
print(Translator.translate(pops[0].prodCode));


