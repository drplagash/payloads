# 🧬 Payload Analysis

`6fdeb6f3bb6ceab042917b74b048ca00df3b8064e33d779cbf4078fad52a40ce`

## 📌 Resumen

Texto ASCII de 604 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `chmod` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/6fdeb6f3bb6ceab042917b74b048ca00df3b8064e33d779cbf4078fad52a40ce.md](../../../../../malware-like/oraculo/downloader/6fdeb6f3bb6ceab042917b74b048ca00df3b8064e33d779cbf4078fad52a40ce.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:51:31.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `6fdeb6f3bb6ceab042917b74b048ca00df3b8064e33d779cbf4078fad52a40ce`
- **SHA1:** `6abc474879f8530bc54ca02f69e22bffbbd5fee7`
- **MD5:** `205837646fd874c480be071a6e5caede`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (483), with CRLF line terminators |
| Tamaño | 604 B |
| Entropía | 5.35 |
| Strings | 6 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with very long lines (483), with CRLF line terminators; iocs=7

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh | strings |
| url | hxxp://www[.]huawei[.]com/vehicle/nu | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/envelope/ | strings |
| url | hxxp://91.92.40.XXX/wget.sh;chmod | strings |
| ip | 91.92.40.XXX | static_analysis |
| ip | 190.179.169.XXX | static_analysis |
| hash | 6fdeb6f3bb6ceab042917b74b048ca00df3b8064e33d779cbf4078fad52a40ce | static_analysis |
| ip | 45.153.34.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
