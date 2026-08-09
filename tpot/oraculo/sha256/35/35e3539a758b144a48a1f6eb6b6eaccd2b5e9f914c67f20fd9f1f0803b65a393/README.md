# 🧬 Payload Analysis

`35e3539a758b144a48a1f6eb6b6eaccd2b5e9f914c67f20fd9f1f0803b65a393`

## 📌 Resumen

Artefacto identificado como XML 1.0 document, ASCII text, with very long lines (710), with no line terminators de 710 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. La evidencia es estática: este snapshot no demuestra por sí solo que la descarga llegara a ejecutarse.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:51:31.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `35e3539a758b144a48a1f6eb6b6eaccd2b5e9f914c67f20fd9f1f0803b65a393`
- **SHA1:** `6387528bb232957529c5f756c8f92f188ac3c3ac`
- **MD5:** `c1dc59a055083ff1a0041ff9debb2be5`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | XML 1.0 document, ASCII text, with very long lines (710), with no line terminators |
| Tamaño | 710 B |
| Entropía | 5.01 |
| Strings | 1 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=XML 1.0 document, ASCII text, with very long lines (710), with no line terminators; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh | strings |
| url | hxxp://91.92.40.XXX/wget.sh;chmod | strings |
| ip | 91.92.40.XXX | static_analysis |
| hash | 35e3539a758b144a48a1f6eb6b6eaccd2b5e9f914c67f20fd9f1f0803b65a393 | static_analysis |
| ip | 45.153.34.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | html response |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
