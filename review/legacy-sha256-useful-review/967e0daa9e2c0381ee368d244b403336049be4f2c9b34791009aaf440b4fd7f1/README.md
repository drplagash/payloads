# 🧬 Payload Analysis

`967e0daa9e2c0381ee368d244b403336049be4f2c9b34791009aaf440b4fd7f1`

## 📌 Resumen

Artefacto de 4.0 KiB. Entropía registrada: 7.09. Las detecciones YARA incluyen `Suspicious_High_Entropy`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 indicador técnico adicional.


## 🗓️ Registro

- **Registrado:** `2026-08-09T20:24:57.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `967e0daa9e2c0381ee368d244b403336049be4f2c9b34791009aaf440b4fd7f1`
- **SHA1:** `417687997d368c6c9ffe06909d0e9f7159591051`
- **MD5:** `e03fd0a588471497ed1aa163c6330610`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 4.0 KiB |
| Entropía | 7.09 |
| Strings | 55 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=7.1; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 967e0daa9e2c0381ee368d244b403336049be4f2c9b34791009aaf440b4fd7f1 | static_analysis |
| ip | 189.79.136.XXX | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_High_Entropy |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | unsupported format |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
