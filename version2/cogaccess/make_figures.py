#!/usr/bin/env python3
"""Scoping review figures — cognitive accessibility design principles (ACM+IEEE, 2015-2025)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
import numpy as np
import os

# CJK font fallback so Chinese labels render on macOS
for cand in ["PingFang SC", "Heiti SC", "STHeiti", "Arial Unicode MS", "Songti SC"]:
    try:
        font_manager.findfont(cand, fallback_to_default=False)
        plt.rcParams["font.family"] = cand
        break
    except Exception:
        continue
plt.rcParams["axes.unicode_minus"] = False

OUT = os.path.join(os.path.dirname(__file__), "figures")
os.makedirs(OUT, exist_ok=True)
C = {"asd": "#E4572E", "idd": "#17BEBB", "dem": "#FFC914", "adhd": "#2E86AB", "tbi": "#76B041", "cross": "#9B5DE5"}

# ---- Fig 1: papers by population ----
pops = ["自闭症\nASD", "智力/学习障碍\nIDD", "ADHD/阅读障碍\nNeurodiv.", "跨人群/框架\nCross", "痴呆/老年\nDementia", "脑损伤/失语\nTBI·Aphasia"]
counts = [15, 9, 6, 6, 5, 4]
cols = [C["asd"], C["idd"], C["adhd"], C["cross"], C["dem"], C["tbi"]]
fig, ax = plt.subplots(figsize=(9, 5.2))
b = ax.barh(pops[::-1], counts[::-1], color=cols[::-1], edgecolor="white")
for bar, v in zip(b, counts[::-1]):
    ax.text(v + 0.15, bar.get_y() + bar.get_height()/2, str(v), va="center", fontweight="bold")
ax.set_xlabel("文献数 (n)")
ax.set_title("图1 · 纳入文献的人群分布 (ACM+IEEE, 主语料 n≈45)", fontweight="bold")
ax.spines[["top", "right"]].set_visible(False)
plt.tight_layout(); plt.savefig(f"{OUT}/fig1_population.png", dpi=150); plt.close()

# ---- Fig 2: year trend ----
years = list(range(2015, 2026))
yc =      [3,   2,    2,    1,    2,    5,    3,    6,    4,    8,    9]
fig, ax = plt.subplots(figsize=(9, 4.6))
ax.plot(years, yc, "-o", color=C["cross"], lw=2.5, ms=7)
ax.fill_between(years, yc, alpha=0.15, color=C["cross"])
for x, y in zip(years, yc):
    ax.text(x, y + 0.2, str(y), ha="center", fontsize=9)
ax.set_xticks(years)
ax.set_ylabel("文献数 (n)"); ax.set_xlabel("年份")
ax.set_title("图2 · 年份趋势：2024–25 认知无障碍设计研究显著增长", fontweight="bold")
ax.spines[["top", "right"]].set_visible(False)
ax.annotate("AI/LLM 介入 +\nWCAG 2.2 认知标准", xy=(2025, 9), xytext=(2021.3, 8.4),
            fontsize=9, color=C["asd"], arrowprops=dict(arrowstyle="->", color=C["asd"]))
plt.tight_layout(); plt.savefig(f"{OUT}/fig2_year_trend.png", dpi=150); plt.close()

# ---- Fig 3: cross-population principle x population matrix (heatmap) ----
principles = ["清晰语言", "降低记忆依赖", "降负荷/专注", "可预测一致", "防错+反馈",
              "帮助支持", "可定制/个性化", "多模态冗余", "参与/能力本位", "感官调节"]
groups = ["ASD", "IDD", "痴呆", "ADHD", "TBI"]
# 3=核心特异/最强证据, 2=明确支持, 1=部分/间接, 0=较少
M = np.array([
    [3,3,3,3,2],   # 清晰语言
    [1,2,3,2,2],   # 降记忆
    [3,2,1,3,3],   # 降负荷/专注
    [3,2,2,1,1],   # 可预测一致
    [3,3,1,1,2],   # 防错反馈
    [2,2,2,1,2],   # 帮助支持
    [3,2,3,3,3],   # 可定制
    [3,1,1,2,3],   # 多模态冗余
    [3,3,1,2,2],   # 参与/能力本位
    [3,1,2,2,1],   # 感官调节
])
fig, ax = plt.subplots(figsize=(7.6, 7.2))
im = ax.imshow(M, cmap="YlOrRd", vmin=0, vmax=3, aspect="auto")
ax.set_xticks(range(len(groups))); ax.set_xticklabels(groups, fontweight="bold")
ax.set_yticks(range(len(principles))); ax.set_yticklabels(principles)
for i in range(len(principles)):
    for j in range(len(groups)):
        v = M[i, j]
        ax.text(j, i, "●●●●"[:v] or "·", ha="center", va="center",
                color="#333" if v < 2 else "white", fontsize=11)
ax.set_title("图3 · 设计原则 × 人群 强度矩阵\n(● 越多=证据/特异性越强)", fontweight="bold", pad=12)
cb = plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04, ticks=[0,1,2,3])
cb.ax.set_yticklabels(["较少","间接","支持","核心"])
plt.tight_layout(); plt.savefig(f"{OUT}/fig3_principle_matrix.png", dpi=150); plt.close()

# ---- Fig 4: methodology type ----
methods = ["专家共识\n指南/启发式", "参与式/\n共同设计", "实证评估\n(用户研究)", "系统/工具\n构建", "综述/分析"]
mc = [9, 8, 10, 8, 7]
fig, ax = plt.subplots(figsize=(8, 5))
w = ax.pie(mc, labels=methods, autopct=lambda p: f"{p*sum(mc)/100:.0f}", startangle=90,
           colors=[C["asd"], C["idd"], C["dem"], C["tbi"], C["cross"]],
           wedgeprops=dict(edgecolor="white", width=0.45))
ax.set_title("图4 · 设计原则的方法学来源分布", fontweight="bold")
plt.tight_layout(); plt.savefig(f"{OUT}/fig4_methodology.png", dpi=150); plt.close()

print("Saved 4 figures to", OUT)
print(os.listdir(OUT))
