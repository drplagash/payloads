# 🧬 Payload Analysis

`b54520be3d454f6926b094aac799ac345c08ee7c09ec7f3d03a90c6ea7e3bc38`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:01:06+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `b54520be3d454f6926b094aac799ac345c08ee7c09ec7f3d03a90c6ea7e3bc38`
- **SHA1:** `8bd9d62f9d06a0e24accd4006b54b1d4042dff60`
- **MD5:** `2fb6b9d97e58f42309e0bf783cf13fb7`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | Adobe Photoshop Color swatch, version 0, 1 colors; 1st RGB space (0), w 0x1, x 0, y 0x4, z 0 |
| Tamaño | 24 B |
| Entropía | 1.02 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=Adobe Photoshop Color swatch, version 0, 1 colors; 1st RGB space (0), w 0x1, x 0, y 0x4, z 0; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | b54520be3d454f6926b094aac799ac345c08ee7c09ec7f3d03a90c6ea7e3bc38 | static_analysis |
| ip | 66.132.172.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
