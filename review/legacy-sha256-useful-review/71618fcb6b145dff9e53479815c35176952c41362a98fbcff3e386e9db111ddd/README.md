# 🧬 Payload Analysis

`71618fcb6b145dff9e53479815c35176952c41362a98fbcff3e386e9db111ddd`

## 📌 Resumen

Texto ASCII de 83 B. La evidencia disponible identifica capacidad de descarga remota. Se dispone de 1 comando observado o extraído. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/71618fcb6b145dff9e53479815c35176952c41362a98fbcff3e386e9db111ddd.md](../../../../../malware-like/oraculo/downloader/71618fcb6b145dff9e53479815c35176952c41362a98fbcff3e386e9db111ddd.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:41:16.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `71618fcb6b145dff9e53479815c35176952c41362a98fbcff3e386e9db111ddd`
- **MD5:** `c78c8008f55d3739cb9cd96b8b4ab932`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 83 B |
| Entropía | 4.8 |
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
| hash | 71618fcb6b145dff9e53479815c35176952c41362a98fbcff3e386e9db111ddd | static_analysis |
| ip | 47.251.107.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
