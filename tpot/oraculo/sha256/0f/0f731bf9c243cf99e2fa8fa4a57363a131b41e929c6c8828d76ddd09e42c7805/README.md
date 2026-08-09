# 🧬 Payload Analysis

`0f731bf9c243cf99e2fa8fa4a57363a131b41e929c6c8828d76ddd09e42c7805`

## 📌 Resumen

Artefacto de 4.0 KiB. Entropía registrada: 7.03. Las detecciones YARA incluyen `Suspicious_High_Entropy`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 indicador técnico adicional.


## 🗓️ Registro

- **Registrado:** `2026-08-09T21:05:38.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `0f731bf9c243cf99e2fa8fa4a57363a131b41e929c6c8828d76ddd09e42c7805`
- **SHA1:** `96aa534afe90c10017dd4da408f381747863ef66`
- **MD5:** `fb2656db04c5510bd97677028cd367c9`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 4.0 KiB |
| Entropía | 7.03 |
| Strings | 96 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=7.0; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 0f731bf9c243cf99e2fa8fa4a57363a131b41e929c6c8828d76ddd09e42c7805 | static_analysis |
| ip | 103.164.110.XXX | artifact_source |

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
