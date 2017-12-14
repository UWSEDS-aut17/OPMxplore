# OPMxplore


**Membrane proteins** are of three types: **Transmembrane**, **Monotopic** and **Small Peptides**. Membrane proteins have interesting structures and funtions.
![](doc/Membrane_prot.png | width=100)



The[**Orientation of Membrane Protein (OPM)** database](http://opm.phar.umich.edu/about.php) is maintained by researchers from University of Michigan. They obtain the information of membrane proteins from PDB and compute the spatial arrangement of protein structures in the lipid bilayer. The OPM database has interesting features of membrane proteins such as **Localization of the membrane**, **Depth**, **Tilt angle**, and **Gibbs free energy** (how likely will the protein go into the membrane from solution).
![](doc/opm.png | width=100)


#**Project Description**

This Python module was built for a quick and interactive exploration of the [OPM website](http://opm.phar.umich.edu/about.php). 
The tools in this module will help to 
1. custom query membrane proteins from the database and save query for future comparisions 
2. visualize trends within 4 high level categories using the computed parameters: hydrophobic thickness, gibbs free energy, and tilt.

### Quick Start



### How to Run OPMxplore

1. Clone the github repo: (https://github.com/UWSEDS-aut17/OPMxplore.git)

2. Navigate to the repo and run the following command in the terminal to install required packages:
~~~~
pip install -r requirements.txt`
~~~~

3. Enable widgets for visualization within your jupyter notebook
~~~~
pip install ipywidgets
jupyter nbextension enable --py widgetsnbextension`
~~~~

4. Call jupyter notebook from the repository and run examples/opm_explore_tutorial_1.ipynb

 
### **Data**

* [RCSB Protein Data Bank (PDB)](https://www.rcsb.org/pdb/home/home.do)- use PyPDB to query.
* [OPM MySQL dataset](http://opm.phar.umich.edu/OPM-2016-10-10.sql)- download mySQL file.

### **Visualization Demo**

<iframe width="560" height="315" src="https://www.youtube.com/embed/8AhEcPVn3ac" frameborder="0" gesture="media" allow="encrypted-media" allowfullscreen></iframe>


**Authors** : David Alan Starkebaum, Sinduja Karl Marx and Felcy Selwyn. 






