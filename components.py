class Net:
    """Represents a wire/net in the circuit, used to store logic level state"""
    def __init__(self, name, initial_value=0):
        self.name = name
        self.value = initial_value
class LogicGate:
    """Base class for all logic gates"""
    def __init__(self, name, input_nets, output_nets):
        self.name = name
        self.input_nets = input_nets   # List containing Net objects
        self.output_nets = output_nets # List containing Net objects
        self.gate_state = 0            # Only used for flip-flops
    def calculateLogic(self):
        raise NotImplementedError("Subclasses must implement specific logic")
class AndGate(LogicGate):
    def calculateLogic(self):
        result = 1
        for net in self.input_nets:
            if net.value == 0:
                result = 0
                break
        for net in self.output_nets:
            net.value = result
class OrGate(LogicGate):
    def calculateLogic(self):
        result = 0
        for net in self.input_nets:
            if net.value == 1:
                result = 1
                break
        for net in self.output_nets:
            net.value = result
class NotGate(LogicGate):
    """NOT gate: Assumes only one input, inverts the input signal"""
    def calculateLogic(self):
        result = 1 if self.input_nets[0].value == 0 else 0
        for net in self.output_nets:
            net.value = result
class NorGate(LogicGate):
    """NOR gate: Outputs 1 when all inputs are 0, otherwise outputs 0"""
    def calculateLogic(self):
        # First calculate OR
        or_result = 0
        for net in self.input_nets:
            if net.value == 1:
                or_result = 1
                break
        # Then invert (NOT)
        result = 1 if or_result == 0 else 0
        for net in self.output_nets:
            net.value = result
class NandGate(LogicGate):
    """NAND gate: Outputs 0 when all inputs are 1, otherwise outputs 1"""
    def calculateLogic(self):
        and_result = 1
        for net in self.input_nets:
            if net.value == 0:
                and_result = 0
                break
        result = 1 if and_result == 0 else 0
        for net in self.output_nets:
            net.value = result
class XorGate(LogicGate):
    """XOR gate: Assumes dual input, outputs 1 if inputs are different, 0 if same"""
    def calculateLogic(self):
        if len(self.input_nets) != 2:
            raise ValueError(f"XOR gate '{self.name}' should have exactly 2 inputs!")
        val1 = self.input_nets[0].value
        val2 = self.input_nets[1].value
        # 1 when not equal
        result = 1 if val1 != val2 else 0
        for net in self.output_nets:
            net.value = result
class XnorGate(LogicGate):
    """XNOR gate: Assumes dual input, outputs 1 if inputs are same, 0 if different"""
    def calculateLogic(self):
        if len(self.input_nets) != 2:
            raise ValueError(f"XNOR gate '{self.name}' should have exactly 2 inputs!")
        val1 = self.input_nets[0].value
        val2 = self.input_nets[1].value
        # 1 when equal
        result = 1 if val1 == val2 else 0
        for net in self.output_nets:
            net.value = result
class MuxGate(LogicGate):
    def calculateLogic(self):
        if len(self.input_nets) != 3:
            raise ValueError(f"MUX gate '{self.name}' requires exactly 3 inputs: [I0, I1, S]")
        
        i0 = self.input_nets[0].value
        i1 = self.input_nets[1].value
        s  = self.input_nets[2].value
        
        result = i1 if s == 1 else i0
        
        for net in self.output_nets:
            net.value = result

class DemuxGate(LogicGate):
    def calculateLogic(self):
        if len(self.input_nets) != 2:
            raise ValueError(f"DEMUX gate '{self.name}' requires exactly 2 inputs: [I, S]")
        if len(self.output_nets) != 2:
            raise ValueError(f"DEMUX gate '{self.name}' requires exactly 2 outputs: [Y0, Y1]")
            
        i = self.input_nets[0].value
        s = self.input_nets[1].value
        
        y0 = i if s == 0 else 0
        y1 = i if s == 1 else 0
        
        self.output_nets[0].value = y0
        self.output_nets[1].value = y1

class DFlipFlop(LogicGate):
    def __init__(self, name, input_nets, output_nets):
        super().__init__(name, input_nets, output_nets)
        self.prev_clk = 0
        self.gate_state = 0

    def calculateLogic(self):
        if len(self.input_nets) != 2:
            raise ValueError(f"DFF '{self.name}' requires exactly 2 inputs: [D, CLK]")
            
        d = self.input_nets[0].value
        clk = self.input_nets[1].value
        
        if clk == 1 and self.prev_clk == 0:
            self.gate_state = d
            
        self.prev_clk = clk
        
        for net in self.output_nets:
            net.value = self.gate_state

            