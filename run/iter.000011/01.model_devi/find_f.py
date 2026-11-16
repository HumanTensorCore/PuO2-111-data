#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import glob
import numpy as np

task_dirs = sorted(glob.glob("task.*.*"))

if len(task_dirs) == 0:
    print("No task directories found!")
    exit()

print("=" * 80)
print("DPGEN Per-Task Force Statistics")
print("=" * 80)

for task in task_dirs:

    model_file = os.path.join(task, "model_devi.out")
    traj_file  = os.path.join(task, "all.lammpstrj")

    if not os.path.exists(model_file):
        continue

    if not os.path.exists(traj_file):
        continue

    avg_devi_list = []
    force_list = []

    # =====================================================
    # read model_devi.out
    # =====================================================

    with open(model_file, "r") as f:

        for line in f:

            line = line.strip()

            if line.startswith("#") or len(line) == 0:
                continue

            parts = line.split()

            avg_devi_f = float(parts[-1])

            avg_devi_list.append(avg_devi_f)

    # =====================================================
    # read all.lammpstrj
    # =====================================================

    with open(traj_file, "r") as f:

        reading_atoms = False

        for line in f:

            if "ITEM: ATOMS" in line:
                reading_atoms = True
                continue

            if "ITEM:" in line:
                reading_atoms = False
                continue

            if reading_atoms:

                parts = line.split()

                try:
                    fx = float(parts[5])
                    fy = float(parts[6])
                    fz = float(parts[7])

                except:
                    continue

                ff = np.sqrt(fx**2 + fy**2 + fz**2)

                force_list.append(ff)

    if len(avg_devi_list) == 0 or len(force_list) == 0:
        continue

    # =====================================================
    # statistics
    # =====================================================

    avg_devi = np.mean(avg_devi_list)

    force_mean = np.mean(force_list)
    force_median = np.median(force_list)
    force_max = np.max(force_list)

    relative_error = avg_devi / force_mean * 100.0

    # =====================================================
    # output
    # =====================================================

    print("-" * 80)
    print(f"{task}")

    print(f"avg_devi_f      : {avg_devi:.6f} eV/Å")
    print(f"average |F|     : {force_mean:.6f} eV/Å")
    print(f"median  |F|     : {force_median:.6f} eV/Å")
    print(f"maximum |F|     : {force_max:.6f} eV/Å")
    print(f"relative error  : {relative_error:.2f} %")

print("-" * 80)
print("Done.")