# 🧬 Payload Analysis

`f346e6dffeb89b27015d29c71d78b4274605ed9b58ab801d76cf63f56a51cc13`

## 📌 Resumen

Artefacto clasificado como **Suspicious Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Suspicious Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:07:53+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `f346e6dffeb89b27015d29c71d78b4274605ed9b58ab801d76cf63f56a51cc13`
- **SHA1:** `31ec57caa717609c898b7607b507579a6226c9cb`
- **MD5:** `1fc13fb42e53ad72b1752314a1d1f4e3`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | OpenPGP Secret Key |
| Tamaño | 1.4 KiB |
| Entropía | 7.86 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=OpenPGP Secret Key; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | f346e6dffeb89b27015d29c71d78b4274605ed9b58ab801d76cf63f56a51cc13 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | candidate malware unknown |
| Prioridad | medium |
| Score | 5.0 |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
