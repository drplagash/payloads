# 🧬 Payload Analysis

`78f04fde909046d82e27118ad9b73fd166aa1f21fd87d9a7f1ce083cd5ae548d`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota, Ejecución. Se asociaron 4 comandos observados o extraídos.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:45:45+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `78f04fde909046d82e27118ad9b73fd166aa1f21fd87d9a7f1ce083cd5ae548d`
- **MD5:** `39ecae64b86351815a5d6eeba350a78f`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 443 B |
| Entropía | 5.2 |
| Strings | 18 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=6

## 🖥️ Comandos observados / extraídos

```text
GET /bins/busycurl.sh HTTP/1.1
GET /bins/busywget.sh HTTP/1.1
GET /bins/wget.sh HTTP/1.1
User-Agent: curl/7.73.0
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 64.89.163.XXX | static_analysis |
| hash | 78f04fde909046d82e27118ad9b73fd166aa1f21fd87d9a7f1ce083cd5ae548d | static_analysis |
| command | GET /bins/busycurl.sh HTTP/1.1 | strings |
| command | GET /bins/busywget.sh HTTP/1.1 | strings |
| command | GET /bins/wget.sh HTTP/1.1 | strings |
| command | User-Agent: curl/7.73.0 | strings |
| ip | [internal-ip-redacted] | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
