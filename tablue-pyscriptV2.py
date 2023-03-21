#install tableauserverclient first using pip
#pip install tableauserverclient

import tableauserverclient as TSC
import difflib

# Initialize credentials for Tableau Server authentication 
tab_auth = TSC.TableauAuth('username', 'password', 'site_id')

# Initialize Tableau Server connection
server = TSC.Server('https://<tableau-server-url>', use_server_version=True)

# Sign in to Tableau Server
server.auth.sign_in(tab_auth)

# User input
search_question = input("Enter question or keyword: ")

# Get a list of all the dashboards, their descriptions, and their URLs
dashboard_data = []
for dashboard in TSC.Pager(server.dashboards.get):
    dashboard_data.append((dashboard.name, dashboard.description, dashboard.content_url))

# Search for the closest match to the search question in dashboard names, descriptions, and URLs
closest_dashboard = difflib.get_close_matches(search_question, [d[0] + " " + d[1] + " " + d[2] for d in dashboard_data], n=1)
if closest_dashboard:
    dashboard_info = closest_dashboard[0].split()
    dashboard_name = dashboard_info[0]
    dashboard_description = " ".join(dashboard_info[1:-1])
    dashboard_url = dashboard_info[-1]
    print(f"Closest dashboard match: {dashboard_name}")
    print(f"Dashboard description: {dashboard_description}")
    print(f"Dashboard URL: {dashboard_url}")
else:
    # If nothing found, search for search_question in graph name and dashboard URL
    graph_data = []
    for datasource in TSC.Pager(server.datasources.get):
        for graph in datasource.views:
            graph_data.append((graph.name, graph.caption, graph.content_url))
    
    closest_graph = difflib.get_close_matches(search_question, [d[0] + " " + d[1] + " " + d[2] for d in graph_data], n=1)
    if closest_graph:
        graph_info = closest_graph[0].split()
        graph_name = graph_info[0]
        dashboard_url = graph_info[-1]
        print(f"Closest graph match: {graph_name}")
        print(f"Dashboard URL: {dashboard_url}")
    else:
        # If still nothing found, search for search_question in calculated fields and dashboard URL
        field_data = []
        for datasource in TSC.Pager(server.datasources.get):
            for field in datasource.calculation_fields:
                field_data.append((field.name, field.description, field.content_url))
        
        closest_field = difflib.get_close_matches(search_question, [d[0] + " " + d[1] + " " + d[2] for d in field_data], n=1)
        if closest_field:
            field_info = closest_field[0].split()
            field_name = field_info[0]
            dashboard_url = field_info[-1]
            print(f"Closest calculated field match: {field_name}")
            print(f"Dashboard URL: {dashboard_url}")
        else:
            # If still nothing found, search for search_question in data source name and dashboard URL
            data_source_data = []
            for datasource in TSC.Pager(server.datasources.get):
                data_source_data.append((datasource.name, datasource.content_url))
            
            closest_data_source = difflib.get_close_matches(search_question, [d[0] + " " + d[1] for d in data_source_data], n=1)
            if closest_data_source:
                data_source_info = closest_data_source[0].split()
                data_source_name = data_source_info[0]
                dashboard_url = data_source_info[-1]
                print(f"Closest data source name: {data_source_name}")
                print(f"Dashboard URL: {dashboard_url}")
            else:
                print("No matches found")
# Sign out of Tableau Server
server.auth.sign_out()