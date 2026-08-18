# 🧬 Payload Analysis

`c531e396e584a2db4e35034212e57a6aa0056995004f9bda55eee6c6afc43640`

## 📌 Resumen

Artefacto de 1003 B. Formato identificado como ASCII text, with very long lines (403), with CRLF line terminators. Entropía registrada: 5.52. Las detecciones YARA incluyen `Big_Numbers1`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificaron 3 indicadores técnicos.


## 🗓️ Registro

- **Registrado:** `2026-08-09T18:42:51.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `c531e396e584a2db4e35034212e57a6aa0056995004f9bda55eee6c6afc43640`
- **MD5:** `66681ecf1ed1527a1acbd220b5c0b955`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (403), with CRLF line terminators |
| Tamaño | 1003 B |
| Entropía | 5.52 |
| Strings | 16 |

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 45.153.34.XXX | static_analysis |
| ip | 190.179.177.XXX | static_analysis |
| hash | c531e396e584a2db4e35034212e57a6aa0056995004f9bda55eee6c6afc43640 | static_analysis |
| ip | 141.98.10.XXX | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Big_Numbers1 |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
