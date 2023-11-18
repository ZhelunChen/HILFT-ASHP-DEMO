import brickschema

# creates a new rdflib.Graph with a recent version of the Brick ontology
# preloaded.
# g = brickschema.Graph(load_brick=True)
g = brickschema.Graph()

# load occupancy extension
# g.load_file("brick-occupancy-extension-master/Brick-1.3.0.ttl")
# g.load_file("brick-occupancy-extension-master/enumerations.ttl")
# g.load_file("brick-occupancy-extension-master/equipment.ttl")
# g.load_file("brick-occupancy-extension-master/occupants.ttl")
# g.load_file("brick-occupancy-extension-master/points.ttl")
# g.load_file("brick-occupancy-extension-master/rules.ttl")
# g.load_file("brick-occupancy-extension-master/core.ttl")

# load in data files from your file system
g.load_file("assets/ashp_brick.ttl")
# g.load_file("brick-occupancy-extension-master/example1.ttl")

# validating using externally-defined shapes
external = brickschema.Graph()
external.load_file("assets/brick_occ_ext.ttl")
valid, _, report = g.validate(shape_graphs=[external])
print(f"Graph is valid? {valid}")
if not valid:
  print(report)

