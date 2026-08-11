# 🧬 Payload Analysis

`22cd3569a4d17c0967db88c18b5d1d903267a80a6ee3dc9ce376d16de614a112`

## 📌 Resumen

Texto ASCII de 803 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `Mozi.m` en `hxxp://103.213.112.XXX:58691/Mozi.m`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/22cd3569a4d17c0967db88c18b5d1d903267a80a6ee3dc9ce376d16de614a112.md](../../../../../malware-like/oraculo/downloader/22cd3569a4d17c0967db88c18b5d1d903267a80a6ee3dc9ce376d16de614a112.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:05:52.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `22cd3569a4d17c0967db88c18b5d1d903267a80a6ee3dc9ce376d16de614a112`
- **SHA1:** `67188f5904e736a1c7553faf248e40dfd3b695ba`
- **MD5:** `99210e924f3e81f19ddf648717e52ddb`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (624), with CRLF line terminators |
| Tamaño | 803 B |
| Entropía | 5.47 |
| Strings | 7 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with very long lines (624), with CRLF line terminators; iocs=5

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://103.213.112.XXX:58691/Mozi.m | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/envelope/ | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/encoding/ | strings |
| ip | 103.213.112.XXX | static_analysis |
| hash | 22cd3569a4d17c0967db88c18b5d1d903267a80a6ee3dc9ce376d16de614a112 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
