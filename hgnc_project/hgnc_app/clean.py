from .download import Download

def clean(link):
    dataset = Download(link)
    dataset.column_position(
        "hgnc_id", "symbol", "name", "prev_symbol", "prev_name", "alias_name", "mane_select"
    )
    selected_data = dataset.selection(
        "hgnc_id", "gene_symbol", "gene_name", "previous_symbols", "previous_names", "aliases",
        "mane_select", "mane_plus_clinical"
    )

    for object in selected_data:
        for key, val in object.items():
            if '"' in val:
                object[key] = val.replace('"', "")

    for object in selected_data:
        for key, val in object.items():
            if '|' in val:
                object[key] = val.split("|")

    for object in selected_data:
        for key, val in object.items():
            if ',' in val:
                object[key] = val.split(", ")

    for object in selected_data:
        for key, val in object.items():
            if val == "":
                object[key] = "Not available"

    return selected_data