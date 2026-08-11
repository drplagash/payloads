# 🧬 Payload Analysis

`d7c21b45421bdc60369844a42a29e87b16f8f7b52455fe94410b7780477dc08f`

## 📌 Resumen

Artefacto de 548 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `Article` en `hxxps://schema[.]org/Article`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/d7c21b45421bdc60369844a42a29e87b16f8f7b52455fe94410b7780477dc08f.md](../../../../../malware-like/oraculo/downloader/d7c21b45421bdc60369844a42a29e87b16f8f7b52455fe94410b7780477dc08f.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:55:35.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d7c21b45421bdc60369844a42a29e87b16f8f7b52455fe94410b7780477dc08f`
- **SHA1:** `079361df0311c81d13123f2aae91b72123ffdd72`
- **MD5:** `b557b826dfd640b581bfeda200781c7c`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.29 |
| Strings | 12 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://schema[.]org/Article | strings |
| hash | d7c21b45421bdc60369844a42a29e87b16f8f7b52455fe94410b7780477dc08f | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
