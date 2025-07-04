# Reeborg's World - Maze Solving Project

This folder contains the code and resources for the Day 6 final project: solving a maze with Reeborg. The primary challenge was not just to find the exit, but to create a robust algorithm that avoids common pitfalls like infinite loops.

---

## Folder Contents

This directory contains the following files:

* `reeborgs_project.py`: The initial Python code written to solve the maze. This version contains a logical flaw that can lead to an infinite loop in certain maze configurations.
* `reeborgs_project_debbuged.py`: The final, corrected version of the code. This script successfully navigates all test mazes without getting stuck.
* `01_reeborgs_challenge_error_1.png`: A screenshot illustrating the infinite loop scenario where Reeborg gets trapped in a cycle.
* `01_reeborgs_challenge_error_solution_1.png`: A screenshot showing the logic of the corrected code that breaks the infinite loop.
* `Reeborg+World+Tests.zip`: A zip file containing various maze worlds. These can be imported into Reeborg's World to test the algorithm against different scenarios and confirm that the infinite loop bug has been resolved.

---

## The Infinite Loop Problem

The initial approach (`reeborgs_project.py`) was based on a simple "follow the right wall" logic. While this works for many mazes, it fails in specific patterns, particularly in open squares or U-shaped turns.

As shown in `01_reeborgs_challenge_error_1.png`, Reeborg can enter a state where it continuously cycles between the same few tiles, never reaching the goal. This happens because the logic doesn't account for scenarios where turning right leads back into the loop.

---

## The Solution

The bug was fixed in `reeborgs_project_debbuged.py` by refining the logic to be more defensive. The key change was to prioritize moving forward when possible and only turning as a last resort.

The corrected algorithm follows a clearer hierarchy:

1.  If the path to the right is clear, turn right and move.
2.  Else, if the path forward is clear, move forward.
3.  Else (if blocked on the right and front), turn left.

This prevents Reeborg from turning back on itself unnecessarily and successfully breaks the infinite loop, as illustrated in `01_reeborgs_challenge_error_solution_1.png`.

---

## Testing Scenarios

To ensure the solution is robust, use the `Reeborg+World+Tests.zip` file. Unzip it and import the different world files into the Reeborg's World environment to test the `reeborgs_project_debbuged.py` script against multiple maze layouts.
