
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
  
  OPTIONAL {
  ?article schema:about ?item .
  ?article schema:inLanguage "en" .
  FILTER (SUBSTR(str(?article), 1, 25) = "https://en.wikipedia.org/")
  }
}
ORDER BY 
  DESC (?sitelink_protein)  
"""

sparqlwd.setQuery(query)
sparqlwd.setReturnFormat(JSON)
data = sparqlwd.query().convert()


protein_names = []
for result in data["results"]["bindings"]: 
    protein_names.append(result["uniprot_id"]["value"])

fixed_names = []
for protein in protein_names: 
    if len(protein) == 6:
        fixed_names.append(protein)
    else:
        continue

with open("src/constants/wordlist.ts", "w+") as f:
    f.write("export const WORDS = " +json.dumps(fixed_names[1:1000],indent=4))

fixed_names.sort()
with open("src/constants/validGuesses.ts", "w") as f:
    f.write("export const VALID_GUESSES = " + json.dumps(fixed_names,indent=4))