pdflatex -synctex=1 -interaction=nonstopmode --shell-escape template_thesis_latex.tex
bibtex.exe .\template_thesis_latex
pdflatex -synctex=1 -interaction=nonstopmode --shell-escape template_thesis_latex.tex
pdflatex -synctex=1 -interaction=nonstopmode --shell-escape template_thesis_latex.tex
