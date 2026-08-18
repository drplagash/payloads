# 🧬 Payload Analysis

`46fbfab92caf353b516d921767ec6500a2f444a6d9413879bb6b2c38c3c7138e`

## 📌 Resumen

Script JavaScript de 1.2 KiB. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `gg10` en `hxxp://94.154.43.XXX/gg10`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/46fbfab92caf353b516d921767ec6500a2f444a6d9413879bb6b2c38c3c7138e.md](../../../../../malware-like/oraculo/downloader/46fbfab92caf353b516d921767ec6500a2f444a6d9413879bb6b2c38c3c7138e.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:57:22.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `46fbfab92caf353b516d921767ec6500a2f444a6d9413879bb6b2c38c3c7138e`
- **SHA1:** `800a1cb464b7b6d925fc4168e1838acf35ea1a45`
- **MD5:** `e8e4939097edac632d77dd93884eaa3e`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | JavaScript source, ASCII text, with very long lines (554), with CRLF line terminators |
| Tamaño | 1.2 KiB |
| Entropía | 5.4 |
| Strings | 14 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=JavaScript source, ASCII text, with very long lines (554), with CRLF line terminators; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://94.154.43.XXX/gg10) | strings |
| url | hxxp://94.154.43.XXX/gg10 | strings |
| ip | 94.154.43.XXX | static_analysis |
| hash | 46fbfab92caf353b516d921767ec6500a2f444a6d9413879bb6b2c38c3c7138e | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
