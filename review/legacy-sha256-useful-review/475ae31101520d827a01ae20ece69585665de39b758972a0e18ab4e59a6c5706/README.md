# 🧬 Payload Analysis

`475ae31101520d827a01ae20ece69585665de39b758972a0e18ab4e59a6c5706`

## 📌 Resumen

Artefacto de 110 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 4.91. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:50:14.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `475ae31101520d827a01ae20ece69585665de39b758972a0e18ab4e59a6c5706`
- **SHA1:** `4f24305b47d035f5e8aaf052073697e43e9e50a9`
- **MD5:** `6062f7cb2fca508ab3b1431da11e41f5`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 110 B |
| Entropía | 4.91 |
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
| ip | 190.179.144.XXX | static_analysis |
| command | User-Agent: curl/7.74.0 | strings |
| hash | 475ae31101520d827a01ae20ece69585665de39b758972a0e18ab4e59a6c5706 | static_analysis |
| ip | 47.250.160.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
