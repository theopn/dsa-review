# Theo's Data Structures & Algorithms Review

[Click here to access the document](./dsa-review.pdf)

Here is my "comprehensive" review for Data Structures & Algorithms

Materials loosely based on

- Purdue University CS251: Data Structures & Algorithms, taught in fall of 2022 by Prof. Andres Bejarano
- Introduction to Algorithms Third Edition by "CLRS"

Compiled with:

- [MacTeX ~2023~ ~2024~ 2025](https://www.tug.org/mactex/)
- confirmed to be compile-able with [TeX Live](https://tug.org/texlive/)
- Compile command: the standard `<leader>ll` keybinding in [VimTeX](https://github.com/lervag/vimtex)

Requires:

- [latex-gruvbox-colorscheme](https://gitlab.com/import-benjamin/latex-gruvbox-colorscheme/) for the beautiful Gruvbox theme (included in the repository)
- [Pypgments] for Python highlights using [minted](https://github.com/gpoore/minted)

Most of the algorithms in the document are written in Python to provide real-life implementation.
You can find the sources in the [code](./code/) directory.
**Some test cases are generated with generative AI models**, either Windsurf model using [Neocodeium](https://github.com/monkoose/neocodeium) Neovim plugin or OpenAI ChatGPT.
However, AI uses were restricted to the generation of test cases and all codes are direct Python translation of pseudocodes in CLRS.
Other pseudocodes are in the standard academic pseudocode form and written using [algpseudocodex](https://ctan.org/pkg/algpseudocodex) package, mainly because I got lazy and did not want to implement them in Python.

Constructive criticism are always welcome, but I do not take any responsibility for any errors in the document.

## "I do not like the theme"

You are weird, but you an comment out `\usepackage{gruvbox-theme}` and re-compile.

