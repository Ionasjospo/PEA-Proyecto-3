# Tarea 3 Probabilidad y Estadística aplicada
El objetivo de esta tarea es simular las variables aleatorias discretas vistas en el curso usando Python para obtener muestras con las que hacer estadıstica descriptiva y una verificacion empırica de la ley de los grandes numeros.

Trabajaremos con tres distribuciones discretas:

• <b>Distribucion 1:</b> binomial de parametros n = 100, p = 0,35. Se puede usar el submodulo binom de la liberarıa scipy.stats para generar una muestra aleatoria simple con esta distribucion, por ejemplo

from scipy.stats import binom

r = binom.rvs(n,p,size = 1000)

• <b>Distribucion 2:</b> geometrica de parametro p = 0,08. Se puede usar el submodulo geom de la liberarıa scipy.stats para generar una muestra aleatoria simple con esta distribucion, por ejemplo

from scipy.stats import geom

r = geom.rvs(p,size = 1000)

• <b>Distribucion 3:</b> poisson de parametro λ = 30. Se puede usar el submodulo poisson de la liberarıa
scipy.stats para generar una muestra aleatoria simple con esta distribucion, por ejemplo

from scipy.stats import poisson

r = poisson.rvs(L,size = 1000)

<b>Se pide:</b>
1. En este ejercicio trabajaremos con la distribucion 1.

    a) Generar muestras aleatorias de tamaños 102, 103, 104 y 105

    b) Hacer un diagrama de cajas para cada una de las muestras generadas en la parte anterior.¿Existen datos atıpicos en las muestras?

    c) Realizar un histograma de las muestras generadas.

    d) Hallar la mediana y la moda de cada muestra.

    e) Hallar la media empırica de cada muestra y compararla con la esperanza teorica de la distribucion 1. ¿Que se puede observar en las muestras mas grandes?

    f) Hallar la varianza empırica de cada muestra y compararla con la varianza teorica de la distribucion 1. ¿Que se puede observar en las muestras mas grandes?

2. En este ejercicio trabajaremos con la distribucion 2.

    a) Generar muestras aleatorias de tamaños 102, 103, 104 y 105.

    b) Hacer un diagrama de cajas para cada una de las muestras generadas en la parte anterior. ¿Existen datos atıpicos en las muestras

    c) Realizar un histograma de las muestras generadas.

    d) Hallar la mediana y la moda de cada muestra.

    e) Hallar la media empırica de cada muestra y compararla con la esperanza teorica de la distribucion 2. ¿Que se puede observar en las muestras mas grandes?

    f) Hallar la varianza empırica de cada muestra y compararla con la varianza teorica de la distribucion 2. ¿Que se puede observar en las muestras mas grandes?

3. En este ejercicio trabajaremos con la distribucion 3.

    a) Generar muestras aleatorias de tamaños 102, 103, 104 y 105.

    b) Hacer un diagrama de cajas para cada una de las muestras  generadas en la parte anterior. ¿Existen datos atıpicos en las muestras?

    c) Realizar un histograma de las muestras generadas.

    d) Hallar la mediana y la moda de cada muestra.

    e) Hallar la media empırica de cada muestra y compararla con la esperanza teorica de la distribucion 3. ¿Que se puede observar en las muestras mas grandes?

    f ) Hallar la varianza empırica de cada muestra y compararla con la varianza teorica de la distribucion 3. ¿Que se puede observar en las muestras mas grandes?
    

Sobre el informe:

• El tiempo para entregar el informe es hasta el sabado 8 de junio inclusive. La entrega se realizara por webasignatura.

• El informe debera estar en formato pdf, la entrega tambien debera incluir los scripts utilizados.

• El informe debera contener tıtulo, fecha, nombre y cedula de los estudiantes.

• Se evaluara: prolijidad del informe, utilizacion correcta del idioma español, redaccion, prolijidad del
codigo presentado en los scripts, conclusiones.