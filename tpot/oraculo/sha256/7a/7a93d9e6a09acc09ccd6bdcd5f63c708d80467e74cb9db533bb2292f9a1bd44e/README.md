# 🧬 Payload Analysis

`7a93d9e6a09acc09ccd6bdcd5f63c708d80467e74cb9db533bb2292f9a1bd44e`

## 📌 Resumen

Artefacto identificado como XML 1.0 document, ASCII text, with very long lines (483), with no line terminators de 483 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. Se extrajeron 3 referencias URL únicas. La evidencia es estática: este snapshot no demuestra por sí solo que la descarga llegara a ejecutarse.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:51:31.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `7a93d9e6a09acc09ccd6bdcd5f63c708d80467e74cb9db533bb2292f9a1bd44e`
- **SHA1:** `4ff56cd1f65c70bd55ccb59fcf90f167416f76dd`
- **MD5:** `efed2686db9f58a00464b7fc5eccab9b`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | XML 1.0 document, ASCII text, with very long lines (483), with no line terminators |
| Tamaño | 483 B |
| Entropía | 5.21 |
| Strings | 1 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=XML 1.0 document, ASCII text, with very long lines (483), with no line terminators; iocs=6

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh | strings |
| url | hxxp://www[.]huawei[.]com/vehicle/nu | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/envelope/ | strings |
| url | hxxp://91.92.40.XXX/wget.sh;chmod | strings |
| ip | 91.92.40.XXX | static_analysis |
| hash | 7a93d9e6a09acc09ccd6bdcd5f63c708d80467e74cb9db533bb2292f9a1bd44e | static_analysis |
| ip | 45.153.34.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | html response |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
