from clean import *

def search():
    inp = input("Search the information required using HGNC or gene_symbol nomeclature: ").upper()

    light_dataset = clean("https://storage.googleapis.com/public-download-files/hgnc/tsv/tsv/hgnc_complete_set.txt")
    n = 0

    for object in light_dataset:
        if object["hgnc_id"] == inp:
            user_dataset = object
            break
        elif object["gene_symbol"] == inp:
            user_dataset = object
            break
        else:
            n += 1
            continue

    if n == len(light_dataset):
        user_dataset = "Un_available"

    formatted_user_data = json.dumps(user_dataset)
    return formatted_user_data