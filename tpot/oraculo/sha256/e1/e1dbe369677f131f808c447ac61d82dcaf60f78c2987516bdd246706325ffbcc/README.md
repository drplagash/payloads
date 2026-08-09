# 🧬 Payload Analysis

`e1dbe369677f131f808c447ac61d82dcaf60f78c2987516bdd246706325ffbcc`

## 📌 Resumen

Artefacto identificado como ASCII text, with CRLF line terminators de 83 B. La evidencia estática disponible identifica capacidad de descarga remota. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:44:08.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `e1dbe369677f131f808c447ac61d82dcaf60f78c2987516bdd246706325ffbcc`
- **MD5:** `5f7e97c2b3ebb16b034453f78eee296c`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 83 B |
| Entropía | 4.85 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Download indicators (wget/curl + /tmp)

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.64.1
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.167.XXX | static_analysis |
| command | User-Agent: curl/7.64.1 | strings |
| hash | e1dbe369677f131f808c447ac61d82dcaf60f78c2987516bdd246706325ffbcc | static_analysis |
| ip | 47.245.143.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
