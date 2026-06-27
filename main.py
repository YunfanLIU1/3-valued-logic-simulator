from circuit import Circuit
# Import all 7 types of logic gates
from components import AndGate, OrGate, NotGate, NorGate, NandGate, XorGate, XnorGate
def main():
    # Instantiate the circuit
    my_circuit = Circuit()
    my_circuit.add_net("A", 1)
    my_circuit.add_net("B", 0)
    # Test all gates
    my_circuit.add_gate(AndGate,  "Gate_AND",  ["A", "B"], ["Out_AND"])  
    my_circuit.add_gate(OrGate,   "Gate_OR",   ["A", "B"], ["Out_OR"])    
    my_circuit.add_gate(NotGate,  "Gate_NOT",  ["A"],      ["Out_NOT_A"]) 
    my_circuit.add_gate(NorGate,  "Gate_NOR",  ["A", "B"], ["Out_NOR"])   
    my_circuit.add_gate(NandGate, "Gate_NAND", ["A", "B"], ["Out_NAND"])  
    my_circuit.add_gate(XorGate,  "Gate_XOR",  ["A", "B"], ["Out_XOR"])   
    my_circuit.add_gate(XnorGate, "Gate_XNOR", ["A", "B"], ["Out_XNOR"])    
    # Run 1 time step to see the results
    my_circuit.simulate(1)
if __name__ == "__main__":
    main()