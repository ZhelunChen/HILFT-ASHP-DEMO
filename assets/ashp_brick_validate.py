from brickschema import Graph

# creates a new rdflib.Graph with a recent version of the Brick ontology
# preloaded.
g = Graph(load_brick=True)
# g = Graph()
g.load_file('assets/ashp_brick.ttl')
# valid, _, _ = g.validate()
# print(f"Graph is valid? {valid}")
# g = brickschema.Graph()

# validating using externally-defined shapes
external = Graph()
external.load_file("assets/brick_occ_ext.ttl")
valid, _, report = g.validate(shape_graphs=[external])
print(f"Graph is valid? {valid}")
if not valid:
  print(report)

