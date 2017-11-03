UWSEDS Project FALL 2017: Querying the PDB for membrane channel information
Team: David, Sinduja, Felcy 

Google Doc version here:
https://docs.google.com/document/d/1m4w0s52DFaE7JMSy4-kE9RmaTrE5Mm0xX00IIsKHyIA/edit

Upcoming Events:
Standup - 11/3 - Present on current status of project (<1min)

Technology review - 11/15 - groups will present in round-robin fashion.


# Pick your Data :
RCSB - PDB database of proteins

# Define the problem (determine type of project and questions of interest):  
 - teaching/exploration tool for channel proteins from the protein data bank
 - Incorporate existing tools and stitch them together into a unified user interface.
 - Allow a user to search the PDB database for specific patterns, 
    and visualize the structures, and do analysis on the amino acid 
    and structural information within a set of PDB’s found by search criteria 

# Write the Functional Specification:

# Who will use it?
 - Protein/peptide researchers with some basic understanding of python scripting
 - What information might users want?
 - Ex: “What is the statistical amino acid contents and secondary structures of membrane proteins, 
   grouped by inward-facing and outward-facing regions of a membrane pore 
   (protein multimer embedded in cell membrane)”

# Use Cases - how will users interact with system?
 - Users could use functions we will write (including documentation and examples), 
   either in their own scripts or as part of a jupyter-notebook template

# Project development:
 - Explore PyPDB (a python package for pdb visualization)
 - Write package for interacting with other relevant software (such as HOLE, dssp)
 - Iterate on other ideas

Short term deliverables: - 
 - Access database **explore PyPDB pakage**
 - Visualize membrane proteins in membrane plane – 3d pymol image **TOOLS**
 - Plot sequence hydropathy plot, ** ANALYSES **
 - secondary structure ** TOOLS **
 - Match or frequency of fragment? ** COMPUTATION ** *maybe*
 - HOLE API access for some data statistics **TOOLS**
 
| Goals | Components | Date
| --- | --- | --- |
| Retrieve sequence data | pyPDB (package for accessing pdb data)| |
| display 3d images | pymol python tools | |
| plot hydropathy plot | matplotlib, or gui style widget | |
| plot secondary structure | use DSSP database |
| frequency of fragment | plotting package, computation funcitons
| API to HOLE | | |
| ..?| | |
 
Resources: 
HOLE: http://www.sciencedirect.com/science/article/pii/S026378559700009X
http://www.holeprogram.org/


Pypdb - API for searching the PDB database: can be used to perform advanced searches for PDB IDs matching various criteria, as well as to look up information associated with specific PDB IDs within Python scripts, allowing it to supplement existing tools (i.e. Biopython) that are designed for manipulating .pdb files.
https://github.com/williamgilpin/pypdb

Biopandas: Python tool to convert PDB and MOL2 files into in pandas DataFrames
https://github.com/rasbt/biopandas

Ipymol: Interface to run Pymol visualization software using python, within jupyter notebook
http://nbviewer.jupyter.org/github/cxhernandez/iPyMol/blob/master/examples/Example1.ipynb

https://omictools.com/protein-channel-detection-category
specific to channels..and other software packages out there.
a database for just channels from pdb
https://webchemdev.ncbr.muni.cz/ChannelsDB/

"Defined Secondary Structure of Proteins"
http://swift.cmbi.ru.nl/gv/dssp/

"VPLG -- The Visualization of Protein-Ligand Graphs"
https://sourceforge.net/projects/vplg/



