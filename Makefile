
thesis.pdf: thesis.bbl thesis.nls
	pdflatex thesis.tex
	pdflatex thesis.tex

thesis.bbl: thesis.aux
	bibtex thesis.aux

thesis.aux:
	pdflatex thesis.tex

thesis.nls:
	makeindex thesis.nlo -s nomencl.ist -o thesis.nls

clean:
	rm -f *.aux *.bbl *.blg *.log *.nlo *.out *.toc *.nls
