# 🧬 Payload Analysis

`d93ca511f34a316a8832942e8e27a5e0ef3887a576d73eb915a2966c1bd5a1e3`

## 📌 Resumen

Texto ASCII de 83 B. La evidencia disponible identifica capacidad de descarga remota. Se dispone de 1 comando observado o extraído. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/d93ca511f34a316a8832942e8e27a5e0ef3887a576d73eb915a2966c1bd5a1e3.md](../../../../../malware-like/oraculo/downloader/d93ca511f34a316a8832942e8e27a5e0ef3887a576d73eb915a2966c1bd5a1e3.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:42:13.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d93ca511f34a316a8832942e8e27a5e0ef3887a576d73eb915a2966c1bd5a1e3`
- **MD5:** `f1c333727564e5f73917a6bb4604a92f`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 83 B |
| Entropía | 4.76 |
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
| hash | d93ca511f34a316a8832942e8e27a5e0ef3887a576d73eb915a2966c1bd5a1e3 | static_analysis |
| ip | 47.251.161.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
