# Minecraft Horse Breeding Tool
A command-line tool for predicting and managing Minecraft horse breeding stats.

## Features

- Add / delete / modify horses
- Detect dominated (backward/baka) horses
- Sort by attributes or weighted score
- Predict offspring stats (using **Jump Strength inheritance**)
- Accurate non-linear jump height conversion

## Jump Model

Jump Height H is computed from Jump Strength J:

H(J) = -0.1817584952·J³ + 3.689713992·J² + 2.128599134·J − 0.343930367  
(Valid for 0.4 ≤ J ≤ 1.0)

## Usage

```bash
python horse.py
