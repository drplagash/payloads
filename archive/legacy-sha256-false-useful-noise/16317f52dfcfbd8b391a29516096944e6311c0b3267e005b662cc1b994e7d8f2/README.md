# 🧬 Payload Analysis

`16317f52dfcfbd8b391a29516096944e6311c0b3267e005b662cc1b994e7d8f2`

## 📌 Resumen

Artefacto de 548 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `team.jpg` en `hxxps://casper[.]ghost[.]org/v1.0.0/images/team.jpg`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/16317f52dfcfbd8b391a29516096944e6311c0b3267e005b662cc1b994e7d8f2.md](../../../../../malware-like/oraculo/downloader/16317f52dfcfbd8b391a29516096944e6311c0b3267e005b662cc1b994e7d8f2.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:41:47.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `16317f52dfcfbd8b391a29516096944e6311c0b3267e005b662cc1b994e7d8f2`
- **MD5:** `d74e3dae3521696a75cc9eea4e9c10d2`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.21 |
| Strings | 9 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://casper[.]ghost[.]org/v1.0.0/images/team.jpg) | strings |
| hash | 16317f52dfcfbd8b391a29516096944e6311c0b3267e005b662cc1b994e7d8f2 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
