import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from binomial import generate_binomial_samples
from geometrica import generate_geometric_samples
from poisson import generate_poisson_samples

n = 100
p_binomial = 0.35
p_geometric = 0.08
lambda_poisson = 30
sample_sizes = [100,1000,10000,100000]

def plot_boxplots(samples, title):
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=list(samples.values()))
    plt.title(title)
    plt.xlabel("Tamaño de Muestra")
    plt.ylabel("Valor")
    plt.show()

def plot_histograms(samples, title):
    plt.figure(figsize=(10, 6))
    for size, sample in samples.items():
        sns.histplot(sample, kde=False, bins=30, label=f'Tamaño={size}', element='step')
    plt.legend()
    plt.title(title)
    plt.xlabel("Valor")
    plt.ylabel("Frecuencia")
    plt.show()

def compare_stats_with_theoretical(stats, theoretical_values):
    for size, stat in stats.items():
        print(f"Muestra de tamaño {size}:")
        for key, value in stat.items():
            print(f"{key.capitalize()}: {value} (Teórico: {theoretical_values[size][key]})")

samples_binomial, stats_binomial = generate_binomial_samples(n, p_binomial, sample_sizes)

theoretical_values_binomial = {
    size: {
        'media': n * p_binomial,
        'varianza': n * p_binomial * (1 - p_binomial),
        'mediana': np.median(np.random.binomial(n, p_binomial, size)),
        'moda': stats.mode(np.random.binomial(n, p_binomial, size)).mode.item() if stats.mode(np.random.binomial(n, p_binomial, size))
        .count > 0 else np.nan
    } for size in sample_sizes
}

print("BINOMIAL")
plot_boxplots(samples_binomial, "Diagramas de Caja para Distribución Binomial")
plot_histograms(samples_binomial, "Histogramas para Distribución Binomial")
compare_stats_with_theoretical(stats_binomial, theoretical_values_binomial)
print("-----------------")

samples_geometric, stats_geometric = generate_geometric_samples(p_geometric, sample_sizes)

theoretical_values_geometric = {
    size: {
        'media': 1 / p_geometric,
        'varianza': (1 - p_geometric) / (p_geometric ** 2),
        'mediana': np.median(np.random.geometric(p_geometric, size)),
        'moda': stats.mode(np.random.geometric(p_geometric, size)).mode.item() if stats.mode(np.random.geometric(p_geometric, size))
        .count > 0 else np.nan
    } for size in sample_sizes
}

print("GEOMETRICA")
plot_boxplots(samples_geometric, "Diagramas de Caja para Distribución Geométrica")
plot_histograms(samples_geometric, "Histogramas para Distribución Geométrica")
compare_stats_with_theoretical(stats_geometric, theoretical_values_geometric)
print("-----------------")

samples_poisson, stats_poisson = generate_poisson_samples(lambda_poisson, sample_sizes)

theoretical_values_poisson = {
    size: {
        'media': lambda_poisson,
        'varianza': lambda_poisson,
        'mediana': np.median(np.random.poisson(lambda_poisson, size)),
        'moda': stats.mode(np.random.poisson(lambda_poisson, size)).mode.item() if stats.mode(np.random.poisson(lambda_poisson, size))
        .count > 0 else np.nan
    } for size in sample_sizes
}

print("POISSON")
plot_boxplots(samples_poisson, "Diagramas de Caja para Distribución de Poisson")
plot_histograms(samples_poisson, "Histogramas para Distribución de Poisson")
compare_stats_with_theoretical(stats_poisson, theoretical_values_poisson)
print("-----------------")