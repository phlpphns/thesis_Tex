# thesis_Tex
This is a template for theses in Latex. For example bachelor, master, PhD....

## general:

This template is the result of several years of work of researching at many places and using pieces of information and inputs from the internet which cannot be traced back anymore. Unless an even better license is found for future releases, for the time being this reposiory is published under the GNU GPLv3 license. You can use it for whatever you want. Never claim that is was your or anyone's else (also not my) work. Even if I compiled it, it was a common effort.

## prerequisites

This temlate requires that several LaTeX-packages are installed. Infos will be found in the directory _Preambel_. Using MikTex on Windows allows to install needed packages on the fly. TexLive (Linux) is easy as well, install them via apt. There is a MikTex for several Linux distros as wel.

To visualize pieces of code _pygmentize_ is required. Often it is already available, Windows didn't give errors).

## usage

---> For compilation, you will need shell escapes like:

*pdflatex -synctex=1 -interaction=nonstopmode --shell-escape template_thesis_latex*

If you are using TexStudio press ALT+T and then T to open the console (terminal). Use one of the the various *latex_compile\** files that are provided.

Under Linux, acttivate the compile files with chmod +x.

Perhaps it also runs fine on overleaf etc.
