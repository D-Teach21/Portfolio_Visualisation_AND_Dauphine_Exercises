import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# --- CONFIGURATION ---
lucky_thinks = Path.home() / 'Desktop' / 'Lucky Thinks'
input_file = lucky_thinks / 'portfolio_data.xlsx'

# Chargement des données (On prend la feuille de synthèse que tu as créée)
df = pd.read_excel(input_file, sheet_name='All_Closing_Prices', index_col=0)

# Séparation : Benchmark (SP500) vs Actifs du portefeuille
benchmark_col = 'SP500'
assets_cols = [col for col in df.columns if col != benchmark_col]

# --- CALCULS FINANCIERS ---
# 1. Rendements quotidiens (log-returns pour la rigueur mathématique)
returns = np.log(df / df.shift(1)).dropna()

# 2. Définition des poids (Equipondéré par défaut : 1/N)
weights = np.array([1/len(assets_cols)] * len(assets_cols))

# 3. Calcul de la performance Portefeuille vs Benchmark
port_returns = returns[assets_cols].dot(weights)
bench_returns = returns[benchmark_col]

# 4. Performance Cumulée (Base 100)
port_cum = np.exp(port_returns.cumsum()) * 100
bench_cum = np.exp(bench_returns.cumsum()) * 100

# 5. Métriques de Risque (Annualisées)
def get_stats(r):
    ann_ret = r.mean() * 252
    ann_vol = r.std() * np.sqrt(252)
    sharpe = ann_ret / ann_vol # Risk-free rate supposé à 0%
    # Drawdown
    cum_ret = np.exp(r.cumsum())
    max_drawdown = (cum_ret / cum_ret.cummax() - 1).min()
    return ann_ret, ann_vol, sharpe, max_drawdown

p_ret, p_vol, p_sharpe, p_dd = get_stats(port_returns)
b_ret, b_vol, b_sharpe, b_dd = get_stats(bench_returns)

# --- VISUALISATION PRO ---
plt.style.use('seaborn-v0_8-whitegrid')
fig = plt.figure(figsize=(15, 12))
gs = fig.add_gridspec(3, 2)

# Graphique 1 : Performance Cumulée (Le "Main")
ax1 = fig.add_subplot(gs[0, :])
ax1.plot(port_cum, label=f'Mon Portefeuille (Sharpe: {p_sharpe:.2f})', lw=2, color='#1f77b4')
ax1.plot(bench_cum, label=f'S&P 500 (Sharpe: {b_sharpe:.2f})', lw=1.5, color='gray', linestyle='--')
ax1.set_title('Performance Cumulative : Portefeuille vs Benchmark (Base 100)', fontsize=14, fontweight='bold')
ax1.legend()

# Graphique 2 : Matrice de Corrélation (Crucial pour la diversification)
ax2 = fig.add_subplot(gs[1, 0])
corr = returns[assets_cols].corr()
sns.heatmap(corr, annot=True, cmap='RdYlGn', ax=ax2, fmt=".2f", cbar=False)
ax2.set_title('Matrice de Corrélation des Actifs')

# Graphique 3 : Risk-Return Profile
ax3 = fig.add_subplot(gs[1, 1])
asset_vols = returns[assets_cols].std() * np.sqrt(252)
asset_rets = returns[assets_cols].mean() * 252
ax3.scatter(asset_vols, asset_rets, alpha=0.5, color='blue')
for i, txt in enumerate(assets_cols):
    ax3.annotate(txt, (asset_vols.iloc[i], asset_rets.iloc[i]))
ax3.scatter(p_vol, p_ret, color='red', s=100, marker='*', label='PORTFOLIO')
ax3.set_xlabel('Volatilité Annualisée')
ax3.set_ylabel('Rendement Attendu Annualisé')
ax3.set_title('Profil Risque/Rendement')
ax3.legend()

# Tableau de synthèse (Subplot 4)
ax4 = fig.add_subplot(gs[2, :])
ax4.axis('off')
stats_data = [
    ['Métrique', 'Portefeuille', 'S&P 500'],
    ['Rendement Ann.', f'{p_ret:.2%}', f'{b_ret:.2%}'],
    ['Volatilité Ann.', f'{p_vol:.2%}', f'{b_vol:.2%}'],
    ['Ratio de Sharpe', f'{p_sharpe:.2f}', f'{b_sharpe:.2f}'],
    ['Max Drawdown', f'{p_dd:.2%}', f'{b_dd:.2%}']
]
table = ax4.table(cellText=stats_data, loc='center', cellLoc='center', colWidths=[0.2, 0.2, 0.2])
table.auto_set_font_size(False)
table.set_fontsize(12)
table.scale(1.2, 2)

plt.tight_layout()
plt.show()

print(f"Analyse terminée. Ratio de Sharpe du portefeuille : {p_sharpe:.2f}")