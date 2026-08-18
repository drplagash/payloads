# 🧬 Payload Analysis

`0052821c75905e37088a8a8b96b7fa4502ca5a35aed8f0ea56a4521e50c094c4`

## 📌 Resumen

Artefacto de 79 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 4.80. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:01:51.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `0052821c75905e37088a8a8b96b7fa4502ca5a35aed8f0ea56a4521e50c094c4`
- **SHA1:** `7c0154fcaba560ba564319f4ff7f5bffe65a4b01`
- **MD5:** `d823eaf6f45e076185e512550feae85a`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 79 B |
| Entropía | 4.8 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.78.0
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.160.XXX | static_analysis |
| command | User-Agent: curl/7.78.0 | strings |
| hash | 0052821c75905e37088a8a8b96b7fa4502ca5a35aed8f0ea56a4521e50c094c4 | static_analysis |
| ip | 8.221.139.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
