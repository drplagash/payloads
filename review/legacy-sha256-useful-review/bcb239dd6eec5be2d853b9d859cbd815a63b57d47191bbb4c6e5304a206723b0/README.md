# 🧬 Payload Analysis

`bcb239dd6eec5be2d853b9d859cbd815a63b57d47191bbb4c6e5304a206723b0`

## 📌 Resumen

Artefacto de 1.4 KiB. Formato identificado como DOS executable (COM), start instruction 0xeb6d178e 0c50a866. Presenta entropía elevada (7.88), compatible con contenido empaquetado, cifrado o de alta aleatoriedad. Las detecciones YARA incluyen `Suspicious_High_Entropy`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 indicador técnico adicional.


## 🗓️ Registro

- **Registrado:** `2026-08-09T20:23:38.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `bcb239dd6eec5be2d853b9d859cbd815a63b57d47191bbb4c6e5304a206723b0`
- **SHA1:** `20c51b18469e4bf0dc05d22c8c26c9dc3d770485`
- **MD5:** `fa84024ffe7956846c7c53cd3cbf8462`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | DOS executable (COM), start instruction 0xeb6d178e 0c50a866 |
| Tamaño | 1.4 KiB |
| Entropía | 7.88 |
| Strings | 3 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=DOS executable (COM), start instruction 0xeb6d178e 0c50a866; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | bcb239dd6eec5be2d853b9d859cbd815a63b57d47191bbb4c6e5304a206723b0 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_High_Entropy |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | archive container |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
