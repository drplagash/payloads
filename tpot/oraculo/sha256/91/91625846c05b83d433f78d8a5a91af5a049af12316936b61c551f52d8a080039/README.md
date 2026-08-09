# 🧬 Payload Analysis

`91625846c05b83d433f78d8a5a91af5a049af12316936b61c551f52d8a080039`

## 📌 Resumen

Artefacto identificado como HTML document, ASCII text, with very long lines (1022) de 1.4 KiB. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `no_avatar-849f9c04a3a0d0cea2424ae97b27447dc64a7dbfae83c036c45b403392f0e8ba.png` en `hxxp://[internal-ip-redacted]/assets/no_avatar-849f9c04a3a0d0cea2424ae97b27447dc64a7dbfae83c036c45b403392f0e8ba.png`. Se extrajeron 2 referencias URL únicas. La evidencia es estática: este snapshot no demuestra por sí solo que la descarga llegara a ejecutarse.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:52:06.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `91625846c05b83d433f78d8a5a91af5a049af12316936b61c551f52d8a080039`
- **SHA1:** `ee6e21d46a38af9a33f2641df0db14c8afecebf7`
- **MD5:** `9bc4b5a8aaec75434eb3072bf8e5c271`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | HTML document, ASCII text, with very long lines (1022) |
| Tamaño | 1.4 KiB |
| Entropía | 5.33 |
| Strings | 6 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=HTML document, ASCII text, with very long lines (1022); iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://[internal-ip-redacted]/assets/no_avatar-849f9c04a3a0d0cea2424ae97b27447dc64a7dbfae83c036c45b403392f0e8ba.png | strings |
| url | hxxp://[internal-ip-redacted] | strings |
| ip | [internal-ip-redacted] | static_analysis |
| hash | 91625846c05b83d433f78d8a5a91af5a049af12316936b61c551f52d8a080039 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | html response |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
