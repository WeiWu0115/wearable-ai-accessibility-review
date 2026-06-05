#!/usr/bin/env python3
"""One-page MAP of HCI cognitive accessibility design principles (ACM+IEEE, 2015-2025)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import os

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

INK = "#22223B"
fig = plt.figure(figsize=(8.5, 12))
ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 100); ax.set_ylim(0, 140); ax.axis("off")
fig.patch.set_facecolor("#F7F7FB")


def card(x, y, w, h, fc, ec, rad=1.6, lw=1.5, alpha=1.0):
    p = FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={rad}",
                       fc=fc, ec=ec, lw=lw, alpha=alpha, zorder=2)
    ax.add_patch(p); return p


# ---------- Title ----------
card(4, 130, 92, 8.4, "#22223B", "#22223B", rad=1.4)
ax.text(50, 135.7, "HCI 认知无障碍 · 设计原则地图", ha="center", va="center",
        fontsize=18, fontweight="bold", color="white")
ax.text(50, 131.7, "Cognitive Accessibility Design Principles  ·  ACM + IEEE  ·  2015–2025",
        ha="center", va="center", fontsize=9.5, color="#C9C9E3")

# ---------- Core backbone (COGA 8 objectives → 9 principles) ----------
ax.text(50, 127.2, "① 跨人群核心共性原则  —  以 W3C COGA 八目标为骨架",
        ha="center", va="center", fontsize=12.5, fontweight="bold", color=INK)

core = [
    ("清晰·字面语言", "简单词汇/直接语态\n少隐喻 · succinct", "#E76F51"),
    ("降低记忆依赖", "提醒/提示\n不靠记忆与计算", "#F4A261"),
    ("降负荷·支持专注", "减步骤/最短路径\n限制干扰 · Focus", "#E9C46A"),
    ("可预测 · 一致", "稳定不突变\n一致视觉/交互", "#2A9D8F"),
    ("防错 + 反馈", "可撤销/验证\n状态可见", "#4895EF"),
    ("帮助与支持", "人工帮助/备用内容\n导航协助", "#577590"),
    ("可定制·个性化", "字体/配色/难度\n应用层非仅系统级", "#9B5DE5"),
    ("多模态冗余表征", "图/文/音并行\n不绑定单一格式", "#C44536"),
    ("参与式·能力本位", "与目标人群共建\n以能力为中心", "#1B998B"),
]
x0, y0, cw, ch, gx, gy = 5, 103, 29.5, 6.0, 1.25, 1.5
for i, (t, d, c) in enumerate(core):
    cx = x0 + (i % 3) * (cw + gx)
    cy = y0 + (2 - i // 3) * (ch + gy)
    card(cx, cy, cw, ch, "white", c, rad=1.2, lw=2)
    card(cx, cy + ch - 1.7, cw, 1.7, c, c, rad=1.2)
    ax.text(cx + cw / 2, cy + ch - 0.85, t, ha="center", va="center",
            fontsize=10, fontweight="bold", color="white")
    ax.text(cx + cw / 2, cy + (ch - 1.7) / 2, d, ha="center", va="center",
            fontsize=7.6, color=INK)

# divider
ax.plot([5, 95], [99.2, 99.2], color="#D0D0E0", lw=1, zorder=1)

# ---------- ASD spotlight ----------
ax.text(50, 96.3, "② 重点人群：自闭症 ASD  —  在共性之上的特异性最强",
        ha="center", va="center", fontsize=12.5, fontweight="bold", color="#E4572E")
card(5, 76.5, 90, 18.4, "#FDEDE8", "#E4572E", rad=1.6, lw=2.2)
asd = [
    ("▍感官调节 (最特异)", "可关闭动画/闪烁/自动播放；降低感官刺激选项；警惕感官过载"),
    ("▍可预测 · 抗界面变化", "界面微小变化即引发不适→保持稳定、变化预告"),
    ("▍字面化语言", "少隐喻/反讽/模糊；图文冗余 (RR)"),
    ("▍深度可定制", "字体/配色/音频引导——不能只靠系统级设置；谱系异质需可适配"),
    ("▍反馈不可缺", "缺失/不完整反馈对 ASD 尤其关键，尤其针对错误"),
    ("▍导航 + 多发展水平", "清晰结构/最短路径；为不同能力层提供内容选项"),
]
for i, (t, d) in enumerate(asd):
    cx = 7 + (i % 2) * 45
    cy = 90.2 - (i // 2) * 4.45
    ax.text(cx, cy, t, ha="left", va="center", fontsize=9.3, fontweight="bold", color="#B83A1A")
    ax.text(cx, cy - 1.9, d, ha="left", va="center", fontsize=7.5, color=INK)
ax.text(50, 77.4, "锚点：GAIA 28条/10模块 · Khowaja&Salim 15启发式 · 共同设计 (青少年/成人)",
        ha="center", va="center", fontsize=7.3, style="italic", color="#B83A1A")

# ---------- Other populations 2x2 ----------
ax.text(50, 73.0, "③ 其他认知障碍人群  —  特异性亮点", ha="center", va="center",
        fontsize=12.5, fontweight="bold", color=INK)
pops = [
    ("智力 / 学习障碍 IDD", "#17BEBB",
     ["WCAG 合规 ≠ 认知可用 → 专用设计模式", "能力本位设计 (ability-based)",
      "创伤知情设计 (trauma-informed)", "Easy-to-Read：减少步骤/内在负荷"]),
    ("痴呆 / 老年认知衰退", "#F4A261",
     ["自适应 UI：导航+内容随情境/画像", "降低记忆依赖：智能提醒/任务提示",
      "应对多重感官衰退 (视听言语灵巧)", "照护者生态 + 健康公平"]),
    ("ADHD / 阅读障碍", "#4895EF",
     ["可读性指南 (排版/字体, 61/41 条)", "注意力自适应→显著降认知负荷",
      "执行功能支持 (界面常 by-design 制障)", "与神经多样用户共同设计"]),
    ("脑损伤 TBI / 失语 Aphasia", "#76B041",
     ["多模态沟通替代 (图像叙事/音频)", "专注模式 + 写作/解读辅助 (SMART-TBI)",
      "语言产出/理解辅助", "个案化：用户主导界面参数"]),
]
px, py, pw, ph, pgx, pgy = 5, 8, 44, 29.5, 2, 2.5
for i, (title, col, items) in enumerate(pops):
    cx = px + (i % 2) * (pw + pgx)
    cy = py + (1 - i // 2) * (ph + pgy)
    card(cx, cy, pw, ph, "white", col, rad=1.5, lw=2)
    card(cx, cy + ph - 3.4, pw, 3.4, col, col, rad=1.5)
    ax.text(cx + pw / 2, cy + ph - 1.7, title, ha="center", va="center",
            fontsize=10.5, fontweight="bold", color="white")
    for j, it in enumerate(items):
        ax.text(cx + 1.8, cy + ph - 6.0 - j * 5.0, "•", ha="left", va="top",
                fontsize=11, color=col, fontweight="bold")
        ax.text(cx + 3.6, cy + ph - 5.7 - j * 5.0, it, ha="left", va="top",
                fontsize=8.2, color=INK, wrap=True)

# ---------- Footer ----------
ax.text(50, 5.2, "共振：ASD 的「专注 + 定制」与 ADHD / TBI 高度重叠，常以 neurodivergent 合并研究",
        ha="center", va="center", fontsize=8.3, fontweight="bold", color="#9B5DE5")
ax.text(50, 2.4, "来源：ACM DL + IEEE Xplore (2015–2025) + W3C COGA / GAIA  ·  约45篇  ·  局限：全文未逐篇通读(反爬)，计数为二手  ·  v1 2026-06-03",
        ha="center", va="center", fontsize=6.6, color="#7A7A8C")

plt.savefig(f"{OUT}/onepage_map.png", dpi=170, facecolor=fig.get_facecolor())
plt.savefig(f"{OUT}/onepage_map.pdf", facecolor=fig.get_facecolor())
plt.close()
print("Saved onepage_map.png / .pdf to", OUT)
