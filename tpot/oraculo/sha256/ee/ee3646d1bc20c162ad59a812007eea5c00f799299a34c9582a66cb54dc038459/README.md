# 🧬 Payload Analysis

`ee3646d1bc20c162ad59a812007eea5c00f799299a34c9582a66cb54dc038459`

## 📌 Resumen

Artefacto de 111 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 4.99. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:44:37.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `ee3646d1bc20c162ad59a812007eea5c00f799299a34c9582a66cb54dc038459`
- **SHA1:** `1dae711cf3a8015833368b0f46f896b9f13af047`
- **MD5:** `9f45f4fa602fdddadef5a8dee5100fd2`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 111 B |
| Entropía | 4.99 |
| Strings | 5 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.74.0
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.166.XXX | static_analysis |
| command | User-Agent: curl/7.74.0 | strings |
| hash | ee3646d1bc20c162ad59a812007eea5c00f799299a34c9582a66cb54dc038459 | static_analysis |
| ip | 47.250.91.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
