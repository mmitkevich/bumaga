ls -1 *.tex|xargs -I% pandoc % -o md/%.md
