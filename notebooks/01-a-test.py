# %% [markdown]
# # Um teste simples
# Quem sabe faz ao vivo.

# %%
import os

# O argumento deve ser o mesmo que está no pix.toml
project_root = str(os.getenv("PROJECT_ROOT"))

# %%
print(f"Project root is set to: {project_root}")

# %%
# data_path = project_root/ "data"/ "dataset.csv"
# dataset_df = pd.read_csv(data_path, header=None, names=["x","y"])
