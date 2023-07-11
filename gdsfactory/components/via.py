from __future__ import annotations

from functools import partial
from typing import Optional, Tuple

import gdsfactory as gf
from gdsfactory.component import Component
from gdsfactory.typings import LayerSpec


@gf.cell
def via(
    size: Tuple[float, float] = (0.7, 0.7),
    spacing: Optional[Tuple[float, float]] = (2.0, 2.0),
    gap: Optional[Tuple[float, float]] = None,
    enclosure: float = 1.0,
    layer: LayerSpec = "VIAC",
    layers_connect_map: tuple = ("M2", "HEATER"),
    bbox_layers: Optional[Tuple[Tuple[int, int], ...]] = None,
    bbox_offset: float = 0,
    add_pins: bool = True,
) -> Component:
    """Rectangular via.

    Defaults to a square via.

     For compatibility with SPICE, standard LVS and RCX tools such as Cadence, we need to place pins in the PIN
     purpose layer for each drawing layer. Include the `add_pins_from_ports` flag in order to enable this
     compatibility. In terms of this via, we need to add pins of the corresponding metal layers in the top and bottom
     layers of each VIA.

    Args:
        size: in x, y direction.
        spacing: pitch_x, pitch_y.
        gap: edge to edge via gap in x, y.
        enclosure: inclusion of via.
        layer: via layer.
        layers_connect_map(tuple): Tuple that maps the connectivity to include pins
        bbox_layers: layers for the bounding box.
        bbox_offset: in um.
        add_pins(bool): Add via contact pins.

    .. code::

        enclosure
        _________________________________________
        |<--->                                  |
        |             gap[0]    size[0]         |
        |             <------> <----->          |
        |      ______          ______           |
        |     |      |        |      |          |
        |     |      |        |      |  size[1] |
        |     |______|        |______|          |
        |      <------------->                  |
        |         spacing[0]                    |
        |_______________________________________|
    """
    if spacing is None and gap is None:
        raise ValueError("either spacing or gap should be defined")
    elif spacing is not None and gap is not None:
        raise ValueError("You can't define spacing and gap at the same time")
    if spacing is None:
        spacing = (size[0] + gap[0], size[1] + gap[1])

    c = Component()
    c.info["spacing"] = spacing
    c.info["enclosure"] = enclosure
    c.info["size"] = size

    width, height = size
    a = width / 2
    b = height / 2
    c.add_polygon([(-a, -b), (a, -b), (a, b), (-a, b)], layer=layer)

    bbox_layers = bbox_layers or []
    a = (width + bbox_offset) / 2
    b = (height + bbox_offset) / 2
    for layer in bbox_layers:
        c.add_polygon([(-a, -b), (a, -b), (a, b), (-a, b)], layer=layer)

    if add_pins:
        for pin_layer_i in layers_connect_map:
            c.add_polygon([(-a, -b), (a, -b), (a, b), (-a, b)], layer=pin_layer_i)

    return c


viac = partial(via, layer="VIAC")
via1 = partial(via, layer="VIA1", enclosure=2)
via2 = partial(via, layer="VIA2")

if __name__ == "__main__":
    c = via()
    # c.pprint()
    print(c)
    c.show(show_ports=True)
