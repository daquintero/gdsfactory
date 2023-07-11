"""
Tests that we get a suitable electrical netlist that represents the physical geometry of our circuit.

We use the `get_missing_models` function in `sax` to extract that it is representing our netlist component correctly.
"""
import gdsfactory as gf
import sax


def test_extract_electrical_netlist_straight_heater_metal():
    """
    This component is a good test because it contains electrical and optical ports, and we can see how effective the
    implementation of adding ports is in this case.

    What we want here is to extract all the electrical models required from our netlist. If our netlist is properly
    composed, then it is possible to have a connectivity that actually represents electrical elements in our circuit,
    and hence, eventually convert it to SPICE.
    """
    our_heater = gf.components.straight_heater_metal()
    our_heater.show()
    our_heater_netlist = our_heater.get_netlist(
        exclude_port_types="optical",
        # allow_multiple=True,
    )
    # print(our_heater_netlist)
    print(sax.get_required_circuit_models(our_heater_netlist))
    print(our_heater_netlist["instances"].keys())
    print(our_heater_netlist["connections"].keys())


def test_netlist_model_extraction():
    """
    Tests that our PIN placement allows the netlister and sax to extract our electrical component model in a composed circuit.
    """

    @gf.cell
    def connected_metal():
        test = gf.Component()
        a = test << gf.components.straight(cross_section="metal1")
        test.add_ports(a.ports)
        return test

    connected_metal().show()
    models_list = sax.get_required_circuit_models(connected_metal().get_netlist())
    # print(models_list)
    assert models_list == ["straight"]

    models_list_electrical_netlist = sax.get_required_circuit_models(
        connected_metal().get_netlist(exclude_port_types="optical")
    )
    # print(models_list_electrical_netlist)
    assert models_list == models_list_electrical_netlist


def test_via_array_netlist_connectivity():
    """
    We want to test how the pins generated in a via array allow us to extract connectivity for its component in between metal layers.
    """
    our_via_stack = gf.components.via_stack()
    our_via_stack.show()
    pass


if __name__ == "__main__":
    # TODO turn all back on.
    test_extract_electrical_netlist_straight_heater_metal()
    # test_netlist_model_extraction()
    # test_via_array_netlist_connectivity()
