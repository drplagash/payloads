# 🧬 Payload Analysis

`8a194961804759638e7071b5e42f1b44cf29247e3b8b4ae27c5169a9c30ff418`

## 📌 Resumen

Artefacto de 84 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 4.84. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:51:31.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `8a194961804759638e7071b5e42f1b44cf29247e3b8b4ae27c5169a9c30ff418`
- **SHA1:** `1deb68186007fc9c7d9b0651d36c36ca72dde24c`
- **MD5:** `53f2d9ef9be90766668db15669cc5e49`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 84 B |
| Entropía | 4.84 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.64.1
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.139.XXX | static_analysis |
| command | User-Agent: curl/7.64.1 | strings |
| hash | 8a194961804759638e7071b5e42f1b44cf29247e3b8b4ae27c5169a9c30ff418 | static_analysis |
| ip | 47.250.124.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
