# Benchmarks de Optimización en Python

## Descripción
- Tamaño del arreglo: 10,000,000 elementos (números aleatorios entre 0 y 1).
- Operación: `sum(sin(x) + x**2)` para cada `x`.
- Versiones:
  - A: Bucle for en Python puro.
  - B: Vectorizado con NumPy.
- Medición: Promedio de 3 ejecuciones usando `time.perf_counter()`.

## Tabla de Resultados

| Versión              | Tiempo Promedio (segundos) | Ratio de Mejora (vs Python loop) |
|----------------------|----------------------------|----------------------------------|
| Python loop (for)    | 4.5123                     | 1x                              |
| NumPy vectorizado    | 0.1487                     | 30.35x                          |

## Conclusión
Aprendí que los bucles en Python puro son lentos para operaciones repetitivas en grandes datasets debido a la interpretación overhead y llamadas a funciones en cada iteración. NumPy, al usar código compilado y vectorización, acelera drásticamente (hasta 30x en este caso) al procesar datos en bloques.

Optimizar importa cuando:
- Trabajas con datos grandes (millones de elementos).
- Operaciones repetitivas o computacionalmente intensas (e.g., ML, análisis de datos).
- Rendimiento es crítico (e.g., apps en tiempo real).
- No optimices prematuramente; mide primero con perfiles para identificar bottlenecks.