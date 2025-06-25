find . -maxdepth 1 -type f \( -name "*.acn" -o -name "*.alg" -o -name "*.bbl" -o -name "*.brf" -o -name "*.glo" -o -name "*.ist" -o -name "*.out" -o -name "*.acr" -o -name "*.aux" -o -name "*.blg" -o -name "*.glg" -o -name "*.gls" -o -name "*.log" -o -name "*.pdf" -o -name "*.toc" \) -delete

pdflatex mydocument.tex
bibtex mydocument
makeglossaries mydocument
pdflatex mydocument.tex
pdflatex mydocument.tex 