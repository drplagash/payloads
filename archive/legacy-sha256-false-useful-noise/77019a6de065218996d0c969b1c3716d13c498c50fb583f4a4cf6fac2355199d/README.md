# 🧬 Payload Analysis

`77019a6de065218996d0c969b1c3716d13c498c50fb583f4a4cf6fac2355199d`

## 📌 Resumen

Artefacto de 548 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `welcome.jpg` en `hxxps://casper[.]ghost[.]org/v1.0.0/images/welcome.jpg`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/77019a6de065218996d0c969b1c3716d13c498c50fb583f4a4cf6fac2355199d.md](../../../../../malware-like/oraculo/downloader/77019a6de065218996d0c969b1c3716d13c498c50fb583f4a4cf6fac2355199d.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:41:47.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `77019a6de065218996d0c969b1c3716d13c498c50fb583f4a4cf6fac2355199d`
- **MD5:** `7223597c2b01f233f68feefea316dc3b`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.16 |
| Strings | 11 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://casper[.]ghost[.]org/v1.0.0/images/welcome.jpg) | strings |
| hash | 77019a6de065218996d0c969b1c3716d13c498c50fb583f4a4cf6fac2355199d | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
