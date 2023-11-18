import brickschema

# creates a new rdflib.Graph with a recent version of the Brick ontology
# preloaded.
g = brickschema.Graph(load_brick=True)

# load in data files from your file system
g.load_file("assets/ashp_brick.ttl")

# perform reasoning on the graph (edits in-place)
g.expand(profile="shacl")

# validate your Brick graph against built-in shapes (or add your own)
valid, _, resultsText = g.validate()
if not valid:
    print("Graph is not valid!")
    print(resultsText)

