# 🧬 Payload Analysis

`0a8abd5751bfac39b2a42b4bb4e64f2c1f8b1de784bf656a701f5689f1a5d2c8`

## 📌 Resumen

Artefacto asociado a la familia **webshell** con evidencia suficiente para atribución. Se identificó 1 indicador técnico adicional. Una detección YARA válida respalda el análisis.


## 🏷️ Clasificación

- **Categoría:** `Web shell`
- **Familia:** `webshell`
- **Confianza de familia:** `Alta`
- **Riesgo:** `Critical`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:30:16.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `0a8abd5751bfac39b2a42b4bb4e64f2c1f8b1de784bf656a701f5689f1a5d2c8`
- **SHA1:** `1adbff511798a0d6c3456ffcf0955e527f0908c2`
- **MD5:** `62e7b2effe05164fe8b93169dc764aee`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | PHP script, ASCII text, with no line terminators |
| Tamaño | 245 B |
| Entropía | 5.85 |
| Strings | 1 |

## 🔬 Evidencia de clasificación

- YARA match: webshell
YARA match: webshell
YARA match: webshell
YARA match: webshell
YARA match: webshell
YARA match: webshell
YARA match: webshell
YARA match: webshell
YARA match: webshell
YARA match: webshell
YARA match: webshell
YARA match: webshell
YARA match: webshell
- Motivos técnicos: mime=PHP script, ASCII text, with no line terminators; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 0a8abd5751bfac39b2a42b4bb4e64f2c1f8b1de784bf656a701f5689f1a5d2c8 | static_analysis |
| ip | 31.132.90.XXX | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_PHP_Webshell |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | obfuscated script |
| Prioridad | high |
| Score | 20.0 |

## 🔭 Enriquecimiento histórico local

| Fuente | Detecciones | Etiquetas |
| --- | --- | --- |
| virustotal | 27 | Trojan.Agent.GRHU (B), Detected, Trojan.PHP.Agent.JQR, PHP/TrojanDownloader.Agent.DW trojan, Dropper.DR/BAT.Agent.CGR, Html.Trojan.A26105228, Trojan:Script/Wacatac.B!ml, php.trojan.wacatac |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
