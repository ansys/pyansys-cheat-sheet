BUILD = build

pdf:
	latexmk -f -pdf Cheat_Sheet_Template_3.tex -use-make cheat_sheets/Cheat_Sheet_Template_3.tex -cd -outdir=$(BUILD) -interaction=nonstopmode || true

clean:
	rm -rf cheat_sheets/$(BUILD)

.PHONY: build clean