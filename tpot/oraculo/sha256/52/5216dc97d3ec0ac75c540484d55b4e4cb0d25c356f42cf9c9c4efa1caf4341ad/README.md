# 🧬 Payload Analysis

`5216dc97d3ec0ac75c540484d55b4e4cb0d25c356f42cf9c9c4efa1caf4341ad`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Se identificó 1 indicador técnico adicional. Una detección YARA válida respalda el análisis. **Ficha malware:** [malware-like/oraculo/botnet/5216dc97d3ec0ac75c540484d55b4e4cb0d25c356f42cf9c9c4efa1caf4341ad.md](../../../../../malware-like/oraculo/botnet/5216dc97d3ec0ac75c540484d55b4e4cb0d25c356f42cf9c9c4efa1caf4341ad.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:52:40.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `5216dc97d3ec0ac75c540484d55b4e4cb0d25c356f42cf9c9c4efa1caf4341ad`
- **SHA1:** `e0ecf1445b102ed0941fb1cc9ffb3e2a12a1a4d1`
- **MD5:** `5127ebe7697af5fdd3a292bedd5939a1`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 4.0 KiB |
| Entropía | 7.98 |
| Strings | 21 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=8.0; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 5216dc97d3ec0ac75c540484d55b4e4cb0d25c356f42cf9c9c4efa1caf4341ad | static_analysis |
| ip | 2.184.239.XXX | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_High_Entropy |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | unsupported format |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
