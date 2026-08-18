# 🧬 Payload Analysis

`ee058b740af8e783e844e18c730a39373ed3798709d81798dc3473921b9df2d9`

## 📌 Resumen

Artefacto de 86 B. Formato identificado como ASCII text. Entropía registrada: 4.92. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:41:46.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `ee058b740af8e783e844e18c730a39373ed3798709d81798dc3473921b9df2d9`
- **MD5:** `41d7b2b087f4ec55286a1c3869034ea3`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text |
| Tamaño | 86 B |
| Entropía | 4.92 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text; iocs=3

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.64.1
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.175.XXX | static_analysis |
| command | User-Agent: curl/7.64.1 | strings |
| hash | ee058b740af8e783e844e18c730a39373ed3798709d81798dc3473921b9df2d9 | static_analysis |
| ip | 47.251.74.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
