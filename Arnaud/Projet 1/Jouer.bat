REM echo off permet de ne pas voir ce que command fait.
@echo off
REM permet de choisir la maximum de ligne et collonnes utiliser. Standardise pour ne pas deformé le texte et image.
mode con: cols=50 lines=30
REM ouvre le jeu lui même.
python jeu.py