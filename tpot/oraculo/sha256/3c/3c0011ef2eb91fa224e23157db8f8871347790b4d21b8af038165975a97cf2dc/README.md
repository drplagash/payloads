# 🧬 Payload Analysis

`3c0011ef2eb91fa224e23157db8f8871347790b4d21b8af038165975a97cf2dc`

## 📌 Resumen

Texto ASCII de 316 B. La evidencia disponible identifica capacidad de descarga remota. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `wget`
2. `curl` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/3c0011ef2eb91fa224e23157db8f8871347790b4d21b8af038165975a97cf2dc.md](../../../../../malware-like/oraculo/downloader/3c0011ef2eb91fa224e23157db8f8871347790b4d21b8af038165975a97cf2dc.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:38:58.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `3c0011ef2eb91fa224e23157db8f8871347790b4d21b8af038165975a97cf2dc`
- **MD5:** `8844bfb4e0deed79ba20bac44df28601`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 316 B |
| Entropía | 5.2 |
| Strings | 12 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=5

## 🖥️ Comandos observados / extraídos

```text
GET /rondo.%5Cbmv.sh%7C%7Cwget HTTP/1.1
User-Agent: curl/7.73.0
GET /rondo.%5Cbmv.sh%7C%7Ccurl HTTP/1.1
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 45.153.34.XXX | static_analysis |
| command | GET /rondo.%5Cbmv.sh%7C%7Cwget HTTP/1.1 | strings |
| command | User-Agent: curl/7.73.0 | strings |
| command | GET /rondo.%5Cbmv.sh%7C%7Ccurl HTTP/1.1 | strings |
| hash | 3c0011ef2eb91fa224e23157db8f8871347790b4d21b8af038165975a97cf2dc | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
