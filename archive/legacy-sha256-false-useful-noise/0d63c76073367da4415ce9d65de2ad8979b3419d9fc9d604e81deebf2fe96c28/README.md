# 🧬 Payload Analysis

`0d63c76073367da4415ce9d65de2ad8979b3419d9fc9d604e81deebf2fe96c28`

## 📌 Resumen

Artefacto de 548 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `css` en `hxxps://fonts[.]googleapis[.]com/css`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/0d63c76073367da4415ce9d65de2ad8979b3419d9fc9d604e81deebf2fe96c28.md](../../../../../malware-like/oraculo/downloader/0d63c76073367da4415ce9d65de2ad8979b3419d9fc9d604e81deebf2fe96c28.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:05:15.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `0d63c76073367da4415ce9d65de2ad8979b3419d9fc9d604e81deebf2fe96c28`
- **SHA1:** `35ee2f579381ebe56dcfc4f440b5909323d1b982`
- **MD5:** `4cc653ee113000e1a7e89a7a66fcd473`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.42 |
| Strings | 3 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://fonts[.]googleapis[.]com/css?family=Libre+Franklin%3A300%2C300i%2C400 | strings |
| hash | 0d63c76073367da4415ce9d65de2ad8979b3419d9fc9d604e81deebf2fe96c28 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
