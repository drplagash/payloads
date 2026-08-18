# 🧬 Payload Analysis

`ad7776b1139c0231fc20171aa0ff53159341ea4a142fab34bbfc562118e6b356`

## 📌 Resumen

Artefacto de 548 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `writing.jpg` en `hxxps://casper[.]ghost[.]org/v1.0.0/images/writing.jpg`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/ad7776b1139c0231fc20171aa0ff53159341ea4a142fab34bbfc562118e6b356.md](../../../../../malware-like/oraculo/downloader/ad7776b1139c0231fc20171aa0ff53159341ea4a142fab34bbfc562118e6b356.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:41:12.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `ad7776b1139c0231fc20171aa0ff53159341ea4a142fab34bbfc562118e6b356`
- **MD5:** `fd96d64f5ae25e30564e768d876412db`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.17 |
| Strings | 11 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://casper[.]ghost[.]org/v1.0.0/images/writing.jpg) | strings |
| hash | ad7776b1139c0231fc20171aa0ff53159341ea4a142fab34bbfc562118e6b356 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
