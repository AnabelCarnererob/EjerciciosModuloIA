## Reto 1 — Matriz de decisión: ¿qué lenguaje elegirías y por qué?

Escenario:
A) Entrenar un modelo y desplegarlo como API para predicciones.

| Criterio                                 |  Peso (1–5) | Python (1–5)  | R (1–5) | Java (1–5)  |  Node (1–5)  |
|------------------------------------------|-------------|---------------|---------|-------------|--------------|
| Ecosistema IA/ML (librerías, comunidad)  |      5      |      5        |    4    |      3      |       2      |
| Productividad / prototipado              |      4      |      5        |    4    |      2      |       3      |
| Rendimiento / latencia                   |      4      |      3        |    2    |      5      |       4      |
| Concurrencia / I-O / servicios           |      5      |      3        |    1    |      5      |       5      |
| Integración Big Data (Spark, conectores) |      3      |      4        |    3    |      5      |       2      |
| Despliegue y portabilidad                |      5      |      3        |    2    |      5      |       4      |
| Mantenibilidad / tipado / tooling        |      4      |      3        |    2    |      5      |       4      |
| Talento disponible (equipo)              |      4      |      5        |    2    |      4      |       4      |
| **TOTAL ponderado**                      |    **34**   |   **131**     |  **84** |   **144**   |    **121**   |


En este escenario, Java es el lenguaje ganador porque maximiza el rendimiento, la concurrencia, la estabilidad del servicio y la facilidad de despliegue en entornos de producción. Su ecosistema enterprise y su fuerte tipado lo hacen especialmente adecuado para APIs críticas con altos SLA. Sin embargo, esta elección introduce un riesgo técnico importante: Java no es el lenguaje ideal para entrenamiento de modelos, tiene un ecosistema ML más limitado y reduce la productividad en la fase experimental. Esto puede ralentizar iteraciones de ciencia de datos o dificultar el uso de frameworks de vanguardia.
La forma más sólida de mitigar este riesgo es adoptar una arquitectura híbrida: usar Python para el entrenamiento, experimentación y gestión del pipeline ML, y Java (o Node) como capa de serving del modelo ya entrenado, expuesto como API. Esto combina la velocidad y potencia del ecosistema de IA en Python con la robustez de Java en producción. Adicionalmente, se puede fortalecer el modelo operativo con contenedores, formatos de exportación estándar como ONNX y un diseño de microservicios desacoplado, permitiendo reemplazar o actualizar modelos sin afectar al servicio.