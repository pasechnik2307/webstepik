#from cgi import parse_qs

#def app(environ, start_response):   
 #   start_response("200 OK", [("Content-Type", "text/plain")])
 #   qs = parse_qs(environ['QUERY_STRING'])
 #   return ["\n".join(environ.get('QUERY_STRING').split("&"))]

def hello_app(environ, start_response):
    q_string = environ.get('QUERY_STRING')
    pairs_list = q_string.split("&")
    body = ""
    for pair in pairs_list:
        body += pair + "\n"

    response_string = [('Content-type', 'text/plain')]

    start_response('200 OK', response_string)
    return [body.strip().encode()]
