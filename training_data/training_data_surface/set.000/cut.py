"""
切除 DeePMD npy 训练数据的最后 N 帧
用法: python trim_npy.py <数据目录> [--n 400] [--out 输出目录]

示例:
  python trim_npy.py ./data/02             # 切除最后400帧，原地覆盖
  python trim_npy.py ./data/02 --n 200     # 切除最后200帧
  python trim_npy.py ./data/02 --out ./data/02_clean  # 输出到新目录
"""

import argparse
import numpy as np
import os
import shutil

NPY_FILES = ["box", "coord", "energy", "force", "virial",
             "atom_ener", "atom_pref"]   # virial等可选，不存在自动跳过

def trim_system(data_dir, n_trim, out_dir):
    os.makedirs(out_dir, exist_ok=True)

    # 复制 type.raw / type_map.raw 等非npy文件
    for fname in os.listdir(data_dir):
        if not fname.endswith(".npy"):
            src = os.path.join(data_dir, fname)
            dst = os.path.join(out_dir, fname)
            if os.path.isfile(src):
                shutil.copy2(src, dst)

    # 处理 set.000 子目录（DeePMD标准格式）
    set_dirs = sorted([d for d in os.listdir(data_dir)
                       if d.startswith("set.") and
                       os.path.isdir(os.path.join(data_dir, d))])

    if set_dirs:
        # 多 set 情况：找到最后一个 set 操作
        _trim_sets(data_dir, set_dirs, n_trim, out_dir)
    else:
        # npy 直接放在根目录的情况
        _trim_flat(data_dir, n_trim, out_dir)


def _trim_flat(data_dir, n_trim, out_dir):
    """npy 直接在根目录"""
    trimmed = {}
    for name in NPY_FILES:
        path = os.path.join(data_dir, f"{name}.npy")
        if not os.path.exists(path):
            continue
        arr = np.load(path)
        original = arr.shape[0]
        if n_trim >= original:
            print(f"  ⚠ {name}.npy: 总帧数 {original} ≤ 要切除的 {n_trim}，跳过")
            continue
        arr_clean = arr[:-n_trim]
        trimmed[name] = (original, arr_clean.shape[0])
        np.save(os.path.join(out_dir, f"{name}.npy"), arr_clean)
        print(f"  {name}.npy: {original} → {arr_clean.shape[0]} 帧")

    if not trimmed:
        print("  未找到任何 npy 文件")


def _trim_sets(data_dir, set_dirs, n_trim, out_dir):
    """npy 在 set.000, set.001 ... 子目录中"""
    # 统计各 set 的帧数
    set_sizes = []
    for sd in set_dirs:
        p = os.path.join(data_dir, sd, "energy.npy")
        if os.path.exists(p):
            set_sizes.append((sd, np.load(p).shape[0]))
        else:
            set_sizes.append((sd, 0))

    total = sum(s for _, s in set_sizes)
    print(f"  共 {len(set_dirs)} 个 set，总帧数 {total}，切除最后 {n_trim} 帧")

    remaining = n_trim
    sets_to_process = list(reversed(set_sizes))   # 从最后一个 set 开始

    for sd, size in sets_to_process:
        src_set = os.path.join(data_dir, sd)
        dst_set = os.path.join(out_dir, sd)
        os.makedirs(dst_set, exist_ok=True)

        if remaining <= 0:
            # 直接复制整个 set
            for f in os.listdir(src_set):
                shutil.copy2(os.path.join(src_set, f), os.path.join(dst_set, f))
            print(f"  {sd}: {size} 帧，完整保留")
        elif remaining >= size:
            # 整个 set 都删掉
            remaining -= size
            print(f"  {sd}: {size} 帧，全部删除")
        else:
            # 部分删除
            keep = size - remaining
            remaining = 0
            for name in NPY_FILES:
                p = os.path.join(src_set, f"{name}.npy")
                if not os.path.exists(p):
                    continue
                arr = np.load(p)
                np.save(os.path.join(dst_set, f"{name}.npy"), arr[:keep])
            print(f"  {sd}: {size} 帧，保留前 {keep} 帧")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("data_dir", help="DeePMD 数据目录")
    parser.add_argument("--n", type=int, default=400, help="切除末尾帧数（默认400）")
    parser.add_argument("--out", type=str, default=None,
                        help="输出目录（默认在原目录名后加 _trimmed）")
    args = parser.parse_args()

    data_dir = args.data_dir.rstrip("/")
    out_dir  = args.out or data_dir + "_trimmed"

    print(f"输入目录 : {data_dir}")
    print(f"输出目录 : {out_dir}")
    print(f"切除末尾 : {args.n} 帧")
    print()

    trim_system(data_dir, args.n, out_dir)
    print("\n完成。")


if __name__ == "__main__":
    main()