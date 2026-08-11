# 🧬 Payload Analysis

`6c4e11d767ce9012aee26d8b57f0a9875faa9ccaaa9acfb7ce36e04790c92c17`

## 📌 Resumen

Artefacto de 548 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `ghost-logo.svg` en `hxxps://casper[.]ghost[.]org/v1.0.0/images/ghost-logo.svg`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/6c4e11d767ce9012aee26d8b57f0a9875faa9ccaaa9acfb7ce36e04790c92c17.md](../../../../../malware-like/oraculo/downloader/6c4e11d767ce9012aee26d8b57f0a9875faa9ccaaa9acfb7ce36e04790c92c17.md)


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
