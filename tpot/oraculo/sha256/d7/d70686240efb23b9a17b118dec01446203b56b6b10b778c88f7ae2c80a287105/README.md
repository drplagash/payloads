# 🧬 Payload Analysis

`d70686240efb23b9a17b118dec01446203b56b6b10b778c88f7ae2c80a287105`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: High entropy.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:01:06+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d70686240efb23b9a17b118dec01446203b56b6b10b778c88f7ae2c80a287105`
- **SHA1:** `5173017679ac07c380d7a8b5b1f0301deda2e640`
- **MD5:** `fe054e45400d7fa86d49f8dcb43c8043`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | DOS executable (COM), start instruction 0xb846ee51 f33df85e |
| Tamaño | 1.4 KiB |
| Entropía | 7.87 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **High entropy**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=DOS executable (COM), start instruction 0xb846ee51 f33df85e; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | d70686240efb23b9a17b118dec01446203b56b6b10b778c88f7ae2c80a287105 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | archive container |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
