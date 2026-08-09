# 🧬 Payload Analysis

`427937cfb027c8ef2669dc1c44edf0ffe333c92638404926c0dcd8d5831787d1`

## 📌 Resumen

Artefacto de 4.0 KiB. Formato identificado como DOS executable (COM), start instruction 0x8c1ecb82 a01e9d19. Presenta entropía elevada (7.94), compatible con contenido empaquetado, cifrado o de alta aleatoriedad. Las detecciones YARA incluyen `Suspicious_High_Entropy`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 indicador técnico adicional.


## 🗓️ Registro

- **Registrado:** `2026-08-09T20:01:36.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `427937cfb027c8ef2669dc1c44edf0ffe333c92638404926c0dcd8d5831787d1`
- **SHA1:** `c15c2dc8091cf7165f596c68038f49adac59927f`
- **MD5:** `5ca8a6e83226cbba5e410ac08179980d`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | DOS executable (COM), start instruction 0x8c1ecb82 a01e9d19 |
| Tamaño | 4.0 KiB |
| Entropía | 7.94 |
| Strings | 4 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=DOS executable (COM), start instruction 0x8c1ecb82 a01e9d19; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 427937cfb027c8ef2669dc1c44edf0ffe333c92638404926c0dcd8d5831787d1 | static_analysis |
| ip | 46.200.89.XXX | artifact_source |

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
