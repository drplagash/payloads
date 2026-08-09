# 🧬 Payload Analysis

`a592eb6302c4b7de408c64bf8b5a9e8255beb0c9f2a737ec0981dd56f3bf9035`

## 📌 Resumen

Artefacto asociado a la familia **webshell** con evidencia suficiente para atribución.

## 🏷️ Clasificación

- **Categoría:** `Script`
- **Familia:** `webshell`
- **Confianza de familia:** `Media`
- **Riesgo:** `Critical`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:07:53+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `a592eb6302c4b7de408c64bf8b5a9e8255beb0c9f2a737ec0981dd56f3bf9035`
- **SHA1:** `52492daacbb3cc33def844459ab59757bf9642e8`
- **MD5:** `7a78e7cba5db4bdf434f230fc4497744`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | PHP script, ASCII text, with no line terminators |
| Tamaño | 241 B |
| Entropía | 5.82 |
| Strings | 1 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=PHP script, ASCII text, with no line terminators; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | a592eb6302c4b7de408c64bf8b5a9e8255beb0c9f2a737ec0981dd56f3bf9035 | static_analysis |
| ip | 211.62.61.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | obfuscated script |
| Prioridad | high |
| Score | 20.0 |

## 🔭 Enriquecimiento histórico local

| Fuente | Detecciones | Etiquetas |
| --- | --- | --- |
| virustotal | 23 | Exploit-CVE-2024-4577.a, TrojanDownloader/PHP.Maloader.a, Detected, Dropper.DR/BAT.Agent.CGR, Malware@#12akt2v7pnogk, Trojan-Downloader.PHP.Agent, Trojan.Script.Malgent.4!c, Trojan[downloader]:Php/Malgent.Gen |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
