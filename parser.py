import csv, os
from pprint import pprint

def load_data(data_folder):
    pinsfile = os.path.join(data_folder,"pins.csv")
    assert os.path.exists(pinsfile)
    r = csv.reader(open(pinsfile,"r").readlines()[1:],delimiter='\t')
    for l in r:
        d = {"_id":l[0], "model" : l[0]}
        try:
            d["pins_num"] = int(l[1])
        except ValueError:
            d["pins_num"] = 0
        if len(l) == 3:
            val = None
            if l[2] =="yes":
                val = True
            elif l[2] =="no":
                val = False
            d["has_security_pins"] = val
        yield d


if __name__ == "__main__":
    g = load_data(".")
    for d in g:
        pprint(d)
