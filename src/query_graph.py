import rdflib
from rdflib.namespace import RDF, RDFS


g = rdflib.Graph()
rdf_file = "../data/mesh_cell_adhesion.rdf"

print(f"Loading RDF data from {rdf_file}...")
g.parse(rdf_file, format="xml")
print(f"Graph loaded! It has {len(g)} triples.\n")


PREFIXES = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX mesh: <http://id.nlm.nih.gov/mesh/>
    PREFIX vocab: <http://id.nlm.nih.gov/mesh/vocab#>
"""


query = PREFIXES + """
SELECT ?qualifierURI ?qualifierLabel ?treeNumberURI
WHERE {
  mesh:D015815 vocab:allowableQualifier ?qualifierURI .
  OPTIONAL { ?qualifierURI rdfs:label ?qualifierLabel . }
  ?qualifierURI vocab:treeNumber ?treeNumberURI .
}
"""

print("Executing Query: Fetching Tree Numbers for Allowable Qualifiers...")
results = g.query(query)


print(f"{'Qualifier Label':<30} | {'Tree Number URI'}")
print("-" * 60)
for row in results:
    label = str(row.qualifierLabel) if row.qualifierLabel else "No Label"
    tree_uri = str(row.treeNumberURI).split('/')[-1] # Show only the ID part
    print(f"{label:<30} | {tree_uri}")