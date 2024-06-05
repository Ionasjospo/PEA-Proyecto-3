import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

# Parámetros
n = 100
p_binomial = 0.35
p_geometric = 0.08
lambda_poisson = 30
sample_sizes = [102, 103, 104, 105]

# Funciones para calcular estadísticas descriptivas
def calculate_descriptive_stats(samples):
    stats = {}
    for size, sample in samples.items():
        # Calcular la moda
        moda_value, moda_count = np.unique(sample, return_counts=True)
        moda_value = moda_value[np.argmax(moda_count)]
        moda = moda_value if moda_count[np.argmax(moda_count)] > 1 else np.nan
        # Calcular estadísticas
        stats[size] = {
            'mediana': np.median(sample),
            'moda': moda,
            'media': np.mean(sample),
            'varianza': np.var(sample)
        }
    return stats

# Funciones para generar muestras aleatorias
def generate_binomial_samples(n, p, sample_sizes):
    return {size: np.random.binomial(n, p, size) for size in sample_sizes}

def generate_geometric_samples(p, sample_sizes):
    return {size: np.random.geometric(p, size) for size in sample_sizes}

def generate_poisson_samples(lambda_, sample_sizes):
    return {size: np.random.poisson(lambda_, size) for size in sample_sizes}

# Funciones para realizar las visualizaciones
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

# Función para comparar estadísticas descriptivas con valores teóricos
def compare_stats_with_theoretical(stats, theoretical_values):
    for size, stat in stats.items():
        print(f"Muestra de tamaño {size}:")
        for key, value in stat.items():
            if key in theoretical_values[size]:  # Verificar si la estadística teórica está disponible
                print(f"{key.capitalize()}: {value} (Teórico: {theoretical_values[size][key]})")  # Corrección aquí

# Generar muestras para la distribución binomial
theoretical_values_binomial = {
    size: {
        'media': n * p_binomial,
        'varianza': n * p_binomial * (1 - p_binomial),
        'mediana': np.median(np.random.binomial(n, p_binomial, size)),
        'moda': stats.mode(np.random.binomial(n, p_binomial, size)).mode if len(np.unique(np.random.binomial(n, p_binomial, size))) > 1 else np.nan  # Corrección aquí
    } for size in sample_sizes
}



samples_binomial = generate_binomial_samples(n, p_binomial, sample_sizes)
stats_binomial = calculate_descriptive_stats(samples_binomial)

# Mostrar gráficos y comparar estadísticas para la distribución binomial
plot_boxplots(samples_binomial, "Diagramas de Caja para Distribución Binomial")
plot_histograms(samples_binomial, "Histogramas para Distribución Binomial")
compare_stats_with_theoretical(stats_binomial, theoretical_values_binomial)


# Generar muestras para la distribución geométrica
theoretical_values_geometric = {
    size: {
        'media': (1 / p_geometric),
        'varianza': (1 - p_geometric) / (p_geometric ** 2),
        'mediana': np.median(np.random.geometric(p_geometric, size)),
        'moda': stats.mode(np.random.geometric(p_geometric, size)).mode if len(np.unique(np.random.geometric(p_geometric, size))) > 1 else np.nan  # Corrección aquí
    } for size in sample_sizes
}

samples_geometric = generate_geometric_samples(p_geometric, sample_sizes)
stats_geometric = calculate_descriptive_stats(samples_geometric)

# Mostrar gráficos y comparar estadísticas para la distribución geométrica
plot_boxplots(samples_geometric, "Diagramas de Caja para Distribución Geométrica")
plot_histograms(samples_geometric, "Histogramas para Distribución Geométrica")
compare_stats_with_theoretical(stats_geometric, theoretical_values_geometric)

# Generar muestras para la distribución de Poisson
theoretical_values_poisson = {
    size: {
        'media': lambda_poisson,
        'varianza': lambda_poisson,
        'mediana': np.median(np.random.poisson(lambda_poisson, size)),
        'moda': stats.mode(np.random.poisson(lambda_poisson, size)).mode if len(np.unique(np.random.poisson(lambda_poisson, size))) > 1 else np.nan  # Corrección aquí
    } for size in sample_sizes
}
samples_poisson = generate_poisson_samples(lambda_poisson, sample_sizes)
stats_poisson = calculate_descriptive_stats(samples_poisson)

# Mostrar gráficos y comparar estadísticas para la distribución de Poisson
plot_boxplots(samples_poisson, "Diagramas de Caja para Distribución de Poisson")
plot_histograms(samples_poisson, "Histogramas para Distribución de Poisson")
compare_stats_with_theoretical(stats_poisson, theoretical_values_poisson)
