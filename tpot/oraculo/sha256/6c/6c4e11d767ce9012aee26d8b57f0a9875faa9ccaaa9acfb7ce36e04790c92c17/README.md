# 🧬 Payload Analysis

`6c4e11d767ce9012aee26d8b57f0a9875faa9ccaaa9acfb7ce36e04790c92c17`

## 📌 Resumen

Artefacto de 548 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `ghost-logo.svg` en `hxxps://casper[.]ghost[.]org/v1.0.0/images/ghost-logo.svg`. Se extrajeron 3 referencias URL únicas. La evidencia es estática: este snapshot no demuestra por sí solo que la descarga llegara a ejecutarse.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:41:12.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `6c4e11d767ce9012aee26d8b57f0a9875faa9ccaaa9acfb7ce36e04790c92c17`
- **MD5:** `bebf3b4cd23242c876022c48b7904a1d`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.22 |
| Strings | 15 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=5

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://casper[.]ghost[.]org/v1.0.0/images/ghost-logo.svg | strings |
| url | hxxps://schema[.]org | strings |
| url | hxxp://[internal-ip-redacted]:80/ | strings |
| ip | [internal-ip-redacted] | static_analysis |
| hash | 6c4e11d767ce9012aee26d8b57f0a9875faa9ccaaa9acfb7ce36e04790c92c17 | static_analysis |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
