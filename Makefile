# name of the project/PDF to create
PAPER=main

# define the tools
LATEX := pdflatex
BIBTEX := bibtex

# define the flags for each tool
LATEX_FLAGS := -shell-escape -halt-on-error
BIBTEX_FLAGS := -terse

# targets
PDF := $(PAPER).pdf
TEX_INPUTS:= $(wildcard *.tex) $(wildcard *.cls)
GENERATED_FIGS := $(DIAFIGS:.dia=.eps) $(PNGFIGS:.png=.eps)

AUX := 	$(PDF:.pdf=.aux) $(PDF:.pdf=.log) $(PDF:.pdf=.toc) \
	$(PDF:.pdf=.lof) $(PDF:.pdf=.lot) $(PDF:.pdf=.bbl) \
	$(PDF:.pdf=.blg) $(PDF:.pdf=.aux.bak)


.PHONY:		all clean
.PRECIOUS:	$(DVI)

all:	$(PDF)

clean:	
	$(RM) $(PDF) $(PS) $(DVI) $(AUX) $(BBL)


%.pdf:   $(TEX_INPUTS) %.bib
	@echo "Running $(LATEX) on $*.tex"
	@$(LATEX) $(LATEX_FLAGS) $*.tex


bib:
	@echo "running bib"
	$(BIBTEX) $(BIBTEX_FLAGS) $(PAPER)

watermark: all
	@rm -f $(PAPER)-draft.pdf
	@pdftk $(PAPER).pdf background wmark/wmark.pdf output $(PAPER)-draft.pdf


