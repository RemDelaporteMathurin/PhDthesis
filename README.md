# PhDthesis

[Download the latest release (pdf)](https://github.com/remdelaportemathurin/phdthesis/releases/latest/download/main.pdf)

To compile locally, simply run:

```
docker run --rm -it -v $(pwd):/workdir danteev/texlive latexmk -pdf main.tex
```
