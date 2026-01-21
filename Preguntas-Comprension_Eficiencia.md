## Comprensión de la eficiencia de Numpy

*** Bloque A — Observación inicial (qué pasa) ***
    Si implementas el mismo cálculo con un for en Python y con una operación vectorizada en NumPy, ¿qué esperas que ocurra con el tiempo de ejecución cuando el tamaño del array pasa de 1.000 a 10.000.000 elementos?
        - Al pasar de 1.000 a 10.000.000 elementos, la diferencia de rendimiento entre ambos enfoques se vuelve enorme. La versión con for se vuelve impráctica, mientras que la versión vectorizada con NumPy sigue siendo eficiente y escalable.
    ¿En qué punto (tamaño aproximado) crees que la diferencia empieza a ser clara? ¿Por qué?
        - La diferencia empieza a ser clara ya alrededor de 10.000 – 100.000 elementos, y se hace muy marcada a partir de 1 millón.
    ¿Qué parte del programa crees que consume más tiempo: el cálculo matemático o el “mecanismo” de recorrer y operar elemento a elemento?
        - El cuello de botella principal es el proceso de iterar elemento a elemento en Python, no la operación matemática en sí.
*** Bloque B — Representación de datos (qué estás procesando realmente) ***
    ¿Cómo almacena Python una lista de números? ¿Es una lista de valores o una lista de referencias a objetos?
        - Una lista de Python es una lista de referencias a objetos, no una lista de valores.
    ¿Qué implica para la CPU acceder a datos dispersos en memoria (objetos separados) frente a datos contiguos?
        - Para la CPU, los datos contiguos son mucho más eficientes; los datos dispersos implican más latencia, más fallos de caché y peor rendimiento.
    ¿Qué significa que un array NumPy sea “homogéneo” (mismo dtype) y por qué podría ayudar al rendimiento?
        - La homogeneidad (dtype único) permite a NumPy trabajar con datos simples, predecibles y contiguos, lo que reduce overhead y permite a la CPU ejecutar los cálculos de forma mucho más eficiente.
    ¿Qué coste adicional tiene Python al operar con tipos dinámicos en cada iteración?
        - El coste adicional de los tipos dinámicos es el overhead del intérprete (comprobaciones de tipo, llamadas indirectas y creación de objetos), que se repite en cada iteración y penaliza fuertemente el rendimiento.
*** Bloque C — Overhead del intérprete (por qué el bucle Python pesa tanto) ***
    En un bucle Python, por cada iteración, ¿qué operaciones “extra” ocurren además de sumar o multiplicar? (pista: resolución de tipos, llamadas, objetos, etc.)
        - En un bucle Python, la suma o multiplicación es solo una pequeña parte del trabajo; la mayor parte del tiempo se va en overhead del intérprete, resolución dinámica de tipos, gestión de objetos y control del bucle.
    ¿Por qué una llamada a math.sin() dentro de un bucle puede ser especialmente cara repetida millones de veces?
        - math.sin() es costosa en bucles grandes porque cada llamada implica cruzar la frontera Python–C, convertir objetos y gestionar memoria, y ese overhead se acumula millones de veces.
    ¿Qué crees que significa realmente “overhead del intérprete” en términos de tiempo por elemento?
        - El “overhead del intérprete” es el coste fijo por elemento (en tiempo de CPU) asociado a ejecutar Python dinámico, y suele ser mucho mayor que la operación matemática que se quiere realizar.
*** Bloque D — Dónde se ejecuta el bucle (Python vs C) ***
    Cuando escribes np.sin(x), ¿quién recorre el array: tu bucle Python o un bucle interno compilado?
        - Al escribir np.sin(x), el recorrido del array lo hace NumPy en código compilado, no tu bucle Python, y esa es la clave del rendimiento.
    ¿Por qué un bucle en C/Fortran puede ser mucho más eficiente que el mismo bucle escrito en Python?
        - Un bucle en C/Fortran es mucho más rápido porque:
            - Trabaja con tipos fijos = cálculo directo.
            - Accede a datos contiguos en memoria = caché eficiente.
            - No tiene overhead de intérprete ni gestión de objetos.
            - Puede ser vectorizado y optimizado por el compilador.
        - En Python, incluso sumar dos números en un bucle pequeño paga todo el overhead del lenguaje, mientras que en C/Fortran solo se ejecuta la instrucción matemática real.    
    ¿Qué cambia en el número de “entradas” al intérprete entre estas dos versiones?
        bucle Python con for
        vectorización NumPy
            - La vectorización NumPy reduce el número de entradas al intérprete de “millones” a “una sola”, eliminando la mayor parte del overhead de Python. Esto explica por qué es tan eficiente frente a un bucle for en Python.
*** Bloque E — Cachés, contigüidad y SIMD (por qué la CPU “vuela” con NumPy) ***
    ¿Qué es la caché de CPU y por qué importa en cálculos sobre arrays grandes?
        - La caché de CPU importa porque reducre drásticamente el tiempo de acceso a los datos. Los arrays grandes y contiguos (NumPy) aprovecha la caché eficientemente, mientras que las listas de Python dispersas sufren por accesos lentos a memoria. Esto explica gran parte de la ventaja de NumPy sobre bucles Python puros.
    ¿Qué es el “prefetching” y por qué funciona mejor con memoria contigua?
        - Prefetching: anticipar datos y cargarlos en caché antes de necesitarlos.
        - Funciona mejor con memoria contigua porque la CPU puede predecir y cargar bloques completos, aumentando el rendimiento en bucles y operaciones sobre arrays grandes.
    ¿Qué tipo de operaciones crees que se benefician más de SIMD (vectorización a nivel CPU): sumas/multiplicaciones, o lógica con muchos if? ¿Por qué?
        - Beneficio alto de SIMD: operaciones aritméticas repetitivas y uniformes (sumas, multiplicaciones, etc.).
        - Beneficio bajo de SIMD: lógica con muchos if, ramificaciones o código muy divergente.
    ¿Qué crees que pasa si tus datos no están contiguos (slicing raro, arrays no contiguos)? ¿Se mantiene la ventaja?
        - La ventaja de SIMD disminuye mucho si los datos no son contiguos, y en algunos casos puede llegar a ser casi nula si la memoria es muy dispersa. Por eso, en vectorización, organizar los datos en arrays contiguos es casi tan importante como vectorizar las operaciones mismas.
*** Bloque F — Experimentación (preguntas para guiar un mini-lab) ***
    Si repites el benchmark con float32 en lugar de float64, ¿qué esperas que pase con:
        velocidad
        consumo de memoria
            - La velocidad debería aumentar, probablemente casi al doble, si el código está limitado por la CPU y no por memoria.
            - Esto también ayuda indirectamente a la velocidad, porque hay menos tráfico de memoria al cargar datos en la CPU.
    ¿Qué ocurre si el array es muy pequeño (por ejemplo 100 o 1.000 elementos)? ¿Sigue ganando NumPy? ¿Por qué podría no compensar?
        - Para arrays muy pequeños, NumPy puede no ser significativamente más rápido, y a veces Python puro con un loop simple puede competir.
        - Para arrays medianos o grandes, la ventaja de NumPy sí se nota mucho.
    Si tu cálculo vectorizado crea muchos arrays temporales (a+b+c+d), ¿qué coste oculto aparece?
        | Problema                    | Por qué ocurre                       | Efecto                                                        |
        | --------------------------- | ------------------------------------ | ------------------------------------------------------------- |
        | Arrays temporales múltiples | Evaluación secuencial de expresiones | Mayor uso de memoria y caché, más tiempo de copia             |
        | Overhead de memoria / cache | Cada suma crea un array nuevo        | Reduce ganancia SIMD                                          |
        | Posible ralentización       | Más lectura/escritura que cálculo    | Pequeño overhead puede superar ventaja SIMD en arrays grandes |
    ¿Qué técnicas conoces para reducir temporales? (pista: operaciones in-place, out=, composición, etc.)
        | Técnica                     | Cómo ayuda                                      |
        | --------------------------- | ----------------------------------------------- |
        | Operaciones in-place (`+=`) | Modifica array existente, cero temporales       |
        | `out=`                      | Función NumPy escribe directo en array destino  |
        | Composición / fusión        | Evita temporales intermedios, más SIMD-friendly |
        | Prealocar arrays            | Reduce a 1 temporal fijo                        |
        | Evitar slicing disperso     | Reduce memoria y mejora caché                   |

    Si haces np.sin(x) y luego np.sum(...), ¿qué parte esperas que sea el cuello de botella: el cálculo o el acceso a memoria?
        | Operación   | Coste relativo          | Cuello de botella esperado       |
        | ----------- | ----------------------- | -------------------------------- |
        | `np.sin(x)` | Alto (cálculo FP)       | Cálculo                          |
        | `np.sum(y)` | Bajo (simple suma SIMD) | Memoria solo si array gigantesco |

*** Bloque G — Cuándo NO usar NumPy (o cuándo no es la mejor primera opción) ***
    Si tu operación por elemento incluye una lógica compleja con ramas (if/elif/else), ¿crees que NumPy seguirá siendo tan ventajoso? ¿Por qué?
        - NumPy es más ventajoso cuando todos los elementos hacen lo mismo.
        - Condicionales por elemento → vectorización se degrada → a veces es mejor escribir loops explícitos en Cython, Numba o usar np.where con cuidado.
    Si el problema es principalmente de I/O (leer archivos, parsear JSON, llamadas a red), ¿tiene sentido optimizar con NumPy? ¿Qué optimizarías antes?
        - Problemas I/O-bound → NumPy casi no ayuda
        - Optimizar antes → acceso a datos, parsing, I/O eficiente
        - NumPy entra en juego solo cuando los datos ya están en memoria y la CPU sí es el cuello de botella
    Si necesitas estructuras heterogéneas (mezcla de tipos, objetos), ¿encaja NumPy o encaja mejor otra estructura? ¿Por qué?
        | Necesidad                 | ¿NumPy? | Mejor opción                         | Por qué                                   |
        | ------------------------- | ------- | ------------------------------------ | ----------------------------------------- |
        | Datos homogéneos, grandes | Sí      | NumPy                                | SIMD, contiguo, vectorizado               |
        | Mezcla de tipos / objetos | No      | Python nativo / Pandas / dataclasses | NumPy pierde ventajas, dtype=object lento |

        NumPy es para datos homogéneos y masivos en memoria. Si necesitas heterogeneidad, usas estructuras de Python o Pandas.
        
    ¿Qué pasa si tu algoritmo es inherentemente secuencial y depende del resultado del paso anterior (no vectorizable)? ¿Qué opciones existen?
        - Si cada paso depende del anterior, la paralelización y SIMD son casi imposibles.
        - La mejora viene de compilar Python o cambiar el algoritmo, no de NumPy puro.
*** Bloque H — Decisión técnica (reglas prácticas que deberían inferir) ***
    Completa esta frase con tu criterio: “Usaré NumPy cuando …” (mínimo 3 condiciones).
        - Los datos sean homogéneos y contiguos en memoria (todos floats o ints del mismo tipo, sin objetos mixtos).
        - Las operaciones sean independientes por elemento (sin dependencias secuenciales estrictas ni ramas complejas que rompan SIMD).
        - El tamaño de los datos sea suficientemente grande para amortizar el overhead de Python y aprovechar vectorización y SIMD.
            NumPy = datos homogéneos + operaciones paralelizables + suficiente tamaño para que la vectorización valga la pena.
    Completa esta frase: “No merece la pena usar NumPy cuando …” (mínimo 3 casos).
        - Los datos son heterogéneos o contienen objetos (mezcla de strings, números, listas, objetos personalizados), porque NumPy pierde eficiencia y termina usando dtype=object
        - El algoritmo es secuencial y depende del resultado del paso anterior, porque la vectorización no es posible y NumPy no aporta ventaja.
        - El problema es principalmente I/O-bound (lectura de archivos, parsing de JSON, llamadas a red), ya que la CPU no es el cuello de botella.
            NumPy no vale la pena cuando los datos son mixtos, el cálculo depende de pasos anteriores, el problema espera I/O o los datos son pequeños o muy ramificados.
    Si te piden acelerar un programa, ¿qué medirías primero para decidir si NumPy es la solución?
        - Perfilado → identificar qué parte consume más tiempo. -
        - CPU vs I/O → decidir si la optimización es de cálculo o de datos.
        - Datos y operaciones → homogéneos, contiguos, independientes = NumPy.
        - Tamaño del problema → suficientemente grande para amortizar overhead.
    Si el cuello de botella no es CPU sino memoria (RAM/cache), ¿qué estrategias aplicarías antes que “más vectorización”?
        | Estrategia                         | Por qué ayuda                                |
        | ---------------------------------- | -------------------------------------------- |
        | Contigüidad / recorrido secuencial | Reduce cache misses y acceso RAM lento       |
        | Reducir temporales / in-place      | Menos memoria, menos tráfico de datos        |
        | Tipos de datos más pequeños        | Menos bytes por elemento, más datos en cache |
        | Procesamiento en bloques           | Mantiene los datos dentro de cache L1/L2     |
        | Memory mapping / compresión        | Evita saturar RAM en datos grandes           |

*** Bloque I — Preguntas de cierre (para consolidar conclusiones) ***
    Resume en una frase: ¿qué ventaja principal aporta NumPy frente a bucles Python?
        - NumPy aporta principalmente velocidad en operaciones numéricas sobre arrays homogéneos grandes, gracias a vectorización, SIMD y ejecución en C, evitando el overhead de los bucles Python.
    Resume en una frase: ¿cuál es el coste oculto típico al usar NumPy sin cuidado?
        - El coste oculto típico es la creación de arrays temporales y copias innecesarias, que aumentan uso de memoria, accesos a caché y tiempo de ejecución, reduciendo o anulando la ventaja de la vectorización.
    ¿Qué “señales” en un problema te indican que probablemente sea vectorizable?
        - 
    ¿Qué “señales” te indican que probablemente no lo sea y requerirá otro enfoque?
        - 
 