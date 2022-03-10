import json
from SPARQLWrapper import SPARQLWrapper, JSON

sparqlwd = SPARQLWrapper("https://query.wikidata.org/sparql")

query = """
SELECT DISTINCT
  ?item ?uniprot_id ?score ?article
WHERE 
{
  ?item wdt:P352 ?uniprot_id .
  ?item wdt:P703 wd:Q15978631 .
  ?item wikibase:sitelinks ?sitelink_protein .
  
  ?article schema:about ?item .
  ?article schema:inLanguage "en" .
  FILTER (SUBSTR(str(?article), 1, 25) = "https://en.wikipedia.org/")
}
ORDER BY 
  DESC (?score)  
"""

sparqlwd.setQuery(query)
sparqlwd.setReturnFormat(JSON)
data = sparqlwd.query().convert()

wikipedia_pages = {}
for result in data["results"]["bindings"]: 
    protein = result["uniprot_id"]["value"]
    if len(protein) == 6:
        fixed_name = protein
    try:
      wikipedia_pages[fixed_name] = result["article"]["value"]
    except:
      wikipedia_pages[fixed_name] = "None"


with open("src/constants/wikipedialist.json", "w+") as f:
    f.write(json.dumps(wikipedia_pages,indent=4))