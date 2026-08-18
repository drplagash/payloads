# 🧬 Payload Analysis

`1f78c30186229502965597b8e99adb4f9977e3465f5827a0af57c76d70877290`

## 📌 Resumen

Artefacto de 936 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 5.67. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificaron 3 indicadores técnicos. **C2 / infraestructura de control:**

- **Posible C2:** `190.179.168.XXX` — confianza Alto, evidencia hardcoded_in_payload
- **Posible C2:** `134.0.0.XXX` — confianza Medio, evidencia hardcoded_in_payload


## 🗓️ Registro

- **Registrado:** `2026-08-09T20:05:15.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `1f78c30186229502965597b8e99adb4f9977e3465f5827a0af57c76d70877290`
- **SHA1:** `350fea41756d6678aa64c7d6b43fbc548856ce27`
- **MD5:** `a3a796cdfd32ad7c1c4c3eed271b2ba9`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 936 B |
| Entropía | 5.67 |
| Strings | 17 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 134.0.0.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | 1f78c30186229502965597b8e99adb4f9977e3465f5827a0af57c76d70877290 | static_analysis |
| ip | 160.119.71.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
