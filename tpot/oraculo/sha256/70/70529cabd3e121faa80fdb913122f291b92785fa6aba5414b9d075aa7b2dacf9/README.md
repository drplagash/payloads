# 🧬 Payload Analysis

`70529cabd3e121faa80fdb913122f291b92785fa6aba5414b9d075aa7b2dacf9`

## 📌 Resumen

Artefacto de 4.0 KiB. Formato identificado como DOS executable (COM), start instruction 0xeb64b0c1 350f1d1f. Presenta entropía elevada (7.94), compatible con contenido empaquetado, cifrado o de alta aleatoriedad. Las detecciones YARA incluyen `Suspicious_High_Entropy`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Binary execution. Se identificó 1 indicador técnico adicional.


## 🗓️ Registro

- **Registrado:** `2026-08-09T20:04:03.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `70529cabd3e121faa80fdb913122f291b92785fa6aba5414b9d075aa7b2dacf9`
- **SHA1:** `84bae6a9e485998ffc1940289ca8ec169e05d31f`
- **MD5:** `59faa34b5ccfc4884a0a3db3451557c5`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | DOS executable (COM), start instruction 0xeb64b0c1 350f1d1f |
| Tamaño | 4.0 KiB |
| Entropía | 7.94 |
| Strings | 8 |

## 🧠 Comportamiento observado

1. **High entropy obfuscation**
2. **Binary execution**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=DOS executable (COM), start instruction 0xeb64b0c1 350f1d1f; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 70529cabd3e121faa80fdb913122f291b92785fa6aba5414b9d075aa7b2dacf9 | static_analysis |
| ip | 37.57.94.XXX | artifact_source |

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
