# thesis_Tex
This is a template for theses in Latex. For example bachelor, master, PhD....

This template is the result of several years of work of researching at many places and using pieces of information and inputs from the internet which cannot be traced back anymore. In spite of this unless a better license is found for future releases, for the time being this reposiory is published under the GNU GPLv3. You can use it for whatever you want but never claim that is was your or anyone's else (also not my) work.

This temlate requires that several LaTeX-packages are installed. 

To visualize pieces of code, _pygmentize_ is required

For compilation, you will need shell escapes like:

pdflatex -synctex=1 -interaction=nonstopmode --shell-escape template_thesis_latex

In any case have a look at the varioius provided *latex_compile** files.

Under Linux, using texlive, everthing runs fine. (Acttivate with chmod +x)
For windows I do not remember problems as well.

Perhaps it also runs fine on overleaf etc.
