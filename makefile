BUILD = build

pdf:
	mkdir -p $(BUILD)
	cd $(BUILD)
	latexmk -r latexmkrc -pdf *.tex -interaction=nonstopmode || true 

clean:
	rm -rf $(BUILD)

.PHONY: build clean