import bs4 as bs
import csv
import urllib.request
import re
sauce = urllib.request.urlopen('https://ckb.jax.org/gene/grid').read()
soup = bs.BeautifulSoup(sauce, 'lxml')
myfile = open('finalCKB.csv', 'w')
writer = csv.writer(myfile, delimiter='\t')
ckb = dict()
ckblist = list()
# gene = urllib.request.urlopen("https://ckb.jax.org/gene/show?geneId=25").read()
# soup = bs.BeautifulSoup(gene, 'lxml')
for genes in soup.find_all("a", {"class": "btn btn-default btn-gene btn-block"}):
    genesurl = genes.get('href')
    genes_url = "https://ckb.jax.org" + genesurl
    sauce1 = urllib.request.urlopen(genes_url).read()
    soup1 = bs.BeautifulSoup(sauce1, 'lxml')

    for url in soup1.find_all('a', {"class": "btn btn-default btn-gene-variant"}):
        varianturl = url.get('href')
        variant_url = "https://ckb.jax.org" + varianturl
        sauce2 = urllib.request.urlopen(variant_url).read()
        soup2 = bs.BeautifulSoup(sauce2, 'lxml')

        table = soup2.find('table')
        table_rows = table.find_all('tr')
        for tr in table_rows:
            td = tr.find_all('td')
            row = [i.text for i in td]
            row[1] = row[1].strip()
           # row[1]=row[1].replace(',','')
            ckblist.append(row)
        # text = str(ckblist[6][1])
        regex = re.compile(r'\d{8}')
        x = regex.findall(str(ckblist[6][1]))
        if x == None:
            x = 'NA'
        # print(ckblist, "\n\n", len(ckblist), "\n\n\n\n")
        # print(ckblist[0][1])

        for i in range(0, len(ckblist) - 1, 7):
            #            print(ckblist[i][1])
            rows = zip([ckblist[i][1]], [ckblist[i + 1][1]], [ckblist[i + 2][1]],
                       [ckblist[i + 3][1]], [ckblist[i + 4][1]], [ckblist[i + 5][1]], x)
            for row in rows:
                writer.writerow(row)
                # print(row)
