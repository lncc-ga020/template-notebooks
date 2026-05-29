# %% [markdown]
# # Um teste simples
#
# Quem sabe faz ao vivo.

# %%
import os
from pathlib import Path
import pandas as pd

project_root = Path(str(os.getenv("PROJECT_ROOT")))

# %% [markdown]
# Verificando se a variável de ambiente está correta:

# %%
print(f"Project root is set to: {project_root}")

# %% [markdown]
# Lendo os dados do problema que vai me dar uma medalha Fields:

# %%
data_path = project_root / "data" / "dataset.csv"

dataset_df = pd.read_csv(data_path, header=None, names=["x", "y"])

dataset_df

# %%
dataset_df.plot.scatter(x="x", y="y", title="Scatter of my datas")
