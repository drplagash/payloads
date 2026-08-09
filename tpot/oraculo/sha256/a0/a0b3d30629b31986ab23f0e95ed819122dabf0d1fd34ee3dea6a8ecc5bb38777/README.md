# 🧬 Payload Analysis

`a0b3d30629b31986ab23f0e95ed819122dabf0d1fd34ee3dea6a8ecc5bb38777`

## 📌 Resumen

Artefacto de 699 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 5.09. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota, Ejecución. Se identificaron 2 comandos observados o extraídos. Se identificaron 4 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:31:17.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `a0b3d30629b31986ab23f0e95ed819122dabf0d1fd34ee3dea6a8ecc5bb38777`
- **MD5:** `27dcc6b6fe444b860c3d6d03fe8c62dc`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 699 B |
| Entropía | 5.09 |
| Strings | 30 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.73.0
GET /wget.sh HTTP/1.1
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 45.130.151.XXX | static_analysis |
| command | User-Agent: curl/7.73.0 | strings |
| command | GET /wget.sh HTTP/1.1 | strings |
| hash | a0b3d30629b31986ab23f0e95ed819122dabf0d1fd34ee3dea6a8ecc5bb38777 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
