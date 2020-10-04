# yml-parser
- input docker-compose file
- extract the services as vertices
- extract edges using links and depends_on
- output -> communication graph of the system
- directed graph
- (serviceA, ServiceB) = serviceA --> serviceB = serviceB is reachable from serviceA
- have to improve this solution when services communicates using docker networking (inspecting 'networks' tag)
