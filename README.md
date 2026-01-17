# MeSH Biomedical Ontology Modeling

A semantic web project that models biomedical knowledge using the **Medical Subject Headings (MeSH)** ontology standards. This repository contains an RDF implementation of the "Cell Adhesion Molecules" descriptor and a set of SPARQL queries to extract hierarchical and associative relationships.

## Project Overview
The goal of this project was to represent specific biomedical concepts using **RDF/XML** and **OWL** standards, following the official NLM MeSH Linked Data structure.

**Key Entity Modeled:**
* **Descriptor:** `Cell Adhesion Molecules` (MeSH ID: [D015815](https://id.nlm.nih.gov/mesh/D015815.html))
* **Qualifiers:** Modeled linked resources including `chemical synthesis`, `pharmacokinetics`, and `toxicity`.
* **Hierarchies:** Implementation of Tree Numbers and parent/child relationships.

## Technologies
* **Semantic Web:** RDF, RDFS, OWL
* **Query Language:** SPARQL 1.1
* **Tools:** Protégé 5.x, Python (`rdflib`)
* **Source Data:** [National Library of Medicine (NLM) Linked Data](https://id.nlm.nih.gov/)

## Repository Structure
* `data/`: Contains the ontology file (`mesh_cell_adhesion.rdf`) in RDF/XML format.
* `queries/`: Collection of SPARQL queries used for data verification and extraction.
* `src/`: Python script demonstrating how to programmatically load and query the graph.
* `docs/`: Detailed project report and implementation notes.

## SPARQL Capabilities
The project includes optimized SPARQL queries to retrieve:
1.  **Tree Numbers & Qualifiers:** Retrieving allowable qualifiers and their hierarchy references.
2.  **Metadata Extraction:** Fetching `prefLabel`, `dateCreated`, and active status.
3.  **Concept Identifiers:** Mapping descriptors to their unique Concept IDs (e.g., M0024222).
4.  **Schema Introspection:** Dynamically listing all utilized Object and Datatype properties.

*Example Result (Screenshot from Protégé):*
<img width="900" height="369" alt="sparql_results" src="https://github.com/user-attachments/assets/658df391-c864-4fca-9e7c-0dc7de60efbd" />

##  Ontology Visualization (Generated from RDF)
```mermaid
graph TD
    %% --- Main Descriptor (The Center of your work) ---
    %% Source: 
    MAIN[("**Cell Adhesion Molecules**<br/>(D015815)")]

    %% --- Allowable Qualifiers ---
    %% Source: linked to Q000138, Q000493, Q000633
    Q1("Chemical Synthesis<br/>(Q000138)")
    Q2("Pharmacokinetics<br/>(Q000493)")
    Q3("Toxicity<br/>(Q000633)")

    %% --- Concepts (Preferred & Narrower) ---
    %% Source: 
    M_PREF("Preferred Concept<br/>(M0024220)")
    M_SACC("Saccharide-Mediated<br/>(M0024222)")
    M_INTER("Intercellular<br/>(M0024223)")
    M_LEUK("Leukocyte<br/>(M0024224)")

    %% --- Broader Descriptors ---
    %% Source: linked to D000954, D008562
    B1("Antigens, Surface<br/>(D000954)")
    B2("Membrane Glycoproteins<br/>(D008562)")

    %% --- Tree Numbers ---
    %% Source: 
    T1["TreeNum: D09.400..."]
    T2["TreeNum: D12.776..."]
    T3["TreeNum: D23.050..."]

    %% --- Styling for Professional Look ---
    style MAIN fill:#f96,stroke:#333,stroke-width:3px,color:white
    style M_PREF fill:#ff9,stroke:#333
    style B1 fill:#ddd,stroke:#999,stroke-dasharray: 5 5
    style B2 fill:#ddd,stroke:#999,stroke-dasharray: 5 5

    %% --- Relationships defined in your RDF ---
    MAIN -- "vocab:allowableQualifier" --> Q1
    MAIN -- "vocab:allowableQualifier" --> Q2
    MAIN -- "vocab:allowableQualifier" --> Q3

    MAIN -- "vocab:preferredConcept" --> M_PREF
    MAIN -- "vocab:concept" --> M_SACC
    MAIN -- "vocab:concept" --> M_INTER
    MAIN -- "vocab:concept" --> M_LEUK

    MAIN -- "vocab:broaderDescriptor" --> B1
    MAIN -- "vocab:broaderDescriptor" --> B2

    MAIN -- "vocab:treeNumber" --> T1
    MAIN -- "vocab:treeNumber" --> T2
    MAIN -- "vocab:treeNumber" --> T3
 ```


##  How to Run (Python)
To reproduce the query results programmatically without Protégé:

1.  **Install dependencies:**
    ```bash
    pip install rdflib
    ```
2.  **Run the script:**
    ```bash
    cd src
    python query_graph.py
    ```

##  Implementation Notes
* **Data Types:** Due to specific tooling versions, some date fields were modeled to ensure compatibility with standard XML Schema types.
* **Expansion:** The model captures depth-2 relationships for instances like *chemical synthesis* (Q000138) to demonstrate inter-connectivity between Descriptors and Qualifiers.

## Author
**Chatziroufas Konstantinos**
