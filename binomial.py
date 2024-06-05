"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import binom, mode

# Parámetros
n = 100
p = 0.35

# Tamaños de muestra
sample_sizes = [102, 103, 104, 105]

# Generar muestras aleatorias
samples = {size: binom.rvs(n, p, size=size) for size in sample_sizes}

# Calcular estadísticas descriptivas
stats = {}
for size, sample in samples.items():
    sample_mode = mode(sample)
    if hasattr(sample_mode, 'mode'):
        if isinstance(sample_mode.mode, np.ndarray) and len(sample_mode.mode) > 0:
            moda = sample_mode.mode[0]
        else:
            moda = sample_mode.mode
    else:
        moda = np.nan
    stats[size] = {
        'mediana': np.median(sample),
        'moda': moda,
        'media': np.mean(sample),
        'varianza': np.var(sample)
    }

# Esperanza y varianza teórica
esperanza_teorica = n * p
varianza_teorica = n * p * (1 - p)

# Visualizaciones
plt.figure(figsize=(12, 10))

# Diagramas de caja
plt.subplot(2, 2, 1)
sns.boxplot(data=[samples[size] for size in sample_sizes])
plt.xticks(range(4), sample_sizes)
plt.title('Diagramas de caja')

# Histogramas
plt.subplot(2, 2, 2)
for size, sample in samples.items():
    sns.histplot(sample, kde=False, bins=30, label=f'Size={size}', element='step')
plt.legend()
plt.title('Histogramas')

# Medianas y Modas
print("Medianas y Modas:")
for size, stat in stats.items():
    print(f"Muestra de tamaño {size}: Mediana={stat['mediana']}, Moda={stat['moda']}")

# Medias y comparación con la esperanza teórica
print("\nMedias empíricas y Esperanza teórica:")
for size, stat in stats.items():
    print(f"Muestra de tamaño {size}: Media={stat['media']} (Esperanza teórica={esperanza_teorica})")

# Varianzas y comparación con la varianza teórica
print("\nVarianzas empíricas y Varianza teórica:")
for size, stat in stats.items():
    print(f"Muestra de tamaño {size}: Varianza={stat['varianza']} (Varianza teórica={varianza_teorica})")

plt.tight_layout()
plt.show()
"""
#Comentar esto para que funcione:
from scipy.stats import binom, mode
import numpy as np

def generate_binomial_samples(n, p, sample_sizes):
    samples = {size: binom.rvs(n, p, size=size) for size in sample_sizes}
    stats = {}
    for size, sample in samples.items():
        sample_mode = mode(sample)
        moda = sample_mode.mode[0] if isinstance(sample_mode.mode, np.ndarray) and len(sample_mode.mode) > 0 else sample_mode.mode
        stats[size] = {
            'mediana': np.median(sample),
            'moda': moda,
            'media': np.mean(sample),
            'varianza': np.var(sample)
        }
    return samples, stats

