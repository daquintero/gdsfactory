# OpenROAD OpenLane Integration

This is still very much of a beta implementation, due to the inherent nature of [OpenLane2](https://openlane2.readthedocs.io/en/latest/#) which is a full python rewrite led by Efabless.

This integration is meant to provide initial bindings that can then be extended for more-production-ready designs as OpenLane2 matures.

## Environment Setup

[OpenLane OpenROAD](https://openlane.readthedocs.io/) and [GDSFactory](https://gdsfactory.github.io/gdsfactory/) need to be in the same python environment for this integration to work. This can be achieved through a custom docker environment which mirrors the [standard OpenLane installation](https://openlane.readthedocs.io/en/latest/getting_started/installation/index.html). A recommended docker environment is the [IIC-OSIC-TOOLS](https://github.com/iic-jku/iic-osic-tools) maintained by [ Institute for Integrated Circuits (IIC), Johannes Kepler University (JKU)](https://iic.jku.at/).

Follow the environment installation instructions provided here for the [IIC-OSIC-TOOLS docker environment](https://github.com/iic-jku/iic-osic-tools).

Another untested option is that you can also install `gdsfactory` into the default `OpenLane2` environment that is the [dockerized installation](https://openlane2.readthedocs.io/en/latest/getting_started/docker_installation/installation_ubuntu.html). This might be the direction of development towards the future.

## Project Setup

`OpenLane` converts HDL-to-GDS. This means that you need a design directory to contain all your digital design sources and possibly testbenches. It is recommended that the digital design directory should follow this minimum structure approximately:

```
design_folder_name
    io/
        pin_order.cfg
    sdc/
        design.sdc
    src/
        source_files.v
    tb/
        testbench.v
```

After OpenLane runs the project structure will include a `runs` folder that will contain all the generated files for particular design runs. The recommendation is that you place this design folder inside the `/foss/designs` IIC-OSIC-TOOLS Docker environment. From there you can continue all your GDSFactory-flow design afterwards.

## Get Started Example

Get started with [this notebook](../docs/notebooks/openlane/01_default.py).
