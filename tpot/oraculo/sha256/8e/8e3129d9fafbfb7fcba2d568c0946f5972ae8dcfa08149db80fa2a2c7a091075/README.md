# 🧬 Payload Analysis

`8e3129d9fafbfb7fcba2d568c0946f5972ae8dcfa08149db80fa2a2c7a091075`

## 📌 Resumen

Artefacto asociado a la familia **webshell** con evidencia suficiente para atribución. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Familia:** `webshell`
- **Confianza de familia:** `Media`
- **Riesgo:** `High`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:37:52.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `8e3129d9fafbfb7fcba2d568c0946f5972ae8dcfa08149db80fa2a2c7a091075`
- **MD5:** `ce8de7ccc7907c0fe2b66d4cc3446070`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.71 |
| Strings | 7 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://www[.]w3[.]org/1999/xlink | strings |
| url | hxxp://www[.]w3[.]org/2000/svg | strings |
| hash | 8e3129d9fafbfb7fcba2d568c0946f5972ae8dcfa08149db80fa2a2c7a091075 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
