# 🧬 Payload Analysis

`dedb09d157722cfc3d3c544e52f3a0ed77466a5ffd1d41a1ed809ea9480bd275`

## 📌 Resumen

Artefacto de 548 B. La evidencia disponible identifica capacidad de descarga remota. Infraestructura remota: `hxxps://api[.]w[.]org/`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/dedb09d157722cfc3d3c544e52f3a0ed77466a5ffd1d41a1ed809ea9480bd275.md](../../../../../malware-like/oraculo/downloader/dedb09d157722cfc3d3c544e52f3a0ed77466a5ffd1d41a1ed809ea9480bd275.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:37:52.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `dedb09d157722cfc3d3c544e52f3a0ed77466a5ffd1d41a1ed809ea9480bd275`
- **MD5:** `09041c5739b5eae935df99cca4ba1d10`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.39 |
| Strings | 8 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://api[.]w[.]org/ | strings |
| hash | dedb09d157722cfc3d3c544e52f3a0ed77466a5ffd1d41a1ed809ea9480bd275 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
