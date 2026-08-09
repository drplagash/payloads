# 🧬 Payload Analysis

`39fb1ae987e5b03e4e0c6e98fdb53f1257735acf23808833c7017830731ddde0`

## 📌 Resumen

Artefacto asociado a la familia **webshell** con evidencia suficiente para atribución. Se identificó 1 indicador técnico adicional.


## 🏷️ Clasificación

- **Categoría:** `Script`
- **Familia:** `webshell`
- **Confianza de familia:** `Media`
- **Riesgo:** `High`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:06:23.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `39fb1ae987e5b03e4e0c6e98fdb53f1257735acf23808833c7017830731ddde0`
- **SHA1:** `e8d43dd373d8c5e8937570e40c3aae35e6da62d0`
- **MD5:** `9c00f9ee68fda45b5b1002c31f0b908d`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | PHP script, ASCII text, with no line terminators |
| Tamaño | 33 B |
| Entropía | 4.38 |
| Strings | 1 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=PHP script, ASCII text, with no line terminators; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 39fb1ae987e5b03e4e0c6e98fdb53f1257735acf23808833c7017830731ddde0 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | valid script |
| Prioridad | medium |
| Score | 10.0 |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
