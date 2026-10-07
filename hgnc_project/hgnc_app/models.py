from json import dumps

def search_hgnc(inp, light_dataset):
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

    formatted_user_data = dumps(user_dataset)
    return formatted_user_data