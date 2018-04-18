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
            d["has_security_pins"] = (l[2] =="yes" and True) or \
                    (l[2] == "no" and False) or "n.a"
        yield d


if __name__ == "__main__":
    g = load_data(".")
    for d in g:
        pprint(d)
