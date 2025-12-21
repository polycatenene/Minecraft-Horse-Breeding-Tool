# Minecraft Horse Breeding Tool

---

## 简介 / Introduction

This tool helps Minecraft players efficiently breed top-tier horses by providing precise stat management, dominance analysis, offspring prediction, and probability estimation — all based on Minecraft’s actual internal mechanics.

该工具用于帮助 Minecraft 玩家高效培育顶级马匹，提供精确的属性管理、劣马（全属性被压制）分析、后代范围预测以及概率估算，全部基于游戏真实内部机制，无需手动计算。

---

## 功能特性 / Features

- 🐴 **Horse Management**  
  Add / delete / modify horses with strict validation  
  HP: `15–30`, Jump Height: `1.086–5.293`, Speed: `4.8375–14.5125`

  马匹管理：添加 / 删除 / 修改马匹，所有属性严格校验  
  生命值 15–30，跳跃高度 1.086–5.293，速度 4.8375–14.5125

- 📊 **Advanced Sorting**  
  Sort by single attribute or weighted score (custom factors)

  高级排序：支持单属性排序或自定义权重加权排序

- 🚫 **Baka Horse Detection (Pareto Dominance)**  
  Identify horses dominated by others in all stats

  Baka 马识别：找出在所有属性上都被其他马压制的低效马匹

- 👪 **Breed Prediction**  
  Predict offspring stat ranges (min / average / max)

  繁殖预测：计算后代可能的属性范围（最小 / 平均 / 最大）

- 🎯 **Target Probability Analysis**  
  Calculate probability of achieving a specific target horse

  目标概率分析：计算培育出指定目标马的概率

- 🔄 **Jump Conversion**  
  Accurate bidirectional conversion between jump strength and jump height

  跳跃转换：跳跃强度与游戏内高度的双向精确换算

- 💾 **Data Export**  
  Export all horses as reusable `add` commands

  数据导出：将所有马匹导出为可再次导入的 `add` 命令

---

## 安装运行 / Installation & Run

### Prerequisites
- Python **3.10+** (required for `match-case`)
- No external dependencies

需要 Python 3.10 及以上版本（用于 `match-case` 语法），无需额外依赖。

### Run
```bash
git clone https://github.com/your-username/minecraft-horse-breeding-tool.git
cd minecraft-horse-breeding-tool
python horse.py
````

---

## 使用指南 / Usage

启动后即可进入交互式命令行：

```bash
python horse.py
```

### 命令列表 / Command List

| Command                      | Description                              |
| ---------------------------- | ---------------------------------------- |
| `add <hp> <jump> <speed>`    | Add a new horse / 添加新马                   |
| `show`                       | Show all horses / 显示所有马                  |
| `sort <hp/jump/speed>`       | Sort by attribute (descending) / 按属性降序排序 |
| `weight <w1> <w2> <w3>`      | Weighted sort / 加权排序                     |
| `factor <w1> <w2> <w3>`      | Set default weight factors / 设置默认权重      |
| `modify <id> <attr> <value>` | Modify horse attribute / 修改马匹属性          |
| `show baka`                  | Show dominated horses / 显示 baka 马        |
| `kill <id>`                  | Delete horse by ID / 删除指定马               |
| `kill baka`                  | Delete all baka horses / 删除所有 baka 马     |
| `target <hp> <jump> <speed>` | Set breeding target / 设置目标马              |
| `breed <id1> <id2>`          | Predict offspring stats / 繁殖预测           |
| `height <strength>`          | Strength → height / 强度转高度                |
| `strength <height>`          | Height → strength / 高度转强度                |
| `save`                       | Export horses / 导出数据                     |
| `help`                       | Show help / 显示帮助                         |
| `exit`                       | Exit program / 退出                        |

---

### 示例流程 / Example Workflow

```bash
add 22 2.8 10.5
add 28 3.9 13.2
add 25 4.1 12.8

show
sort speed
weight 0.3 0.5 0.2

modify 2 hp 29

show baka
kill baka

target 26 4.2 13.5
breed 1 2

height 0.75
strength 3.5

save
exit
```

---

## 跳跃模型说明 / Jump Model

Jump height is calculated from Minecraft’s internal jump strength using the following polynomial (valid for `J ∈ [0.4, 1.0]`):

跳跃高度基于 Minecraft 内部跳跃强度计算，公式如下（适用于 `J ∈ [0.4, 1.0]`）：

```
H(J) = -0.1817584952·J³ + 3.689713992·J² + 2.128599134·J − 0.343930367
```

* `J`: Jump strength (internal)
* `H`: Jump height (blocks)

反向计算通过二分搜索完成，保证精度与稳定性。

---

## 许可证 / License

This project is licensed under the **MIT License**.
本项目采用 **MIT 许可证**。

See the `LICENSE` file for details.
