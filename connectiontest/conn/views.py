from django.shortcuts import render
from django.db import connections

def check_database_connections(request):
    connection_status = {}
    for alias in connections:
        connection = connections[alias]
        try:
            connection.ensure_connection()
            connection_status[alias] = "Connection successful"
        except Exception as e:
            connection_status[alias] = f"Connection failed: {e}"
    
    return render(request, 'connection_status.html', {'connection_status': connection_status})


