# 🧬 Payload Analysis

`d08d0801e61c28bed6913ca1a07a15af9bfe08c030d68a0b247094ffdee106b9`

## 📌 Resumen

Artefacto de 1.4 KiB. Formato identificado como PGP symmetric key encrypted data - salted -. Presenta entropía elevada (7.88), compatible con contenido empaquetado, cifrado o de alta aleatoriedad. Las detecciones YARA incluyen `Suspicious_High_Entropy`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 indicador técnico adicional.


## 🗓️ Registro

- **Registrado:** `2026-08-09T20:43:55.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d08d0801e61c28bed6913ca1a07a15af9bfe08c030d68a0b247094ffdee106b9`
- **SHA1:** `4d78c3e9c692609c9e245abf2020cce732baa820`
- **MD5:** `778fd65d8540e7602edd8651792df86d`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | PGP symmetric key encrypted data - salted - |
| Tamaño | 1.4 KiB |
| Entropía | 7.88 |
| Strings | 2 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=PGP symmetric key encrypted data - salted -; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | d08d0801e61c28bed6913ca1a07a15af9bfe08c030d68a0b247094ffdee106b9 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

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
