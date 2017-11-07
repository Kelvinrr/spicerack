# spicerack

Application for managing and syncing SPICE server data

An overview of spice can be found at: https://naif.jpl.nasa.gov/pub/naif/toolkit_docs/Tutorials/pdf/individual_docs/03_spice_overview.pdf

FAQ

What is SPICE?

SPICE stands for Spacecraft Planet Instrument Camera-matrix Events. This is the
collection of Ancillary Data used by scientists and engineers to determine the
locations and orientations of spacecrafts and planetary objects.

What are the different data kernels(files)?

Spacecraft --> SPK
Planet --> SPK and PcK
Instrument --> IK
C-Matrix --> CK
Events --> EK (ESP, ESQ, ENB)
Others

# Running the Sample App

If necessary, build the docker image.  Then run the service and navigate to localhost:5000 to see the JSON response.

```bash
$ docker build -t spicerack .
$ docker run -v 5000:5000 spicerack 
```
