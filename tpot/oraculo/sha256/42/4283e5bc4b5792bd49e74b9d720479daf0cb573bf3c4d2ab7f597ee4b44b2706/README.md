# 🧬 Payload Analysis

`4283e5bc4b5792bd49e74b9d720479daf0cb573bf3c4d2ab7f597ee4b44b2706`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota, Ejecución. Se asociaron 2 comandos observados o extraídos.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:31:17+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `4283e5bc4b5792bd49e74b9d720479daf0cb573bf3c4d2ab7f597ee4b44b2706`
- **MD5:** `138b50284e9532f8ce7f7f6b4ac020b2`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 840 B |
| Entropía | 5.09 |
| Strings | 36 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
GET /wget.sh HTTP/1.1
User-Agent: curl/7.73.0
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 45.130.151.XXX | static_analysis |
| hash | 4283e5bc4b5792bd49e74b9d720479daf0cb573bf3c4d2ab7f597ee4b44b2706 | static_analysis |
| command | GET /wget.sh HTTP/1.1 | strings |
| command | User-Agent: curl/7.73.0 | strings |
| ip | [internal-ip-redacted] | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
