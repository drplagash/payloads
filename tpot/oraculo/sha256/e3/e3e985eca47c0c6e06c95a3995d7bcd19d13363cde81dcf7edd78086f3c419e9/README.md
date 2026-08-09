# 🧬 Payload Analysis

`e3e985eca47c0c6e06c95a3995d7bcd19d13363cde81dcf7edd78086f3c419e9`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:07:44+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `e3e985eca47c0c6e06c95a3995d7bcd19d13363cde81dcf7edd78086f3c419e9`
- **SHA1:** `6a616e5dae7809a2a6462a1805303a3233a1b040`
- **MD5:** `a34a5cedf5369e1269a7b39716d733f6`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 212 B |
| Entropía | 5.19 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.172.XXX | static_analysis |
| hash | e3e985eca47c0c6e06c95a3995d7bcd19d13363cde81dcf7edd78086f3c419e9 | static_analysis |
| ip | 5.187.35.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
