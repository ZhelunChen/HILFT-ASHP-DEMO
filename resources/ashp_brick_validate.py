from brickschema import Graph

# g = Graph(load_brick=True)
# print(list(g.namespaces()))
external = Graph()
external.load_file("resources/Brick_v1-3-0.ttl")
g = Graph()
g.load_file('assets/hil_ashp_brick_v1-3-0.ttl')
# valid, _, report = g.validate()
valid, _, report = g.validate(shape_graphs=[external])
print(f"Graph is valid? {valid}")
if not valid:
  print(report)
# g = brickschema.Graph()

# # validating using externally-defined shapes
# external = Graph()
# external.load_file("assets/brick_occ_ext.ttl")
# valid, _, report = g.validate(shape_graphs=[external])
# print(f"Graph is valid? {valid}")
# if not valid:
#   print(report)

# from rdflib import Namespace
# from buildingmotif import BuildingMOTIF
# from buildingmotif.dataclasses import Model, Library
# from buildingmotif.namespaces import BRICK

# # in-memory instance
# bm = BuildingMOTIF("sqlite://")

# # create the namespace for the building
# BLDG = Namespace('urn:bldg/')

# # create the building model
# model = Model.create(BLDG, description="This is a test model for a simple building")

# # load tutorial 1 model
# model.graph.parse("tutorial1_model.ttl", format="ttl")

# brick = Library.load(ontology_graph="../../libraries/brick/Brick-subset.ttl")