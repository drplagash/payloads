# 🧬 Payload Analysis

`fbfb8d9cc34663e945bfa1e87a564c6ec2a85d13b77504ffb60da9797c7b7f3b`

## 📌 Resumen

Texto ASCII de 83 B. La evidencia disponible identifica capacidad de descarga remota. Se dispone de 1 comando observado o extraído. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/fbfb8d9cc34663e945bfa1e87a564c6ec2a85d13b77504ffb60da9797c7b7f3b.md](../../../../../malware-like/oraculo/downloader/fbfb8d9cc34663e945bfa1e87a564c6ec2a85d13b77504ffb60da9797c7b7f3b.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:42:13.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `fbfb8d9cc34663e945bfa1e87a564c6ec2a85d13b77504ffb60da9797c7b7f3b`
- **MD5:** `2be0dd8db014c79f1bca34c73910c3e2`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 83 B |
| Entropía | 4.75 |
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
| ip | 190.179.177.XXX | static_analysis |
| command | User-Agent: curl/7.64.1 | strings |
| hash | fbfb8d9cc34663e945bfa1e87a564c6ec2a85d13b77504ffb60da9797c7b7f3b | static_analysis |
| ip | 8.209.236.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
