from circuit import Circuit
from components import (AndGate, OrGate, NotGate, NorGate, NandGate, XorGate, XnorGate, 
                        MuxGate, DemuxGate, DFlipFlop)

def main():
    my_circuit = Circuit()
    
    my_circuit.add_net("A", 1)
    my_circuit.add_net("B", 0)
    
    my_circuit.add_gate(AndGate,  "Gate_AND",  ["A", "B"], ["Out_AND"])  
    my_circuit.add_gate(OrGate,   "Gate_OR",   ["A", "B"], ["Out_OR"])    
    my_circuit.add_gate(NotGate,  "Gate_NOT",  ["A"],      ["Out_NOT_A"]) 
    my_circuit.add_gate(NorGate,  "Gate_NOR",  ["A", "B"], ["Out_NOR"])   
    my_circuit.add_gate(NandGate, "Gate_NAND", ["A", "B"], ["Out_NAND"])  
    my_circuit.add_gate(XorGate,  "Gate_XOR",  ["A", "B"], ["Out_XOR"])   
    my_circuit.add_gate(XnorGate, "Gate_XNOR", ["A", "B"], ["Out_XNOR"])    

    my_circuit.add_net("I0", 1)
    my_circuit.add_net("I1", 0)
    my_circuit.add_net("S", 0)
    
    my_circuit.add_net("D", 1)
    my_circuit.add_net("CLK", 0)

    my_circuit.add_gate(MuxGate, "Gate_MUX", ["I0", "I1", "S"], ["Out_MUX"])
    my_circuit.add_gate(DemuxGate, "Gate_DEMUX", ["A", "S"], ["Out_DEMUX_Y0", "Out_DEMUX_Y1"])
    my_circuit.add_gate(DFlipFlop, "Gate_DFF", ["D", "CLK"], ["Out_DFF_Q"])

    print("--- Time Step 0 ---")
    my_circuit.simulate(1)
    
    print("\n--- Time Step 1 ---")
    my_circuit.nets["S"].value = 1
    my_circuit.nets["CLK"].value = 1
    my_circuit.nets["D"].value = 0
    
    my_circuit.simulate(1)

if __name__ == "__main__":
    main()