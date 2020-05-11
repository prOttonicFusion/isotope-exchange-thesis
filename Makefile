
thesis.pdf: thesis.bbl 
	pdflatex thesis.tex
	pdflatex thesis.tex

thesis.bbl: thesis.aux
	bibtex thesis.aux

thesis.aux:
	pdflatex thesis.tex

clean:
	rm -f *.aux *.bbl *.blg *.log *.nlo *.out *.toc
