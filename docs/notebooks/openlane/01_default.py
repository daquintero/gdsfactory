# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .md
#       format_name: markdown
#       format_version: '1.1'
#       jupytext_version: 1.1.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---
import gdsfactory as gf

# # Get Started - OpenLane Integration
# Please read the environment setup instructions provided in docs/plugins_openlane before attempting this notebook, otherwise it will not work.

# ## Default Example Setup
# We use in our example the standard `spm` design which is the default example given by `OpenLane` as described in [this tutorial](https://openlane.readthedocs.io/en/latest/getting_started/quickstart.html#) but we will build it using the Python API and then interact with it through GDSFactory.
# To start you need to copy the `spm` design files into the `/foss/design` directory and access it under the docker environment. A function that does this for the `IIC-OSIC-TOOLS` environment is provided:


# This python file also needs to be copied into this directory. This is already included in the standard openlane2 installation, so in this integration we provide an example setup function.
