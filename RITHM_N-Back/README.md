# RITHM_N-Back

This repository contains all the code needed to reproduce the RITHM version of N-Back task using Psychopy 2022.2.5 [here](https://github.com/psychopy/psychopy/releases/tag/2022.2.5). In this version, simuli can be letters but also robot video clips.

```
📦RITHM_N-Back
 ┣ 📂data    
 ┃ ┣ 📂subject_0
 ┃ ┣ 📂subject_1
 ┃ ┗ ...
 ┣ 📂robot_stimuli <-- video clips are supposed to be downloaded here
 ┃ ┗ 📜.gitkeep
 ┣ 📂Scripts
 ┣ 📜generate_conditions.ipynb
 ┣ 📜robot_nback_sign_lastrun.py
 ┣ 📜robot_nback_sign.psyexp
 ┣ 📜nback_results.ipynb
 ┗ 📜README.md
 ```

Several notebooks are here for data manipulation :
- 📜generate_conditions.ipynb allows to manipulate task initial parameters by modifying one 📜conditions.csv or more
- 📜nback_results.ipynb allows to process results
