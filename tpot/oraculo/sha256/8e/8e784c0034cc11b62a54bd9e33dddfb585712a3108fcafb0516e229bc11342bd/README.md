# 🧬 Payload Analysis

`8e784c0034cc11b62a54bd9e33dddfb585712a3108fcafb0516e229bc11342bd`

## 📌 Resumen

Artefacto de 123 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 5.12. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificaron 2 indicadores técnicos. **C2 / infraestructura de control:**

- **Posible C2:** `190.179.140.XXX` — confianza Alto, evidencia hardcoded_in_payload


## 🗓️ Registro

- **Registrado:** `2026-08-09T20:04:38.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `8e784c0034cc11b62a54bd9e33dddfb585712a3108fcafb0516e229bc11342bd`
- **SHA1:** `9357340debc8a22600517b9fd791a6901501e66a`
- **MD5:** `a27545f52d261a804d2370e1810ce679`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 123 B |
| Entropía | 5.12 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.140.XXX | static_analysis |
| hash | 8e784c0034cc11b62a54bd9e33dddfb585712a3108fcafb0516e229bc11342bd | static_analysis |
| ip | 52.165.80.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
