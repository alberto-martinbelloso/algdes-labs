from algorithm import maximum_flow
from input_parser import parse_input_to_model

edges = parse_input_to_model()

result = maximum_flow(edges, 0, 54)
print("Res ")
for res in result:
    print(res)



