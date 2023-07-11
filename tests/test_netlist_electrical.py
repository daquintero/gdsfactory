"""The intention of this test file is to test the functionality of the electrical netlist extraction, layout pin
addition, circuit model composition, and more. """
import gdsfactory as gf
import sax


@gf.cell
def connected_metal():
    test = gf.Component()
    a = test << gf.components.straight(cross_section="metal1")
    test.add_ports(a.ports)
    return test


connected_metal().show()
print(connected_metal().get_netlist())
print(sax.get_required_circuit_models(connected_metal().get_netlist()))
