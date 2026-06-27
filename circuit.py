from components import Net
class Circuit:
    def __init__(self):
        self.nets = {}
        self.gates = []
    def add_net(self, name, initial_value=0):
        if name not in self.nets:
            self.nets[name] = Net(name, initial_value)
        return self.nets[name]
    def add_gate(self, gate_class, name, input_names, output_names):
        # Create corresponding Net objects by name
        inputs = [self.add_net(n) for n in input_names]
        outputs = [self.add_net(n) for n in output_names]
        # Instantiate the logic gate and add it to the circuit
        gate_instance = gate_class(name, inputs, outputs)
        self.gates.append(gate_instance)
    def simulate(self, time_steps):
        print("Starting simulation...")
        for step in range(time_steps):
            print(f"\n--- Time Step {step} ---")
            # Iterate and calculate logic for all gates
            for gate in self.gates:
                gate.calculateLogic()            
            # Print the current state of all Nets
            for name, net in sorted(self.nets.items()):
                print(f"Net '{name}': {net.value}")