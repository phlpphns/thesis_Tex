#!/usr/bin/python3

import sys
#import os


#directory = "."
#extension = ".png"
#files = [file for file in os.listdir(directory) if file.lower().endswith(extension)]
#for file in files:

with open(sys.argv[1], 'w') as file:
	for fileName in sys.argv[2:]:
		reference = fileName.strip('.'+fileName.split(sep='.')[-1])
		print(r"\begin{figure}",  file=file)
		print(r"	\centering",  file=file)
		print(r"	\includegraphics[height=0.45\textheight,width=\textwidth]{%s.png}" % reference,  file=file)
		print(r"	\caption{Refinement of %s done with X}" % reference.split(sep='_')[-1],   file=file)
		print(r"	\label{fig:ref_%s}" % reference.split(sep='_')[-1],  file=file)
		print(r"\end{figure}",  file=file)
		print(file=file)
		print(file=file)

