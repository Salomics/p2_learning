import requests
import json

class Download():

    def __init__(self, link: str):

        self.dataset = requests.get(link).text.split("\n")
        self.header = self.dataset[0].split("\t")

    def column_position(self, *columns): # *columns should be all the columns required from the dataset
        
        self.indx = []

        for column in columns:

            self.indx.append(self.header.index(column))
        
        return self.indx

    def selection(self, *colname): ## *colname should be all the columns names wanted in the lightweight dataset in the same order as *columns
        
        self.dict_output = []

        for row in self.dataset[1:len(self.dataset) -1]:

            dict_response = {}
            
            line = row.split("\t")

            if len(line) < len(self.header):
                line += [""] * (len(self.header) - len(line))

            
            for idx in range(len(colname)):

                if len(colname) != len(self.indx):
                    if len(colname) > len(self.indx):
                        for i in range(len(colname) - len(self.indx)):
                            self.indx += [len(self.indx)+1]
                    else:
                        colname += ["unkown"] * (len(self.indx) - len(colname))
                dict_response[colname[idx]] = line[self.indx[idx]]


            self.dict_output.append(dict_response)
        
        return self.dict_output

"""
hgnc_dataset = Download("https://storage.googleapis.com/public-download-files/hgnc/tsv/tsv/hgnc_complete_set.txt")
hgnc_dataset.column_position(
    "hgnc_id", "symbol", "name", "prev_symbol",
    "prev_name", "alias_name", "mane_select"
)
testing = hgnc_dataset.selection(
    "hgnc_id", "gene_symbol", "gene_name", "previous_symbols",
    "previous_names", "aliases", "mane_select", "mane_plus_clinical"
)

"""