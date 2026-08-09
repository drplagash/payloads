# 🧬 Payload Analysis

`6194d58d2957dfcc01d6e670ae444de1ae37a83f3540ce72ac7d82213ed2f09d`

## 📌 Resumen

Artefacto asociado a la familia **webshell** con evidencia suficiente para atribución.

## 🏷️ Clasificación

- **Categoría:** `Web shell`
- **Familia:** `webshell`
- **Confianza de familia:** `Media`
- **Riesgo:** `High`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:30:12+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `6194d58d2957dfcc01d6e670ae444de1ae37a83f3540ce72ac7d82213ed2f09d`
- **MD5:** `e2467c50b767ac5d33ef0b8d1cbc2591`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.73 |
| Strings | 6 |

## 🔬 Evidencia de clasificación

- Webshell indicators (PHP eval/system)

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://www[.]w3[.]org/1999/xlink | strings |
| url | hxxp://www[.]w3[.]org/2000/svg | strings |
| hash | 6194d58d2957dfcc01d6e670ae444de1ae37a83f3540ce72ac7d82213ed2f09d | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
