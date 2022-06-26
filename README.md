# PhD Thesis

### [Download the latest release (pdf)](https://github.com/remdelaportemathurin/phdthesis/releases/latest/download/main.pdf)


## Compile
To compile locally, simply run:

```
docker run --rm -it -v $(pwd):/workdir danteev/texlive latexmk -pdf main.tex
```

## How to reproduce

I've made a big effort to make this thesis as reproducible as possible!

Find the repositories to reproduce the results shown in this manuscript:

- Chapter 2:
    - Section 2.5.1 Analytical verification:
        - [Case 1: H transport MES](https://github.com/RemDelaporteMathurin/PhDthesis/blob/main/scripts/mes_simple_diffusion.py)
        - Case 2a: 1D H transport MMS: need to find the repo
        - Case 2b: 2D H transport MMS: need to find the repo
    - [Section 2.5.2 Experimental validation](https://github.com/RemDelaporteMathurin/tds_optimisation)
    - [Section 2.5.3 Comparison with TMAP7](https://github.com/RemDelaporteMathurin/interface_conditions_paper)

- Chapter 3:
    - Section 3.2 Simulation simplifications:
        - [Section 3.2.1 Thermal behaviour](https://github.com/RemDelaporteMathurin/monoblock_parametric)
        - [Section 3.2.2 Influence of dimensionality](https://github.com/RemDelaporteMathurin/monoblock_dimension_effects)
        - [Section 3.2.3 Influence of interface condition](https://github.com/RemDelaporteMathurin/monoblock_interface_condition)
        - [Section 3.2.4 Influence of cycling](https://github.com/RemDelaporteMathurin/monoblock_cycling)
    - [Section 3.3 Monoblock behaviour law](https://github.com/RemDelaporteMathurin/monoblock_parametric)
- [Chapter 4](https://github.com/RemDelaporteMathurin/divHretention-Nucl.Fusion-2021)
- Chapter 5:
    - [Section 5.2 Direct implantation](https://github.com/RemDelaporteMathurin/he_fenics)
    - Section 5.3 Indirect sources:
        - [Section 5.3.1 Neutron induced transmutation](https://github.com/RemDelaporteMathurin/monoblock_neutronics)
        - [Section 5.3.2 Tritium Decay](https://github.com/RemDelaporteMathurin/t_decay_in_monoblocks)
    - [Section 5.4 Influence on H transport](https://github.com/RemDelaporteMathurin/he_h_coupling)
- Appendix:
    - A. FESTIM verification:
        - [A.1 Conservation of chemical potential (MES)](https://github.com/RemDelaporteMathurin/interface_conditions_paper)
        - [A.2 Conservation of chemical potential (MMS)](https://github.com/RemDelaporteMathurin/interface_conditions_paper)
        - [A.3 Heat transfer (MMS)](https://github.com/RemDelaporteMathurin/PhDthesis/blob/main/scripts/verif_heat_transfer_elbow.py)
    - [B. Interface transient model](https://github.com/RemDelaporteMathurin/interface_conditions_paper)
    - [C. DEMO monoblocks](https://github.com/RemDelaporteMathurin/3d_monoblocks)