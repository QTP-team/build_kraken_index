import argparse
import subprocess

parser = argparse.ArgumentParser(
        usage = 'python rules/complete_taxo.py -i data/taxo.txt -t data/tmp.txt -o data/complete_taxo.txt')
parser.add_argument("-i", "--infile", help = 'Output file from gtdbtk')
parser.add_argument("-t", "--tmp", help = 'Extract classification information')
parser.add_argument("-o", "--output", help = 'Complete classification file')

args = parser.parse_args()

gtdbtk_file = open(args.infile, "r")
tmp_file = open(args.tmp, "w")
subprocess.run(["awk","-F","\t",'NR>1{ print $1"\t"$2 }'], encoding = 'UTF-8', stdin = gtdbtk_file, stdout = tmp_file)
tmp_file.close()
f_o = open(args.output, "w")
f_o.write("Genome_ID\tTaxo\n")

list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []
list7 = []
list8 = []
for i in open(args.tmp).readlines():
    items = i.split("\t")
    Genome_ID,Taxo = items[0],items[1]
    Taxos = Taxo.split(";")
    Kingdom,Phylum,Class,Ordes,Family,Genus,Species = Taxos[0],Taxos[1],Taxos[2],Taxos[3],Taxos[4],Taxos[5],Taxos[6].strip()
    list1.append(Genome_ID)
    list2.append(Kingdom)
    list3.append(Phylum)
    list4.append(Class)
    list5.append(Ordes)
    list6.append(Family)
    list7.append(Genus)
    list8.append(Species)

for i in range(len(list1)):
    if len(list2[i]) == 3:
        list2[i] = list2[i] + list1[i]


for i in range(len(list1)):
    if len(list3[i]) == 3:
        list3[i] = list3[i] + list1[i]


for i in range(len(list1)):
    if len(list4[i]) == 3:
        list4[i] = list4[i] + list1[i]


for i in range(len(list1)):
    if len(list5[i]) == 3:
        list5[i] = list5[i] + list1[i]


for i in range(len(list1)):
    if len(list6[i]) == 3:
        list6[i] = list6[i] + list1[i]


for i in range(len(list1)):
    if len(list7[i]) == 3:
        list7[i] = list7[i] + list1[i]


for i in range(len(list1)):
    if len(list8[i]) != 3:
        list8[i] = list8[i]


for i in range(len(list1)):
    if len(list8[i]) == 3:
        list8[i] = list8[i] + list7[i][3:] + " " + list1[i]

for i in range(len(list1)):
    nstr = "%s\t%s;%s;%s;%s;%s;%s;%s\n" %(list1[i],list2[i],list3[i],list4[i],list5[i],list6[i],list7[i],list8[i])
    f_o.write(nstr)
f_o.close()
