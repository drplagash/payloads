# 🧬 Payload Analysis

`57d1eb32900945bf723ef9089097a91239a9b4e21984cfef10b07e7c4511bfe8`

## 📌 Resumen

Artefacto de 1.4 KiB. Formato identificado como PDP-11 overlaid pure executable not stripped. Presenta entropía elevada (7.86), compatible con contenido empaquetado, cifrado o de alta aleatoriedad. Las detecciones YARA incluyen `Suspicious_High_Entropy`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 indicador técnico adicional.


## 🗓️ Registro

- **Registrado:** `2026-08-09T19:41:47.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `57d1eb32900945bf723ef9089097a91239a9b4e21984cfef10b07e7c4511bfe8`
- **MD5:** `74b509ea612d653e298e52cdafcf600d`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | PDP-11 overlaid pure executable not stripped |
| Tamaño | 1.4 KiB |
| Entropía | 7.86 |
| Strings | 1 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=PDP-11 overlaid pure executable not stripped; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 57d1eb32900945bf723ef9089097a91239a9b4e21984cfef10b07e7c4511bfe8 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_High_Entropy |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
