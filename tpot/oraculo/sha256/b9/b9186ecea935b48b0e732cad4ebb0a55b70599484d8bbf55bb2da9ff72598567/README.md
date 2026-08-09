# 🧬 Payload Analysis

`b9186ecea935b48b0e732cad4ebb0a55b70599484d8bbf55bb2da9ff72598567`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Limpieza, Descarga remota. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:30:44+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `b9186ecea935b48b0e732cad4ebb0a55b70599484d8bbf55bb2da9ff72598567`
- **MD5:** `a6a39e23ae64e8c10f6257c50db3bc39`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 4.0 KiB |
| Entropía | 6.74 |
| Strings | 10 |

## 🧠 Comportamiento observado

1. **Limpieza**
2. **Descarga remota**

## 🔬 Evidencia de clasificación

- Download indicators (wget/curl + /tmp)

## 🖥️ Comandos observados / extraídos

```text
shell:rm -rf /data/local/tmp/*
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | b9186ecea935b48b0e732cad4ebb0a55b70599484d8bbf55bb2da9ff72598567 | static_analysis |
| command | shell:rm -rf /data/local/tmp/* | strings |
| ip | 218.205.95.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
