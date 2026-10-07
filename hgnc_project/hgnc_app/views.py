from typing import Any, Dict, Optional

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

import requests
from .models import search_hgnc
from .clean import clean
from json import loads


hgnc_data = clean("https://storage.googleapis.com/public-download-files/hgnc/tsv/tsv/hgnc_complete_set.txt")

def home(request: HttpRequest) -> HttpResponse:
    return render(request, "hgnc_app/index.html")

def search(request: HttpRequest) -> HttpResponse:
    if request.method != "POST":
        return render(request, "hgnc_app/index.html")

    gene = request.POST.get("gene", "").strip().upper()

    if not gene:
        return render(
            request,
            "hgnc_app/index.html",
            {
                "output_text_1": "Error: No gene provided.",
                "output_text_2": "",
            }
    )
    
    response_data = loads(search_hgnc(gene, hgnc_data))

    if response_data == "Un_available":
        return render(
            request,
            "hgnc_app/index.html",
            {
                "output_text_1": f"Error: '{gene}' not found.",
                "output_text_2": "",
            },
        )    

    return render(
            request,
            "hgnc_app/index.html",
            {
                "output_text_1": f"The Gene identifiers are: {
                    response_data.get("hgnc_id")} and {response_data.get("gene_symbol")
                }",
                "output_text_2": f"""Here is more information about this gene:

gene_name: {response_data.get("gene_name")}
previous_symbols: {response_data.get("previous_symbols")}
previous_names: {response_data.get("previous_names")}
aliases: {response_data.get("aliases")}
mane_select: {response_data.get("mane_select")}
mane_plus_clinical: {response_data.get("mane_plus_clinical")}
"""
            },
        )