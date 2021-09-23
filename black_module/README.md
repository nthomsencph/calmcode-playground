
# Black commands
Code-along @ https://calmcode.io/black/introduction.html <br>

## Install black
`pip install black`

## Run black
`black code.py` will output the following if any changes are made.

    reformatted code.py
    All done! ✨ 🍰 ✨
    1 file reformatted.

Then run again and see

    All done! ✨ 🍰 ✨
    1 file left unchanged.

## Specify line length
This is pretty much the only customization that Black offers..
Black, by design, is a very opiniated tool. This is itentional.

    black --line-length 100 code.py


## Add black as pre-commit hook
Create `.pre-commit-config.yaml` file

    repos:
        - repo: https://github.com/psf/black
          rev: stable
          hooks:
           - id: black
             language_version: python3.8