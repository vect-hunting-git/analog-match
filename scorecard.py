import pandas as pd
import matplotlib.pyplot as plt

SHOW = False  # True opens chart windows; False only saves the images

criteria = ["Temperature", "Illumination", "Regolith", "Isolation", "Access"]
weights = [0.25, 0.25, 0.20, 0.15, 0.15]

scenarios = {
    "Baseline":        [0.25, 0.25, 0.20, 0.15, 0.15],
    "Power-focused":   [0.15, 0.40, 0.15, 0.15, 0.15],
    "Logistics-first": [0.15, 0.15, 0.15, 0.20, 0.35],
    "Equal weights":   [0.20, 0.20, 0.20, 0.20, 0.20],
}

# ---- Read the evidence table ----
evidence = pd.read_csv("evidence.csv")
evidence["Score (1-5)"] = pd.to_numeric(evidence["Score (1-5)"], errors="coerce")

missing = evidence[evidence["Score (1-5)"].isna()]
if len(missing) > 0:
    print(f"{len(missing)} rows still have no score:")
    print(missing[["Target", "Site", "Criterion"]].to_string(index=False))
    raise SystemExit("Fill in all scores in evidence.csv first.")


def scores_for(target):
    sub = evidence[evidence["Target"] == target]
    table = sub.pivot(index="Site", columns="Criterion", values="Score (1-5)")
    return table[criteria]


def finish_plot(filename):
    plt.tight_layout()
    plt.savefig(filename, dpi=200)
    if SHOW:
        plt.show()
    plt.close()


targets = {
    "Moon south pole": scores_for("Moon south pole"),
    "Mars": scores_for("Mars"),
}
baseline_totals = {}

for target_name, base in targets.items():
    tag = target_name.split()[0].lower()  # "moon" or "mars"

    df = base.copy()
    df["Total"] = (df[criteria] * weights).sum(axis=1)
    df = df.sort_values("Total", ascending=False)
    baseline_totals[target_name] = df["Total"]

    print(f"\n=== Ranking for target: {target_name} ===")
    print(df.round(2))
    df.round(2).to_csv(f"ranking_{tag}.csv")

    df["Total"].plot(kind="bar", color="steelblue")
    plt.ylabel("Weighted score (out of 5)")
    plt.title(f"Earth analog sites for: {target_name}")
    finish_plot(f"ranking_{tag}.png")

    results = pd.DataFrame(
        {name: (base[criteria] * w).sum(axis=1) for name, w in scenarios.items()}
    )
    print(f"\nSensitivity analysis ({target_name}):")
    print(results.round(2))
    print("\nTop site per scenario (first listed if tied):")
    print(results.idxmax())
    results.round(2).to_csv(f"sensitivity_{tag}.csv")

    results.plot(kind="bar", figsize=(9, 5))
    plt.ylabel("Weighted score (out of 5)")
    plt.title(f"Ranking under different priorities: {target_name}")
    finish_plot(f"sensitivity_{tag}.png")

both = pd.DataFrame(baseline_totals)
both["Average (both)"] = both.mean(axis=1)
both = both.sort_values("Average (both)", ascending=False)

print("\n=== Best sites for both Moon and Mars ===")
print(both.round(2))
both.round(2).to_csv("ranking_both.csv")

both.plot(kind="bar", figsize=(9, 5))
plt.ylabel("Weighted score (out of 5)")
plt.title("Moon vs Mars suitability of each Earth site")
finish_plot("ranking_both.png")

print("\nDone. Charts and CSV files saved in this folder.")