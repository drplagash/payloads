# 🧬 Payload Analysis

`e17f77c6d327440c95a728e9cc3cbc0026f57d4c94a1e2ef07dc9d366d83f7a3`

## 📌 Resumen

Texto ASCII de 916 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `icy.sh` en `hxxp://109.104.153.XXX/icy.sh`. **C2 / infraestructura de control:**

- **Posible C2:** `109.104.153.XXX` — confianza Bajo, evidencia hardcoded_in_payload Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/e17f77c6d327440c95a728e9cc3cbc0026f57d4c94a1e2ef07dc9d366d83f7a3.md](../../../../../malware-like/oraculo/downloader/e17f77c6d327440c95a728e9cc3cbc0026f57d4c94a1e2ef07dc9d366d83f7a3.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:20:23.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `e17f77c6d327440c95a728e9cc3cbc0026f57d4c94a1e2ef07dc9d366d83f7a3`
- **SHA1:** `c7f950a1f7de0d167135c60d957959b8e06ff79b`
- **MD5:** `54cea268718a06828cb014abd343d5b6`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (775), with CRLF line terminators |
| Tamaño | 916 B |
| Entropía | 5.35 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with very long lines (775), with CRLF line terminators; iocs=5

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://109.104.153.XXX/icy.sh | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/envelope/ | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/encoding/ | strings |
| ip | 109.104.153.XXX | static_analysis |
| hash | e17f77c6d327440c95a728e9cc3cbc0026f57d4c94a1e2ef07dc9d366d83f7a3 | static_analysis |
| ip | 103.96.140.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
