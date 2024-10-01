# RITHM_Cogshifting

This repository contains all the code needed to reproduce the RITHM Cogshifting task using Psychopy 2022.2.5 [here](https://github.com/psychopy/psychopy/releases/tag/2022.2.5). In this version, simuli can be letters but also robot video clips.

```
📦RITHM_Cogshifting
 ┣ 📂data    
 ┃ ┣ 📂subject_0
 ┃ ┣ 📂subject_1
 ┃ ┗ ...
 ┣ 📂robot_stimuli <-- video clips are supposed to be downloaded here
 ┃ ┗ 📜.gitkeep
 ┣ 📂Scripts
 ┣ 📜generate_conditions.ipynb
 ┣ 📜robot_cogshifting_sign_lastrun.py
 ┣ 📜robot_cogshifting_sign.psyexp
 ┣ 📜cogshifting_results.ipynb
 ┗ 📜README.md
 ```

Several notebooks are here for data manipulation :
- 📜generate_conditions.ipynb allows to manipulate task initial parameters by modifying one 📜conditions.csv or more
- 📜cogshifting_results.ipynb allows to process results
