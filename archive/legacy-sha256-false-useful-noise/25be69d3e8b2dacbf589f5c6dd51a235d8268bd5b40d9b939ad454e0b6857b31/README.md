# 🧬 Payload Analysis

`25be69d3e8b2dacbf589f5c6dd51a235d8268bd5b40d9b939ad454e0b6857b31`

## 📌 Resumen

Artefacto de 548 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `blog-cover.jpg` en `hxxps://casper[.]ghost[.]org/v1.0.0/images/blog-cover.jpg`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/25be69d3e8b2dacbf589f5c6dd51a235d8268bd5b40d9b939ad454e0b6857b31.md](../../../../../malware-like/oraculo/downloader/25be69d3e8b2dacbf589f5c6dd51a235d8268bd5b40d9b939ad454e0b6857b31.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:59:38.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `25be69d3e8b2dacbf589f5c6dd51a235d8268bd5b40d9b939ad454e0b6857b31`
- **SHA1:** `67a00fa0d621c6d8182513411ed9bf8b9f0ab682`
- **MD5:** `2565bbde97e870041f8c41c086f559c2`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.24 |
| Strings | 12 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://casper[.]ghost[.]org/v1.0.0/images/blog-cover.jpg) | strings |
| hash | 25be69d3e8b2dacbf589f5c6dd51a235d8268bd5b40d9b939ad454e0b6857b31 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
