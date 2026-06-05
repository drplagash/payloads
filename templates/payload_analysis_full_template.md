# Payload Analysis Full Template

> Uso: copiá este archivo dentro de cada análisis de payload y completalo.
>
> Alcance: análisis defensivo, CTFs, labs propios, honeypots/T-Pot y evidencia sanitizada.
>
> No publicar malware vivo, payloads weaponizados, credenciales, tokens, dumps, datos personales ni infraestructura interna sensible.

---

## 1. Información general

```text
Título:
Fecha:
Analista:
Fuente:
Repositorio:
Estado:
Confianza:
```

Ejemplo:

```text
Título: Payload HTTP sospechoso observado en T-Pot
Fecha: 2026-06-05
Analista: DrPlaga.sh
Fuente: T-Pot / DockerLab / CTF / Web log
Estado: En análisis
Confianza: media
```

---

## 2. Alcance

```text
Entorno:
Origen del evento:
Sensor:
Sistema afectado:
IP origen:
IP destino:
Puerto destino:
Protocolo:
```

> Recomendación: si el análisis va a ser público, sanitizar IP destino, hostnames internos, tokens, cookies, rutas internas y cualquier dato sensible.

Ejemplo público:

```text
Entorno: Honeypot/lab
Origen del evento: HTTP request
Sensor: [REDACTED]
Sistema afectado: web honeypot
IP origen: 203.0.113.10
IP destino: [REDACTED]
Puerto destino: 80
Protocolo: HTTP
```

---

## 3. Resumen ejecutivo

```text
El payload intenta:
Técnica probable:
Riesgo:
Impacto esperado:
Estado del análisis:
Acción recomendada:
```

Ejemplo:

```text
El payload intenta ejecutar comandos remotos mediante un parámetro web.
Técnica probable: command injection.
Riesgo: medio en laboratorio; alto si el servicio real fuera vulnerable.
Impacto esperado: ejecución de comandos.
Estado del análisis: payload decodificado parcialmente.
Acción recomendada: bloquear patrón, monitorear logs y validar controles de input.
```

---

## 4. Evento original

### 4.1 Metadata

```text
Timestamp:
Sensor:
Log source:
Event ID:
Service:
Method:
URI:
User-Agent:
Content-Type:
Status code:
Response size:
```

### 4.2 Payload bruto sanitizado

> No pegar secretos reales. Si contiene algo riesgoso, reemplazar con `[REDACTED]`.

```text
[PEGAR PAYLOAD SANITIZADO]
```

### 4.3 Evidencia asociada

```text
Archivo de log:
Captura:
Hash del archivo:
Ruta del reporte:
```

---

## 5. Normalización

### 5.1 Limpieza inicial

```text
Cambios realizados:
- Se removieron tokens/cookies.
- Se reemplazó IP destino por [REDACTED].
- Se preservó estructura del payload.
```

### 5.2 Payload normalizado

```text
[PAYLOAD NORMALIZADO]
```

---

## 6. Decodificación

### 6.1 Tipo de encoding detectado

```text
URL encoding:
Base64:
Hex:
Unicode escape:
Gzip/deflate:
Double encoding:
Ofuscación simple:
Otro:
```

### 6.2 Comandos útiles

URL decode:

```bash
python3 - <<'PY'
from urllib.parse import unquote
payload = '''PEGAR_PAYLOAD'''
print(unquote(payload))
PY
```

Base64:

```bash
echo 'BASE64_AQUI' | base64 -d
```

Hex:

```bash
echo 'HEX_AQUI' | xxd -r -p
```

Strings:

```bash
strings archivo.bin
```

Hash:

```bash
sha256sum archivo
```

### 6.3 Pasos realizados

```text
Paso 1:
Entrada:
Salida:
Observación:

Paso 2:
Entrada:
Salida:
Observación:
```

### 6.4 Payload decodificado

```text
[PAYLOAD DECODIFICADO O PARCIALMENTE DECODIFICADO]
```

---

## 7. Análisis técnico

### 7.1 Intención probable

```text
Reconocimiento:
Explotación:
Descarga de archivo:
Ejecución de comandos:
Robo de información:
Persistencia:
Movimiento lateral:
Otro:
```

### 7.2 Técnica observada

```text
Categoría:
Técnica:
Servicio afectado:
Precondición:
Resultado esperado por el atacante:
```

Ejemplos de categoría:

```text
SQL Injection
XSS
Command Injection
Path Traversal / LFI
RFI
SSRF
Deserialization
Credential brute force
Downloader
Scanner/bot
```

### 7.3 Mapeo MITRE ATT&CK, si aplica

```text
Táctica:
Técnica:
ID:
Confianza:
Notas:
```

### 7.4 Comportamiento esperado

```text
Qué intenta hacer:
Qué requiere para funcionar:
Qué fallaría si el sistema está protegido:
Qué evidencia dejaría:
```

---

## 8. Indicadores extraídos

### 8.1 Red

```text
IPs:
Dominios:
URLs:
Puertos:
Protocolos:
ASN:
País:
Hosting/VPS:
```

### 8.2 Archivos

```text
Nombres de archivo:
Rutas:
Extensiones:
Hashes MD5:
Hashes SHA1:
Hashes SHA256:
Tamaño:
Tipo MIME:
```

### 8.3 HTTP

```text
Método:
URI:
Parámetros:
Headers:
User-Agent:
Cookie:
Referer:
Body:
```

### 8.4 Comandos / strings

```text
Comandos observados:
Strings relevantes:
Variables:
Rutas:
Binarios llamados:
```

---

## 9. Enriquecimiento OSINT

> Solo fuentes defensivas. No hacer escaneo agresivo ni interacción innecesaria con infraestructura externa.

```text
VirusTotal:
AbuseIPDB:
GreyNoise:
Shodan:
Censys:
URLhaus:
AlienVault OTX:
ThreatFox:
MISP/OpenCTI:
```

Resultado resumido:

```text
Reputación:
Primera vez visto:
Última vez visto:
Detecciones:
Familia asociada:
Campaña asociada:
Confianza:
```

---

## 10. Detección

### 10.1 Patrones simples

```text
Regex:
String:
URI pattern:
Header pattern:
User-Agent:
```

### 10.2 Sigma, si aplica

```yaml
title: Suspicious Payload Pattern
id: reemplazar-con-uuid
status: experimental
description: Detecta patrón sospechoso observado en laboratorio.
author: DrPlaga.sh
date: 2026-06-05
logsource:
  category: webserver
detection:
  selection:
    cs-uri-query|contains:
      - "REEMPLAZAR_PATRON"
  condition: selection
falsepositives:
  - Unknown
level: medium
```

### 10.3 YARA, si aplica

```yara
rule Suspicious_Payload_Example
{
    meta:
        author = "DrPlaga.sh"
        description = "Payload sospechoso observado en laboratorio"
        date = "2026-06-05"
    strings:
        $s1 = "REEMPLAZAR_STRING" ascii nocase
    condition:
        $s1
}
```

### 10.4 Suricata, si aplica

```text
alert http any any -> any any (msg:"Suspicious payload pattern observed in lab"; content:"REEMPLAZAR"; http_uri; sid:1000001; rev:1;)
```

### 10.5 Búsquedas en logs

```text
Wazuh/OpenSearch:
KQL:
grep:
jq:
```

Ejemplo grep:

```bash
grep -R "PATRON" /var/log/
```

Ejemplo jq:

```bash
jq 'select(.url | contains("PATRON"))' events.json
```

---

## 11. Mitigación

```text
Validación de entrada:
WAF:
Bloqueo por patrón:
Rate limit:
Parche:
Hardening:
Monitoreo:
Segmentación:
Reglas IDS/IPS:
```

Acciones recomendadas:

```text
1.
2.
3.
```

---

## 12. Impacto defensivo

```text
Impacto si fuera exitoso:
Exposición requerida:
Sistemas en riesgo:
Prioridad:
Urgencia:
```

---

## 13. Confianza analítica

```text
Confianza: baja / media / alta
Base:
Limitaciones:
Qué falta validar:
```

Ejemplo:

```text
Confianza: media
Base: payload decodificado y patrón compatible con command injection.
Limitaciones: no se observó ejecución exitosa ni descarga posterior.
Qué falta validar: correlación con otros eventos del mismo origen.
```

---

## 14. Línea de tiempo

```text
YYYY-MM-DD HH:MM:SS - Evento recibido
YYYY-MM-DD HH:MM:SS - Payload normalizado
YYYY-MM-DD HH:MM:SS - Decodificación realizada
YYYY-MM-DD HH:MM:SS - Indicadores extraídos
YYYY-MM-DD HH:MM:SS - Reglas propuestas
```

---

## 15. Conclusión

```text
Conclusión:
Clasificación:
Riesgo:
Recomendación:
Estado:
```

Ejemplo:

```text
El payload analizado es compatible con intento automatizado de explotación web.
No se observó compromiso en el entorno analizado.
Se recomienda monitorear recurrencia, bloquear patrones de alto ruido y correlacionar por IP/ASN/User-Agent.
```

---

## 16. Archivos relacionados

```text
logs/
reports/
screenshots/
sanitized-samples/
rules/
scripts/
```

---

## 17. Referencias

```text
- MITRE ATT&CK:
- OWASP:
- Vendor:
- NVD:
- URLhaus:
- GreyNoise:
- AbuseIPDB:
- VirusTotal:
- Documentación interna:
```

---

## 18. Estado final

```text
Payload decodificado:
IOCs extraídos:
Reglas creadas:
Mitigación propuesta:
Publicado:
Pendiente:
```

---

## Disclaimer

Este análisis es defensivo, educativo y basado en entornos autorizados o evidencia sanitizada.  
No publicar malware vivo, payloads weaponizados, credenciales, tokens, dumps ni datos sensibles.  
No usar este material contra sistemas de terceros.

**Menos humo, más evidencia.**
