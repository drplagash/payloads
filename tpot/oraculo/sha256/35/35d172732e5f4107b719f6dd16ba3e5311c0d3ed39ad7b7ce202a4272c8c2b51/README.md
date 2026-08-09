# 🧬 Payload Analysis

`35d172732e5f4107b719f6dd16ba3e5311c0d3ed39ad7b7ce202a4272c8c2b51`

## 📌 Resumen

Artefacto de 3.3 KiB. Entropía registrada: 6.61. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Limpieza. Se identificó 1 comando observado o extraído. Se identificaron 2 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:36:46.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `35d172732e5f4107b719f6dd16ba3e5311c0d3ed39ad7b7ce202a4272c8c2b51`
- **MD5:** `8c2e356fa7b409c9d07c72db1119c3a8`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 3.3 KiB |
| Entropía | 6.61 |
| Strings | 27 |

## 🧠 Comportamiento observado

1. **Limpieza**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; iocs=2

## 🖥️ Comandos observados / extraídos

```text
shell:rm -rf /data/local/tmp/*
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| command | shell:rm -rf /data/local/tmp/* | strings |
| hash | 35d172732e5f4107b719f6dd16ba3e5311c0d3ed39ad7b7ce202a4272c8c2b51 | static_analysis |
| ip | 49.91.39.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
