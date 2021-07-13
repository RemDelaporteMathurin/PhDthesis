# PhDthesis


Pull the texlive Docker image

```
docker run -it -v $(pwd):/workdir danteev/texlive
```

Update Latex packages
```
tlmgr update --all
```

Compile the main.tex file

```
latexmk -pdf main.tex
```