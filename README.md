# OPMxplore
This Python module was built for a quick and interactive exploration of the [Orientations of Proteins in Membranes](http://opm.phar.umich.edu/about.php). 


The tools in this module will help to 

1. custom query membrane proteins from the database and save query for future comparisions 

2. visualize trends within 4 high level categories using the computed parameters: hydrophobic thickness, gibbs free energy, and tilt.

# Quick Start
Open the following url to see OPMxplore functions in action within a jupyter notebook rendered on nbviewer
~~~~
link to notebook: https://github.com/UWSEDS-aut17/OPMxplore/blob/master/examples/opm_explore_tutorial_1.ipynb
~~~~


# How to Run OPMxplore
1. Clone the github repo: 
~~~~
git clone https://github.com/UWSEDS-aut17/OPMxplore.git
~~~~

2. Navigate to the repo and run the following command in the terminal to install required packages:
~~~~
pip install -r requirements.txt
~~~~

3. Enable widgets for visualization within your jupyter notebook
~~~~
pip install ipywidgets
jupyter nbextension enable --py widgetsnbextension
~~~~

4. Call jupyter notebook from the repository and run examples/opm_explore_tutorial_1.ipynb

 
# Where we get our data
* [RCSB Protein Data Bank (PDB)](https://www.rcsb.org/pdb/home/home.do)
* [OPM MySQL dataset](http://opm.phar.umich.edu/OPM-2016-10-10.sql)

The [Orientations of Proteins in Membranes (OPM) database](http://opm.phar.umich.edu/about.php) is maintained by researchers from University of Michigan. They obtain the information of membrane proteins from PDB and compute the spatial arrangement of protein structures in the lipid bilayer. The OPM database has interesting features of membrane proteins such as **Localization of the membrane**, **Depth**, **Tilt angle**, and **Gibbs free energy** (how likely will the protein go into the membrane from solution).
![](doc/opm.png)


# Video Demo
<p align="center">
 <a href="http://www.youtube.com/watch?feature=player_embedded&v=8AhEcPVn3ac
" target="_blank"><img src="http://img.youtube.com/vi/8AhEcPVn3ac/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>
</p>


# Authors  
David Alan Starkebaum, Sinduja Karl Marx and Felcy Selwyn. 






