import pandas as pd
import copy
from pprint import pprint
from .str_wrapper import strf

class Converter:
    def __init__(self, fstream):
        self.fstream = fstream

    def convert(self, excel_path):
        sheet = pd.read_excel(excel_path)
        cols = list(sheet)
        nodelist = []
        for index, row in sheet.iterrows():
            node = copy.deepcopy(self.convert_row(cols, row))
            if node is None:
                continue
            nodelist.append(node)
        if len(nodelist) == 1:
            pprint(nodelist[0], self.fstream)
        else:
            pprint(nodelist, self.fstream)



    def convert_row(self, cols, row):
        json = {}
        jpaths = {}
        vals = {}
        jp_no = 0

        for col in cols:
            val = row.loc[col]
            if pd.isna(val):
                continue
            if isinstance(val, str):
                val = strf(val)
            vals.update({jp_no: val})

            jpath = col.split('__')
            for idx, field in enumerate(jpath):
                jpath[idx] = strf(field)
            jpaths.update({jp_no: jpath})

            jp_no += 1
        # jpaths.sort(key=len, reverse = True)
        
        if vals == {}:
            return None

        for path_no in range(0, jp_no):
            json = self.generate_json(jpaths[path_no], json, vals[path_no])
       
        return json
            

    def generate_json(self, jpath, json, val):
        if len(jpath) == 0:
            return val
        if jpath[0] not in json:
            json.update({jpath[0]: self.generate_json(jpath[1:], {}, val)})
            return json
        else:
            json[jpath[0]].update( 
                    self.generate_json( 
                        jpath[1:], json[jpath[0]], val 
                        )  
                )
            return json      
