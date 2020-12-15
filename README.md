# A Molecular Dynamics Study of Hydrogen Isotope Exchange in Tungsten

A PDF version of the thesis can be found at http://urn.fi/URN:NBN:fi:hulib-202012114996

## Abstract
Due to its exceptional thermal properties and irradiation resistance, tungsten is the material of choice for critical plasma-facing components in many leading thermonuclear fusion projects.
Owing to the natural retention of hydrogen isotopes in materials such as tungsten, the safety of a fusion device depends heavily on the inventory of radioactive tritium in its plasma-facing components. 
The proposed methods of tritium removal typically include thermal treatment of massive metal structures for prolonged timescales.
A novel way to either shorten the treatment times or lower the required temperatures is based performing the removal under an H-2 atmosphere, effectively exchanging the trapped tritium for non-radioactive protium. 

In this thesis, we employ molecular dynamics simulations to study the mechanism of hydrogen isotope exchange in vacancy, dislocation and grain boundary type defects in tungsten.
By comparing the results to simulations of purely diffusion-based tritium removal methods, we establish that hydrogen isotope exchange indeed facilitates faster removal of tritium for all studied defect types at temperatures of 500 K and above.
The fastest removal, when normalising based on the initial occupation of the defect, is shown to occur in vacancies and the slowest in grain boundaries.   
Through an atom level study of the mechanism, we are able to verify that tritium removal using isotope exchange depends on keeping the defect saturated with hydrogen.

This study also works to show that molecular dynamics indeed is a valid tool for studying tritium removal and isotope exchange in general. 
Using small system sizes and spatially-parallelised simulation tools, we have managed to model isotope exchange for timescales extending from hundreds of nanoseconds up to several microseconds.

## Building

### Requirements
- [TexLive](https://www.tug.org/texlive/) or similar
- BibTex & MakeIndex (usually distributed with LaTex)
- The following LaTex packages
	- amsmath, amssymb
	- bf, bm
	- fancyhdr
	- geometry
	- graphicx
	- lastpage
	- lmodern
	- miller
	- subcaption
	- textcomp
	- tikz
	- titlesec, titletoc

### Compilation
The thesis can be compiled using the proved `Makefile`, by simply running
```
make
```
from within the `tex/` directory. Temporary files can be removed using
```
make clean
```
