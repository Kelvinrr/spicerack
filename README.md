# spicerack

Application for managing and syncing SPICE server data

An overview of spice can be found at: https://naif.jpl.nasa.gov/pub/naif/toolkit_docs/Tutorials/pdf/individual_docs/03_spice_overview.pdf

FAQ

What is SPICE?

SPICE stands for Spacecraft Planet Instrument Camera-matrix Events. This is the
collection of Ancillary Data used by scientists and engineers to determine the
locations and orientations of spacecrafts and planetary objects.

What are the different data kernels(files)?

- Spacecraft --> SPK
- Planet --> SPK and PcK
- Instrument --> IK
- C-Matrix --> CK
- Events --> EK (ESP, ESQ, ENB)

Different Parts of SpiceRack:
- PandasHashing: Contains code that hashes a dataframe to tell if the dataframe's contain different data
- P2P_ChatServer: Contains code for two classes that act as a client and a server, and can send simple text messages between    Client_One and Client_Two inside separate Docker containers
- RestfulDirectory: Contains a Flask app that builds your local file system in a ReSFTful way. Each directory you can delve into more by putting into the running app on localhost



In order for this to work:

- Need to add everyone to a config.txt file that you want to be synced with
- Need to generate ssh keys using ssh-keygen (The path to that key must be
                                              listed in the ssh.py file, and run
                                              the ssh.py script as well)
