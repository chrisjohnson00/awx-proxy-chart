{{- range $key, $value := .Values.TOWER }}
TOWER_{{ $key }}='{{ $value }}'
{{- end }}