# 🧬 Payload Analysis

`ec523c5780f851837fab5727e1272d4fcb97a60c195f6188211c444615f5323c`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Binary execution.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:26:56+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `ec523c5780f851837fab5727e1272d4fcb97a60c195f6188211c444615f5323c`
- **SHA1:** `1348ef2fa42590ea0eb688f5abaa29ac990e5281`
- **MD5:** `a18d79dd0def2420b1315c0b4edaf44c`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | DOS executable (COM), start instruction 0x8c994aa7 384bb53e |
| Tamaño | 4.0 KiB |
| Entropía | 5.75 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Binary execution**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=DOS executable (COM), start instruction 0x8c994aa7 384bb53e; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | ec523c5780f851837fab5727e1272d4fcb97a60c195f6188211c444615f5323c | static_analysis |
| ip | 189.79.136.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | archive container |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
