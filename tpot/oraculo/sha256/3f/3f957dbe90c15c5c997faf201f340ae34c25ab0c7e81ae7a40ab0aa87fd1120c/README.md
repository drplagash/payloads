# 🧬 Payload Analysis

`3f957dbe90c15c5c997faf201f340ae34c25ab0c7e81ae7a40ab0aa87fd1120c`

## 📌 Resumen

Artefacto de 548 B. La evidencia disponible identifica capacidad de descarga remota. Infraestructura remota: `hxxps://wordpress[.]org/`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/3f957dbe90c15c5c997faf201f340ae34c25ab0c7e81ae7a40ab0aa87fd1120c.md](../../../../../malware-like/oraculo/downloader/3f957dbe90c15c5c997faf201f340ae34c25ab0c7e81ae7a40ab0aa87fd1120c.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:05:15.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `3f957dbe90c15c5c997faf201f340ae34c25ab0c7e81ae7a40ab0aa87fd1120c`
- **SHA1:** `1329ed15699dd05f077534f9f8f6d0ff5c507651`
- **MD5:** `d37033c59a554b31810c73b4bff9e8a9`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.18 |
| Strings | 10 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://wordpress[.]org/ | strings |
| hash | 3f957dbe90c15c5c997faf201f340ae34c25ab0c7e81ae7a40ab0aa87fd1120c | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
