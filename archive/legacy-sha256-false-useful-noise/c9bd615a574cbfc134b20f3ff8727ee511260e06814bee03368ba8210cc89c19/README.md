# 🧬 Payload Analysis

`c9bd615a574cbfc134b20f3ff8727ee511260e06814bee03368ba8210cc89c19`

## 📌 Resumen

Artefacto de 548 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `Article` en `hxxps://schema[.]org/Article`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/c9bd615a574cbfc134b20f3ff8727ee511260e06814bee03368ba8210cc89c19.md](../../../../../malware-like/oraculo/downloader/c9bd615a574cbfc134b20f3ff8727ee511260e06814bee03368ba8210cc89c19.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:49:11.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `c9bd615a574cbfc134b20f3ff8727ee511260e06814bee03368ba8210cc89c19`
- **SHA1:** `bbc97310a2d6144f1430e267b60957389c1d95e4`
- **MD5:** `761f93f246cb4b7002de2f9e96cea044`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.29 |
| Strings | 12 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://schema[.]org/Article | strings |
| hash | c9bd615a574cbfc134b20f3ff8727ee511260e06814bee03368ba8210cc89c19 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
