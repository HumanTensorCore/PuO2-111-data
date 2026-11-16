# AIMD input files

本目录保存 Deep Potential 训练集中三类 AIMD 来源体系的 CP2K 输入文件。三个文件对应不同体系，不是重复版本；对于完整训练数据，三个都应保留。

## 文件与训练数据的对应关系

| AIMD 输入文件 | 体系 | 对应训练数据目录 | AIMD 构型数 | 是否保留 |
|---|---|---|---:|---|
| `PuO2-111-water-aimd.inp` | PuO₂(111)–水界面 | `D:\data\training_data\training_data_surface` | 1600 | 保留 |
| `PuO2-1-aimd.inp` | 体相 PuO₂ | `D:\data\training_data\training_data_bluk` | 800 | 保留 |
| `MD.inp` | 体相水 | `D:\data\training_data\training_data_water` | 500 | 保留 |

三部分合计 **2900 个 AIMD 标注构型**。构型数来自各训练目录 `set.000/energy.npy` 的第一维长度：

- `training_data_surface`: `(1600, 1)`
- `training_data_bluk`: `(800, 1)`
- `training_data_water`: `(500, 1)`

> 注意：`training_data_bluk` 是现有目录名中的拼写，实际含义是 bulk PuO₂。

## 哪个可以不用？

- 若只整理 `training_data_surface` 中的1600个界面构型，只需要 `PuO2-111-water-aimd.inp`；另外两个不属于这1600个界面构型。
- 若整理论文所述的完整 AIMD 训练来源，三个输入文件都需要，没有应删除的文件。

## 输入文件概况

### `PuO2-111-water-aimd.inp`

- PuO₂(111)–水界面体系
- NVT，330 K
- 20,000步，时间步长1 fs
- 直接对应1600个界面训练构型的来源模拟

### `PuO2-1-aimd.inp`

- 体相 PuO₂ 体系
- NPT_F，300 K
- 5,000步，时间步长0.5 fs
- 对应800个体相 PuO₂ 训练构型

### `MD.inp`

- 体相水体系，结构从 `H2O.cif` 读取
- NVT，330 K
- 20,000步，时间步长1 fs
- 对应500个体相水训练构型
- 文件中 H 的质量设置为2.0；复现时还需要 `H2O.cif`、基组、赝势及 DFT-D3 参数文件

## 完整性提示

这些 `.inp` 文件是计算设置，不包含所有运行依赖。实际复现时还需准备文件中引用的结构、基组、赝势、色散参数以及可能的波函数重启文件。
