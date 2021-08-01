# PhDthesis


Pull the texlive Docker image

```
docker run -it -v $(pwd):/workdir danteev/texlive:edge
```

Update Latex packages (if needed)
```
tlmgr update --all
```

Compile the main.tex file

```
latexmk -pdf main.tex
```
