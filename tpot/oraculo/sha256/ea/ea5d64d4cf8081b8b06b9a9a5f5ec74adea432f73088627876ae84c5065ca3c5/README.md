# 🧬 Payload Analysis

`ea5d64d4cf8081b8b06b9a9a5f5ec74adea432f73088627876ae84c5065ca3c5`

## 📌 Resumen

Artefacto asociado a la familia **webshell** con evidencia suficiente para atribución.

## 🏷️ Clasificación

- **Categoría:** `Script`
- **Familia:** `webshell`
- **Confianza de familia:** `Media`
- **Riesgo:** `Critical`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:08:37+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `ea5d64d4cf8081b8b06b9a9a5f5ec74adea432f73088627876ae84c5065ca3c5`
- **SHA1:** `3d699f76a03e2046fce9412de120e2f9a4d73ee4`
- **MD5:** `8b742676a04b29232b7ed0d9fdd8c681`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | PHP script, ASCII text, with very long lines (1189), with no line terminators |
| Tamaño | 1.2 KiB |
| Entropía | 5.84 |
| Strings | 1 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=PHP script, ASCII text, with very long lines (1189), with no line terminators; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | ea5d64d4cf8081b8b06b9a9a5f5ec74adea432f73088627876ae84c5065ca3c5 | static_analysis |
| ip | 170.9.16.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | obfuscated script |
| Prioridad | high |
| Score | 20.0 |

## 🔭 Enriquecimiento histórico local

| Fuente | Detecciones | Etiquetas |
| --- | --- | --- |
| virustotal | 22 | Dropper.DR/BAT.Agent.CGR, Trojan.Generic.D4CB6577, php.trojan.generic, Malware@#3enhdqo8dd4fn, Trojan.GenericKD.80438647 (B), Trojan.GenericKD.80438647, Detected, Php.Trojan-Downloader.Der.Bwnw |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
