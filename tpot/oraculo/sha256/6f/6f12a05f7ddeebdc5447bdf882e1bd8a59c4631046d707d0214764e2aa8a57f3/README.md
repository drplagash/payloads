# 🧬 Payload Analysis

`6f12a05f7ddeebdc5447bdf882e1bd8a59c4631046d707d0214764e2aa8a57f3`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:47:28+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `6f12a05f7ddeebdc5447bdf882e1bd8a59c4631046d707d0214764e2aa8a57f3`
- **SHA1:** `a19b00dbf5709bbb1f4f4aedf3e4178e6c35f54e`
- **MD5:** `c92239c1a7f9a5c233625e31446a5684`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 799 B |
| Entropía | 5.46 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 161.30.150.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | 6f12a05f7ddeebdc5447bdf882e1bd8a59c4631046d707d0214764e2aa8a57f3 | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
