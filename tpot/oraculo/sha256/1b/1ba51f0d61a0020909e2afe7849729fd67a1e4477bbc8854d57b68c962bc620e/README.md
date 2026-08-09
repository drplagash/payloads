# 🧬 Payload Analysis

`1ba51f0d61a0020909e2afe7849729fd67a1e4477bbc8854d57b68c962bc620e`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:02:12+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `1ba51f0d61a0020909e2afe7849729fd67a1e4477bbc8854d57b68c962bc620e`
- **SHA1:** `1edbcbd785f42705faef3deed46029e410fb5ff1`
- **MD5:** `47b1fdf1a24766f6fb6a82ecd8b57cc2`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | OpenPGP Public Key |
| Tamaño | 4.0 KiB |
| Entropía | 5.98 |
| Strings | 36 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=OpenPGP Public Key; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 1ba51f0d61a0020909e2afe7849729fd67a1e4477bbc8854d57b68c962bc620e | static_analysis |
| ip | 37.57.94.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
