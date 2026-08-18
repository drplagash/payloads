# 🧬 Payload Analysis

`72d28d75baf959d3190f70b728b17626edded5a2459fb2a2f1732e310e06943d`

## 📌 Resumen

Artefacto de 548 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `fbml` en `hxxp://www[.]facebook[.]com/2008/fbml`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/72d28d75baf959d3190f70b728b17626edded5a2459fb2a2f1732e310e06943d.md](../../../../../malware-like/oraculo/downloader/72d28d75baf959d3190f70b728b17626edded5a2459fb2a2f1732e310e06943d.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:46:43.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `72d28d75baf959d3190f70b728b17626edded5a2459fb2a2f1732e310e06943d`
- **SHA1:** `a3c48859bea4595c36585abaf3e8ac13361d472a`
- **MD5:** `622f5e8fd8af40a5e3f48f34fcdcc0b6`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.6 |
| Strings | 9 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=5

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://www[.]facebook[.]com/2008/fbml | strings |
| url | hxxp://www[.]w3[.]org/TR/xhtml1/DTD/xhtml1-transitional.dtd | strings |
| url | hxxp://www[.]w3[.]org/1999/xhtml | strings |
| url | hxxp://opengraphprotocol[.]org/schema/ | strings |
| hash | 72d28d75baf959d3190f70b728b17626edded5a2459fb2a2f1732e310e06943d | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
