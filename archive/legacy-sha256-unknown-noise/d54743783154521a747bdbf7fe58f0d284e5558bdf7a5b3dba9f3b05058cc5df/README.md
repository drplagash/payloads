# 🧬 Payload Analysis

`d54743783154521a747bdbf7fe58f0d284e5558bdf7a5b3dba9f3b05058cc5df`

## 📌 Resumen

Artefacto de 420 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 5.33. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificaron 3 indicadores técnicos. **C2 / infraestructura de control:**

- **Posible C2:** `190.179.168.XXX` — confianza Alto, evidencia hardcoded_in_payload
- **Posible C2:** `1.1.1.XXX` — confianza Bajo, evidencia hardcoded_in_payload
- **Posible C2:** `103.132.236.XXX` — confianza Descartado, evidencia hardcoded_in_payload


## 🗓️ Registro

- **Registrado:** `2026-08-09T20:04:38.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d54743783154521a747bdbf7fe58f0d284e5558bdf7a5b3dba9f3b05058cc5df`
- **SHA1:** `de492c4ba18544057c10e6c0c6a8683ba45e714f`
- **MD5:** `bc1b355035bb45b69705dddeab2b63eb`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 420 B |
| Entropía | 5.33 |
| Strings | 11 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 103.132.236.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| ip | 1.1.1.XXX | static_analysis |
| hash | d54743783154521a747bdbf7fe58f0d284e5558bdf7a5b3dba9f3b05058cc5df | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
