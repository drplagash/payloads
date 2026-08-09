# 🧬 Payload Analysis

`4f734b6448e5c2032fbda359b238c18aa8d119b274accce27b8f032e743e16e1`

## 📌 Resumen

Artefacto asociado a la familia **webshell** con evidencia suficiente para atribución. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Categoría:** `Web shell`
- **Familia:** `webshell`
- **Confianza de familia:** `Media`
- **Riesgo:** `High`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:30:44.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `4f734b6448e5c2032fbda359b238c18aa8d119b274accce27b8f032e743e16e1`
- **MD5:** `aa4c35ad04baa73b3249a2c11c527c57`

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
| url | hxxp://www[.]w3[.]org/2000/svg | strings |
| url | hxxp://www[.]w3[.]org/1999/xlink | strings |
| hash | 4f734b6448e5c2032fbda359b238c18aa8d119b274accce27b8f032e743e16e1 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
