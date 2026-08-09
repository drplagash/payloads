# 🧬 Payload Analysis

`08246801325afd8d149b384aa0b2b372fa36f22732b7a6db8588f6031fa09a8c`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:51:39+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `08246801325afd8d149b384aa0b2b372fa36f22732b7a6db8588f6031fa09a8c`
- **SHA1:** `6d6f1d7aa3432b01662d94d26d642b25267f3858`
- **MD5:** `ac7ca27ecea56f7b5b1dddc7eba7fe01`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 51 B |
| Entropía | 4.46 |
| Strings | 3 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 08246801325afd8d149b384aa0b2b372fa36f22732b7a6db8588f6031fa09a8c | static_analysis |
| ip | 45.198.224.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
