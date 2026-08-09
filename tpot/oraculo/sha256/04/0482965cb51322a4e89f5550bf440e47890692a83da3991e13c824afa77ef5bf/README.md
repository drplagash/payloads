# 🧬 Payload Analysis

`0482965cb51322a4e89f5550bf440e47890692a83da3991e13c824afa77ef5bf`

## 📌 Resumen

Artefacto clasificado como **Suspicious Payload** a partir de la evidencia disponible en Oráculo SOC. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Suspicious Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:26:57+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `0482965cb51322a4e89f5550bf440e47890692a83da3991e13c824afa77ef5bf`
- **SHA1:** `a750cdcb52953a8587166b9e06144558c1c6d1fd`
- **MD5:** `23c05b730837ce3b6d50968a1609dd1a`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | OpenPGP Public Key Version 2, Created Thu Sep  3 17:03:17 2037, Unknown Algorithm (0x28) |
| Tamaño | 4.0 KiB |
| Entropía | 7.94 |
| Strings | 10 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=OpenPGP Public Key Version 2, Created Thu Sep  3 17:03:17 2037, Unknown Algorithm (0x28); high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 0482965cb51322a4e89f5550bf440e47890692a83da3991e13c824afa77ef5bf | static_analysis |
| ip | 189.79.136.XXX | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_High_Entropy |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | candidate malware unknown |
| Prioridad | medium |
| Score | 5.0 |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
