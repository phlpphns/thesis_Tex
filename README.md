# thesis_Tex
This is a template for theses in Latex. For example bachelor, master, PhD....

This template is the result of several years of work of researching at many places and using pieces of information and inputs from the internet which cannot be traced back anymore. Unless an even better license is found for future releases, for the time being this reposiory is published under the GNU GPLv3 license. You can use it for whatever you want. Never claim that is was your or anyone's else (also not my) work. Even if I compiled it, it was a common effort.


This temlate requires that several LaTeX-packages are installed. Infos will be found in the directory _Preambel_.

To visualize pieces of code _pygmentize_ is required

For compilation, you will need shell escapes like:

pdflatex -synctex=1 -interaction=nonstopmode --shell-escape template_thesis_latex

In any case have a look at the various *latex_compile** files that are provided.

Under Linux, using texlive, everything runs fine. (Acttivate the compile files with chmod +x)
For windows I do not remember problems as well.

Perhaps it also runs fine on overleaf etc.
