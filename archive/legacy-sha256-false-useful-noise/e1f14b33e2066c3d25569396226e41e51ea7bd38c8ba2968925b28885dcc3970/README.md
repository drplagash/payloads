# 🧬 Payload Analysis

`e1f14b33e2066c3d25569396226e41e51ea7bd38c8ba2968925b28885dcc3970`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Comportamientos destacados: Binary execution. Se identificó 1 indicador técnico adicional. **Ficha malware:** [malware-like/oraculo/botnet/e1f14b33e2066c3d25569396226e41e51ea7bd38c8ba2968925b28885dcc3970.md](../../../../../malware-like/oraculo/botnet/e1f14b33e2066c3d25569396226e41e51ea7bd38c8ba2968925b28885dcc3970.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:24:57.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `e1f14b33e2066c3d25569396226e41e51ea7bd38c8ba2968925b28885dcc3970`
- **SHA1:** `505cb2a3605c374cea03990063e9a9fce3ee1513`
- **MD5:** `a162b5bd10a7dea634d190b6e779e89d`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | DOS executable (COM), start instruction 0xeb5e52e1 eb5e52d1 |
| Tamaño | 4.0 KiB |
| Entropía | 5.91 |
| Strings | 132 |

## 🧠 Comportamiento observado

1. **Binary execution**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=DOS executable (COM), start instruction 0xeb5e52e1 eb5e52d1; strings=132; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | e1f14b33e2066c3d25569396226e41e51ea7bd38c8ba2968925b28885dcc3970 | static_analysis |
| ip | 189.79.136.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | archive container |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
