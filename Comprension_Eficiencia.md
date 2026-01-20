## Comprensión de la eficiencia de Numpy

*** Bloque A — Observación inicial (qué pasa) ***
    Si implementas el mismo cálculo con un for en Python y con una operación vectorizada en NumPy, ¿qué esperas que ocurra con el tiempo de ejecución cuando el tamaño del array pasa de 1.000 a 10.000.000 elementos?
    ¿En qué punto (tamaño aproximado) crees que la diferencia empieza a ser clara? ¿Por qué?
    ¿Qué parte del programa crees que consume más tiempo: el cálculo matemático o el “mecanismo” de recorrer y operar elemento a elemento?
*** Bloque B — Representación de datos (qué estás procesando realmente) ***
    ¿Cómo almacena Python una lista de números? ¿Es una lista de valores o una lista de referencias a objetos?
    ¿Qué implica para la CPU acceder a datos dispersos en memoria (objetos separados) frente a datos contiguos?
    ¿Qué significa que un array NumPy sea “homogéneo” (mismo dtype) y por qué podría ayudar al rendimiento?
    ¿Qué coste adicional tiene Python al operar con tipos dinámicos en cada iteración?
*** Bloque C — Overhead del intérprete (por qué el bucle Python pesa tanto) ***
    En un bucle Python, por cada iteración, ¿qué operaciones “extra” ocurren además de sumar o multiplicar? (pista: resolución de tipos, llamadas, objetos, etc.)
    ¿Por qué una llamada a math.sin() dentro de un bucle puede ser especialmente cara repetida millones de veces?
    ¿Qué crees que significa realmente “overhead del intérprete” en términos de tiempo por elemento?
*** Bloque D — Dónde se ejecuta el bucle (Python vs C) ***
    Cuando escribes np.sin(x), ¿quién recorre el array: tu bucle Python o un bucle interno compilado?
    ¿Por qué un bucle en C/Fortran puede ser mucho más eficiente que el mismo bucle escrito en Python?
    ¿Qué cambia en el número de “entradas” al intérprete entre estas dos versiones?
        bucle Python con for
        vectorización NumPy
*** Bloque E — Cachés, contigüidad y SIMD (por qué la CPU “vuela” con NumPy) ***
    ¿Qué es la caché de CPU y por qué importa en cálculos sobre arrays grandes?
    ¿Qué es el “prefetching” y por qué funciona mejor con memoria contigua?
    ¿Qué tipo de operaciones crees que se benefician más de SIMD (vectorización a nivel CPU): sumas/multiplicaciones, o lógica con muchos if? ¿Por qué?
    ¿Qué crees que pasa si tus datos no están contiguos (slicing raro, arrays no contiguos)? ¿Se mantiene la ventaja?
*** Bloque F — Experimentación (preguntas para guiar un mini-lab) ***
    Si repites el benchmark con float32 en lugar de float64, ¿qué esperas que pase con:
        velocidad
        consumo de memoria
    ¿Qué ocurre si el array es muy pequeño (por ejemplo 100 o 1.000 elementos)? ¿Sigue ganando NumPy? ¿Por qué podría no compensar?
    Si tu cálculo vectorizado crea muchos arrays temporales (a+b+c+d), ¿qué coste oculto aparece?
    ¿Qué técnicas conoces para reducir temporales? (pista: operaciones in-place, out=, composición, etc.)
    Si haces np.sin(x) y luego np.sum(...), ¿qué parte esperas que sea el cuello de botella: el cálculo o el acceso a memoria?
*** Bloque G — Cuándo NO usar NumPy (o cuándo no es la mejor primera opción) ***
    Si tu operación por elemento incluye una lógica compleja con ramas (if/elif/else), ¿crees que NumPy seguirá siendo tan ventajoso? ¿Por qué?
    Si el problema es principalmente de I/O (leer archivos, parsear JSON, llamadas a red), ¿tiene sentido optimizar con NumPy? ¿Qué optimizarías antes?
    Si necesitas estructuras heterogéneas (mezcla de tipos, objetos), ¿encaja NumPy o encaja mejor otra estructura? ¿Por qué?
    ¿Qué pasa si tu algoritmo es inherentemente secuencial y depende del resultado del paso anterior (no vectorizable)? ¿Qué opciones existen?
*** Bloque H — Decisión técnica (reglas prácticas que deberían inferir) ***
    Completa esta frase con tu criterio: “Usaré NumPy cuando …” (mínimo 3 condiciones).
    Completa esta frase: “No merece la pena usar NumPy cuando …” (mínimo 3 casos).
    Si te piden acelerar un programa, ¿qué medirías primero para decidir si NumPy es la solución?
    Si el cuello de botella no es CPU sino memoria (RAM/cache), ¿qué estrategias aplicarías antes que “más vectorización”?
*** Bloque I — Preguntas de cierre (para consolidar conclusiones) ***
    Resume en una frase: ¿qué ventaja principal aporta NumPy frente a bucles Python?
    Resume en una frase: ¿cuál es el coste oculto típico al usar NumPy sin cuidado?
    ¿Qué “señales” en un problema te indican que probablemente sea vectorizable?
    ¿Qué “señales” te indican que probablemente no lo sea y requerirá otro enfoque?
 