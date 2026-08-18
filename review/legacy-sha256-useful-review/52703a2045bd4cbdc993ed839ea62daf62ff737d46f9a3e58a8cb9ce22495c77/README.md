# 🧬 Payload Analysis

`52703a2045bd4cbdc993ed839ea62daf62ff737d46f9a3e58a8cb9ce22495c77`

## 📌 Resumen

Artefacto de 1.4 KiB. Formato identificado como DOS executable (COM), start instruction 0xeb375bac 782eab0a. Presenta entropía elevada (7.88), compatible con contenido empaquetado, cifrado o de alta aleatoriedad. Las detecciones YARA incluyen `Suspicious_High_Entropy`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 indicador técnico adicional.


## 🗓️ Registro

- **Registrado:** `2026-08-09T19:36:13.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `52703a2045bd4cbdc993ed839ea62daf62ff737d46f9a3e58a8cb9ce22495c77`
- **MD5:** `d0670f5ee1ce2a8fe338ecd5a506ea48`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | DOS executable (COM), start instruction 0xeb375bac 782eab0a |
| Tamaño | 1.4 KiB |
| Entropía | 7.88 |
| Strings | 2 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=DOS executable (COM), start instruction 0xeb375bac 782eab0a; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 52703a2045bd4cbdc993ed839ea62daf62ff737d46f9a3e58a8cb9ce22495c77 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_High_Entropy |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
