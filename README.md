# Minecraft Horse Breeding Tool
A CLI tool for predicting, managing, and optimizing Minecraft horse breeding with accurate stat calculations.  
一款用于Minecraft马匹培育的命令行工具，支持属性管理、后代预测与育种优化，基于游戏真实机制计算。

---

## 中英双语目录 / Table of Contents
1. [简介 / Introduction](#简介--introduction)
2. [功能特性 / Features](#功能特性--features)
3. [安装运行 / Installation & Run](#安装运行--installation--run)
4. [使用指南 / Usage](#使用指南--usage)
5. [跳跃模型说明 / Jump Model](#跳跃模型说明--jump-model)
6. [许可证 / License](#许可证--license)

---

## 简介 / Introduction
This tool simplifies Minecraft horse breeding by managing horse stats (HP, jump, speed), identifying underperforming horses, predicting offspring traits, and converting between jump strength and height. It’s designed for players aiming to breed top-tier horses efficiently without manual calculation.  
该工具简化Minecraft马匹培育流程，支持管理马匹属性（生命值、跳跃、速度）、识别低效马匹、预测后代特性、转换跳跃强度与高度，帮助玩家无需手动计算即可高效培育顶级马匹。

---

## 功能特性 / Features
- 🐴 **Horse Management**: Add/delete/modify horse stats (HP:15-30, Jump:1.086-5.293, Speed:4.8375-14.5125)  
  马匹管理：添加/删除/修改马匹属性（生命值15-30、跳跃高度1.086-5.293、速度4.8375-14.5125）
- 📊 **Sorting**: Sort by single attribute (HP/jump/speed) or custom weighted score  
  排序功能：按单一属性或自定义加权分数排序
- 🚫 **Baka Horse Detection**: Identify horses dominated in all stats by others  
  Baka马识别：找出全属性被其他马匹压制的低效马匹
- 👪 **Breed Prediction**: Calculate possible stat ranges for offspring of two horses  
  繁殖预测：计算两匹马后代的属性可能范围
- 🔄 **Jump Conversion**: Bidirectional conversion between jump strength (0.4-1.0) and height  
  跳跃转换：跳跃强度（0.4-1.0）与高度双向换算
- 💾 **Data Export**: Save horse data as importable commands  
  数据导出：将马匹数据保存为可导入的命令

---

## 安装运行 / Installation & Run
### Prerequisites
- Python 3.8+ (No extra dependencies required)  
- Python 3.8+（无需额外依赖）

### Run
```bash
# Clone the repository
git clone https://github.com/your-username/minecraft-horse-breeding-tool.git

# Enter directory
cd minecraft-horse-breeding-tool

# Run the tool
python horse.py
```

---

## 使用指南 / Usage
After running `python horse.py`, use the following commands (supports "baka" keyword directly):  
运行后输入以下命令（直接支持「baka」关键词）：

| Command                  | Description (English & 中文)                                                                 |
|--------------------------|---------------------------------------------------------------------------------------------|
| `add <hp> <jump> <speed>` | Add a new horse with valid stats / 添加符合属性范围的新马匹                                  |
| `show`                   | Display all horses / 显示所有马匹                                                            |
| `show baka`              | Show underperforming horses (dominated in all stats) / 显示全属性落后的baka马                |
| `sort <hp/jump/speed>`   | Sort horses by specified attribute (descending) / 按指定属性降序排序                        |
| `weight <w1> <w2> <w3>`  | Sort by weighted score (HP×w1 + Jump×w2 + Speed×w3) / 按自定义权重分数排序                  |
| `modify <id> <attr> <val>` | Modify a horse’s attribute by ID (attr: hp/jump/speed) / 按ID修改马匹属性（属性：hp/jump/speed） |
| `delete <id>`            | Delete a horse by ID / 按ID删除马匹                                                          |
| `delete baka`            | Delete all underperforming horses / 删除所有baka马                                          |
| `breed <id1> <id2>`      | Predict offspring stats of two horses / 预测两匹马的后代属性范围                              |
| `height <strength>`      | Convert jump strength to height / 将跳跃强度转换为高度                                      |
| `strength <height>`      | Convert jump height to strength / 将跳跃高度转换为强度                                      |
| `save`                   | Export horses as importable `add` commands / 导出马匹数据为可导入的add命令                  |
| `help`                   | Show full command list / 显示完整命令列表                                                    |
| `exit`                   | Exit the tool / 退出工具                                                                    |

### Example
```bash
# 1. Add multiple horses (HP:15-30, Jump:1.086-5.293, Speed:4.8375-14.5125)
# 添加多匹符合属性范围的马匹
add 22 2.8 10.5
add 28 3.9 13.2
add 18 1.5 8.7
add 25 4.1 12.8
add 20 3.0 9.9

# 2. Show all horses in the stable (check added data)
# 查看马厩中所有马匹（验证添加结果）
show

# 3. Sort horses by "speed" (descending order)
# 按速度降序排序马匹
sort speed

# 4. Weighted sort (e.g., prioritize HP=0.3, Jump=0.5, Speed=0.2)
# 加权排序（例：生命值权重0.3、跳跃0.5、速度0.2）
weight 0.3 0.5 0.2

# 5. Modify a horse's attribute (e.g., update Horse 2's HP to 29)
# 修改马匹属性（例：将2号马的生命值改为29）
modify 2 hp 29
modify 3 jump 2.2  # Update Horse 3's jump height to 2.2
modify 4 speed 13.5 # Update Horse 4's speed to 13.5

# 6. Show "baka" horses (underperforming in all stats)
# 查看全属性落后的「baka马」
show baka

# 7. Delete a specific horse (e.g., remove Horse 3)
# 删除指定马匹（例：删除3号马）
kill 3

# 8. Delete all baka horses (clean up underperforming ones)
# 删除所有baka马（清理低效马匹）
kill baka

# 9. Predict offspring (breed Horse 1 and Horse 2)
# 预测繁殖后代（让1号马与2号马配对）
breed 1 2

# 10. Convert jump values (strength ↔ height)
# 跳跃值双向转换（强度↔高度）
height 0.75  # Convert strength 0.75 to in-game height
strength 3.5 # Convert height 3.5 to internal strength

# 11. Export all horses as importable "add" commands (for backup/transfer)
# 导出所有马匹为可导入的add命令（备份/迁移用）
save

# 12. Show help for more details
# 查看帮助文档（获取更多命令说明）
help

# 13. Exit the tool
# 退出工具
exit
```

---

## 跳跃模型说明 / Jump Model
The jump calculation is based on Minecraft’s actual game mechanics (valid for jump strength `J ∈ [0.4, 1.0]`):  
跳跃计算公式基于Minecraft游戏真实机制（适用于跳跃强度 `J ∈ [0.4, 1.0]`）：

```
H(J) = -0.1817584952·J³ + 3.689713992·J² + 2.128599134·J − 0.343930367
```
- `H`: Jump height (in-game units) / 跳跃高度（游戏内单位）  
- `J`: Jump strength (game internal value) / 跳跃强度（游戏内部值）

---

## 许可证 / License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.  
本项目采用MIT许可证 - 详见 [LICENSE](LICENSE) 文件。
