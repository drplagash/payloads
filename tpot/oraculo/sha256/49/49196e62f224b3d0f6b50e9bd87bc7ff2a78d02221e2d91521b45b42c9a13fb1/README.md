# 🧬 Payload Analysis

`49196e62f224b3d0f6b50e9bd87bc7ff2a78d02221e2d91521b45b42c9a13fb1`

## 📌 Resumen

Artefacto de 1.4 KiB. Formato identificado como Award BIOS Logo, 128 x 126. Presenta entropía elevada (7.88), compatible con contenido empaquetado, cifrado o de alta aleatoriedad. Las detecciones YARA incluyen `Suspicious_High_Entropy`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 indicador técnico adicional.


## 🗓️ Registro

- **Registrado:** `2026-08-09T20:29:36.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `49196e62f224b3d0f6b50e9bd87bc7ff2a78d02221e2d91521b45b42c9a13fb1`
- **SHA1:** `a7e110b6c8d61482171b6a6f288c866904283d77`
- **MD5:** `a72299caa25b26d695cd44833f9eed66`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | Award BIOS Logo, 128 x 126 |
| Tamaño | 1.4 KiB |
| Entropía | 7.88 |
| Strings | 1 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=Award BIOS Logo, 128 x 126; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 49196e62f224b3d0f6b50e9bd87bc7ff2a78d02221e2d91521b45b42c9a13fb1 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_High_Entropy |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | media or resource |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
