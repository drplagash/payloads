# 🧬 Payload Analysis

`f779b1e735708849eaa76d9e01afdc339b3719eacb89538eca0cdf9af618ad79`

## 📌 Resumen

Texto ASCII de 83 B. La evidencia disponible identifica capacidad de descarga remota. Se dispone de 1 comando observado o extraído. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/f779b1e735708849eaa76d9e01afdc339b3719eacb89538eca0cdf9af618ad79.md](../../../../../malware-like/oraculo/downloader/f779b1e735708849eaa76d9e01afdc339b3719eacb89538eca0cdf9af618ad79.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:44:08.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `f779b1e735708849eaa76d9e01afdc339b3719eacb89538eca0cdf9af618ad79`
- **MD5:** `f9e5c2dcbd33ce4c2b5b2351596d7c8b`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 83 B |
| Entropía | 4.82 |
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
| hash | f779b1e735708849eaa76d9e01afdc339b3719eacb89538eca0cdf9af618ad79 | static_analysis |
| ip | 8.216.3.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
