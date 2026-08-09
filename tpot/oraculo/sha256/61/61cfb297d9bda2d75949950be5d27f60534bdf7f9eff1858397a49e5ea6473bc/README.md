# 🧬 Payload Analysis

`61cfb297d9bda2d75949950be5d27f60534bdf7f9eff1858397a49e5ea6473bc`

## 📌 Resumen

Artefacto de 548 B. La evidencia estática disponible identifica capacidad de descarga remota. Se extrajo como destino remoto `hxxp://172[.]20[.]254[.]`. Se extrajeron 4 referencias URL únicas. La evidencia es estática: este snapshot no demuestra por sí solo que la descarga llegara a ejecutarse.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:59:38.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `61cfb297d9bda2d75949950be5d27f60534bdf7f9eff1858397a49e5ea6473bc`
- **SHA1:** `65a2db76d6b342e2e6d18bc707ec6db98b35a3dc`
- **MD5:** `bbcb3232429144bf8450807bcf1643af`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.03 |
| Strings | 17 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=6

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://172[.]20[.]254[.] | strings |
| url | hxxps://casper[.]ghost[.]org/v1.0.0/images/ghost-logo.svg | strings |
| url | hxxps://casper[.]ghost[.]org/v1.0.0/images/blog-cover.jpg | strings |
| url | hxxp://[internal-ip-redacted]:80/ | strings |
| ip | [internal-ip-redacted] | static_analysis |
| hash | 61cfb297d9bda2d75949950be5d27f60534bdf7f9eff1858397a49e5ea6473bc | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
